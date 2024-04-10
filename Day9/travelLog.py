country = input()
visits = int(input())
list_of_cities = eval(input())

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


# Add new country
def add_new_country(add_country, add_visits, add_list_of_cities):
    travel_dict = {"country": add_country, "visits": add_visits, "cities": add_list_of_cities}
    travel_log.append(travel_dict)


add_new_country(country, visits, list_of_cities)
print(f"I have been to {travel_log[2]["country"]} {travel_log[2]["visits"]} times.")
print(f"My fav cities was {travel_log[2]["cities"][0]}.")