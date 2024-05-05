NUMBER_OF_BYTES_TO_READ = 10000

batch_number = 0
length = 0

with open("brazil_exports_from_2018.csv", encoding="utf8") as file:
	while True:
		lines = file.readlines(NUMBER_OF_BYTES_TO_READ)
		if len(lines) == 0:
			break
		
		length += len(lines)
		batch_number += 1
		print(f"{length=}")


print("Number of batches:", batch_number)
print("The total length is:", length)
