import arcpy
# Set geoprocessing environments
arcpy.env.workspace = r"C:\EsriTraining\PythonGP\Data\SanJuan.gdb"
arcpy.env.overwriteOutput = True
# Set parameters used to join the BufferDistance table to the Roads feature class
inFeatures = "Roads"
inField = "ROUTE_TYPE"
joinTable = "BufferDistance"
joinField = "ROUTE_TYPE"
# Join table to feature class
arcpy.JoinField_management(inFeatures, inField, joinTable, joinField)
# Set parameters used to buffer Roads feature class
outBuffers = "RoadBuffers"
buffField = "DISTANCE"
# Buffer the roads based on DISTANCE attribute
arcpy.Buffer_analysis(inFeatures, outBuffers, buffField)
