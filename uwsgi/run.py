from app import api, app
from app.resources.recipe import RecipeAPI, RecipesAPI


""" Defining the API endpoints """
api.add_resource(RecipesAPI, "/recipes")
api.add_resource(RecipeAPI, "/recipes/<string:id>")

if __name__ == '__main__':
    app.run()
