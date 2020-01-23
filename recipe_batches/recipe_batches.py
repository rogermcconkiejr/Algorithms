#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  min_ingredients = []
  # Check to make sure that ingredients in both lists match.
  if ingredients.keys() != recipe.keys():
    print("You don't have any of at least one ingredient!")
    return 0
  else:
    # Divide available ingredients by required ingredients, append to list.
    for key in recipe.keys():
      min_ingredients.append(ingredients[key] // recipe[key])
    # Check list to make sure that minimum requirements are met.
      return min(min_ingredients)

  


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 100, 'butter': 500, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))


  recipe_batches(recipe, ingredients)