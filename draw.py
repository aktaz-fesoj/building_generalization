from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtGui import QMouseEvent, QPaintEvent
from PyQt6.QtWidgets import *


class Draw(QWidget):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.buildings = [] #list[QPolygonF]
        self.buildings_simp = [] #list[QPolygonF]
        self.building_correct = [] #list[QPolygonF]
        
    def paintEvent(self, e: QPaintEvent):
        #Create new graphic object
        qp = QPainter(self)
        
        #Set graphical attributes
        qp.setPen(Qt.GlobalColor.gray)
        qp.setBrush(Qt.GlobalColor.yellow)
        
        #Draw building
        for building in self.buildings:
            qp.drawPolygon(building)
        
        #Set graphical attributes
        qp.setPen(Qt.GlobalColor.blue)
        qp.setBrush(Qt.GlobalColor.transparent)
        
        #Draw building
        for building_simp in self.buildings_simp:
            qp.drawPolygon(building_simp)

        qp.setPen(Qt.GlobalColor.gray)
        qp.setBrush(Qt.GlobalColor.green)
        for building_corr in self.building_correct:
            qp.drawPolygon(building_corr)

    def paintInputEvent(self, polygons):
        self.buildings = polygons
    
    def setSimplifiedBuilding(self, building_simp_):
        self.building_simp = building_simp_
    
    def clearBuildings(self):
        #Clear polygons
        self.buildings.clear()
        self.buildings_simp.clear()
        self.building_correct.clear()
        
        #Repaint screen
        self.repaint()
    
    def clearSimpBuilding(self):
        self.buildings_simp.clear()
        self.building_correct.clear()

        self.repaint()