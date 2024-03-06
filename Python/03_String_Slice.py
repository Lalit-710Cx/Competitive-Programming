my_string = "Bikram"
print(my_string[0])  #output: 0 index P
print(my_string[1:4]) #output: yth[4th num not consider]

# Example 1
text = "Bikram mahato"
first_char = text[0]
print(first_char)  # Output: B

# Example 2
third_char = text[2]
print(third_char)  # Output: k

# Example 3 (negative indexing, counting from the end)
last_char = text[-1]
print(last_char)   # Output: o

# Example 4
second_last_char = text[-2]
print(second_last_char)  # Output: t

# --------------------SLicing-----------------------
text = "hello, World!"
substring = text[7:12]
print(substring)  # Output: World

# Example 1 (omitting start or end index)
first_five_chars = text[:5]
print(first_five_chars)  # Output: Hello

last_five_chars = text[-5:]
print(last_five_chars)   # Output: World

# Example 2 (using a step in slicing)
every_second_char = text[::2]
print(every_second_char)  # Output: Hlo ol!

# Example 3 (reverse a string)
reversed_text = text[::-1]
print(reversed_text)  # Output: !dlroW ,olleH

# text[7:12] extracts the substring from index 7 to 11.
# text[:5] extracts the substring from the beginning up to index 4.
# text[-5:] extracts the substring from the last 5 characters to the end.
# text[::2] extracts every second character in the string.
# text[::-1] reverses the entire string.