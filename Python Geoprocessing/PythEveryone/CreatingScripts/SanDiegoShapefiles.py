# Author: Rufai Balogun
# Purpose: Basic Geoprocessing with Python workflow::

"""
The city of San Diego, California, has a folder of newly created shapefiles. The GIS department needs to review the
shapefiles and has asked you to produce a text file that lists them. Some of the shapefile names, however, do not fit
the standard naming template (<data>_SD.shp). As the data manager, you have decided to write a Python script that will
create a list of the shapefiles; later, the script will be used to update the shapefile names
"""

# Pseudocode:
# Assign variables to the shapefiles
park = "Parks_sd.shp"
school = "Schools_sd.shp"
sewer = "Sewer_Main_sd.shp"

# Create a list of shapefile variables
shapeList = [park, school, sewer]

#Create and open new text file for updated shapefile
path = r"C:\Users\rufai\OneDrive\Desktop\Summer Semester\GIS Application Development\Python Geoprocessing\PythEveryone\CreatingScripts\SanDiegoUpd.txt"
file = open(path, 'w')

# update the names of the shapefiles in shapefile list
for shp in shapeList:
    print(shp)
    shp = shp.replace("sd", "SD")
    print(shp)
    file.write(shp + "\n")

file.close()