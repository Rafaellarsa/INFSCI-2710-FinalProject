from flask import Flask, jsonify

from user import User
from recipe import Recipe

app = Flask(__name__)    

@app.route("/")
def index():
    return """
    <p>Hello, Welcome to Student Meal Express!</p>
    <p>These are our endpoints:</p> <ul>
    <li>get_user - /users/<user_id></li>
    </ul>"""

@app.route("/users/<user_id>", methods=['GET'])
def get_user(user_id):
    user = User()
    return jsonify(user.get_by_id(user_id))


@app.route('/recipes', methods=['GET'])
def get_recipes():
    recipes = Recipe()
    return jsonify(recipes.get_all())

app.run()
