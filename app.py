from flask import Flask, jsonify, render_template, request, redirect
from random import randint

app = Flask(__name__)

@app.route("/")
def home():
  return jsonify(message="Hello World")

@app.route("/greeting")
def greeting():
  return render_template("index.html", name="Anna and Sarah")

@app.route("/pie")
def pie():
  ingredients_list = ["apples", "cherries", "pumpkins", "pecans", "chocolate", "limes", "custard"]
  return jsonify({"pie ingredient": ingredients_list[randint(0, len(ingredients_list) - 1)]})


ingredients_list = ["Sugar", "Butter", "Flour", "Baking Soda"]

@app.route("/recipe", methods=["GET", "POST"])
def recipe():
  global ingredients_list

  if request.method == "GET":
    pie_list = ["Apple", "Cherry", "Pumpkin", "Pecan", "Boston Creme", "Key Lime"]
    pie_idx = randint(0, len(pie_list) -1)
    ingredients_list.append(pie_list[pie_idx])
    ingred_list_len = len(ingredients_list)
    return render_template("recipe.html", pie=pie_list[pie_idx], ingredients=ingredients_list, len=ingred_list_len)

  new_ingredient = request.form["new-ingredient"]
  pie_type = request.form["pie-type"]
  ingredients_list.append(new_ingredient.capitalize())

  return redirect(f"/recipe/{pie_type}")

@app.route("/recipe/<pie>", methods=["GET", "POST"])
def specific_recipe(pie):
  global ingredients_list
  if request.method == "GET":
    ingred_list_len = len(ingredients_list)
    return render_template("recipe.html", pie=pie, ingredients=ingredients_list, len=ingred_list_len)

  new_ingredient = request.form["new-ingredient"]
  ingredients_list.append(new_ingredient.capitalize())

  return redirect(f"/recipe/{pie}")
    

if __name__ == "__main__":
  app.run()