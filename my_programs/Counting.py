num_of_coders = int(input())
counting = input()
who_is_first = int(input())

array_of_counting = counting.split(" ")
count = who_is_first - 1

for i in range(len(array_of_counting)):
    if count == num_of_coders:
        count = 1
    else:
        count += 1
        
print(count)

# вместо for можно юзать формулу ((len(array_of_counting) + num_of_coders - 2) % who_is_first + 1)
