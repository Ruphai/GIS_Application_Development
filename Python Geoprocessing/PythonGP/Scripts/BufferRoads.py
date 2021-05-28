import arcpy
# Set geoprocessing environments
arcpy.env.workspace = r"C:\Users\rufai\OneDrive\Desktop\Summer Semester\GIS Application Development\Python Geoprocessing\PythonGP\Data\SanJuan.gdb"
arcpy.env.overwriteOutput = True

# Set parameters used to join the BufferDistance table to the Roads feature class
inFeatures, inFields, joinTable, joinField = "Roads", "ROUTE_TYPE", "BufferDistance", "ROUTE_TYPE"

# Join table to feature class
arcpy.JoinField_management(inFeatures, inFields, joinTable, joinField)

# Set parameters used to buffer Roads feature class
outBuffers = "RoadBuffers"
buffField = "DISTANCE"

# Buffer the roads based on DISTANCE attribute
# To enter the variables in the correct order, use the arcpy.Usage function in the Python Console or read the
# Documentation on Buffer
arcpy.Buffer_analysis(inFeatures, outBuffers, buffField) #ensure that arcGIS Pro is closed before running thsi script
#if arcGIS Pro is open, it locks the geodatabase and the Python Script will not have write access to the geodatabase


