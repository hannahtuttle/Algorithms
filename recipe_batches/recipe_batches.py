#!/usr/bin/python
#receives a recipe in the form of a dictionary, as well as all of the ingredients you have available to you, also in the form of a dictionary. Both of these dictionaries will have the same form, and might look something like this:
#                 {'eggs': 5, 'butter': 10, 'sugar': 8, 'flour': 15}

# The keys will be the ingredient names, with their associated values being the amounts. In the case of the recipe dictionary, these amounts will represent the amount of each ingredient needed for the recipe, while in the case of the ingredients dictionary, the amounts represent the amounts available to you. 

# Your function should output the maximum number of whole batches that can be made for the supplied recipe using the ingredients available to you, as indicated by the second dictionary. 


# # should return 0 since we don't have enough butter!
# recipe_batches(
#   { 'milk': 100, 'butter': 50, 'flour': 5 },
#   { 'milk': 138, 'butter': 48, 'flour': 51 }
# )

    # understand: The function takes in two dictionaries that have the same keys. Each key has an integer which an amount of what you need or what you have. you need to compare the two dictionaries and see if you have enough from the ingredient dictionary to make the recipe and how many times (batches) you can make from the values of those dictionaries. then you need to return the amount of batches.

    # plan: 
      # have a place holder arr for the outcomes of the values  
      # create a batches place holder
      # you need to loop through the ingredients arr once and devide the values of the ingredients by the value of the recipe.
      # add the devided values to the place holder arr make sure the values are rounded down so if the value is less than one it becomes zero.
      # find the smallest value in the place holder array and set it to batches.
      # return batches


import math

def recipe_batches(recipe, ingredients):
  divided = []

  for k in recipe:
    if k in ingredients:
      divided.append(ingredients[k]//recipe[k])
    else:
      divided.append(0)

  
  batches = min(divided)

  return batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }
  ingredients = { 'milk': 1288, 'flour': 9, 'sugar': 95 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))