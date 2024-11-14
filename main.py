# ch 4.2.3 main.py

import sys
from ui import View
from ctrl import Control # Control 클래스 추가
from PyQt5.QtWidgets import QApplication

def main():
    calc = QApplication(sys.argv)
    app = QApplication(sys.argv)
    view = View()
    ctrl = Control(view=view) # Control 클래스 추가
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()