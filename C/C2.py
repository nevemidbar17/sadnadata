from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import os
import time 
COUNTRY_INDEX = 3
CITY_INDEX = 4
SH2_DESC_INDEX = 6
BYTES = 1024
step = 100
csvs = [
    "brazil_exports_only_2018.csv",
    "brazil_exports_only_2019.csv",
    "brazil_exports_only_2020.csv",
]


def run_single_file(file_name):
    cities = set()
    with open(file_name, encoding="utf8") as file:
        header = file.readline()
        lines = file.readlines(BYTES)
        while lines:
            for line in lines:
                line_array = line.split(",")
                city = line_array[CITY_INDEX]
                cities.add(city)
            lines = file.readlines(BYTES)
    new_file_name = f"cities_{file_name.split('.')[0]}.json"

    cities = list(cities)

    open(new_file_name, "w").write("{")
    index = 0
    while index <= len(cities):
        legit_cities = [
            city
            for temp_index, city in enumerate(cities)
            if temp_index < index + step and temp_index >= index
        ]
        country_stock = {}
        with open(file_name) as file:
            header = file.readline()
            lines = file.readlines(BYTES)
            while lines:
                for line in lines:
                    line_array = line.split(",")
                    country = line_array[COUNTRY_INDEX]
                    city_file = line_array[CITY_INDEX]
                    sh2_desc = line_array[SH2_DESC_INDEX]
                    if city_file in legit_cities:
                        if city_file not in country_stock.keys():
                            country_stock[city_file] = {}
                        if country not in country_stock[city_file].keys():
                            country_stock[city_file][country] = set()
                        country_stock[city_file][country].add(sh2_desc)
                lines = file.readlines(BYTES)

            for city in country_stock.keys():
                for country in country_stock[city].keys():
                    country_stock[city][country] = len(country_stock[city][country])
                open(new_file_name, "a").write(
                    f""""{city}": {sum(country_stock[city].values()) / len(country_stock[city].keys())},"""
                )
        index += step

    with open(new_file_name, "a")as file:
        file.seek(file.tell() - 1, os.SEEK_SET)
        file.truncate()
        file.write("}")

    file = open(new_file_name)
    data = json.load(file)
    return {
        file_name.split("_")[-1].split(".")[0]: sum(data.values()) / len(data.keys())
    }


with ThreadPoolExecutor(max_workers=3) as executor:
    start_time = time.time()
    task_instances = {executor.submit(run_single_file, csv): csv for csv in csvs}
    all_years = {}
    for future in as_completed(task_instances):
        all_years.update(future.result())
    print(all_years)
    print(time.time() - start_time)
