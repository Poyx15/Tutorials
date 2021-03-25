Author = input("Name of the Author(s): ")
TitlePaper = input("Title of Paper: ")
TitleJournal = input("Title of the Journal: ")
VolumeNumber = input("Volume/Issue/Page/Date: ")
DOI = input("Enter DOI: ")
URL = input("URL: ")
if DOI == "":
    Citation = f'{Author}, "{TitlePaper}", {TitleJournal}, {VolumeNumber}, [Online]. Available: {URL}[Accessed September 2, 2020].\n'
elif URL == "":
    Citation = f'{Author}, "{TitlePaper}", {TitleJournal}, {VolumeNumber}. doi: {DOI}.\n'
with open("Citation.txt", "a") as text_file:
    print(Citation, file=text_file)
print(Citation)


# same = "same"
# seym = "seym"
# shame = "shame"
#
# message = '''{}
#     {}
#     {}'''.format(same, seym, shame)
#
# count = 0
# while count < 150:
#     count = count+1
#     with open("same.txt", "a") as text_file:
#         print(message, file=text_file)


# DOI = input("Enter DOI: ")
# URL = input("URL: ")
# if DOI == "":
#     Citation = f'{Author}, "{TitlePaper}", {TitleJournal}, {VolumeNumber}, [Online]. Available: {URL}[Accessed September 2, 2020].\n'
# elif URL == "":
#     Citation = f'{Author}, "{TitlePaper}", {TitleJournal}, {VolumeNumber}. doi: {DOI}.\n'
# with open("Citation.txt", "a") as text_file:
#     print(Citation, file=text_file)
# print(Citation)
