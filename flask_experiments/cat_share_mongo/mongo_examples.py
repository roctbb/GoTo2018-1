from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('mongodb://user:GoTo1234@ds155529.mlab.com:55529/catshare')
db = client['catshare']
cat_collection = db['cats']

print('connection is OK')
# добавление одного элемента
cat = {
        "name": "Бывалый",
        "description": "Многое повидал...",
        "img": "https://avalon.fabiosacdn.com/image/ba83e515-8001-40ed-898f-724de3638537.jpg"
}

cat_collection.insert_one(cat)
print(cat)

# получение записей из бд
cats = cat_collection.find()
print('cats:')
for cat in cats:
    print(cat)

# поиск элемента
print('cat number 5b348f8dea2f51fab0c45462:')
cat = cat_collection.find_one({"_id": ObjectId('df5b348f8dea2f51fab0c45462')})
print(cat)

# удаление
# cat_collection.remove({"_id": ObjectId('5b348f8dea2f51fab0c45462')})

# изменение
cat['name'] = 'Васька'
cat_collection.update_one({"_id": ObjectId('5b348f8dea2f51fab0c45462')}, {'$set':cat})