numbers = [3, 1, 2, 3, 4, 1, 5, 2]

no_dupes = []

for num in numbers:
    if num in no_dupes:
        continue
    else:
        no_dupes.append(num)

print(f"List without duplicates: {no_dupes}")