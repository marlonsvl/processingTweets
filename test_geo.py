""" geolocalizacion: https://github.com/geopy/geopy
Install: pip install geopy

"""
from geopy.geocoders import Nominatim

if __name__ == '__main__':
    """
    """
    geolocator = Nominatim()
    location = geolocator.geocode("Loja Ecuador")
    print(location.address)
    print((location.latitude, location.longitude))
    print(location.raw)