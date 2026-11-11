
cities = {
    'jakarta': {
        'country': 'indonesia',
        'population': '10.6 million',
        'fact': 'the capital city of indonesia'
    },

    'tokyo': {
        'country': 'japan',
        'population': '14 million',
        'fact': 'one of the largest metropolitan areas in the world'
    },

    'paris': {
        'country': 'france',
        'population': '2.1 million',
        'fact': 'famous for the eiffel tower'
    }
}

for city, city_info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"\tCountry: {city_info['country'].title()}")
    print(f"\tPopulation: {city_info['population']}")
    print(f"\tFact: {city_info['fact'].title()}")
