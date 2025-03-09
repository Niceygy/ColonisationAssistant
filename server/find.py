import math
from sqlalchemy import func

from server.constants import WHAT_MAKES_THIS, CONSTANT_BUY_LOCATIONS
from server.database.database import Station, StarSystem, database


def system_coordinates(system_name, database):
    """
    Gets the coordinates for a system

    Requires:
        - [String] system_name: The name of the system
        - [Object] database: The current database connection.

    Returns:
        - [int[]] Coordinates: [latitude, longitude, height]
    """
    result = (
        database.session.query(
            StarSystem.latitude, StarSystem.longitude, StarSystem.height
        )
        .filter(StarSystem.system_name == system_name)
        .first()
    )

    if result == [None, None, None] or result == None:
        print(f"?? for {system_name}")
        return [None, None, None]

    return [result.latitude, result.longitude, result.height]


def distance_to_system(start_system, end_system, database):
    """
    How far is it from start_system to end_system? In LY
    """
    [startx, starty, startz] = system_coordinates(start_system, database)
    [endx, endy, endz] = system_coordinates(end_system, database)

    if (
        startx == None
        or endx == None
        or starty == None
        or endy == None
        or startz == None
        or endz == None
    ):
        return 0

    # diffrences
    xdist = endx - startx
    ydist = endy - starty
    zdist = endz - startz

    # square them
    xdistSqr = xdist * xdist
    ydistSqr = ydist * ydist
    zdistSqr = zdist * zdist

    # add them all
    sumOfSqares = xdistSqr + ydistSqr + zdistSqr

    distance = math.sqrt(sumOfSqares)

    return distance


def find_stations(commodity_list, user_location):
    # make a list of each type we need
    result = {}
    for key, value in commodity_list:
        if not key in WHAT_MAKES_THIS:
            print(key)
            continue
        station_type = WHAT_MAKES_THIS[key]
        if station_type[0] == "Constant":
            buy_locations = CONSTANT_BUY_LOCATIONS[key]
            buy_systems = []
            for location in buy_locations:
                buy_systems.append(location.split("/")[0])
            nearest_station = find_nearest_station(
                station_type[1:], user_location, buy_systems
            )
            result[key] = [nearest_station, value]
        else:
            nearest_station = find_nearest_station(station_type, user_location, None)
            result[key] = [nearest_station, value]
    # copper = [Dadeleus, 400]
    return result


def find_nearest_station(economy: list[str], user_location: str, system_list: list = None):
    """Finds the nearest station for that economy from a set list of systems

    Args:
        economy (str): the economy. see WHAT_MAKES_THIS
        user_location (str): user location (e.g Sol)
        system_list (list): list of systems to consider

    Returns:
        (station name, system name)
    """
    user_coords = system_coordinates(user_location, database)
    if len(economy) > 1:
        economy = economy[1]
    else:
        economy = economy[0]

    if None in user_coords:
        return
    (userx, usery, userz) = user_coords

    distance_formula = func.sqrt(
        func.pow(StarSystem.latitude - userx, 2)
        + func.pow(StarSystem.longitude - usery, 2)
        + func.pow(StarSystem.height - userz, 2)
    )

    if system_list:
        filter_condition = StarSystem.system_name.in_(system_list)
    else:
        filter_condition = True

    nearest_station = None
    if "/" in economy:
        location = economy.split("/")[1]
        economy = economy.split("/")[0]
        nearest_station = (
            database.session.query(
                Station.station_name,
                Station.star_system,
                distance_formula.label("distance"),
            )
            .join(StarSystem, Station.star_system == StarSystem.system_name)
            .filter(
                Station.economy == economy,
                Station.station_type == location,
                filter_condition,
            )
            .order_by(distance_formula)
            .first()
        )
    elif "!" in economy:
        #all but
        nearest_station = (
            database.session.query(
                Station.station_name,
                Station.star_system,
                distance_formula.label("distance"),
            )
            .join(StarSystem, Station.star_system == StarSystem.system_name)
            .filter(Station.economy != economy, filter_condition)
            .order_by(distance_formula)
            .first()
        )
    else:
        nearest_station = (
            database.session.query(
                Station.station_name,
                Station.star_system,
                distance_formula.label("distance"),
            )
            .join(StarSystem, Station.star_system == StarSystem.system_name)
            .filter(Station.economy == economy, filter_condition)
            .order_by(distance_formula)
            .first()
        )

    return (
        (nearest_station.station_name, nearest_station.star_system)
        if nearest_station
        else None
    )
