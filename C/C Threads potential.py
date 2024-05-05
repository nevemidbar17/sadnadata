from concurrent.futures import ThreadPoolExecutor, as_completed

COUNTRY_INDEX = 3
CITY_INDEX = 4 
SH2_DESC_INDEX = 6

city_stock = {}

csvs = ["brazil_exports_only_2018.csv", "brazil_exports_only_2019.csv","brazil_exports_only_2020.csv"]


def run_single_file(file_name):
	city_country_stock = {}
	with open(file_name, encoding="utf8") as file:
		start_line = file.readline()
		while True:
			line = file.readline()
			if len(line) == 0:
				break

			line_array = line.split(",")
			country = line_array[COUNTRY_INDEX]
			city = line_array[CITY_INDEX]
			sh2_desc = line_array[SH2_DESC_INDEX]

			if city not in city_country_stock.keys():
				city_country_stock[city] = {}
			if country not in city_country_stock[city].keys():
				city_country_stock[city][country] = set()
			city_country_stock[city][country].add(sh2_desc)

	city_averages_per_country_counter = 0
	city_amount = len(city_country_stock.keys())
	for city in city_country_stock.keys():
		country_number_of_sh2 = 0
		country_amount = len(city_country_stock[city].keys())
		for country in city_country_stock[city].keys():
			country_number_of_sh2 += len(city_country_stock[city][country])
		city_averages_per_country_counter += country_number_of_sh2 / country_amount

	return {file_name.split("_")[-1].split(".")[0]: city_averages_per_country_counter / city_amount}


with ThreadPoolExecutor(max_workers=3) as executor:
	task_instances = {executor.submit(run_single_file, csv): csv for csv in csvs}
	all_years = {}
	for future in as_completed(task_instances):
		all_years.update(future.result())
	print(all_years)
