""" geolocalizacion: https://github.com/geopy/geopy
Install: pip install geopy

"""
from geopy.geocoders import Nominatim
from countries import short2long
from bd import *
import json

if __name__ == '__main__':
    """
    """
    geolocator = Nominatim()
    objeto = BDdatos()
    registros = objeto.datos_tabla_por_row('tweetselnino_a');
    for registro in registros:
    	tweet = json.loads(registro['json'])
    	if tweet['coordinates'] != None :
    		# guardar en la base
    		objeto.update_datos('tweetselnino_a', 'location_json', str(json.dumps(tweet['coordinates'])), registro['id'])
    	elif tweet['place'] != None :
    		# guardar en la base
    		objeto.update_datos('tweetselnino_a', 'location_json', str(json.dumps(tweet['place'])), registro['id'])
    	elif tweet['user']['location'] != None and tweet['user']['location'] != "":
    		location = geolocator.geocode(tweet['user']['location'], timeout=None)
    		print(">>>>>>>>>>> "+tweet['user']['location'])
    		if location != None :
    			print(location.raw)
    			objeto.update_datos('tweetselnino_a', 'location_json', str(json.dumps(location.raw)), registro['id'])
    		else:
    			objeto.update_datos('tweetselnino_a', 'location_json', str(json.dumps(tweet['user']['location'])), registro['id'])
    	elif tweet['user']['time_zone'] != None and tweet['user']['time_zone'] != "":
    		location = geolocator.geocode(tweet['user']['time_zone'], timeout=None)
    		print(">>>>>>>>>>>>>>>>> "+tweet['user']['time_zone'])
    		if location != None :
    			objeto.update_datos('tweetselnino_a', 'location_json', str(json.dumps(location.raw)), registro['id'])
    		else:
    			time = tweet['user']['time_zone']
    			c = time[time.find("(")+1:time.find(")")]
    			print("Time: "+c)
    			l = geolocator.geocode(c, timeout=None)
    			objeto.update_datos('tweetselnino_a', 'location_json', str(json.dumps(l.raw)), registro['id'])
    	else:
			texto = registro['text']
			for p in short2long:
				print(short2long[p])
				if short2long[p] in texto :
					location = geolocator.geocode(short2long[p], timeout=None)
					objeto.update_datos('tweetselnino_a', 'location_json', json.dumps(location.raw), registro['id'])	
					break;