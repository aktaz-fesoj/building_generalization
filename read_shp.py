import geopandas as gpd
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

def load_shapefile(data_path, width, height):
    """"
    Loads geometry from a file (using geopandas read_file)
    
    Args:
        file_path (str): path to the file,
        width (int): max width - used to calculate scaling factor,
        heigt (int): max height - used to calculate scaling factor

    Returns:
        List of polygons as QPolygonF objects
    """
    data = gpd.read_file(data_path)

    qpolygons_list = []

    #finding min and max coordinates (for drawing)
    min_x, min_y, max_x, max_y = data.total_bounds

    # scale the coordinates to fit the current window size
    scaled_x = width / (max_x - min_x)
    scaled_y = height / (max_y - min_y)
    scaled_factor = min(scaled_x, scaled_y)

    #iterate through polygons in data, creating QPolygonFs
    for i in range(0,len(data)):
        polygon = data.get_geometry(0)[i]
        
        q_polygon = QPolygonF()
        
        #iterate through bounding points of a polygon, saving them in QPolygonF, 
        # rescaling the coordinates to make the polygons visible in the canvas
        for x,y in polygon.exterior.coords:
            x = (x - min_x) * scaled_factor
            y = (max_y - y) * scaled_factor
            point = QPointF(x, y)
            q_polygon.append(point)
        qpolygons_list.append(q_polygon)    #append created polygon to the list of polygons
    
    return qpolygons_list