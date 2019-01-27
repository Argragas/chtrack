import time
from classes.python.opensky_api import OpenSkyApi
from classes.utils import search_avion

api = OpenSkyApi()
api_second = OpenSkyApi()
print("Reception")
start = api.get_states(0, None, None, [42.291710, 51.060550, 5.140094, 8.643547])
i = True
while i:
	s = start
	print("3 s de pause")
	time.sleep(3)
	print("Reception")
	second = api_second.get_states(0, None, None, [42.291710, 51.060550, 5.140094, 8.643547])
	'''
	for s in s.states:
		print("(%r, %r, %r, %r, %r, %r)" % (s.longitude, s.latitude, s.baro_altitude, s.velocity, s.vertical_rate , s.on_ground ))
	'''

	for su in second.states:
		second_item = search_avion(s, su.icao24)
		if su is not None and second_item != "1":
			#print(su)
			if second_item.baro_altitude is not None and su.baro_altitude is not None and not su.on_ground:
				if -700.0 < float(second_item.baro_altitude) - float(su.baro_altitude) < -250.0:
					print("l'altitude à changée ", su.icao24, su.baro_altitude, " : a ", second_item.icao24, second_item.baro_altitude, " diff : ", float(second_item.baro_altitude) - float(su.baro_altitude))
				# if su.longitude != second_item.longitude:
				# 	print("la longitude de ", su.icao24, " à changée", su.longitude, " : ", second_item.longitude)

	s = None
	second = None
	s = second
	
	api = OpenSkyApi()
	api_second = OpenSkyApi()

