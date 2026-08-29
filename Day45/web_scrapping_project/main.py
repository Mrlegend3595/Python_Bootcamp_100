from bs4 import BeautifulSoup
import requests
import random

URL = "https://reelnerdspodcast.com/2020/07/30/catching-the-classics-100-movies-to-see-before-you-die/"

print("Hi\n"
      "Welcome to random movie selector from movies that you must see before of die.")
print("++++++++++++++++++++++++++++++++++++++")
print("Wait Second........")
print("++++++++++++++++++++++++++++++++++++++")

try:
      with open("movies.txt", "r") as file:
          content = file.readlines()

except FileNotFoundError:

      response = requests.get(URL)
      response.raise_for_status()

      site_content = response.text
      soup = BeautifulSoup(site_content, 'html.parser')

      movies = [movie.text for movie in soup.select(".wp-block-list li")]

      with open("movies.txt", "a",encoding="utf-8") as file:
            for movie in movies:
                  index_movie = movies.index(movie) + 1
                  file.write(f"{index_movie}) {movie}\n")

      with open("movies.txt", "r",) as file:
          content = file.readlines()

finally:
      selected_movies = random.choice(content)
      print(f"Recommended Movie for You is: {selected_movies.strip()}")