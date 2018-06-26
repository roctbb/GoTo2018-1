from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!<br><a href='/cat'>Коты</a>"

@app.route("/cat")
def cats():
    return render_template('cats.html')

@app.route("/hello")
def greeting():
    if "name" in request.args:
        name = request.args['name']
        return "Hello, {}!".format(name)
    else:
        return "<img src='http://pbs.twimg.com/media/CLeVxPeW8AAI-OF.jpg'>" \
               "<form><input type='text' name='name'/><input type='submit'></form>"

@app.route("/hello_smart")
def greeting_smart():
    name = request.args.get('name', 'Анонимус')
    return "Hello, {}!".format(name)

@app.route("/story")
def story():
    first_name = request.args.get('first_name', '')
    second_name = request.args.get('second_name', '')

    if first_name == '' or second_name == '':
        return render_template('empty_story.html')
    else:
        return render_template('story.html', first=first_name,
                               second=second_name)


app.run()