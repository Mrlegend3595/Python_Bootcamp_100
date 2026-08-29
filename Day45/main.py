from bs4 import BeautifulSoup


with open("website.html", encoding="utf-8") as file:
    content = file.read()


soup = BeautifulSoup(content, 'html.parser')
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print("_______________________________________")
# print(soup)
# print("_______________________________________")
# print(soup.prettify())
# print(soup.a) first of tag

print("--------------------------------------------")
# all_anchor = soup.find_all(name="a")
# print(all_anchor)

# for tag in all_anchor:
#     # print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name") #first item simlar
# print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.get("class"))

