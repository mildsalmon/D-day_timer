import sys
import datetime as dt
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import os

form_class = uic.loadUiType('D:\CloudStation\SourceCode\d-day\main.ui')[0]
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SAVE_DIR = os.path.join(BASE_DIR, 'save.txt')

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        if os.path.exists(SAVE_DIR):
            recode_datetime = self.open_file()
        else:
            recode_datetime = dt.datetime.now()

        self.dateTimeEdit_2.setDateTime(recode_datetime)

        self.goal_time = recode_datetime

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.time_check)

        # 설정 버튼 클릭시 발생하는 이벤트
        self.pushButton.clicked.connect(self.set_goal_time)

    def time_check(self):
        # current_time = dt.datetime.now()
        current_time = self.display_time()
        goal_time = self.goal_time
        # goal_time = goal_time.toPyDateTime()
        diff_time = goal_time - current_time
        diff_seconds = diff_time.seconds % 60
        diff_minutes = (diff_time.seconds % 3600 - diff_seconds) // 60
        diff_hours = (diff_time.seconds % 86400 - diff_minutes - diff_seconds) // (60 * 60)
        diff_days = diff_time.days
        diff_full = str(diff_days) + "일 " + str(diff_hours) + "시" + str(diff_minutes) + "분" + str(diff_seconds) + "초"

        diff_total = diff_time.seconds + (diff_time.days * 24 * 3600)

        # print(diff_total)
        # print(type(diff_time))

        self.label_1.setText(str(diff_total))
        self.lineEdit.setText(diff_full)

    def display_time(self):
        self.current_date_time = QDateTime.currentDateTime()
        self.dateTimeEdit.setDateTime(self.current_date_time)
        self.display_date_time = self.dateTimeEdit.dateTime()
        time = self.display_date_time.toPyDateTime()

        return time

    def set_goal_time(self):
        goal_date_time = self.dateTimeEdit_2.dateTime()
        goal_time = goal_date_time.toPyDateTime()
        self.goal_time = goal_time

        # if self.goal_time in '.':
        #     index_dot = self.goal_time.find('.')
        #     self.goal_time = self.goal_time[:index_dot]

        self.write_file(self.goal_time)

    def write_file(self, goal_time):
        with open(SAVE_DIR, 'w+', encoding='utf-8') as f_write:
            f_write.writelines(str(goal_time))

    def open_file(self):
        with open(SAVE_DIR, 'r+', encoding='utf-8') as f_read:
            recode_time = f_read.readline()

        recode_datetime = dt.datetime.strptime(recode_time, '%Y-%m-%d %H:%M:%S.%f')

        return recode_datetime

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MyWindow()
    main_window.show()
    sys.exit(app.exec_())
    app=None