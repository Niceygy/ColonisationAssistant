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

WHAT_MAKES_THIS = {
    "Aluminium": ["Refinery"],
    "Ceramic Composites": ["Refinery/Surface"],
    "CMM Composite": ["Refinery/Surface"],
    "Computer components": ["Industrial"],
    "Copper": ["Refinery"],
    "Food cartridges": ["Industrial"],
    "Fruit and vegetables": ["Agri"],
    "Insulating membrane": ["Refinery/Space"],
    "Liquid oxygen": ["Refinery"],
    "Medical diagnostic equipment": ["HighTech"],
    "Non-lethal weapons": ["HighTech", "Military"],
    "Polymers": ["Refinery"],
    "Power generators": ["Industrial"],
    "Semiconductors": ["Refinery"],
    "Steel": ["Refinery"],
    "Superconductors": ["Refinery"],
    "Titanium": ["Refinery"],
    "Water": ["Agri", "Extraction/Surface"],
    "Water purifiers": ["Industrial"],
}
