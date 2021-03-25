text_file = '''First Line
Second Line
Third Line'''

# Writing a file. 'w' as arguement will make the file in write mode
with open('how_many_lines.txt', 'w') as lines_doc:
    lines_doc.write(text_file)

# Reading a file. 'r' as arguement will make the file in write mode. Default arguement is 'r'
# .readlines() will read the file by each line
with open('how_many_lines.txt') as lines_doc:
  for line in lines_doc.readlines():
    print(line)

# Appending a file. 'a' as arguement will make the file in append mode.
with open('how_many_lines.txt', 'a') as cool_dogs_file:
  cool_dogs_file.write('\nAir Buddy')

# This block will read the whole file
with open('how_many_lines.txt') as lines_doc:
  print(lines_doc.read())

# Accessing a CSV or Comma Separated Values
#
# -------> 'Cool Fact' in print(cool['Cool Fact']) is the Key in a dictionary
# import csv
#
# with open('cool_csv.csv') as cool_csv_file:
#   cool_csv_dict = csv.DictReader(cool_csv_file)
#   for cool in cool_csv_dict:
#     print(cool['Cool Fact'])


# import csv
#
# with open('addresses.csv', newline='') as addresses_csv:
#   address_reader = csv.DictReader(addresses_csv, delimiter=';')   -------> Notice that there is a delimiter parameter
#   for row in address_reader:                                      -------> This parameter split the data other than
#     print(row['Address'])                                         -------> commas. That is optional


# import csv
#
# isbn_list = []
# with open('books.csv') as books_csv:
#   books_reader = csv.DictReader(books_csv, delimiter = '@')
#   for book in books_reader:
#     isbn_list.append(book['ISBN'])
#
# print(isbn_list)


# Reading a JSON file

# import json
#
# with open('message.json') as message_json:
#   message = json.load(message_json)
# print(message['text'])
