import json
from flask import request
from flask_restful import Resource, marshal

from app.models import Recipe, Ingredient, Procedure
from app import db
from app.serializers import datetime_serial

from sqlalchemy.exc import SQLAlchemyError


class RecipesAPI(Resource):
    """View all recipes; add new recipe
    URL: /api/v1/recipes
    Request methods: POST, GET
    """

    def get(self):
        recipes = Recipe.query.all()
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

        return json.dumps(response, default=datetime_serial), 200

    def post(self):
        # if request contains only site_url, get information from site_url.
        data = json.loads(request.data.decode('utf-8'))
        recipe = Recipe(user_id=data["user_id"],
                        name=data["name"],
                        site_url=data["site_url"],
                        image_url=data["image_url"])

        try:
            db.session.add(recipe)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error": str(e.__dict__['orig'])}, 400

        recipe_id = recipe.recipe_id

        if "ingredients" in data.keys():
            for d in data["ingredients"]:
                print(d)
                ingredient = Ingredient(recipe_id=recipe_id,
                                        name=d["name"])
                try:
                    db.session.add(ingredient)
                    db.session.commit()
                except SQLAlchemyError as e:
                    db.session.rollback()
                    return {"error": str(e.__dict__['orig'])}, 400

        if "procedures" in data.keys():
            for d in data["procedures"]:
                procedure = Procedure(recipe_id=recipe_id,
                                      name=d["name"])
                try:
                    db.session.add(procedure)
                    db.session.commit()
                except SQLAlchemyError as e:
                    db.session.rollback()
                    return {"error": str(e.__dict__['orig'])}, 400

        return {"success": "you successfully created a new recipe"}, 201


class RecipeAPI(Resource):
    """View, update and delete a single student.
    URL: /api/v1/recipes/<id>
    Request methods: GET, PUT, DELETE
    """

    def get(self, id):
        recipe = Recipe.query.filter(Recipe.recipe_id==id).first()
        if recipe is None:
            return {"error": "There is not such recipe. Please request by a correct id."}

        response = {}
        ingredients = [{"ingredient_id": ingredient.ingredient_id,
                        "recipe_id": ingredient.recipe_id,
                        "name": ingredient.name}
                       for ingredient in Ingredient.query.filter(
                Ingredient.recipe_id == recipe.recipe_id).all()]
        procedures = [{"procedure_id": procedure.procedure_id,
                       "recipe_id": procedure.recipe_id,
                       "name": procedure.name}
                      for procedure in Procedure.query.filter(
                Procedure.recipe_id == recipe.recipe_id).all()]

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

    def put(self, id):
        data = json.loads(request.data.decode('utf-8'))
        recipe = Recipe.query.filter_by(recipe_id=id).first()

        if recipe:
            for key in ["user_id", "name", "site_url", "image_url"]:
                if key in data.keys():
                    if data[key] is not None and data[key] != '':
                        setattr(recipe, key, data[key])
            try:
                db.session.add(recipe)
                db.session.commit()
            except SQLAlchemyError as e:
                db.session.rollback()
                return {"error": str(e.__dict__['orig'])}, 400
        else:
            return {"error": "There is no such recipe."}, 400

        if "ingredients" in data.keys():
            for d in data["ingredients"]:
                print(d)
                if d["ingredient_id"] is not None:
                    ingredient = Ingredient.query.filter_by(ingredient_id=d["ingredient_id"]).first()
                    if ingredient:
                        print('hi, i found ingredient.')
                        for key in ["recipe_id", "name"]:
                            if d[key] is not None and d[key] != '':
                                setattr(ingredient, key, d[key])
                    else:
                        ingredient = Ingredient(recipe_id=id, name=d["name"])
                else:
                    ingredient = Ingredient(recipe_id=id, name=d["name"])

                print('============ingredient============== \n ', ingredient)

                try:
                    db.session.add(ingredient)
                    db.session.commit()
                except SQLAlchemyError as e:
                    db.session.rollback()
                    return {"error": str(e.__dict__['orig'])}, 400

        if "procedures" in data.keys():
            for d in data["procedures"]:
                if d["procedure_id"] is not None:
                    procedure = Procedure.query.filter_by(procedure_id=d["procedure_id"]).first()
                    if procedure:
                        print('hi, i found procedure')
                        for key in ["recipe_id", "name"]:
                            if d[key] is not None and d[key] != '':
                                setattr(procedure, key, d[key])
                    else:
                        procedure = Procedure(recipe_id=id, name=d["name"])
                else:
                    procedure = Procedure(recipe_id=id, name=d["name"])

                print('============procedure============== \n ', procedure)

                try:
                    db.session.add(procedure)
                    db.session.commit()
                except SQLAlchemyError as e:
                    db.session.rollback()
                    return {"error": str(e.__dict__['orig'])}, 400

        return {"message": "You have successfully updated a recipe."}, 201

    def delete(self, id):
        try:
            db.session.query(Ingredient).filter(Ingredient.recipe_id==id).delete()
            db.session.query(Procedure).filter(Procedure.recipe_id==id).delete()
            db.session.query(Recipe).filter(Recipe.recipe_id==id).delete()
            db.session.commit()

        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error": str(e.__dict__['orig'])}, 400

        return {"message": "You have successfully delete a record."}