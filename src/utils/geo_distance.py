from geopy.distance import geodesic


def calculate_geo_distance(point1, point2, result_in):
    distance = geodesic(point1, point2)
    if result_in == "kilometers":
        distance = distance.kilometers
    elif result_in == "meters":
        distance = distance.meters
    elif result_in == "miles":
        distance = distance.miles
    return distance
