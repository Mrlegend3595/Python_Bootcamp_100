from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    update_year = datetime.datetime.now().year
    random_number = random.randint(1, 10)
    return render_template("index.html",num=random_number,
                           update_year=update_year)

@app.route('/guess/<name>')
def guess(name):
    dict_params = {
        'name': name,
    }
    response = requests.get("https://api.agify.io", params=dict_params)
    age = response.json()['age']
    response = requests.get("https://api.genderize.io", params=dict_params)
    gender = response.json()['gender']

    return render_template("guess.html",name=name,age=age,gender=gender)

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/47de8a1d6b8a23abfdbf"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html",posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True)


#npoint : https://npoint.io