
from json import loads

NUMBER_OF_BYTES_TO_READ = 10000

YEAR_INDEX = 1 
CITY_INDEX = 4 
SH2_DESC = 6


def get_years():
	years = []
	with open("brazil_exports_from_2018.csv", encoding="utf8") as file:
		start_line = file.readline()
		while True:
			lines = file.readlines(NUMBER_OF_BYTES_TO_READ)
			if len(lines) == 0:
				break

			for line in lines:
				line_array = line.split(",")
				year = int(line_array[YEAR_INDEX])
				if year not in years:
					years.append(year)
	return years


def write_to_disk(year_filter):
	city_stock = {}

	with open("brazil_exports_from_2018.csv", encoding="unicode_escape") as file:
		start_line = file.readline()
		while True:
			lines = file.readlines(NUMBER_OF_BYTES_TO_READ)
			if len(lines) == 0:
				break

			for line in lines:
				line_array = line.split(",")
				year = int(line_array[YEAR_INDEX])
				city = line_array[CITY_INDEX]
				sh2_desc = line_array[SH2_DESC]

				if year == year_filter:
					if city not in city_stock.keys():
						city_stock[city] = {}
					if sh2_desc not in city_stock[city].keys():
						city_stock[city][sh2_desc] = 0
					city_stock[city][sh2_desc] += 1
		
	for city in city_stock.keys():
		largest_count = max(city_stock[city].values())
		city_stock[city] = {stock: count for stock, count in city_stock[city].items() if count == largest_count}

	with open(f"largest_code_{year_filter}.txt", "w") as file:
		file.write(str(city_stock).replace("'", '"'))


def read_from_files(year):
	with open(f"largest_code_{year}.txt", encoding="unicode_escape") as file:
		return file.read()

years =  get_years()
for year in years:
	write_to_disk(year)

city_stocks_all_years = {}
for year in years:
	text = f"""{read_from_files(year)}"""
	city_stocks_all_years[year] = loads(text)

print(f"Stocks per city per year: {city_stocks_all_years}")

