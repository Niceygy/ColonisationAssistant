from server.database.database import database, UserData
import json

def save(commodities, system_name, station_type, squadron):
    """Saves it to the db

    Args:
        commodities (str[]): commodities list
        system_name (str): system name as str
        station_type (str): station type as str
        squadron (str): squadron name as str

    Returns:
        int: the ID of the data
    """
    data = json.dumps(commodities)
    new_entry = UserData(
        system_name=system_name,
        jsondata=data,
        station_type=station_type,
        squadron=squadron
    )
    database.session.add(new_entry)
    database.session.commit()
    return new_entry.ID

def find(squadron):
    qry_res = database.session.query(
        UserData.jsondata, UserData.system_name
    ).filter(UserData.squadron == squadron).all()
    result = []
    for item in qry_res:
        result.append([item.system_name, item.id])
    return result

    
def load(ID):
    qry_res = database.session.query(
        UserData.jsondata, UserData.system_name, UserData.station_type
    ).filter(UserData.ID == ID).first()
    data = json.loads(qry_res.jsondata)
    return (data, qry_res.system_name, qry_res.station_type)
    
def update(ID, commodities):
    qry_res = database.session.query(
        UserData.jsondata, UserData.system_name
    ).filter(UserData.ID == ID).first()
    qry_res.jsondata = json.dumps(commodities)
    database.session.commit()

