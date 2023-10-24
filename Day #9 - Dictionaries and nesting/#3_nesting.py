# Nesting:

# In Python, lists and dictionaries can be nested within other lists and dictionaries. 
# This means that it is possible to have lists containing other lists, or dictionaries containing other dictionaries or lists. 
# This type of nested data structure can be useful for representing complex and hierarchical data in an organized and logical manner.

# Simple nesting in a simple dictionary:
capitals = {
    "France": "Paris", # Key: Value
    "Germany": "Berlin",
}

print(capitals)

# Nesting a list in a dictionary:
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

print(travel_log)

# Nesting a dictionary in a dictionary:
detailed_travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"]},
}

print(detailed_travel_log)

# Nesting a dictionary in a list:

detailed_travel_log = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12
    },
    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 15
    },
]

print(detailed_travel_log)

