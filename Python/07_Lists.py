# some basic about the list
# It is order of collection of data.
# I can change the data after create an List.
# I can Add any types of data like string number or even other lists.
# Its access through the index.
# Third brace is used for the initilize the list.
# []---> this is the list 



# taking the String example 
#             index 0   index 1   Index 2
first_list = ["bikram", "Sourav", "Soumya"]
print(first_list[1]) # print Sourav
print(first_list[2]) # print Soumya

# contain with  0   1     2     3   4    5
Second_list = [100, 200, 300, 400, 500, 600]
print(Second_list)

# modify list:
Second_list[0] = 999 # change the value of 0 index
print(Second_list)

# Mix data structure:
Third_Mix_list = ['Bikram', 10, True, 3.156, "Sourav", False]
print(Third_Mix_list)


# Slicing Data Structure 
# ----------->list[start_index:end_index:step]
newlist =  ["Zero", "one", "two", "Three", "four"]
print(newlist[1:3]) # output 1 2 
print(newlist[::2]) # outpu 0 2 4 
print(newlist[::-2]) # output 4 2 0
print(newlist[0:2:3])
print(newlist[0:4]) 






