import json
from flask_restful import Resource, marshal

from app.models import Recipe, Ingredient, Procedure
from app import db

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
                            for ingredient in Ingredient.query.filter_by(
                                              Ingredient.recipe_id==recipe.id)]
            procedures = [{"procedure_id": procedure.ingredient_id,
                            "recipe_id": procedure.recipe_id,
                            "name": procedure.name}
                            for procedure in Procedure.query.filter_by(
                                             Procedure.recipe_id==recipe.id)]
            response["recipe_{}".format(recipe.id)] = {"user_id": recipe.user_id,
                                                       "name": recipe.name,
                                                       "site_url": recipe.site_url,
                                                       "image_url": recipe.image_url,
                                                       "created_at": recipe.created_at,
                                                       "updated_at": recipe.updated_at,
                                                       "ingredients": ingredients,
                                                       "procedures": procedures}
        return json.dumps(response), 200

    def post(self):
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
        q = db.session.query(Recipe, Ingredient, Procedure). \
            outerjoin(Ingredient, Recipe.recipe_id==Ingredient.ingredient_id). \
            outerjoni(Procedure, Recipe.recipe_id==Procedure.procedure_id). \
            filter(Recipe.recipe_id==id).all()
        return q

    def put(self, id):
        data = json.load(request.json)
        recipe = Recipe.query.filter_by(recipe_id=id).first()

        if recipe:
            for key in ["user_id", "name", "site_url", "image_url"]:
                if key in data.keys():
                    if data[key] is not None: # is not None or !=''
                        setattr(recipe, key, data[key])
            try:
                db.session.add(recipe)
                db.session.commit()
            except:
                return {"error": "An error occurred."}, 400
        else:
            return {"error": "There is no such recipe."}, 400

        if "ingredients" in data.keys():
            for d in data["ingredients"]:
                ingredient = Ingredient.query.filter_by(ingredient_id=d["ingredient_id"]).first()

                if ingredient:
                    for key in ["recipe_id", "name"]:
                        if d[key] is not None:
                            setattr(ingredient, key, d[key])
                else:
                    ingredient = Ingredient(recipe_id=id,
                                            name=d["name"])

                try:
                    db.session.add(ingredient)
                    db.session.commit()
                except:
                    return {"error": "An error occurred."}, 400

        if "procedures" in data.keys():
            for d in data["procedures"]:
                procedure = Ingredient.query.filter_by(ingredient_id=d["procedure_id"]).first()

                if procedure:
                    for key in ["recipe_id", "name"]:
                        if d[key] is not None:
                            setattr(procedure, key, d[key])
                else:
                    procedure = Procedure(recipe_id=id,
                                          name=d["name"])

                try:
                    db.session.add(procedure)
                    db.session.commit()
                except:
                    return {"error": "An error occurred."}, 400

        response = marshal(data)
        message = {"message": "You have successfully updated a record."}
        response.update(message)

        return response, 201

    def delete(self, id):
        try:
            db.session.query(Ingredient).filter(Ingredient.recipe_id==id).delete()
            db.session.query(Procedure).filter(Procedure.recipe_id==id).delete()
            db.session.query(Recipe).filter(Recipe.recipe_id==id).delete()
            db.session.commit()

        except:
            return {"error": "An error occurred."}, 400

        return {"message": "You have successfully delete a record."}