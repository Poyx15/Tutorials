import requests
from bs4 import BeautifulSoup

website = "http://bahaphilippines2020.pythonanywhere.com/data"
class Website:
    def __init__(self, name):
        self.name = name

        webpage_response = requests.get(self.name)
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
        while (i < 11):
            stripped_content.append(contents[i])
            i = i + 2

        string_content = ""

        for content in stripped_content:
            # print(content)
            string_content = string_content + str(content)

        self.time_date, self.height_inches, self.level, self.category_level, self.message = stripped_content

    def __repr__(self):
        return """Website: {website}
        Time: {time}
        Height: {height}
        Level: {level}
        Category Level: {category}
        Message: {message}""".format(website=self.name, time=self.time_date, height=self.height_inches, level=self.level, category=self.category_level, message=self.message)








