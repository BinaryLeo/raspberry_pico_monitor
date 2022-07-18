# -*- coding: utf-8 -*-
import sys
import math
import re
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo

font_family = 'Courier New'
main_color ='#fff'

class SerialMonitor(QtWidgets.QMainWindow):
    def __init__(self):
        super(SerialMonitor, self).__init__()
        self.port = QSerialPort()
        self.serialDataView = SerialDataView(self)

        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint 
        # keeps only minimize button and close button
                            | QtCore.Qt.WindowCloseButtonHint)

        self.setStyleSheet("background-color: rgb(13,17,23)") 
        self.setCentralWidget( QtWidgets.QWidget(self) )
        layout = QtWidgets.QVBoxLayout( self.centralWidget() )
        layout.addWidget(self.serialDataView)
        layout.setContentsMargins(3, 3, 3, 3)
        self.setWindowTitle('RPico Monitor')

        ### Tool Bar ###
        self.toolBar = ToolBar(self)
        self.addToolBar(self.toolBar)

        ### Status Bar ###
        self.setStatusBar( QtWidgets.QStatusBar(self) )
        self.statusText = QtWidgets.QLabel(self)
        self.statusText.setStyleSheet("color: rgb(56,163,180); margin-left: 25px;")
        self.statusBar().addWidget( self.statusText )
        
        ### Signal Connect ###
        self.toolBar.portOpenButton.clicked.connect(self.portOpen)
        self.port.readyRead.connect(self.readFromPort)
    
    def portClose(self):
        self.port.close()
        self.statusText.setText('Port closed')
        self.toolBar.serialControlEnable(True)
    def portOpen(self, flag):
        if flag:
            self.port.setBaudRate( self.toolBar.baudRate() )
            self.port.setPortName( self.toolBar.portName() )
            self.port.setDataBits( self.toolBar.dataBit() )
            self.port.setParity( self.toolBar.parity() )
            self.port.setStopBits( self.toolBar.stopBit() )
            r = self.port.open(QtCore.QIODevice.ReadWrite)
            if not r:
                self.statusText.setText('Port open error')
                self.toolBar.portOpenButton.setChecked(False)
                self.toolBar.serialControlEnable(True)
            else:
                self.statusText.setText('Port opened')
                self.toolBar.serialControlEnable(False)
        else:
            self.port.close()
            self.statusText.setText('Port closed')
            self.toolBar.serialControlEnable(True)
        
    def readFromPort(self):
        data = self.port.readAll()
        if len(data) > 0:
            self.serialDataView.appendSerialText( QtCore.QTextStream(data).readAll(), QtGui.QColor(255,201,113))
 
    def sendFromPort(self, text):
        self.port.write( text.encode() )
        self.serialDataView.appendSerialText( text, QtGui.QColor(255,201,113) )

class SerialDataView(QtWidgets.QWidget):
    def __init__(self, parent):
        super(SerialDataView, self).__init__(parent)
        self.serialData = QtWidgets.QTextEdit(self)
        self.serialData.setAlignment(QtCore.Qt.AlignCenter)
        self.serialData.setReadOnly(True)
        self.serialData.setFontFamily(font_family)
        self.serialData.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.serialData.setFixedWidth(210)
        #set background color
        self.serialData.setStyleSheet("background-color: rgb(13,17,23); border:1px solid rgb(255,255,255);")
        self.serialData.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.serialDataHex = QtWidgets.QTextEdit(self)
        self.serialDataHex.setStyleSheet("background-color: rgb(13,17,23); border:1px solid rgb(255,255,255);")
        self.serialDataHex.setReadOnly(True)
        self.serialDataHex.setFontFamily(font_family)
        self.serialDataHex.setFixedWidth(380)
        self.serialDataHex.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.label = QtWidgets.QLabel('00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F')
        self.label.setFont( QtGui.QFont(font_family) )
        self.label.setIndent(5)
        self.label.setStyleSheet("color: % s" % main_color)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.setLayout( QtWidgets.QGridLayout(self) )
        self.layout().addWidget(self.serialData,    0, 0, 2, 1)
        self.layout().addWidget(self.label,         0, 1, 1, 1)
        self.layout().addWidget(self.serialDataHex, 1, 1, 1, 1)
        self.layout().setContentsMargins(2, 2, 2, 2)
        
    def appendSerialText(self, appendText, color):
        self.serialData.moveCursor(QtGui.QTextCursor.End)
        self.serialData.setFontFamily('Courier New')
        self.serialData.setTextColor(color)
        self.serialData.setStyleSheet("background-color: rgb(13,17,23); border:1px solid rgb(56,163,180);")
        self.serialDataHex.moveCursor(QtGui.QTextCursor.End)
       
        self.serialDataHex.setFontFamily(font_family)
        self.serialDataHex.setTextColor(color)
        self.serialDataHex.setStyleSheet("background-color: rgb(13,17,23); border:1px solid rgb(56,163,180);")

        self.serialData.insertPlainText(appendText)
        
        LAST_DATA = self.serialDataHex.toPlainText().split('\n')[-1]
        LAST_LENGTH= math.ceil( len(LAST_DATA) / 3 )
        
        APPEND_LIST = []
        SPLIT_BY_TWOCHAR = re.split( '(..)', appendText.encode().hex() )[1::2]
        if LAST_LENGTH > 0:
            t = SPLIT_BY_TWOCHAR[ : 16-LAST_LENGTH ] + ['\n']
            APPEND_LIST.append( ' '.join(t) )
            SPLIT_BY_TWOCHAR = SPLIT_BY_TWOCHAR[ 16-LAST_LENGTH : ]

        APPEND_LIST += [ ' '.join(SPLIT_BY_TWOCHAR[ i*16 : (i+1)*16 ] + ['\n']) for i in range( math.ceil(len(SPLIT_BY_TWOCHAR)/16) ) ]
        if len(APPEND_LIST[-1]) < 47:
            APPEND_LIST[-1] = APPEND_LIST[-1][:-1]

        for insertText in APPEND_LIST:
            self.serialDataHex.insertPlainText(insertText)
        
        self.serialData.moveCursor(QtGui.QTextCursor.End)
        self.serialDataHex.moveCursor(QtGui.QTextCursor.End)


