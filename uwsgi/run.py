from app import api, app
from app.resources.recipe import RecipeAPI, RecipesAPI
from app.resources.user import UserAPI
from flask import render_template, Flask


""" Defining the API endpoints """
api.add_resource(RecipesAPI, "/recipes")
api.add_resource(RecipeAPI, "/recipes/<int:id>")
api.add_resource(UserAPI, "/users/<string:id>")

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
