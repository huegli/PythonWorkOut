rainfall = {}


def get_rainfall(city, rain):
    rainfall[city] = rainfall.get(city, 0) + rain
    return rainfall
