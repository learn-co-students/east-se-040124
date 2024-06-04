from flask import make_response

from config import app
from models.dog import Dog
# REST convention 
# GET all '/dogs'
# POST '/dogs'
# GET one '/dogs/<int:id>'
# PATCH '/dogs/<int:id>'
# DELETE '/dogs/<int:id>'

@app.route('/dogs', methods=['GET'])
def get_all_dogs():
    all_dogs = []
    for dog in Dog.query.all():
        # dog_dict = {
        #     'id': dog.id,
        #     'name': dog.name,
        #     'age': dog.age,
        #     'favorite_treat': dog.favorite_treat
        # }
        all_dogs.append(dog.to_dict())
    return make_response(all_dogs)