NUMBER_OF_BYTES_TO_READ = 10000

COUNTRY_INDEX = 3
SH2_DESC_INDEX = 6
YEAR_INDEX = 1

country_to_sh2 = {}

counts_per_range = {"0-20": 0, "21-40": 0, "41-60": 0, "61-80": 0, "81-100": 0}

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
			
		
			if country not in country_to_sh2.keys():
				country_to_sh2[country] = set()
			country_to_sh2[country].add(sh2_desc)

		
for country in country_to_sh2.keys():
	country_to_sh2[country] = len(country_to_sh2[country])
	
	if country_to_sh2[country] < 21:
		counts_per_range["0-20"] += 1
	elif country_to_sh2[country]< 41:
		counts_per_range["21-40"] += 1
	elif country_to_sh2[country] < 61:
		counts_per_range["41-60"] += 1
	elif country_to_sh2[country] < 81:
		counts_per_range["61-80"] += 1
	else:
		counts_per_range["81-100"] += 1


print(f"Number of countries in each bucket {counts_per_range}")

