
schema = {
    'type': 'object',
    "description":"Schema to request production plains",
    'properties': {
        "load":{
            "type":"integer",
            "description":"Maximun load allowed",
            "minimum":0
        },
        "fuels":{
            "type":"object",
            "description":"Fuels cost provided",
            "properties":{
                "":{
                    "type":"number",
                    "description":"Fuel cost provided",
                    "minimum":0
                }
            }
        },
        "powerplants":{
            "type":"array",
            "description":"List with the power plant",
            "items":{
                "type":"object",
                "description":"Plant definition",
                "properties":
                {
                    "name":{
                        "type":"string",
                        "description":"Plant name",
                        "minlength":4
                    },
                    "type":{
                        "type":"string",
                        "description":"Plant type",
                        "minlength":4
                    },
                    "eficiency":{
                        "type":"number",
                        "description":"Plant efficiency",
                        "minimum":0
                    },
                    "pmin":{
                        "type":"integer",
                        "description":"Minimun power produced by plant",
                        "minimum":0
                    },
                    "pmax":{
                        "type":"integer",
                        "description":"Maximum power produced by plant",
                        "minimum":0
                    }
                },
                "additionalProperties":False,
                "required":["name","type","efficiency","pmin","pmax"]                
            },
            "minItems":1
        }
        
    },
    'required': ['load', 'fuels',"powerplants"],
    "additionalProperties":False
}