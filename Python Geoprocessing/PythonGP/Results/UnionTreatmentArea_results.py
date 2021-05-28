import arcpy
# Set environments
arcpy.env.workspace = r"C:\EsriTraining\PythonGP\Data\SanJuan.gdb"
arcpy.env.overwriteOutput = True
# Create Python list of treatment area feature classes
treatmentList = ["RoadBuffers", "WaterBuffers"]
# Union treatment areas
arcpy.Union_analysis(treatmentList, "NonChemical")
