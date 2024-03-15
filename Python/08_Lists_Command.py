# Lets create an List contain with various data structure;
Command_list = ["Alpha","Beta", "Gamma", "Delta", "fusion"]
print(Command_list)

Command_list.append(999)
print(Command_list)

# Inserts elements:
Command_list.insert(2, 1000)
print(Command_list)

# remove element from list
Command_list.remove(1000)
print(Command_list)

# deleting element by the list 
del Command_list[1]
print(Command_list)

# length of the list:
print(f"The lenght of the string is: {len(Command_list)}")

