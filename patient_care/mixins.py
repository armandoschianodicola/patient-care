from django.conf import settings
from django.shortcuts import redirect
from urllib.parse import urlencode
import requests
import json


'''
Handles form error that are passed back to AJAX calls
'''


def FormErrors(*args):
    message = ""
    for f in args:
        if f.errors:
            message = f.errors.as_text()
    return message


'''
Used to append url parameters when redirecting users
'''


def RedirectParams(**kwargs):
    url = kwargs.get("url")
    params = kwargs.get("params")
    response = redirect(url)
    if params:
        query_string = urlencode(params)
        response['Location'] += '?' + query_string
    return response


class APIMixin:

    def __init__(self, *args, **kwargs):

        self.query = kwargs.get("query")
        self.cat = kwargs.get("cat")
        self.ingredient_id = kwargs.get('ingredient_id')

    def get_data(self):

        url_dict = {
            "recipes": "recipes/complexSearch?",
            "ingredients": "food/ingredients/search?",
            "ingredients-info": "food/ingredients/",
            "menuItems": "food/menuItems/search?",
            "products": "food/products/search?"
        }

        url = f"https://api.spoonacular.com/{url_dict[self.cat]}"

        if self.query:
            url += f'query={self.query}'

        if self.ingredient_id:
            url += f'{self.ingredient_id}/information?'

        url += f'&apiKey={settings.SA_API_KEY}'

        r = requests.get(url)
        if r.status_code == 200:
            try:
                return r.json()[self.cat]
            except KeyError:
                return r.json()['results']
        else:
            return None
