NUMBER_OF_BYTES_TO_READ = 10000
YEAR_INDEX = 1 

min_year = 2050
max_year = 50


with open("brazil_exports_from_2018.csv", encoding="utf8") as file:
	start_line = file.readline()
	while True:
		lines = file.readlines(NUMBER_OF_BYTES_TO_READ)
		if len(lines) == 0:
			break
		for line in lines:
			year = int(line.split(",")[YEAR_INDEX])
			if year < min_year:
				min_year = year
			if year > max_year:
				max_year = year

		
print(f"{min_year=}")
print(f"{max_year=}")
