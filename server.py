from flask import Flask, render_template, redirect, request
app = Flask(__name__)

# bring in the model file to talk to it
from dog_model import Dog

# ---- READ ALL ---- dashboard
@app.route("/")
def index():
    all_dogs = Dog.get_all()
    return render_template("dashboard.html", 
                           all_dogs = all_dogs)

# ---- CREATE RENDER page -----
# /tablename/?id?/action
# localhost:5000/dogs/create
@app.route("/dogs/create_page")
def create_form_page():
    return render_template("dog_new.html")

# --- CREATE METHOD (ACTION) -----
@app.route("/dogs/create", methods = ['post'])
def create_dog_action():
    print("\n >>>>> request.form <<<<<\n", request.form)
    new_dog_id = Dog.create(request.form)
    print(new_dog_id)
    return redirect("/dogs/create_page")


# ----- READ ONE PAGE ------
@app.route("/dogs/<int:id>")
def one_dog_page(id):
    this_dog = Dog.get_one(id)
    return render_template("dog_show_one.html", 
                           this_dog=this_dog)


# ----- UPDATE PAGE ------
@app.route("/dogs/<int:id>/update")
def update_dog_page(id):
    this_dog = Dog.get_one(id)
    return render_template("dog_update.html", 
                           this_dog = this_dog)

# --- UPDATE ACTION ------
@app.route("/dogs/<int:id>/update_action", methods=['post'])
def update_dog_action(id):
    print("<><><><><><><>", request.form)
    # prepare the data dict
    data = {
        **request.form,
        'id' : id
    }
    Dog.update(data)
    return redirect(f"/dogs/{id}")

if __name__ == "__main__":
    app.run(debug=True)