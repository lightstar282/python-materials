# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(413, 299)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 413, 20))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menuOpen_Recent = QtWidgets.QMenu(self.menu_File)
        self.menuOpen_Recent.setObjectName("menuOpen_Recent")
        self.menu_Edit = QtWidgets.QMenu(self.menubar)
        self.menu_Edit.setObjectName("menu_Edit")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_New = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("ui/resources/file-new.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.action_New.setIcon(icon)
        self.action_New.setObjectName("action_New")
        self.action_Open = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap("ui/resources/file-open.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.action_Open.setIcon(icon1)
        self.action_Open.setObjectName("action_Open")
        self.action_Save = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap("ui/resources/file-save.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.action_Save.setIcon(icon2)
        self.action_Save.setObjectName("action_Save")
        self.action_Exit = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap("ui/resources/file-exit.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.action_Exit.setIcon(icon3)
        self.action_Exit.setObjectName("action_Exit")
        self.action_Copy = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(
            QtGui.QPixmap("ui/resources/edit-copy.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.action_Copy.setIcon(icon4)
        self.action_Copy.setObjectName("action_Copy")
        self.action_Paste = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(
            QtGui.QPixmap("ui/resources/edit-paste.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.action_Paste.setIcon(icon5)
        self.action_Paste.setObjectName("action_Paste")
        self.action_Cut = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(
            QtGui.QPixmap("ui/resources/edit-cut.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.action_Cut.setIcon(icon6)
        self.action_Cut.setObjectName("action_Cut")
        self.actionOpen_All = QtWidgets.QAction(MainWindow)
        self.actionOpen_All.setObjectName("actionOpen_All")
        self.action_About = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(
            QtGui.QPixmap("ui/resources/help-content.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.action_About.setIcon(icon7)
        self.action_About.setObjectName("action_About")
        self.action_Find_Replace = QtWidgets.QAction(MainWindow)
        self.action_Find_Replace.setObjectName("action_Find_Replace")
        self.menuOpen_Recent.addAction(self.actionOpen_All)
        self.menu_File.addAction(self.action_New)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.menuOpen_Recent.menuAction())
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Save)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Exit)
        self.menu_Edit.addAction(self.action_Copy)
        self.menu_Edit.addAction(self.action_Paste)
        self.menu_Edit.addAction(self.action_Cut)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.action_Find_Replace)
        self.menu_Help.addAction(self.action_About)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.toolBar.addAction(self.action_New)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Open)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Save)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Copy)
        self.toolBar.addAction(self.action_Paste)
        self.toolBar.addAction(self.action_Cut)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_About)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sample Editor"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menuOpen_Recent.setTitle(_translate("MainWindow", "Open &Recent"))
        self.menu_Edit.setTitle(_translate("MainWindow", "&Edit"))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_New.setText(_translate("MainWindow", "&New..."))
        self.action_New.setToolTip(
            _translate("MainWindow", "Create a New Document")
        )
        self.action_New.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.action_Open.setText(_translate("MainWindow", "&Open..."))
        self.action_Open.setToolTip(
            _translate("MainWindow", "Open a Document")
        )
        self.action_Open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_Save.setText(_translate("MainWindow", "&Save"))
        self.action_Save.setToolTip(
            _translate("MainWindow", "Save the Current Document")
        )
        self.action_Save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_Exit.setText(_translate("MainWindow", "&Exit"))
        self.action_Copy.setText(_translate("MainWindow", "&Copy"))
        self.action_Copy.setToolTip(
            _translate("MainWindow", "Copy Slected Text")
        )
        self.action_Copy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.action_Paste.setText(_translate("MainWindow", "&Paste"))
        self.action_Paste.setToolTip(
            _translate("MainWindow", "Paste Copied Text")
        )
        self.action_Paste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.action_Cut.setText(_translate("MainWindow", "C&ut"))
        self.action_Cut.setToolTip(
            _translate("MainWindow", "Cut Selected Text")
        )
        self.action_Cut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionOpen_All.setText(_translate("MainWindow", "Open All"))
        self.actionOpen_All.setToolTip(
            _translate("MainWindow", "Open All Recent Documents")
        )
        self.action_About.setText(_translate("MainWindow", "&About..."))
        self.action_Find_Replace.setText(
            _translate("MainWindow", "&Find and Replace...")
        )
        self.action_Find_Replace.setToolTip(
            _translate("MainWindow", "Launch Find and Replace Dialog")
        )
        self.action_Find_Replace.setShortcut(
            _translate("MainWindow", "Ctrl+F")
        )