class ToolBar(QtWidgets.QToolBar):
    def __init__(self, parent):
        super(ToolBar, self).__init__(parent)
        
        self.portOpenButton = QtWidgets.QPushButton()
        self.portOpenButton.setText("Open / Close")
        self.portOpenButton.setStyleSheet("color: % s" % main_color)

        self.portOpenButton.setCheckable(True)
        self.portOpenButton.setMinimumHeight(32)
        self.portNames = QtWidgets.QComboBox(self)
        self.portNames.setStyleSheet("color: % s" % main_color)
        self.portNames.addItems([ port.portName() for port in QSerialPortInfo().availablePorts() ])
        self.portNames.setMinimumHeight(30)

        self.baudRates = QtWidgets.QComboBox(self)
        self.baudRates.setStyleSheet("color: % s" % main_color)
        self.baudRates.addItems([
            '9600',
            '115200'
        ])
        self.baudRates.setCurrentText('115200')
        self.baudRates.setMinimumHeight(30)

        self.dataBits = QtWidgets.QComboBox(self)
        self.dataBits.setStyleSheet("color: % s" % main_color)
        self.dataBits.addItems(['5 bit', '6 bit', '7 bit', '8 bit'])
        self.dataBits.setCurrentIndex(3)
        self.dataBits.setMinimumHeight(30)

        self._parity = QtWidgets.QComboBox(self)
        self._parity.setStyleSheet("color: % s" % main_color)
        self._parity.addItems(['No Parity', 'Even Parity', 'Odd Parity', 'Space Parity', 'Mark Parity'])
        self._parity.setCurrentIndex(0)
        self._parity.setMinimumHeight(30)

        self.stopBits = QtWidgets.QComboBox(self)
        self.stopBits.setStyleSheet("color: % s" % main_color)
        self.stopBits.addItems(['One Stop', 'One And Half Stop', 'Two Stop'])
        self.stopBits.setCurrentIndex(0)
        self.stopBits.setMinimumHeight(30)


        self.addWidget( self.portOpenButton )
        self.addWidget( self.portNames)
        self.addWidget( self.baudRates)
        self.addWidget( self.dataBits)
        self.addWidget( self._parity)
        self.addWidget( self.stopBits)

    def serialControlEnable(self, flag):
        self.portNames.setEnabled(flag)
        self.baudRates.setEnabled(flag)
        self.dataBits.setEnabled(flag)
        self._parity.setEnabled(flag)
        self.stopBits.setEnabled(flag)

        
    def baudRate(self):
        return int(self.baudRates.currentText())

    def portName(self):
        return self.portNames.currentText()

    def dataBit(self):
        return int(self.dataBits.currentIndex() + 5)

    def parity(self):
        return self._parity.currentIndex()

    def stopBit(self):
        return self.stopBits.currentIndex()

    

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = SerialMonitor()
    window.show()
    app.exec()