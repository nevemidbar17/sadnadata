NUMBER_OF_BYTES_TO_READ = 10000

COUNTRY_INDEX = 3
SH2_DESC_INDEX = 6
YEAR_INDEX = 1

country_code = {}

counts_per_date = {"0-20": 0, "21-40": 0, "41-60": 0, "61-80": 0, "81-100": 0}

with open("brazil_exports_from_2018.csv", encoding="utf8") as file:
	start_line = file.readline()

	while True:
		lines = file.readlines(NUMBER_OF_BYTES_TO_READ)
		if len(lines) == 0:
			break
		
		for line in lines:
			line_array = line.split(",")
			country = line_array[COUNTRY_INDEX]
			sh2_desc = line_array[SH2_DESC_INDEX]
			year = int(line_array[YEAR_INDEX])
			
		
			if country not in country_code.keys():
				country_code[country] = set()
			country_code[country].add(sh2_desc)

		
for country in country_code.keys():
	country_code[country] = len(country_code[country])
	
	if country_code[country] < 21:
		counts_per_date["0-20"] += 1
	elif country_code[country]< 41:
		counts_per_date["21-40"] += 1
	elif country_code[country] < 61:
		counts_per_date["41-60"] += 1
	elif country_code[country] < 81:
		counts_per_date["61-80"] += 1
	else:
		counts_per_date["81-100"] += 1


print(f"Months: {counts_per_date}")

