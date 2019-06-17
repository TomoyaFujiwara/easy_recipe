#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json

url_base='http://127.0.0.1:5000'

def get_recipes_api():
    response = requests.get(url_base+'/api/v1/recipes')
    print(response)

def post_recipes_api():
    post = {'user_id': 'test_id',
            'name': '肉じゃが',
            'site_url': 'http://test_site.com',
            'image_url': 'http://test_image.com',
            'ingredients':[
                {'name': 'じゃがいも'},
                {'name': 'にんじん'}],
            'procedures': [
                {'name': '牛肉を炒める'},
                {'name': '野菜を煮込む'}]
            }

    response = requests.post(url_base+'/api/v1/recipes', json.dumps(post))
    print(response)

def get_user_api():
    response = requests.get(url_base+'/api/v1/users/test_id')
    print(response)

def get_recipe_api():
    response = requests.get(url_base+'/api/v1/recipes/8')
    print(response)

def put_recipe_api():
    put = {'user_id': 'test_update_id',
           'name': 'カレー',
           'site_url': 'http://test_site_update.com',
           'image_url': 'http://test_image_update.com',
           'ingredients':[
                {'ingredient_id': 11, 'name': 'カレールーの素', 'recipe_id': 8},
                {'ingredient_id': 12, 'name': '牛肉', 'recipe_id': 8}],
           'procedures': [
                {'procedure_id': 1, 'name': 'てすと', 'recipe_id': 8},
                {'procedure_id': 2, 'name': 'ほげほげ', 'recipe_id': 8}]
           }
    response = requests.put(url_base+'/api/v1/recipes/8', json.dumps(put))
    print(response)

def delete_recipe_api():
    response = requests.delete(url_base+'/api/v1/recipes/12')
    print(response)


def main():
    post_recipes_api()
    get_recipes_api()
    get_user_api()
    get_recipe_api()
    put_recipe_api()
    get_recipe_api()
    # delete_recipe_api()


if __name__=='__main__':
    main()