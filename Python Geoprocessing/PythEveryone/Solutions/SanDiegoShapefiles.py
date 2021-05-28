#Assign variables to the shapefiles
park = "Parks_sd.shp"
school = "Schools_sd.shp"
sewer = "Sewer_Main_sd.shp"

#Create a list of shapefile variables
shapeList = [park, school, sewer]

#Create and open new text file for updated shapefile
path = r"C:\EsriTraining\PythEveryone\CreatingScripts\SanDiegoUpd.txt"
file = open(path, 'w')

#Update the names of the shapefiles in shapefile list
for shp in shapeList:
    print(shp)
    shp = shp.replace("sd", "SD")
    print(shp)
    file.write(shp + "\n")

file.close()

