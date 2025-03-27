from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtGui import QMouseEvent, QPaintEvent
from PyQt6.QtWidgets import *


class Draw(QWidget):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.building = QPolygonF()
        self.building_simp = QPolygonF()
        
    def mousePressEvent(self, e: QMouseEvent):
        #Get coordinates of q
        x = e.position().x()
        y = e.position().y()
        
        p = QPointF(x, y)
            
        self.building.append(p)
            
        #Repaint screen
        self.repaint()
        
        
    def paintEvent(self, e: QPaintEvent):
        #Create new graphic object
        qp = QPainter(self)
        
        #Start drawing
        qp.begin(self)
        
        #Set graphical attributes
        qp.setPen(Qt.GlobalColor.black)
        qp.setBrush(Qt.GlobalColor.yellow)
        
        #Draw building
        qp.drawPolygon(self.building)
        
        #Set graphical attributes
        qp.setPen(Qt.GlobalColor.gray)
        qp.setBrush(Qt.GlobalColor.blue)
        
        #Draw building
        qp.drawPolygon(self.building_simp)
    
    def getBuilding(self):
        # Return analyzed building
        return self.building
    
    def setSimplifiedBuilding(self, building_simp_):
        self.building_simp = building_simp_
    
    def clearData(self):
        #Clear polygon
        self.building.clear()
        
        #Repaint screen
        self.repaint()
        