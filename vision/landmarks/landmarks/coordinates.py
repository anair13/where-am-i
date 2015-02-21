"""Walid's coordinate conversion code"""

def degMinSecCoordsToDecimalLat(coordinate_string):
	list_of_coordinate_elements = coordinate_string.split(" ")

	latitude = float(list_of_coordinate_elements[0][1:])

	if list_of_coordinate_elements[0][0] == "S":
		latitude = latitude * -1

	latitude += (float(list_of_coordinate_elements[1])/60) + (float(list_of_coordinate_elements[2])/3600)

	return latitude

def degMinSecCoordsToDecimalLong(coordinate_string):
	list_of_coordinate_elements = coordinate_string.split(" ")

	longitude = float(list_of_coordinate_elements[3][1:])

	if list_of_coordinate_elements[3][0] == "W":
		longitude = longitude * -1

	longitude += (float(list_of_coordinate_elements[4])/60) + (float(list_of_coordinate_elements[5])/3600)

	return longitude
	
latitude = degMinSecCoordsToDecimalLat
longitude = degMinSecCoordsToDecimalLong

if __name__ == "__main__":
    coordinate_string = raw_input("Enter coordinate string in deg min sec format: ")
    print "Latitude = " + str(degMinSecCoordsToDecimalLat(coordinate_string))
    print "Longitude = " + str(degMinSecCoordsToDecimalLong(coordinate_string))


