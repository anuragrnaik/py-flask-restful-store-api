from datetime import timedelta
from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity

from resources.item import Item, Items
from resources.store import Store, StoreList
from resources.user import UserRegister

app = Flask(__name__)
app.secret_key = 'john doe'
app.config['JWT_AUTH_URL_RULE'] = '/login'
# config JWT to expire within half an hour
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
# config JWT auth key name to be 'email' instead of default 'username'
# app.config['JWT_AUTH_USERNAME_KEY'] = 'email'

api = Api(app)

jwt = JWT(app, authenticate, identity)

@jwt.auth_response_handler
def customized_response_handler(access_token, identity):
    return jsonify({
                        'access_token': access_token.decode('utf-8'),
                        'user_id': identity.id
                   })

# @jwt.error_handler
# def error_handler(error):
#     return jsonify({
#                        'message': error.description,
#                        'code': error.status_code
#                    }), error.status_code

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db, get_connection
    app.config['SQLALCHEMY_DATABASE_URI'] = get_connection()
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    app.run(port=5000, debug=True)
