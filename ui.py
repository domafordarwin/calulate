# ch 5.2.1 ui.py

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QPlainTextEdit, \
    QHBoxLayout, QLineEdit, QComboBox) 
from PyQt5.QtGui import QIcon # 아이콘을 추가하기 위한 모듈
from PyQt5 import QtCore


class View(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # 텍스트 에디트 위젯 추가
        self.te1 = QPlainTextEdit(self)  # 텍스트 박스 추가
        self.te1.setReadOnly(True)  # 텍스트 박스 읽기 전용으로 설정


        # 삭제하기 버튼 추가하기
        self.btn2 = QPushButton('Clear', self) # 버튼 2 추가
        self.btn1 = QPushButton('Calc', self) # 버튼 추가

        self.le1 = QLineEdit('0', self) # 라인 에디트 위젯 추가
        self.le1.setAlignment(QtCore.Qt.AlignRight) # 오른쪽 정렬로 설정

        self.le2 = QLineEdit('0', self) # 라인 에디트 위젯 추가
        self.le2.setAlignment(QtCore.Qt.AlignRight)
        self.le2.setFocus(True)
        self.le2.selectAll()

        self.cb = QComboBox(self) # 콤보 박스 위젯 추가
        self.cb.addItems(['+', '-', '*', '/']) # 콤보 박스 아이템 추가

        hbox_formular = QHBoxLayout() # 수평 박스 레이아웃 추가
        hbox_formular.addWidget(self.le1)
        hbox_formular.addWidget(self.cb)
        hbox_formular.addWidget(self.le2)


        hbox = QHBoxLayout() # 수평 박스 레이아웃 추가
        hbox.addStretch(1) # 빈 공간 추가
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)

        vbox = QVBoxLayout() # 수직 박스 위젯 레이아이
        vbox.addWidget(self.te1)  # 새롭게 추가된 텍스트 박스 위젯 
        vbox.addLayout(hbox_formular)
        vbox.addLayout(hbox)
        vbox.addStretch(1)   # 빈 공간 추간

        self.setLayout(vbox)  # 박스 만들기

        self.setWindowTitle('계산기')
        self.setWindowIcon(QIcon('icon.png')) # 아이콘 추가
        self.resize(256, 256)
        self.show()

    def setDisplay(self):
        # QMessageBox.information(self, 'information', 'Button Clicked') # 메시지 박스 생성
        self.te1.appendPlainText('Button Clicked')  # 텍스트 박스에 'Button Clicked' 추가

    def clearMessage(self):
        self.te1.clear()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    #view = Calculator()
    ex= Calculator()
    sys.exit(app.exec_())