from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "سلام! سرور Flask روشن شد ✅"
@app.route('/bye')
def say_bye():
    return "<h1>GoodBye--</h1>"

if __name__ == '__main__':
    app.run(debug=True)