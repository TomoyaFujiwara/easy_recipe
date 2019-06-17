from app import api, app
from app.resources.recipe import RecipeAPI, RecipesAPI
from app.resources.user import UserAPI


""" Defining the API endpoints """
api.add_resource(RecipesAPI, "/recipes")
api.add_resource(RecipeAPI, "/recipes/<int:id>")
api.add_resource(UserAPI, "/users/<string:id>")

if __name__ == '__main__':
    app.run()
