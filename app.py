from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

#create mock database
fakeDatabase = {
    1:{'name':'Clean car'},
    2:{'name':'Write blog'},
    3:{'name':'Start stream'},
}

#create class-based views
class Items(Resource):
    def get(self):
        return fakeDatabase

