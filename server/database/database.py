from sqlalchemy import Column, Integer, String, Float, Boolean, func
from flask_sqlalchemy import SQLAlchemy
import math

database = SQLAlchemy()
"""
TABLES:

star_systems:

    system_name text pri key
    latitude float
    longitude float
    height float
    state text (powerplay state)
    shortcode text (power shortcode)
    is_anarchy bool
    has_res_sites bool

stations:

    id int pri key
    name text
    system text
    type text (Starport, Outpost, PlanetaryPort, Settlement, EngineerBase)
    economy text

megaships: 
    name text pri key
    system1 text
    system2 text
    system3 text
    system4 text
    system5 text
    system6 text
"""


class StarSystem(database.Model):
    __tablename__ = "star_systems"
    system_name = Column(String(255), primary_key=True)
    latitude = Column(Float)
    longitude = Column(Float)
    height = Column(Float)
    state = Column(String(255))
    shortcode = Column(String(255))
    is_anarchy = Column(Boolean)
    has_res_sites = Column(Boolean)


class Station(database.Model):
    __tablename__ = "stations"
    id = Column(Integer, primary_key=True, autoincrement=True)
    station_name = Column(String(255))
    star_system = Column(String(255))
    station_type = Column(String(255))
    economy = Column(String(255))


class Megaship(database.Model):
    __tablename__ = "megaships"
    name = Column(String(255), primary_key=True)
    SYSTEM1 = Column(String(255))
    SYSTEM2 = Column(String(255))
    SYSTEM3 = Column(String(255))
    SYSTEM4 = Column(String(255))
    SYSTEM5 = Column(String(255))
    SYSTEM6 = Column(String(255))


class RareGoods(database.Model):
    __tablename__ = "Raregoods"
    good_name = Column(String(255), primary_key=True)
    system_name = Column(String(255))
    station_name = Column(String(255))


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