from django.test import TestCase
from django.urls import resolve, reverse

from .views import category, home, recipe

# Create your tests here.

class RecipeViewTest(TestCase):
    def test_recipe_home_views_function_is_correct(self):
        view = resolve(reverse('/'))
        self.assertIs(view.func, home)

    def test_recipe_category_views_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, category)

    def test_recipe_detail_views_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, recipe)
