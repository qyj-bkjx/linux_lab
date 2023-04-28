from PyQt5.QtWidgets import QApplication
import sys

from trainGUI import TrainSystem

if __name__ == '__main__':
    # 建立QApplication应用
    app = QApplication(sys.argv)
    # 加载窗口
    trainS = TrainSystem()
    # 显示窗口
    trainS.show()
    # 窗口结束与程序结束挂钩
    sys.exit(app.exec())