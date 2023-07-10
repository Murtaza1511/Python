capitals = {
    "Gujarat" : "Gandhinagar",
    "India" : "Delhi",
    "Maharashtra" : "Mumbai"
}

# Nesting a list in a dictionary
travel_log = {
    "India": ['Kerala', 'Mumbai', 'Kolkata'],
    "France": ['Berlin', 'Hamburg', 'Stuttgart']
}
# We can't give multiple values to a single key, we can do it using lists

# Nesting Dictionary in a Dictionary
travel_log = {
    "India": {"cities_visited": ['Kerala', 'Mumbai', 'Kolkata'], "total_visits": 40},
    "France": {"cities_visited":['Berlin', 'Hamburg', 'Stuttgart'], "total_visits":1}
}

# Nesting Dictionary in a List

travel_log = [
    {
        "country":"India",
        "cities_visited": ['Kerala', 'Mumbai', 'Kolkata'], 
        "total_visits": 40
    },
    {
        "country":"France",
        "cities_visited":['Berlin', 'Hamburg', 'Stuttgart'], 
        "total_visits":1
    }
]