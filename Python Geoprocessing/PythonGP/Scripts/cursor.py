import arcpy
# Set the workspace
arcpy.env.workspace = r"C:\Users\rufai\OneDrive\Desktop\Summer Semester\GIS Application Development\Python Geoprocessing\PythonGP\Data\SanJuan.gdb"

# Create a new insert cursor for a table named Plants
rows = arcpy.da.InsertCursor("Plants")

# Create a new row
row = rows.newRow()

# Update the PLANT_NAME attribute
row.PLANT_NAME = "Canada Thistle"
#Add the new row to the table
rows.insertRow(row)

del rows
del row
