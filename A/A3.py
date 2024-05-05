NUMBER_OF_BYTES_TO_READ = 10000
COUNTRY_INDEX = 3 

countries = []

with open("brazil_exports_from_2018.csv", encoding="utf8") as file:
	start_line = file.readline()
	while True:
		lines = file.readlines(NUMBER_OF_BYTES_TO_READ)
		if len(lines) == 0:
			break
		for line in lines:
			country = (line.split(",")[COUNTRY_INDEX])
			if country not in countries:
				countries.append(country)

		
print(f"Amount of countries: {len(countries)}")
print(f"Countries: {countries}")
