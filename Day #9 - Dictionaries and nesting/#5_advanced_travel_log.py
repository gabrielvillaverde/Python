# You are going to write a program that adds to a travel_log. 
# You can see a travel_log which is a List that contains 2 Dictionaries. 
# Your job is to create a function that can add new countries to this list.

# Write a function that will work with the following line of code to add the entry for Brazil to the travel_log.

# Entry: add_new_country("Brazil", 5, ["Sao Paulo", "Rio de Janeiro"])

print('''
To work out this code, you need to type this into the console:

Brazil
2
["Sao Paulo", "Rio de Janeiro"]

''')

country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 

def add_new_country(name_of_country, times_visited, cities_visited):
    new_country = {
        "country": name_of_country,
        "visits": times_visited,
        "cities": cities_visited
    }
    travel_log.append(new_country)
    
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")




