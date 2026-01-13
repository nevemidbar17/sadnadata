NUMBER_OF_BYTES_TO_READ = 10000

COUNTRY_INDEX = 3 
PROFIT_INDEX = 8

countries = {}

with open("brazil_exports_from_2018.csv", encoding="utf8") as file:
	start_line = file.readline()
	print(start_line)
	while True:
		lines = file.readlines(NUMBER_OF_BYTES_TO_READ)
		if len(lines) == 0:
			break
		for line in lines:
			line_array = line.split(",")
			country = line_array[COUNTRY_INDEX]
			profit = int(line_array[PROFIT_INDEX])
			
			if country not in countries.keys():
				countries[country] = profit
			else:
				countries[country] += profit

		
print(f"Profit per country: {countries}")

print(f"Countries: {countries}")
