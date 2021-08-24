from flask import Blueprint

#Define the blueprint variable for this module
power_plant_production_bp = Blueprint('productionplain',__name__)
from . import routes