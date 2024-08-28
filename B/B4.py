NUMBER_OF_BYTES_TO_READ = 50_000

COUNTRY_INDEX = 3
CITY_INDEX = 4
SH4_DESC_INDEX = 6

print(f"{NUMBER_OF_BYTES_TO_READ=}")

bucket_labels = ["0-10", "11-20", "21-30", "31-40", "41-50", "51-60", ">60"]
product_num_per_bucket = [0] * len(bucket_labels)

N = 5

for modulo in range(N):
    products_per_city_country = {}

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

                key = hash((country, city))

                if (key % N) == modulo:
                    if key not in products_per_city_country.keys():
                        products_per_city_country[key] = set()
                    products_per_city_country[key].add(hash(sh4_desc))
            
    for product_set in products_per_city_country.values():
        product_num_per_bucket[min(len(product_set) // 10, len(product_num_per_bucket) - 1)] += 1

print(f"Number of city-country duos in each number-of-products bucket:")
print(dict(zip(bucket_labels, product_num_per_bucket)))