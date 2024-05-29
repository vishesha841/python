numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


odd_numbers = [num for num in numbers if num % 2 != 0]
even_numbers = [num for num in numbers if num % 2 == 0]


odd_squares = [num ** 2 for num in odd_numbers]


even_squares = [num ** 2 for num in even_numbers]


print("Odd Numbers:", odd_numbers)
print("Even Numbers:", even_numbers)
print("Square of Odd Numbers:", odd_squares)
print("Square of Even Numbers:", even_squares)

##########################

numbers = [10, 5, 8, 20, 3, 15, 7]


largest = numbers[0]
smallest = numbers[0]


for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num


print("Largest number in the list:", largest)
print("Smallest number in the list:", smallest)

##########################

numbers = [10, 5, 8, 20, 3, 15, 7]


second_largest = float('-inf')
largest = float('-inf')
second_smallest = float('inf')
smallest = float('inf')


for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
    
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest and num != smallest:
        second_smallest = num


print("Second largest number in the list:", second_largest)
print("Second smallest number in the list:", second_smallest)

########################

numbers = [5, 3, 7, 9, 8, 4, 2]


for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

ascending_order = numbers


for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] < numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

descending_order = numbers


print("Ascending Order:", ascending_order)
print("Descending Order:", descending_order)

########################

a = [45, 67, 83, 24, 55, 87, 77, 34]


number_to_find = 55


position = None


for i in range(len(a)):
    if a[i] == number_to_find:
        position = i
        break


if position is not None:
    print("The position of", number_to_find, "is:", position)
else:
    print("The number", number_to_find, "is not in the list.")

######################

a = [4, 5, 6, 4, 6, 7, 4, 2, 4, 8, 4]


element_count = {}


for num in a:
    if num in element_count:
        element_count[num] += 1
    else:
        element_count[num] = 1


most_frequent_element = max(element_count, key=element_count.get)


print("The most frequent element in the list is:", most_frequent_element)

##################
