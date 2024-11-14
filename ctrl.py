# ch 5.2.1 ctrl.py
# UI에서 입력되는 이벤트 처리나 UI동작을 제어하는 내용을 포함하는 파일

class Control:
    def __init__(self, view):
        self.view = view
        self.connectSignals()

    def connectSignals(self):
        self.btn2.clicked.connect(self.clearMessage) # 버튼 클릭 시 clearMessage 메소드 호출
        self.btn1.clicked.connect(self.activateMessage) # 버튼 클릭 시 activateMessage 메소드 호출
