from datetime import datetime
from app import app, db

class Recipe(db.Model):
    __tablename__ = "recipe"

    recipe_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(128)) # Google Oath id

    name = db.Column(db.String(50))
    site_url = db.Column(db.String(128))
    image_url = db.Column(db.String(128))

    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.now)

    def __repr__(self):
        return "<recipe_id: {}, " \
               "user_id: {}, " \
               "name: {}, " \
               "site_url: {}, " \
               "image_url: {}, " \
               "created_at: {}, " \
               "updated_at: {}>".format(
                self.recipe_id, self.user_id, self.name,
                self.site_url, self.image_url, self.created_at, self.updated_at)

class Ingredient(db.Model):
    __tablename__ = "ingredient"

    ingredient_id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipe.recipe_id"))
    name = db.Column(db.String(128))

    def __repre__(self):
        return "<ingredient_id: {}, recipe_id: {}, name: {}>".format(
                self.ingredient_id, self.recipe_id, self.name)

class Procedure(db.Model):
    __tablename__ = "procedure"

    procedure_id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipe.recipe_id"))
    name = db.Column(db.String(128))

    def __repre__(self):
        return "<procedure_id: {}, recipe_id: {}, name: {}>".format(self.procedure_id, self.recipe_id, self.name)


