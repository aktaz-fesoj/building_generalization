from PyQt6 import QtCore, QtGui, QtWidgets
from draw import Draw
from algorithms import *

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(1755, 1327)
        self.centralwidget = QtWidgets.QWidget(parent=MainForm)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Canvas = Draw(parent=self.centralwidget)
        self.Canvas.setObjectName("Canvas")
        self.horizontalLayout.addWidget(self.Canvas)
        MainForm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainForm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1755, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSimplify = QtWidgets.QMenu(parent=self.menubar)
        self.menuSimplify.setObjectName("menuSimplify")
        self.menuView = QtWidgets.QMenu(parent=self.menubar)
        self.menuView.setObjectName("menuView")
        MainForm.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainForm)
        self.statusbar.setObjectName("statusbar")
        MainForm.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(parent=MainForm)
        self.toolBar.setObjectName("toolBar")
        MainForm.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.actionOpen = QtGui.QAction(parent=MainForm)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icons/open_file.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionOpen.setIcon(icon)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtGui.QAction(parent=MainForm)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/icons/exit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionExit.setIcon(icon1)
        self.actionExit.setObjectName("actionExit")
        self.actionMBR = QtGui.QAction(parent=MainForm)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/icons/maer.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionMBR.setIcon(icon2)
        self.actionMBR.setObjectName("actionMBR")
        self.actionPCA = QtGui.QAction(parent=MainForm)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/icons/pca.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionPCA.setIcon(icon3)
        self.actionPCA.setObjectName("actionPCA")
        
        self.actionLongestEdge = QtGui.QAction(parent=MainForm)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/icons/longestedge.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionPCA.setIcon(icon7)
        self.actionPCA.setObjectName("actionLongestEdge")

        self.actionWeightedBisector = QtGui.QAction(parent=MainForm)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/icons/weightedbisector.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionWeightedBisector.setIcon(icon6)
        self.actionWeightedBisector.setObjectName("actionWeightedBisector")
        
        self.actionClear_results = QtGui.QAction(parent=MainForm)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/icons/clear.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionClear_results.setIcon(icon4)
        self.actionClear_results.setObjectName("actionClear_results")
        self.actionClear_all = QtGui.QAction(parent=MainForm)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/icons/clear_er.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionClear_all.setIcon(icon5)
        self.actionClear_all.setObjectName("actionClear_all")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuSimplify.addAction(self.actionMBR)
        self.menuSimplify.addAction(self.actionPCA)
        self.menuSimplify.addAction(self.actionLongestEdge)
        self.menuSimplify.addAction(self.actionWeightedBisector)
        self.menuView.addAction(self.actionClear_results)
        self.menuView.addAction(self.actionClear_all)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSimplify.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionMBR)
        self.toolBar.addAction(self.actionPCA)
        self.toolBar.addAction(self.actionLongestEdge)
        self.toolBar.addAction(self.actionWeightedBisector)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionClear_results)
        self.toolBar.addAction(self.actionClear_all)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit)

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

        #Connect components and slots
        self.actionMBR.triggered.connect(self.simplifyBuildingMBR)
        self.actionPCA.triggered.connect(self.simplifyBuildingPCA)
        self.actionClear_all.triggered.connect(self.clearData)
        self.actionClear_results.triggered.connect(self.clearResult)
        self.actionExit.triggered.connect(self.closeApp)
        self.actionLongestEdge.triggered.connect(self.simplifyBuildingLongestEdge)
        self.actionWeightedBisector.triggered.connect(self.simplifyBuildingWeightedBisector)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "Building simplify"))
        self.menuFile.setTitle(_translate("MainForm", "File"))
        self.menuSimplify.setTitle(_translate("MainForm", "Simplify"))
        self.menuView.setTitle(_translate("MainForm", "View"))
        self.toolBar.setWindowTitle(_translate("MainForm", "toolBar"))
        self.actionOpen.setText(_translate("MainForm", "Open"))
        self.actionOpen.setToolTip(_translate("MainForm", "Open file"))
        self.actionExit.setText(_translate("MainForm", "Exit"))
        self.actionExit.setToolTip(_translate("MainForm", "Close application"))
        self.actionMBR.setText(_translate("MainForm", "MBR"))
        self.actionMBR.setToolTip(_translate("MainForm", "Simplify building using MBR"))
        self.actionPCA.setText(_translate("MainForm", "PCA"))
        self.actionPCA.setToolTip(_translate("MainForm", "Simplify building using PCA"))
        self.actionClear_results.setText(_translate("MainForm", "Clear results"))
        self.actionClear_all.setText(_translate("MainForm", "Clear all"))
        self.actionClear_all.setToolTip(_translate("MainForm", "Clear all data"))

    def clearData(self):
        ui.Canvas.clearBuildings()

    def clearResult(self):
        ui.Canvas.clearSimpBuilding()

    def closeApp(self):
        QApplication.instance().quit()

    def simplifyBuildingMBR(self, building):
        a = Algorithms()
        # get input data
        building = ui.Canvas.getBuilding()
        
        building_simp = a.createMBR(building)
        
        # set result
        ui.Canvas.setSimplifiedBuilding(building_simp)

        #repaint
        ui.Canvas.repaint()
        
    def simplifyBuildingPCA(self, building):
        a = Algorithms()
        # get input data
        building = ui.Canvas.getBuilding()
        
        building_simp = a.createBRPCA(building)
        
        # set result
        ui.Canvas.setSimplifiedBuilding(building_simp)

        #repaint
        ui.Canvas.repaint()
        
    def simplifyBuildingLongestEdge(self, building):
        a = Algorithms()
        # get input data
        building = ui.Canvas.getBuilding()
        
        # simplify building
        building_simp = a.createLongestEdge(building)
        
        # set result
        ui.Canvas.setSimplifiedBuilding(building_simp)

        #repaint
        ui.Canvas.repaint()

    def simplifyBuildingWeightedBisector(self, building):
        a = Algorithms()

        building = ui.Canvas.getBuilding()

        building_simp = a.createWeightedBisector(building)

        ui.Canvas.setSimplifiedBuilding(building_simp)

        ui.Canvas.repaint()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainForm = QtWidgets.QMainWindow()
    ui = Ui_MainForm()
    ui.setupUi(MainForm)
    MainForm.show()
    sys.exit(app.exec())
