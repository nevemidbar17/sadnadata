import pandas as pd

bucket_labels = ["0-10", "11-20", "21-30", "31-40", "41-50", "51-60", ">60"]
product_num_per_bucket = [0] * len(bucket_labels)

df = pd.read_csv("brazil_exports_from_2018.csv")

routes = df.groupby(['City', 'Country'])['SH4 Description'].nunique().to_dict()

for number_of_prodacts in routes.values():
        product_num_per_bucket[min(number_of_prodacts // 10, len(product_num_per_bucket) - 1)] += 1
    
print(dict(zip(bucket_labels, product_num_per_bucket)))
