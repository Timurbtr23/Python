with open('data.txt') as f:
    data = f.readlines()

count = 0
for char in data[0]:
    if char.isnumeric():
        count += 1

print(count)
