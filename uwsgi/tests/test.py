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

    print(json.dumps(post))
    response = requests.post(url_base+'/api/v1/recipes', json.dumps(post))
    print(response)

def main():
    post_recipes_api()
    get_recipes_api()

if __name__=='__main__':
    main()