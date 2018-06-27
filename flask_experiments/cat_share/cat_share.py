from flask import Flask, render_template, request, redirect

app = Flask(__name__)

cats = [
    {
        "name": "Бывалый",
        "description": "Многое повидал...",
        "img": "https://avalon.fabiosacdn.com/image/ba83e515-8001-40ed-898f-724de3638537.jpg"
    },
    {
        "name": "Фидель",
        "description": "Кастра",
        "img": "http://img-fotki.yandex.ru/get/5630/27433797.7d/0_81c19_4a96d9e6_-1-XL"
    }
]

@app.route('/')
def main():
    return render_template('main.html', cats=cats)

@app.route('/add', methods=['get', 'post'])
def add():
    name = request.form.get('name', '')
    img = request.form.get('img', '')
    description = request.form.get('description', '')

    if name == '' or img == '' or description == '':
        return render_template('add.html')
    else:
        new_cat = {
            'name': name,
            'img': img,
            'description': description
        }
        cats.append(new_cat)
        return redirect('/cat?id={}'.format(len(cats)-1))

@app.route('/cat')
def details():
    id = int(request.args.get('id', -1))
    if id < 0 or id >= len(cats):
        return 'Cat not found'
    else:
        return render_template('cat.html', cat=cats[id])

app.run(debug=True, host='0.0.0.0')