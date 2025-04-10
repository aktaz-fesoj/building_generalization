from math import *
from itertools import combinations
from heapq import heapify, heappop, heappush

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import numpy as np

class Algorithms:
    def __init__(self):
        pass
    
    def get2VectorsAngle(self, p1: QPointF, p2: QPointF, p3: QPointF, p4:QPointF):
        # Compute angle between two vectors
        ux = p2.x() - p1.x()
        uy = p2.y() - p1.y()
        
        vx = p4.x() - p3.x()
        vy = p4.y() - p3.y()
        
        # Dot product
        uv = ux*vx + uy*vy
        
        # Norms u, v
        norm_u = sqrt(ux**2 + uy**2)
        norm_v = sqrt(vx**2 + vy**2)
        
        arg = uv/(norm_u*norm_v)
        
        arg = min(arg, 1)
        arg = max(arg, -1)
        
        return acos(arg)
    
    def createCH(self, polygon: QPolygonF):
        """
        Create convex hull using Jarvis Scan
        """
        ch = QPolygonF()
        
        # Create pivot
        q = min(polygon, key = lambda k: k.y())
        # pj cant be same as px, otherwise vector size would be 0 and program would crash
        pj = QPointF(q.x()+0.1e-6, q.y()+0.1e-6)
        
        # Create point ph1
        px = min(polygon, key = lambda k: k.x())
        pj1 = QPointF(px.x(), pj.y())
        
        # Add pivot to ch
        ch.append(pj)
        
        # Process all points
        while True:
            #Initialize maximum and its index
            phi_max = 0
            idx_max = -1
            
            for i in range(len(polygon)):
                if pj != polygon[i]:
                    #Compute angle
                    phi = self.get2VectorsAngle(pj, pj1, pj, polygon[i])
            
                    #Update maximum
                    if phi > phi_max:
                        phi_max = phi
                        idx_max = i
            
            #Add point to ch
            ch.append(polygon[idx_max])
            
            #Update indices
            pj1 = pj
            pj = polygon[idx_max]
            
            #Stop
            if pj == q:
                break
        
        return ch  
    
    def rotate(self, pol: QPolygonF, sigma):
        #Rotate polygon by angle sigma
        pol_r = QPolygonF()
        
        #Process points one by one
        for p in pol:
            
            #Rotate polygon point
            x_r = p.x()*cos(sigma) - p.y()*sin(sigma)
            y_r = p.x()*sin(sigma) + p.y()*cos(sigma)
            
            #Create point
            p_r =QPointF(x_r, y_r)
            
            #Add point to polygon
            pol_r.append(p_r)
        
        return pol_r
    
    def createMMB(self, pol:QPolygonF):
        # Create min-max box
        mmb = QPolygonF()
        
        #Find extreme coordinates
        x_min = min(pol, key = lambda k: k.x()).x()
        x_max = max(pol, key = lambda k: k.x()).x()
        
        y_min = min(pol, key = lambda k: k.y()).y()
        y_max = max(pol, key = lambda k: k.y()).y()
        
        #Compute area
        area = abs((x_max - x_min) * (y_max - y_min))
        
        #Create min-max box vertices
        v1 = QPointF(x_min, y_min)
        v2 = QPointF(x_max, y_min)
        v3 = QPointF(x_max, y_max)
        v4 = QPointF(x_min, y_max)
        
        #Create min-max box polygon
        mmb.append(v1)
        mmb.append(v2)
        mmb.append(v3)
        mmb.append(v4)
        
        return mmb, area
        
    def getArea(self, pol: QPolygonF):
        # Compute area of a polygon
        area = 0
        n = len(pol)
        
        #Process vertices one by one
        for i in range(n):
            area += pol[i].x()*(pol[(i+1)%n].y()-pol[(i-1+n)%n].y())
            
        return abs(area)/2
            
    def resizeRectangle(self,building:QPolygonF, mbr:QPolygonF):
        # Resizing rectangle to match the building area
        mbr_res = QPolygonF()
                    
        #Compute k
        Ab = self.getArea(building)
        A = self.getArea(mbr)
        if A == 0: k = 1
        k = Ab / A
        
        # Compute centroid
        x_t = 0.25*(mbr[0].x()+mbr[1].x()+mbr[2].x()+mbr[3].x())
        y_t = 0.25*(mbr[0].y()+mbr[1].y()+mbr[2].y()+mbr[3].y())
        
        #Compute vectors
        v1_x = mbr[0].x() - x_t
        v1_y = mbr[0].y() - y_t
        
        v2_x = mbr[1].x() - x_t
        v2_y = mbr[1].y() - y_t
        
        v3_x = mbr[2].x() - x_t
        v3_y = mbr[2].y() - y_t
        
        v4_x = mbr[3].x() - x_t
        v4_y = mbr[3].y() - y_t
        
        #Compute coordinates of resized points
        v1_xr = x_t + v1_x * sqrt(k)
        v1_yr = y_t + v1_y * sqrt(k)
        
        v2_xr = x_t + v2_x * sqrt(k)
        v2_yr = y_t + v2_y * sqrt(k)
        
        v3_xr = x_t + v3_x * sqrt(k)
        v3_yr = y_t + v3_y * sqrt(k)
        
        v4_xr = x_t + v4_x * sqrt(k)
        v4_yr = y_t + v4_y * sqrt(k)
        
        #Create new vertices
        v1_res = QPointF(v1_xr, v1_yr)
        v2_res = QPointF(v2_xr, v2_yr)
        v3_res = QPointF(v3_xr, v3_yr)
        v4_res = QPointF(v4_xr, v4_yr)
        
        #Add vertices to the resized mbr
        mbr_res.append(v1_res)
        mbr_res.append(v2_res)
        mbr_res.append(v3_res)
        mbr_res.append(v4_res)
        
        return mbr_res
        
    def createMBR(self, building: QPolygonF):
        #Simplify building using MBR
        sigma_min = 0

        #Create convex hull
        ch = self.createCH(building)
        
        #Initilize MBR a its area
        mmb_min, area_min = self.createMMB(ch)
        
        #Browse CH segments
        n = len(ch)
            
        for i in range(n): 
            
            #Coordinate differences
            dx = ch[(i+1)%n].x() - ch[i].x()
            dy = ch[(i+1)%n].y() - ch[i].y()
            
            #Compute direction
            sigma = atan2(dy, dx)
            
            #Rotate polygon
            ch_r = self.rotate(ch, -sigma)
            
            #Compute min-max box 
            mmb, area = self.createMMB(ch_r)
            
            #Update minimum
            if area < area_min:
                area_min = area
                mmb_min = mmb
                sigma_min = sigma
        
        #resize        
        mmb_min_res = self.resizeRectangle(building, mmb_min)
                
        return self.rotate(mmb_min_res, sigma_min)
        
    def createBRPCA(self, building: QPolygonF):
        """"
        Simpliefies building using PCA and min max box

        Reutrns: The simplified building: QPolygonF
        """
        x = []
        y = []
        
        for p in building:
            x.append(p.x())
            y.append(p.y())
        
        A = np.array([x, y])
        
        C = np.cov(A)
        
        #singular value decomposition
        [U, S, V] = np.linalg.svd(C)
        
        #direction of the principal vector
        
        dx = V[0][0]
        dy = V[0][1]
        sigma = atan2(dy, dx)
        
        
        #Simplify building using MBR
        sigma_min = 0
        
        building_r = self.rotate(building, -sigma)
        
        mmb, area = self.createMMB(building_r)
        
        #resize        
        mmb_min_res = self.resizeRectangle(building_r, mmb)
                
        return self.rotate(mmb_min_res, sigma)
    
    def createLongestEdge(self, building: QPolygonF):
        # creates simplified polygon using Longest Edge method, 
        # returns resized MMB oriented in the same angle as the longest edge of the original polygon

        #find the longest edge
        max_edge_len = 0
        alfa = 0
        
        for i in range(len(building)):
            p1_x, p1_y = building[i].x(), building[i].y()
            p2_x, p2_y = building[(i + 1) % len(building)].x(), building[(i + 1) % len(building)].y()

            dx, dy = p1_x - p2_x, p1_y - p2_y
            edge_len = sqrt(dx**2 + dy**2)

            if edge_len > max_edge_len:
                max_edge_len = edge_len
                alfa = self.get2VectorsAngle(QPointF(0,0), QPointF(1,0), building[i], building[(i + 1) % len(building)])
                #QPointF(polygon[i].x(), polygon[i].y()), [polygon[(i + 1) % len(polygon)].x(), polygon[(i + 1) % len(polygon)].y()])
                
        
        #rotate the original polygon before creating mmb
        rotated_polygon = self.rotate(building, alfa)
        
        mmb, area = self.createMMB(rotated_polygon)
        
        #rerotate the mmb to align with the longest edge of the original polygon
        mmb_rotated = self.rotate(mmb, -alfa)
        
        return self.resizeRectangle(building, mmb_rotated)

    def gain(self, p1: QPoint, p2: QPoint):
        dx = p1.x() - p2.x()
        dy = p1.y() - p2.y()
        gain = atan2(dy, dx)

        return gain
    
    def createWallAverage(self, building: QPolygonF):
        # creates a simplified building using the Wall Average method
        
        #calculate gain of the first edge
        sigma_base = self.gain(building[0], building[1])
        
        sigma_list = []
        # count the sigma_dif for each edge
        for i in range(len(building)):
            p1 = building[i]
            p2 = building[(i + 1) % len(building)]
            sigma = self.gain(p1, p2)
            sigma_list.append(sigma)

    def createWeightedBisector(self, building: QPolygonF) -> QPolygonF:
        """"
        Simpliefies building using weighted bisector and min max box

        Reutrns: The simplified building: QPolygonF
        """
        #todo list
        #filter out lines that intersect polygons from diagonals
        #filter out edges from diagonals
        #if no correct diagonals are found create a fallback

        #there might be bug with angle wrapping? (not sure how to solve it)

        points = [building[i] for i in range(len(building))]
        point_pairs = list(combinations(points, 2))

        #Z hloubi duše bych se chtěl omluvit všem, kteří si čtou tento kód. Je to prohřešek, za který se budu zpovídat před branou nebeskou.
        diagonals_all = []
        diagonals = [0,0]
        distances = [0,0]
        angles = [0,0]

        #find the longest diagonals
        for pair in point_pairs:
            dist = self.euclideanDistance(pair[0], pair[1])
            diagonals_all.append((pair, dist))
        diagonals_all.sort(key=lambda x: x[1], reverse=True)
        diagonals[0], distances[0] = diagonals_all[0]
        diagonals[1], distances[1] = diagonals_all[1]

        #calculate direction of each diagonal
        angles[0] = atan2(diagonals[0][1].y() - diagonals[0][0].y(), diagonals[0][1].x() - diagonals[0][0].x())
        angles[1] = atan2(diagonals[1][1].y() - diagonals[1][0].y(), diagonals[1][1].x() - diagonals[1][0].x())

        #calculate the principal direction
        sigma = (distances[0] * angles[0] + distances[1] * angles[1]) / (distances[0] + distances[1])

        building_rotated = self.rotate(building, -sigma)

        mmb, area = self.createMMB(building_rotated)

        mmb_min_res = self.resizeRectangle(building_rotated, mmb)
            
        return self.rotate(mmb_min_res, sigma)

    def euclideanDistance(self, point1: QPointF, point2: QPointF) -> float:
        """
        Calculates the euclidean distance of two points

        Returns: the calculated distance: float
        """

        dist = sqrt((point1.x() - point2.x())**2 + (point1.y() - point2.y())**2)
        return dist