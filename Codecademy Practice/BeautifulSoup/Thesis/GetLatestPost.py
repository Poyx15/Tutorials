import requests
from bs4 import BeautifulSoup

def get_data(self):
    webpage_response = requests.get('http://bahaphilippines2020.pythonanywhere.com/data')

    webpage = webpage_response.content
    soup = BeautifulSoup(webpage, "html.parser")

    contents = []
    turtle_links = soup.find_all("tr")
    i = 0
    for content in turtle_links[1]:
        contents.append(str(content).strip("<td>").strip(' class="col-md-10">').strip("</"))


    stripped_content = []
    #
    # print(turtle_links[1])
    i = 1
    while(i < 11):
        stripped_content.append(contents[i])
        i = i + 2

    string_content = ""

    for content in stripped_content:
        # print(content)
        string_content = string_content + str(content)

    self.time_date, self.height_inches, self.level, self.category_level, self.message = stripped_content






