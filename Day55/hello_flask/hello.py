from flask import Flask

def make_bold(func):
    def wrapper_function():
        return f"<b>{func()}</b>"
    return wrapper_function

def make_emphasis(func):
    def wrapper_function():
        return f"<em>{func()}</em>"
    return wrapper_function

def make_underlined(func):
    def wrapper_function():
        return f"<u>{func()}</u>"
    return wrapper_function

app = Flask(__name__)

@app.route('/')
def hello_world():
    return ("<h1>Hello, world!</h1>"
            "<p>This is an example page</p>"
            "<img src='https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/1280px-Cat03.jpg?utm_source=en.wiktionary.org&utm_campaign=index&utm_content=thumbnail'>")

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"

if __name__ == "__main__":
    app.run(debug=True)