import arcpy
# Set geoprocessing environments
arcpy.env.workspace = r"C:\EsriTraining\PythonGP\Data\SanJuan.gdb"
arcpy.env.overwriteOutput = True
# Create list of feature classes in SanJuan.gdb
fcList = arcpy.ListFeatureClasses()
# Create a loop to buffer Lakes and Streams
bufferList = []
for fc in fcList:
    if fc == "Lakes" or fc == "Streams":
        arcpy.Buffer_analysis(fc, fc + "Buffer", "1000 meters")
        bufferList.append(fc + "Buffer")
arcpy.Union_analysis(bufferList, "WaterBuffers")
