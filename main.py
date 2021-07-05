# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pycalc.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, PyCalc):
        PyCalc.setObjectName("PyCalc")
        PyCalc.resize(338, 520)
        PyCalc.setWindowFlag(QtCore.Qt.FramelessWindowHint) 
        PyCalc.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.StyleSheet = QtWidgets.QWidget(PyCalc)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        self.dragPos = QtCore.QPoint()
        self.StyleSheet.setFont(font)
        self.StyleSheet.setStyleSheet("QWidget{\n"
"    color: rgb(221, 221, 221);\n"
"    font: 36pt Courier;\n"
"}\n"
"#bgFrame {    \n"
"    \n"
"    background-color: rgb(51, 57, 68);\n"
"    border: 1px solid rgb(44, 49, 58);\n"
"    border-radius: 10px;\n"
"\n"
"}\n"
"#buttonsFrame {\n"
"    border-top-left-radius: 25px;\n"
"    border-top-right-radius: 25px;\n"
"    background-color: rgb(40, 44, 52);\n"
"    border: 1px solid black;\n"
"}\n"
"#buttonsFrame .QPushButton {\n"
"    background-color: rgb(40, 44, 52);\n"
"    \n"
"}")
        self.StyleSheet.setObjectName("StyleSheet")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.StyleSheet)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.bgFrame = QtWidgets.QFrame(self.StyleSheet)
        self.bgFrame.setObjectName("bgFrame")

        self.outputLabel = QtWidgets.QLabel(self.bgFrame,text="0")
        self.outputLabel.setObjectName("outputLabel")
        self.outputLabel.setGeometry(QtCore.QRect(0, 0, 320, 110))
        self.outputLabel.setFocusPolicy(QtCore.Qt.StrongFocus)

        self.outputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputLabel.setIndent(10)

        self.buttonsFrame = QtWidgets.QFrame(self.bgFrame)
        self.buttonsFrame.setObjectName("buttonsFrame")
        self.buttonsFrame.setGeometry(QtCore.QRect(0, 100, 320, 400))
        self.buttonsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
    
        self.actionC = QtWidgets.QPushButton(self.buttonsFrame,text="C",clicked=lambda : self.presses ("C"))
        self.actionC.setGeometry(QtCore.QRect(36, 42, 45, 45))
        self.actionC.setStyleSheet("background-color: #FF605C")
        self.actionC.setObjectName("actionC")
        self.actionC.setShortcut("c")
        
        self.actionSlash = QtWidgets.QPushButton(self.buttonsFrame,text="/",clicked=lambda : self.presses ("/"))
        self.actionSlash.setGeometry(QtCore.QRect(106, 42, 45, 45))
        self.actionSlash.setStyleSheet("background-color: rgb(51, 57, 68);")
        self.actionSlash.setObjectName("actionSlash")
        self.actionSlash.setShortcut("/")

        self.actionMult = QtWidgets.QPushButton(self.buttonsFrame,text="*",clicked=lambda : self.presses ("*"))
        self.actionMult.setGeometry(QtCore.QRect(173, 42, 45, 45))
        self.actionMult.setStyleSheet("background-color: rgb(51, 57, 68);")
        self.actionMult.setObjectName("actionMult")
        self.actionMult.setShortcut("*")
        
        self.actionBackspace = QtWidgets.QPushButton(self.buttonsFrame,text="←",clicked=lambda : self.presses ("<"))
        self.actionBackspace.setGeometry(QtCore.QRect(242, 42, 45, 45))
        self.actionBackspace.setStyleSheet("background-color: rgb(51, 57, 68);")
        self.actionBackspace.setObjectName("actionBackspace")
        self.actionBackspace.setShortcut("Backspace")

        self.actionMinus = QtWidgets.QPushButton(self.buttonsFrame,text="-",clicked=lambda : self.presses ("-"))
        self.actionMinus.setGeometry(QtCore.QRect(242, 112, 45, 45))
        self.actionMinus.setStyleSheet("background-color: rgb(51, 57, 68);")
        self.actionMinus.setObjectName("actionMinus")
        self.actionMinus.setShortcut("-")
        
        self.actionSum = QtWidgets.QPushButton(self.buttonsFrame,text="+",clicked=lambda : self.presses ("+"))
        self.actionSum.setGeometry(QtCore.QRect(242, 180, 45, 45))
        self.actionSum.setStyleSheet("background-color: rgb(51, 57, 68);")
        self.actionSum.setObjectName("actionSum")
        self.actionSum.setShortcut("+")        

        self.actionEqual = QtWidgets.QPushButton(self.buttonsFrame,text="=",clicked=lambda : self.presses ("="))
        self.actionEqual.setGeometry(QtCore.QRect(242, 248, 45, 114))
        self.actionEqual.setStyleSheet("background-color: rgb(21, 168, 133);")
        self.actionEqual.setObjectName("actionEqual")
        self.actionEqual.setShortcut("Enter")

        self.actionPercent = QtWidgets.QPushButton(self.buttonsFrame,text="%",clicked=lambda : self.presses ("%"))
        self.actionPercent.setGeometry(QtCore.QRect(36, 317, 45, 45))
        self.actionPercent.setStyleSheet("background-color: rgb(51, 57, 68);")
        self.actionPercent.setObjectName("actionPercent")
        self.actionPercent.setShortcut("%")

        self.actionDot = QtWidgets.QPushButton(self.buttonsFrame,text=".",clicked=lambda : self.presses ("."))
        self.actionDot.setGeometry(QtCore.QRect(173, 317, 45, 45))
        self.actionDot.setStyleSheet("background-color: rgb(51, 57, 68);")
        self.actionDot.setObjectName("actionDot")
        self.actionDot.setShortcut(".")

        self.num0 = QtWidgets.QPushButton(self.buttonsFrame,text="0",clicked=lambda : self.presses ("0"))
        self.num0.setGeometry(QtCore.QRect(106, 317, 45, 45))
        self.num0.setObjectName("num0")
        self.num0.setShortcut("0")

        self.num1 = QtWidgets.QPushButton(self.buttonsFrame,text="1",clicked=lambda : self.presses ("1"))
        self.num1.setGeometry(QtCore.QRect(36, 248, 45, 45))
        self.num1.setObjectName("num1")
        self.num1.setShortcut("1")
        
        self.num2 = QtWidgets.QPushButton(self.buttonsFrame,text="2",clicked=lambda : self.presses ("2"))
        self.num2.setGeometry(QtCore.QRect(106, 248, 45, 45))
        self.num2.setObjectName("num2")
        self.num2.setShortcut("2")

        self.num3 = QtWidgets.QPushButton(self.buttonsFrame,text="3",clicked=lambda : self.presses ("3"))
        self.num3.setGeometry(QtCore.QRect(173, 248, 45, 45))
        self.num3.setObjectName("num3")
        self.num3.setShortcut("3")

        self.num4 = QtWidgets.QPushButton(self.buttonsFrame,text="4",clicked=lambda : self.presses ("4"))
        self.num4.setGeometry(QtCore.QRect(36, 180, 45, 45))
        self.num4.setObjectName("num4")
        self.num4.setShortcut("4")
        
        self.num5 = QtWidgets.QPushButton(self.buttonsFrame,text="5",clicked=lambda : self.presses ("5"))
        self.num5.setGeometry(QtCore.QRect(106, 180, 45, 45))
        self.num5.setObjectName("num5")
        self.num5.setShortcut("5")

        self.num6 = QtWidgets.QPushButton(self.buttonsFrame,text="6",clicked=lambda : self.presses ("6"))
        self.num6.setGeometry(QtCore.QRect(173, 180, 45, 45))
        self.num6.setObjectName("num6")
        self.num6.setShortcut("6")

        self.num7 = QtWidgets.QPushButton(self.buttonsFrame,text="7",clicked=lambda : self.presses ("7"))
        self.num7.setGeometry(QtCore.QRect(36, 112, 45, 45))
        self.num7.setObjectName("num7")
        self.num7.setShortcut("7")
        
        self.num8 = QtWidgets.QPushButton(self.buttonsFrame,text="8",clicked=lambda : self.presses ("8"))
        self.num8.setGeometry(QtCore.QRect(106, 112, 45, 45))
        self.num8.setObjectName("num8")
        self.num8.setShortcut("8")

        self.num9 = QtWidgets.QPushButton(self.buttonsFrame,text="9",clicked=lambda : self.presses ("9"))
        self.num9.setGeometry(QtCore.QRect(173, 112, 45, 45))
        self.num9.setObjectName("num9")
        self.num9.setShortcut("9")

        self.closeButton = QtWidgets.QPushButton(self.bgFrame,text="X")
        self.closeButton.setShortcut("ESC")
        self.closeButton.setGeometry(QtCore.QRect(10, 10, 21, 21))
        self.closeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeButton.setStyleSheet("background-color: rgb(255, 96, 92);\n"
"border: 1px solid transparent;\n"
"border-radius: 10px;\n"
"font:10px bold aria;")
        self.closeButton.setObjectName("closeButton")
        self.closeButton.clicked.connect(lambda: PyCalc.close())
        
        self.horizontalLayout.addWidget(self.bgFrame)
        PyCalc.setCentralWidget(self.StyleSheet)

        QtCore.QMetaObject.connectSlotsByName(PyCalc)
        

