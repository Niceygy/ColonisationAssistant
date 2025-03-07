from server.constants import STATION_TYPES
import json, os

def get_required_items(station_type: str):
    if station_type in STATION_TYPES:
        #valid type
        # print(f"{os.getcwd()}")
        rawdata = open(f"{os.getcwd()}/static/data/data.json").read()
        jsondata = json.loads(rawdata)
        commodities = jsondata[station_type]
        result = []
        for item, value in commodities.items():
            if value != "0":
                result.append([item, int(value)])
        return result