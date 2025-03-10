STATION_TYPES = [
    "Coriolis",
    "Asteroid Base",
    "Ocellus",
    "Orbis",
    "Commercial Outpost",
    "Industrial Outpost",
    "Criminal Outpost",
    "Civilian Outpost",
    "Scientific Outpost",
    "Military Outpost",
    "Satellite",
    "Communication Station",
    "Space Farm",
    "Pirate Base",
    "Mining Outpost",
    "Relay Station",
    "Military",
    "Security Station",
    "Government",
    "Medical",
    "Research Station",
    "Tourist",
    "Bar",
    "Outpost",
    "Port",
    "Agriculture Tier 1",
    "Agriculture Tier 2",
    "Extraction Tier 1",
    "Extraction Tier 2",
    "Industrial Tier 1",
    "Industrial Tier 2",
    "Military Tier 1",
    "Military Tier 2",
    "Research Bio Tier 1",
    "Research Bio Tier 2",
    "Tourism Tier 1",
    "Tourism Tier 2",
    "Extraction",
    "Civilian",
    "Exploration",
    "Scientific",
    "Refinery",
    "High Tech",
    "Industrial",
]

MATERIAL_LISTS = [
    "Aluminium",
    "Ceramic Composites",
    "CMM Composite",
    "Computer components",
    "Copper",
    "Food cartridges",
    "Fruit and vegetables",
    "Insulating membrane",
    "Liquid oxygen",
    "Medical diagnostic equipment",
    "Non-lethal weapons",
    "Polymers",
    "Power generators",
    "Semiconductors",
    "Steel",
    "Superconductors",
    "Titanium",
    "Water",
    "Water purifiers",
]


"""



"""

# SurfaceStation
WHAT_MAKES_THIS = {
    "Aluminium": ["Refinery"],
    "Biowaste": ["!Agri"],
    "Building Fabricators": ["Industrial"],
    "Ceramic Composites": ["Refinery/CraterOutpost"],
    "CMM Composite": ["Refinery/CraterOutpost"],
    "Computer Components": ["Industrial"],
    "Copper": ["Refinery"],
    "Crop Harvesters": ["Industrial"],
    "Evacuation Shelter": ["HighTech"],
    "Emergency Power Cells": ["Constant", "High Tech", "Refinery"],
    "Food Cartridges": ["Industrial"],
    "Fruit and Vegetables": ["Agri"],
    "Grain": ["Agri"],
    "Insulating Membrane": ["Refinery/Starport"],
    "Liquid Oxygen": ["Refinery"],
    "Medical Diagnostic Equipment": ["HighTech"],
    "Micro Controllers": ["HighTech"],
    "Non-Lethal Weapons": ["HighTech", "Military"],
    "Land Enrichment Systems": ["HighTech"],
    "Polymers": ["Refinery"],
    "Pesticides": ["HighTech"],
    "Power Generators": ["Industrial"],
    "Semiconductors": ["Refinery"],
    "Survival Equipment": ["Industrial"],
    "Steel": ["Refinery"],
    "Structural Regulators": ["HighTech/CraterOutpost"],
    "Surface Stabilisers": ["Refinery/CraterOutpost"],
    "Superconductors": ["Refinery"],
    "Titanium": ["Refinery"],
    "Water": ["Agri", "Extraction/CraterOutpost"],
    "Water Purifiers": ["Industrial"],
}

COMMDOTIES = list(WHAT_MAKES_THIS.keys())

CONSTANT_BUY_LOCATIONS = {
    # system/starport
    "Emergency Power Cells": [
        "Alrai/Bounds Hub",
        "LFT 1748/Otiman Dock",
        "BD+75 58/Stephenson Station",
        "LHS 1663/Frobisher City",
        "Aktzin/Feoktistov Station"
        "HR 244/Kepler City",
        "Gladutjin/Chadwick Port",
        "Apala/Wilson City",
        "NLTT 13249/Lewis Orbital",
        "Catuntinigi/Hui Enterprise",
        "LTT 17102/Velazquez Ring"
    ]
}
