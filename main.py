from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

from user import User
from recipe import Recipe

app = Flask(__name__)  

SWAGGER_URL = "/swagger"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    "/static/swagger.json",
    config={
        'app_name': 'Student Meal Express'
    }
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

@app.route("/")
def index():
    return """
    <p>Hello, Welcome to Student Meal Express!</p>
    <p>This is the final project for Database Management Systems (INFSCI 2710).</p>
    <p>The system was created by:</p><ul>
    <li>Arezou Farzaneh - arf111@pitt.edu</li>
    <li>Kun Zhang - kuz5@pitt.edu</li>
    <li>Rafaella Sampaio de Alencar - ras555@pitt.edu</li>
    </ul>
    Please go to "/swagger" or <a href="/swagger">click here</a> to test the endpoints."""

@app.route("/users/<user_id>", methods=['GET'])
def get_user(user_id):
    user = User()
    return jsonify(user.get_by_id(user_id))


@app.route('/recipes', methods=['GET'])
def get_recipes():
    recipes = Recipe()
    return jsonify(recipes.get_all())

app.run()
