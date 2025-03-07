from server.constants import STATION_TYPES
import json

def get_required_items(station_type: str):
    if station_type in STATION_TYPES:
        #valid type
        rawdata = open("../../static/data/data.json").read()
        jsondata = json.loads(rawdata)
        commodities = jsondata[station_type]
        result = []
        for item, value in commodities.items():
            if value != "0":
                result.append([item, int(value)])
        return value