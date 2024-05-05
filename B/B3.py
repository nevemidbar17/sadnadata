NUMBER_OF_BYTES_TO_READ = 10000

COUNTRY_INDEX = 3
SH4_DESC_INDEX = 6
YEAR_INDEX = 1

country_code = {}

counts_per_date = {"0-150": 0, "151-300": 0, "301-450": 0, "451-600": 0, "601-750": 0,"751-900": 0,"900+": 0}

with open("brazil_exports_from_2018.csv", encoding="utf8") as file:
	start_line = file.readline()

	while True:
		lines = file.readlines(NUMBER_OF_BYTES_TO_READ)
		if len(lines) == 0:
			break
		
		for line in lines:
			line_array = line.split(",")
			country = line_array[COUNTRY_INDEX]
			sh4_desc = line_array[SH4_DESC_INDEX]
			year = int(line_array[YEAR_INDEX])
			
		
			if country not in country_code.keys():
				country_code[country] = set()
			country_code[country].add(sh4_desc)

		
for country in country_code.keys():
	index = list(counts_per_date.keys())[min(len(country_code[country]) // 150, 6)]
	counts_per_date[index] += 1

print(f"Months: {counts_per_date}")

