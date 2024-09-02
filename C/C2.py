from concurrent.futures import ThreadPoolExecutor, as_completed
COUNTRY_INDEX = 3
CITY_INDEX = 4
SH2_DESC_INDEX = 6
NUMBER_OF_BYTES_TO_READ = 50_000
csvs = [
    "brazil_exports_only_2018.csv",
    "brazil_exports_only_2019.csv",
    "brazil_exports_only_2020.csv",
]


def run_single_file(file_name):
    city_country_set = set()
    product_city_country_set = set()
    with open(file_name, encoding="utf8") as file:
        header = file.readline()
        while True:
            lines = file.readlines(NUMBER_OF_BYTES_TO_READ)
            if len(lines) == 0:
                break
        
            for line in lines:
                line_array = line.split(",")
                city = line_array[CITY_INDEX]
                country = line_array[COUNTRY_INDEX]
                sh2_desc = line_array[SH2_DESC_INDEX]
                city_country_set.add(hash((city, country)))
                product_city_country_set.add(hash((sh2_desc, city, country)))
    year_average = len(product_city_country_set)/len(city_country_set)
    return {file_name: year_average}

with ThreadPoolExecutor(max_workers=3) as executor:
    task_instances = {executor.submit(run_single_file, csv): csv for csv in csvs}
    all_years = {}
    for future in as_completed(task_instances):
        all_years.update(future.result())
    print(all_years)
