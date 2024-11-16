# ch 5.2.1 ctrl.py
# UI에서 입력되는 이벤트 처리나 UI동작을 제어하는 내용을 포함하는 파일

class Control:
    def __init__(self, view):
        self.view = view
        self.connectSignals()

    def calculate(self):
        num1 = float(self.view.le1.text())
        num2 = float(self.view.le2.text())
        operator = self.view.cb.currentText()

        if operator == '+':
            result = f'{num1} + {num2} = {self.sum(num1, num2)}'
        
        else:
            result = 'Calculation Error'

        return result

    def sum(sefl, a, b):
        return a + b
       

    def connectSignals(self):
        self.view.btn2.clicked.connect(self.view.clearMessage) # 버튼 클릭 시 clearMessage 메소드 호출
        self.view.btn1.clicked.connect(lambda:\
            self.view.setDisplay(str(self.calculate()))) # 버튼 클릭 시 activateMessage 메소드 호출
