from flask_app import app
from flask_app.controllers import controller_ninja, controller_dojo


if __name__ == "__main__":
    app.run(debug=True)