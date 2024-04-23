from flask import Flask, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint

from user import User
from recipe import Recipe
from tag import Tag

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

# Users

@app.route('/users/all', methods=['GET'])
def get_users():
    user = User()
    return jsonify(user.get_all())

@app.route("/users", methods=['GET'])
def get_user():
    user_id = request.args.get('user_id')
    user = User()
    return jsonify(user.get_by_id(user_id))

@app.route('/users', methods=['POST'])
def create_user():
    user_data = request.get_json()
    user = User(user_data.get("user_id"), user_data.get("username"), user_data.get("email"), 
                     user_data.get("password_hash"), user_data.get("join_date"), user_data.get("is_active"))
    return jsonify(user.create())

@app.route('/users', methods=['PUT'])
def update_user():
    user_data = request.get_json()
    user = User(user_data.get("user_id"), user_data.get("username"), user_data.get("email"), 
                     user_data.get("password_hash"), user_data.get("join_date"), user_data.get("is_active"))
    return jsonify(user.update())

@app.route('/users', methods=['DELETE'])
def delete_user():
    user_id = request.args.get('user_id')
    user = User()
    return jsonify(user.delete(user_id))

# Recipes

@app.route('/recipes/all', methods=['GET'])
def get_recipes():
    recipe = Recipe()
    return jsonify(recipe.get_all())

@app.route("/recipes", methods=['GET'])
def get_recipe_by_id():
    recipe_id = request.args.get('recipe_id')
    recipe = Recipe()
    return jsonify(recipe.get_by_id(recipe_id))

@app.route('/recipes', methods=['POST'])
def create_recipe():
    recipe_data = request.get_json()
    recipe = Recipe(recipe_data.get("recipe_id"), recipe_data.get("title"), recipe_data.get("description"), 
                     recipe_data.get("creation_date"), recipe_data.get("cook_time"), recipe_data.get("serving_size"),
                     recipe_data.get("created_by"))
    return jsonify(recipe.create())

@app.route('/recipes', methods=['PUT'])
def update_recipe():
    recipe_data = request.get_json()
    recipe = Recipe(recipe_data.get("recipe_id"), recipe_data.get("title"), recipe_data.get("description"), 
                     recipe_data.get("creation_date"), recipe_data.get("cook_time"), recipe_data.get("serving_size"),
                     recipe_data.get("created_by"))
    return jsonify(recipe.update())

@app.route('/recipes', methods=['DELETE'])
def delete_recipe():
    recipe_id = request.args.get('recipe_id')
    recipe = Recipe()
    return jsonify(recipe.delete(recipe_id))

# Tags

@app.route('/tags/all', methods=['GET'])
def get_tags():
    tags = Tag()
    return jsonify(tags.get_all())

@app.route("/tags", methods=['GET'])
def get_tag_by_id():
    tag_id = request.args.get('tag_id')
    tags = Tag()
    return jsonify(tags.get_by_id(tag_id))

@app.route('/tags', methods=['POST'])
def create_tag():
    tag_data = request.get_json()
    tags = Tag(tag_data.get("tag_id"), tag_data.get("name"), tag_data.get("description"))
    return jsonify(tags.create())

@app.route('/tags', methods=['PUT'])
def update_tag():
    tag_data = request.get_json()
    tags = Tag(tag_data.get("tag_id"), tag_data.get("name"), tag_data.get("description"))
    return jsonify(tags.update())

@app.route('/tags', methods=['DELETE'])
def delete_tag():
    tag_id = request.args.get('tag_id')
    tags = Tag()
    return jsonify(tags.delete(tag_id))

if __name__=="__main__":
    app.run(debug=True)