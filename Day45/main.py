from bs4 import BeautifulSoup

# with open("website.html", encoding="utf-8") as file:
#     content = file.read()

# soup = BeautifulSoup(content, 'html.parser')
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print("_______________________________________")
# print(soup)
# print("_______________________________________")
# print(soup.prettify())
# print(soup.a) #first of tag

# print("--------------------------------------------")
# all_anchor = soup.find_all(name="a")
# print(all_anchor)
#
# for tag in all_anchor:
#     # print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name") #first item simlar
# print(heading)

#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))


# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# heading = soup.select(".heading")
# print(heading)


#------------------------------------------------------
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_page = response.text

soup = BeautifulSoup(yc_page, "html.parser")

articles= soup.find_all(name="span", class_="titleline")
articles_text = []
article_links = []

for article_tag in articles:
    text = article_tag.get_text()
    link = article_tag.a.get("href")
    article_links.append(link)
    articles_text.append(text)

# print(article_tag)
# article_text = article_tag.get_text()
# article_link = article_tag.a.get("href")
# print(article_link)

article_upvotes =[int(score.text.split()[0]) for score in soup.find_all(name="span", class_="score")]
print("============================")
largest_number=max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(article_upvotes[largest_index])
print(article_links[largest_index])
print(articles_text[largest_index])