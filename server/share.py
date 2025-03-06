from server.database.database import database, UserData

def save_to_share(data, system_name):
    new_entry = UserData(
        system_name=system_name,
        jsondata=data
    )
    database.session.add(new_entry)
    database.session.commit()
    return new_entry.ID

def load(ID):
    qry_res = UserData.query(
        UserData.jsondata, UserData.system_name
    ).filter(ID=ID).first()
    return (qry_res.jsondata, qry_res.system_name)