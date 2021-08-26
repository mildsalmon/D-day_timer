import sys
import datetime as dt
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType('main.ui')[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.time_check)

    def time_check(self):
        current_time = dt.datetime.now()
        goal_time = dt.datetime(2021, 10, 27, 21, 6, 0)
        diff_time = goal_time - current_time
        diff_seconds = diff_time.seconds
        diff_days = diff_time.days
        diff_months = diff_time.days

        diff_total = diff_time.seconds + (diff_time.days * 24 * 3600)

        print(diff_total)

        print(type(diff_time))

        self.label_1.setText(str(diff_total))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MyWindow()
    main_window.show()
    sys.exit(app.exec_())
    app=None