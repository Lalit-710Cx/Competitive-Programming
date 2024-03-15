# define an list
numbers = [1, 2, 3, 4, 5]

# Loop through each element in the list
for num in numbers:
    print(num)

#iterate the every element between 0 to len(numbers) element .    
for i in range(len(numbers)):
    numbers[i] *= 5
print(numbers)

# Define a list
numbers1 = [1, 2, 3, 4, 5]

# Create a new list with each element multiplied by 2
doubled_numbers = [num * 2 for num in numbers1]

print(doubled_numbers)  # Output: [2, 4, 6, 8, 10]


    

