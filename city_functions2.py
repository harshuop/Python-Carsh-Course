def CityCountry(city, country, population=""):
    if population:
        name = city + ' ' + country + ' ' + str(population)
    else:
        name = city + ' ' + country
    return name.title()
