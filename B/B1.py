YEAR_INDEX = 1 
MONTH_INDEX = 2
COUNTRY_INDEX = 3
WEIGHT_INDEX = 9 

country_month_weight = {}

with open("brazil_exports_from_2018.csv", encoding="utf8") as file:
	start_line = file.readline()
	print(start_line)

	while True:
		line = file.readline()
		if len(line) == 0:
			break

		line_array = line.split(",")
		year = int(line_array[YEAR_INDEX])
		month = int(line_array[MONTH_INDEX])
		country = line_array[COUNTRY_INDEX]
		weight = int(line_array[WEIGHT_INDEX])

		if country not in country_month_weight.keys():
			country_month_weight[country] = {}
		if year not in country_month_weight[country].keys():
			country_month_weight[country][year] = {}
		if month not in country_month_weight[country][year].keys():
			country_month_weight[country][year][month] = (0, 0)
		total_weight = country_month_weight[country][year][month][0]
		count = country_month_weight[country][year][month][1]
		country_month_weight[country][year][month] = (total_weight + weight, count + 1)

for country in country_month_weight.keys():
	for year in country_month_weight[country].keys():
		for month in country_month_weight[country][year].keys():
			country_month_weight[country][year][month] = country_month_weight[country][year][month][0] / country_month_weight[country][year][month][1]
		

print(f"Countries average: {country_month_weight}")

