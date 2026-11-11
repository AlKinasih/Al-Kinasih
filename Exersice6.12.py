
cities = {
    'jakarta': {
        'country': 'indonesia',
        'population': '10.6 million',
        'fact': 'the capital city of indonesia',
        'language': 'indonesian',
        'famous_food': 'nasi uduk'
    },

    'tokyo': {
        'country': 'japan',
        'population': '14 million',
        'fact': 'one of the largest metropolitan areas in the world',
        'language': 'japanese',
        'famous_food': 'sushi'
    },

    'paris': {
        'country': 'france',
        'population': '2.1 million',
        'fact': 'famous for the eiffel tower',
        'language': 'french',
        'famous_food': 'croissant'
    }
}

for city, city_info in cities.items():
    print("\n" + "=" * 30)
    print(f"CITY: {city.upper()}")
    print("=" * 30)

    print(f"Country       : {city_info['country'].title()}")
    print(f"Population    : {city_info['population']}")
    print(f"Fact          : {city_info['fact'].capitalize()}")
    print(f"Language      : {city_info['language'].title()}")
    print(f"Famous Food   : {city_info['famous_food'].title()}")
