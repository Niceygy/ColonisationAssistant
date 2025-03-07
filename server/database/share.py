from server.database.database import database, UserData
import json

def save_to_share(commodities, system_name):
    """Saves it to the db

    Args:
        commodities (str[]): commdites list
        system_name (str): system name as str

    Returns:
        int: the ID of the data
    """
    data = json.dumps(commodities)
    new_entry = UserData(
        system_name=system_name,
        jsondata=data
    )
    database.session.add(new_entry)
    database.session.commit()
    return new_entry.ID

def load(ID):
    qry_res = database.session.query(
        UserData.jsondata, UserData.system_name
    ).filter(UserData.ID == ID).first()
    data = json.dumps(qry_res.jsondata)  # Ensure commodities are encoded as JSON string
    commodities = str(json.loads(data))
    commodities = commodities.replace("[", "").replace("]", "").replace('"', '').split(",")  # Decode JSON string back into array
    return (commodities, qry_res.system_name)

def update_shared(ID, commodities, system_name):
    qry_res = database.session.query(
        UserData.jsondata, UserData.system_name
    ).filter(UserData.ID == ID).first()
    