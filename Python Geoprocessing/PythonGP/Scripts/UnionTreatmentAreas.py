# Union feature classes together
import arcpy
# Set geoprocessing environments
arcpy.env.workspace = r"C:\Users\rufai\OneDrive\Desktop\Summer Semester\GIS Application Development\Python Geoprocessing\PythonGP\Data\SanJuan.gdb"
arcpy.env.overwriteOutput = True

# Create Python list of treatment area feature classes
treatmentList = ["RoadBuffers", "WaterBuffers"]

# Union treatment areas
arcpy.Union_analysis(treatmentList,"NonChemical")
