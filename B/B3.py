NUMBER_OF_BYTES_TO_READ = 50_000

COUNTRY_INDEX = 3
CITY_INDEX = 4
SH4_DESC_INDEX = 6

print(f"{NUMBER_OF_BYTES_TO_READ=}")

N = 5

number_of_unique = 0

for modulo in range(N):
    unique_values_per_modulo = set()

    print(f"{modulo=}")
    with open("brazil_exports_from_2018.csv", encoding="utf8") as file:
        start_line = file.readline()

        while True:
            lines = file.readlines(NUMBER_OF_BYTES_TO_READ)
            if len(lines) == 0:
                break
            
            for line in lines:
                line_array = line.split(",")
                country = line_array[COUNTRY_INDEX]
                city = line_array[CITY_INDEX]
                sh4_desc = line_array[SH4_DESC_INDEX]

                key = f"{country}-{city}-{sh4_desc}"

                if (hash(key) % N) == modulo:
                    unique_values_per_modulo.add(key) 
            
    number_of_unique+=len(unique_values_per_modulo)


print(f"Number of city-country-sh4 unique values:")
print(number_of_unique)