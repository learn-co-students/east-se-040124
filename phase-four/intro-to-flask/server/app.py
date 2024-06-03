#!/usr/bin/env python3

# Run the server with `flask run --debug` 
# --debug to allow for restarting of server when changes are made
# and allow for ipdb.set_trace() breakpoint

#  where the flask app instance is located
#  export FLASK_APP=server/app.py

#  change the run port
#  export FLASK_RUN_PORT=5555

#  set debug to true so you don't have to restart after making changes
#  export FLASK_DEBUG=true

# 1a. Set Up Imports
from flask import Flask, make_response, request

# 1b. Create instance of Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

#3. Create a path /cats
@app.route('/cats', methods=['GET', 'POST'])
def get_cats():
    print('get cats')
    if request.method == 'GET':
        cats = [
            {
                'name': 'Luke',
                'age': 2
            },
            {
                'name': 'Leia',
                'age': 2
            },
            {
                'name': 'Rose',
                'age': 12
            },
        ]
        return make_response(cats, 200)
    elif request.method == 'POST':
        return make_response({'message': 'successfully create cat'}, 201)

# 4. Create a dynamic route
@app.route('/cats/<int:id>')
def cat_by_id(id):
    cats = [
        {
            'id': 1,
            'name': 'Luke',
            'age': 2
        },
        {
            'id': 2,
            'name': 'Leia',
            'age': 2
        },
        {
            'id': 3,
            'name': 'Rose',
            'age': 12
        },
    ]
    for cat in cats:
        if cat['id'] == id:
            return make_response(cat)

    return make_response({'error': 'Cat not found'}, 404)


# 6. Use the before_request request hook, what this hook does is up to you. You could hit a breakpoint, print something to server console or anything else you can think of.
@app.before_request
def runs_before():
    print('runs before request')

@app.after_request
def runs_after(response):
    print('runs after request')
    return response

# Note: If you'd like to run the application as a script instead of using `flask run`, uncomment the line below 
# and run `python app.py`

# if __name__ == '__main__':
#     app.run(port=5555, debug=True)