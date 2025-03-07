DATABASE_CONNECTION_STRING = "mysql+pymysql://assistant:6548@10.0.0.52/elite"

INITIAL_STATION_TYPES = ["Outpost", "Starport"]

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

#SurfaceStation
WHAT_MAKES_THIS = {
    "Aluminium": ["Refinery"],
    "Ceramic Composites": ["Refinery/CraterOutpost"],
    "CMM Composite": ["Refinery/CraterOutpost"],
    "Computer components": ["Industrial"],
    "Copper": ["Refinery"],
    "Food cartridges": ["Industrial"],
    "Fruit and vegetables": ["Agri"],
    "Insulating membrane": ["Refinery/Starport"],
    "Liquid oxygen": ["Refinery"],
    "Medical diagnostic equipment": ["HighTech"],
    "Non-lethal weapons": ["HighTech", "Military"],
    "Polymers": ["Refinery"],
    "Power generators": ["Industrial"],
    "Semiconductors": ["Refinery"],
    "Steel": ["Refinery"],
    "Superconductors": ["Refinery"],
    "Titanium": ["Refinery"],
    "Water": ["Agri", "Extraction/CraterOutpost"],
    "Water purifiers": ["Industrial"],
}

SHORTCODE_ASSOCIATIONS = {
    "Aluminium": 1,
    "Ceramic Composites": 2,
    "CMM Composite": 3,
    "Computer components": 4,
    "Copper": 5,
    "Food cartridges": 6,
    "Fruit and vegetables": 7,
    "Insulating membrane": 8,
    "Liquid oxygen": 9,
    "Medical diagnostic equipment": 10,
    "Non-lethal weapons": 11,
    "Polymers": 12,
    "Power generators": 13,
    "Semiconductors": 14,
    "Steel": 15,
    "Superconductors": 16,
    "Titanium": 17,
    "Water": 18,
    "Water purifiers": 19,
}

