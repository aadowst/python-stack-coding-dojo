
from flask_app import app, bcrypt
from flask import render_template, redirect, request, session

from flask_app.models.model_recipe import Recipe
from flask_app.models import model_user


# Display
@app.route('/recipes/new')
def add_recipe_display():
    if "user_id" not in session:
        return redirect('/')
    return render_template("newrecipe.html")

# Action
@app.route('/submitnew', methods=["POST"])
def add_recipe_action():
    recipe = {
        **request.form,
        "user_id": session["user_id"]
    }
    if not Recipe.validate_input(recipe):
        return redirect ('/recipes/new')

    Recipe.save_recipe(recipe)
    return redirect("/recipes")


@app.route('/recipes')
def all_recipes():
    if "user_id" not in session:
        return redirect('/')
    model_user.User.get_one({"id": session["user_id"]})
    all_recipes = Recipe.get_all_recipes()
    return render_template("recipes.html", all_recipes = all_recipes)



@app.route('/recipes/<int:id>')
def one_recipe(id):
    if "user_id" not in session:
        return redirect('/')
    one_recipe = Recipe.get_one_recipe({"id": id})
    return render_template("onerecipe.html", one_recipe=one_recipe)

@app.route('/recipes/edit/<int:id>')
def edit_one_display(id):
    if "user_id" not in session:
        return redirect('/')
    one_recipe = Recipe.get_one_recipe({"id": id})
    return render_template("editrecipe.html", one_recipe=one_recipe)

@app.route('/recipes/<int:id>/update', methods=["post"])
def edit_one_action(id):
    if "user_id" not in session:
        return redirect('/')

    dict = {
        **request.form,
        "id": id,
        "user_id": session["user_id"]
    }
    if not Recipe.validate_input(dict):
        return redirect (f'/recipes/edit/{id}')

    Recipe.edit_recipe_action(dict)
    return redirect('/recipes')

@app.route('/recipes/delete/<int:id>')
def delete_one(id):
    Recipe.delete({"id":id})
    return redirect('/recipes')
