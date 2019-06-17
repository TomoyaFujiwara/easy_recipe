import json
from flask_restful import Resource

from app.models import Recipe, Ingredient, Procedure
from app.serializers import datetime_serial



class UserAPI(Resource):
    """View a User.
    URL: /api/v1/users/<id>
    Request methods: GET
    """

    def get(self, id):
        recipes = Recipe.query.filter(Recipe.user_id==id)
        if recipes is None:
            return {"error": "There is not such recipe. Please request by a correct id."}

        response = {}
        for recipe in recipes:
            ingredients = [{"ingredient_id": ingredient.ingredient_id,
                            "recipe_id": ingredient.recipe_id,
                            "name": ingredient.name}
                            for ingredient in Ingredient.query.filter(
                                              Ingredient.recipe_id==recipe.recipe_id).all()]
            procedures = [{"procedure_id": procedure.procedure_id,
                           "recipe_id": procedure.recipe_id,
                           "name": procedure.name}
                           for procedure in Procedure.query.filter(
                                            Procedure.recipe_id==recipe.recipe_id).all()]

            response["recipe_{}".format(recipe.recipe_id)] \
                = {"user_id": recipe.user_id,
                   "name": recipe.name,
                   "site_url": recipe.site_url,
                   "image_url": recipe.image_url,
                   "created_at": recipe.created_at,
                   "updated_at": recipe.updated_at,
                   "ingredients": ingredients,
                   "procedures": procedures}

        print(response)
        return json.dumps(response, default=datetime_serial), 200