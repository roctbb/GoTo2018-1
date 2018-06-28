from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
client = MongoClient('mongodb://user:GoTo1234@ds155529.mlab.com:55529/catshare')
db = client['catshare']
cat_collection = db['cats']


@app.route('/')
def main():
    cats = cat_collection.find()
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
        cat_collection.insert(new_cat)
        return redirect('/cat?id={}'.format(str(new_cat['_id'])))

@app.route('/cat')
def details():
    id = request.args.get('id', '')
    try:
        cat = cat_collection.find_one({'_id': ObjectId(id)})
        return render_template('cat.html', cat=cat)
    except:
        return 'Cat not found'


app.run(debug=True, host='0.0.0.0')