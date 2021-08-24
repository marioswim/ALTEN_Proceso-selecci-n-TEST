from flask import Flask

#declare Flask app
app = Flask(__name__)
    

# register blueprints
from power_plant_production import power_plant_production_bp
app.register_blueprint(power_plant_production_bp)


if __name__ == "__main__":
    app.run()