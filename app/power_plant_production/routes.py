from flask import request, jsonify
from flask_expects_json import expects_json
from .schemas import schema
from . import power_plant_production_bp


@power_plant_production_bp.route('/productionplain', methods=['POST'])
@expects_json(schema)
def power_plant_production():
    """
    API callback to calculate the power plants producions
    """

    # load json payload
    data = request.json

    target_load = data["load"]

    tota_plant_production = {plant["name"]: 0 for plant in data["powerplants"]}

    total_load = 0

    # load to calculate load
    while total_load != target_load:

        # loop to iterate over plants
        for plant in data["powerplants"]:

            # calculating pmax in function of the efficiency
            if "wind" in plant["name"]:
                plant["pmax"] = plant["pmax"]*(data["fuels"]["wind(%)"]/100)

            # if the sum of pmax´s plant and the total load calculated is less o equal than the target load, use the pmax
            if total_load+plant["pmax"] <= target_load:

                total_load += plant["pmax"]
                tota_plant_production[plant["name"]] = plant["pmax"]

            else:

                # if the sum of pmin´s plant and the total load calculated is equal than the target load, use the pmin
                if total_load+plant["pmin"] == target_load:

                    total_load += plant["pmin"]

                    tota_plant_production[plant["name"]] = plant["pmin"]

                # if the sum of pmin´s plant and the total load calculated is less than the target load, calculate the needed load between the target load and the total load calculated at the moment
                elif total_load+plant["pmin"] < target_load:

                    plant_power = target_load-total_load

                    total_load += plant_power

                    tota_plant_production[plant["name"]] += plant_power

    result = [{"name": k, "p": v} for k, v in tota_plant_production.items()]

    return jsonify(result)
