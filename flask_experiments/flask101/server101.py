from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!<br><a href='/cat'>Коты</a>"

@app.route("/cat")
def cats():
    return render_template('cats.html')

app.run()