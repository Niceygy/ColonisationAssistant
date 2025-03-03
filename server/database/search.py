from server.database.database import StarSystem
from sqlalchemy import func


def query_star_systems(query):
    """"
    Returns a list of 10 systems that roughtly match the query by name.

    Expects: 
        - [String]
    """
    results = (
        StarSystem.query.filter(StarSystem.system_name.ilike(f"%{query}%"))
        .limit(10)
        .all()
    )
    
    try:
        if results != []:
            return [row.system_name for row in results]
        else:
            return ["No System Found"]
    except Exception:
        return ["No System Found"]
    

def find_systems_within_range(system_name, range_units, session):
    """
    Finds systems within a specified range of a given system.

    Expects:
        - [String] system_name: The name of the reference system
        - [Float] range_units: The range within which to find other systems
        - [Session] session: The current database session

    Returns:
        - [List] List of system names within the specified range
    """
    reference_system = session.query(StarSystem).filter(StarSystem.system_name == system_name).first()
    if not reference_system:
        return []

    latitude = reference_system.latitude
    longitude = reference_system.longitude
    height = reference_system.height

    distance_formula = func.sqrt(
        func.pow(StarSystem.latitude - latitude, 2) +
        func.pow(StarSystem.longitude - longitude, 2) +
        func.pow(StarSystem.height - height, 2)
    )

    results = session.query(StarSystem.system_name).filter(distance_formula <= range_units).all()
    return [row.system_name for row in results]