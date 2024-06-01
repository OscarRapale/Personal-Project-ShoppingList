from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from forms import RegistrationForm, LoginForm

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'login'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from models import User, Category, Item, ShoppingListItem

        @login_manager.user_loader 
        def load_user(user_id):  #This callback is used to reload the user object from the user ID stored in the session 
            return User.query.get(int(user_id)) #Returns the user object


        @app.route("/")
        def home():
            return render_template("index.html")

        @app.route("/register", methods=["GET", "POST"]) #GET is used to request data from a specified resource. POST is used to submit data to a specified resource.
        def register(): #This function is used to register a new user
            form = RegistrationForm() #This is the form that the user will fill out to register
            if form.validate_on_submit(): 
                hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8") #Hashes the password
                user = User(username=form.username.data, password=hashed_password) #Creates a new user object
                db.session.add(user) #Adds the user to the database
                db.session.commit() 
                return redirect(url_for("login")) #Redirects the user to the login page
            return render_template("register.html", form=form) 


        @app.route("/login", methods=["GET", "POST"]) #This function is used to log in a user
        def login():
            form = LoginForm()
            if form.validate_on_submit():
                user = User.query.filter_by(username=form.username.data).first() #Queries the database for the user
                if user and bcrypt.check_password_hash(user.password, form.password.data): #Checks if the user exists and the password is correct
                    login_user(user, remember=form.remember.data) #Logs in the user
                    return redirect(url_for("home"))
            return render_template("login.html", form=form)


        @app.route("/logout") #This function is used to log out a user
        def logout():
            logout_user()
            return redirect(url_for("login"))


        @app.route("/categories")
        def categories():
            categories = Category.query.all() #Queries the database for all categories
            return render_template("categories.html", categories=categories)


        @app.route("/category/<int:category_id>")
        @login_required
        def category(category_id):
            category = Category.query.get_or_404(category_id) #Queries the database for the category
            return render_template("category.html", category=category, items=category.items)

        @app.route('/category/<int:category_id>/items')
        @login_required
        def category_items(category_id):
            category = Category.query.get_or_404(category_id)
            items = [{"id": item.id, "name": item.name} for item in category.items]
            return jsonify({"category": category.name, "items": items})

        @app.route("/update-item", methods=["POST"])
        @login_required
        def update_item():
            data = request.get_json() #Gets the JSON data from the request
            item_id = data["item_id"]
            checked = data["checked"]
            item = ShoppingListItem.query.filter_by(user_id=current_user.id, item_id=item_id).first()
            if item:
                item.checked = checked

            else:
                new_item = ShoppingListItem(user_id=current_user.id, item_id=item_id, checked=checked) #Creates a new shopping list item
                db.session.add(new_item)
            db.session.commit()
            return jsonify({"success": True})


        @app.route("/shopping-list")
        @login_required
        def shopping_list():
            shopping_list_items = ShoppingListItem.query.filter_by(user_id=current_user.id).all() #Queries the database for all shopping list items
            items = [item.item for item in shopping_list_items] #Gets the items from the shopping list items
            return render_template("shopping_list.html", items=items)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)