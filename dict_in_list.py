travel_log = [
  {
    "country": "France",
    "cities_visited": ["Paris", "Little", "Dijon"],
    "total_visits": 12
  },
  {"country": "Germany",
   "cities_visited": ["Berlin", "Hamburg", "Stutgart"],
   "total_visits": 3}
]

#ADDING NEW DICTIONARY TO TRAVEL LOG

def add_new_country(country_visited, times_visited, cities_visited):
  new_country = {}
  new_country["country"] = country_visited
  new_country["visits"] = times_visited
  new_country["city"] = cities_visited
  travel_log.append(new_country)

add_new_country("Russia", 2,  ["Moskow", "St.Peterburg"])
print(travel_log)
