NUMBER_OF_BYTES_TO_READ = 10000

ECONOMIC_BLOCK_INDEX = 0
SHIPMENT_PRICE_INDEX = 1
economic_block_to_shipment_price = {}
with open("shipment_prices.csv", encoding="utf8") as file:
    start_line = file.readline()

    while True:
        lines = file.readlines(NUMBER_OF_BYTES_TO_READ)
        if len(lines) == 0:
            break

        for line in lines:
            line_array = line.split(",")
            economic_block = line_array[ECONOMIC_BLOCK_INDEX]
            shipment_price = line_array[SHIPMENT_PRICE_INDEX]
            economic_block_to_shipment_price[economic_block] = shipment_price

YEAR_INDEX = 1
MONTH_INDEX = 2
ECONOMIC_BLOCK_INDEX = 7

years = [2018, 2019, 2020]
year_to_money_saved = {}

for year in years:
    money_saved = 0
    month_economic_block_count = {}
    with open("brazil_exports_from_2018.csv", encoding="utf8") as file:
        start_line = file.readline()

        while True:
            lines = file.readlines(NUMBER_OF_BYTES_TO_READ)
            if len(lines) == 0:
                break

            for line in lines:
                line_array = line.split(",")
                if year != int(line_array[YEAR_INDEX]):
                    continue
                month = line_array[MONTH_INDEX]
                economic_block = line_array[ECONOMIC_BLOCK_INDEX]
                if month not in month_economic_block_count.keys():
                    month_economic_block_count[month] = {}
                if economic_block not in month_economic_block_count[month].keys():
                    month_economic_block_count[month][economic_block] = 1
                else:
                    month_economic_block_count[month][economic_block] += 1

    for economic_block, shipment_price in economic_block_to_shipment_price.items():
        for month in month_economic_block_count.keys():
            if economic_block in month_economic_block_count[month].keys():
                month_economic_block_count[month][economic_block] = (
                        (month_economic_block_count[month][economic_block] - 1) * int(shipment_price))

    for month in month_economic_block_count.keys():
        for economic_block in month_economic_block_count[month].keys():
            money_saved += month_economic_block_count[month][economic_block]

    year_to_money_saved[year] = money_saved

print(year_to_money_saved)
