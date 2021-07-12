from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

movie = db.movies.find_one({'title':'매트릭스'},{'_id':False})
print(movie['star'])

same_movies = list(db.movies.find({'star':'9.39'},{'_id':False}))
for same_movie in same_movies:
    print(same_movie['title'])

db.movies.update_one({'title':'매트릭스'},{'$set':{'star':'0'}})