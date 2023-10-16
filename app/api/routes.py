from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Recipe, recipe_schema, recipes_schema

api = Blueprint('api',__name__, url_prefix='/api')


@api.route('/recipes', methods = ['POST'])
@token_required
def create_recipe(current_user_token):
    title = request.json['title']
    contributor = request.json['contributor']
    ingredients = request.json['ingredients']
    instructions = request.json['instructions']
    user_token = current_user_token.token

    recipe = Recipe(title, contributor, ingredients, instructions, user_token = user_token )

    db.session.add(recipe)
    db.session.commit()

    response = recipe_schema.dump(recipe)
    return jsonify(response)

@api.route('/recipes', methods = ['GET'])
@token_required
def get_recipes(current_user_token):
    a_user = current_user_token.token
    recipes = Recipe.query.filter_by(user_token = a_user).all()
    response = recipes_schema.dump(recipes)
    return jsonify(response)

@api.route('/recipes/<id>', methods = ['GET'])
@token_required
def get_single_recipe(current_user_token, id):
    recipe = Recipe.query.get(id)
    response = recipe_schema.dump(recipe)
    return jsonify(response)

@api.route('/recipes/<id>', methods = ['POST','PUT'])
@token_required
def update_recipe(current_user_token,id):
    recipe = Recipe.query.get(id) 
    recipe.title = request.json['title']
    recipe.contributor = request.json['contributor']
    recipe.ingredients = request.json['ingredients']
    recipe.instructions = request.json['instructions']
    recipe.user_token = current_user_token.token

    db.session.commit()
    response = recipe_schema.dump(recipe)
    return jsonify(response)

@api.route('/recipes/<id>', methods = ['DELETE'])
@token_required
def delete_recipe(current_user_token, id):
    recipe = Recipe.query.get(id)
    db.session.delete(recipe)
    db.session.commit()
    response = recipe_schema.dump(recipe)
    return jsonify(response)