class MyWin(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dragPos = QtCore.QPoint()
        self.action = None
        self.val = 0
        self.outputLabel.mouseMoveEvent = self.mouseMoveEvent
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        
    def mouseMoveEvent(self, event):   
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()
    
    def presses(self,event):
        self.val = self.outputLabel.text()
        # Check last event is digit or no
        last_var_isdigit = self.val[-1].isdigit() and self.val[-1] != "."

        if event == "C":
            self.val = "0"
            self.action = None
        elif event == "<":
            # set val to 0 if all cleared
            if len(self.val) <= 1:
                self.val = "0"
            else:
                # before delete check last event is action, if True just set self.action to None
                if not last_var_isdigit:
                    self.action = None
                self.val = self.val[:-1]

        elif event == "=" or (last_var_isdigit and not event.isdigit() and self.action):

            if not last_var_isdigit:
                self.val = self.val + self.val[:-1]
            self.val = eval(self.val)
            # Check float number decimal is zero, if True remove decimal
            self.val = str(int(self.val)) if self.val - int(self.val) == 0 else str(self.val)
            
            if event != "=":
                self.val += event

        elif not last_var_isdigit and not event.isdigit() and self.action:
            self.val = self.val[:-1] + event
            
        else:
            if not event.isdigit() and event != ".":
                self.action = event
            self.val += event
            
        # Check if first value is zero, if True just remove that 
        if len(self.val) > 1 and self.val.startswith("0"): self.val = self.val[1:]        
        self.outputLabel.setText(self.val)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MyWin()
    w.show()
    sys.exit(app.exec_())