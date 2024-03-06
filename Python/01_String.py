def printquote(container):
    container['single_quoted'] = 'Bikram mahato'

    container['double_quoted'] = "Bikram Mahato"

    container['triple_quoted'] = '''Bikram Mahato'''

quotes_directory = {}

printquote(quotes_directory)

print(quotes_directory['single_quoted'])
print(quotes_directory['double-quoted'])
print(quotes_directory['triple_quoted'])

