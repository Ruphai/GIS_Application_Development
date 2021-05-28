import arcpy

# Set geo-processing environment
arcpy.env.workspace = r"C:\Users\rufai\OneDrive\Desktop\Summer Semester\GIS Application Development\Python Geoprocessing\PythonGP\Data\SanJuan.gdb"
arcpy.env.overwriteOutput = True

# Create list of feature classes in SanJuan.gdb
fcList = arcpy.ListFeatureClasses()

bufferList = []
# Create a loop to buffer Lakes and Streams
for fc in fcList:
    if fc == "Lakes" or fc == "Streams":
        arcpy.Buffer_analysis(fc, fc + "Buffer", "1000 meters", "", "", "ALL")
        # Specifying the units of your code allows it to be more readable
        # If you specify only the distance, the units of the spatial reference will be used
        bufferList.append(fc + "Buffer")
arcpy.analysis.Union(bufferList, "WaterBuffers.shp")
#arcpy.Union_analysis(bufferList, "WaterBuffers")
    # Look at your result in a GIS GUI software
