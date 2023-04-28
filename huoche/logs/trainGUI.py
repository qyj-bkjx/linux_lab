from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QAbstractItemView,QTableWidget,QMessageBox,QWidget,QHBoxLayout
from train import Ui_Form
from DBHelper import DbHelper

class TrainSystem(QMainWindow, Ui_Form):

    def __init__(self, parent=None):
        super(TrainSystem, self).__init__(parent)
        # 将控件全部加入窗口
        self.setupUi(self)
        # 窗口大小固定
        self.setFixedSize(self.width(), self.height())
        # 设置标题
        self.setWindowTitle("Train ticket inquiry system")
    
        # 加载数据库
        self.db = DbHelper()
        # 设置索引 和 数据 以及 长度
        sql = "select * from trains"
        self.lengthen, self.data = self.db.select(sql)
        self.index = 0
        self.LineFill()
        self.buttonEnable()

        # 设置表格属性
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(['Trips', 'class', 'start', 'end'])

        # 将表格设置为禁止编辑模式
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 设置表格整行选中    self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 将每个条目扩展到充满容器
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        # 查询按钮
        self.inquire.clicked.connect(self.inquireSlot)
        # 第一条按钮
        self.first.clicked.connect(self.firstSlot)
        # 前一条按钮
        self.front.clicked.connect(self.frontSlot)
        # 下一条按钮
        self.next.clicked.connect(self.nextSlot)
        # 最后一条按钮
        self.last.clicked.connect(self.lastSlot)
        # 详细按钮
        self.detail.clicked.connect(self.detailSlot)
    # 给车次 和 型号 赋值
    def LineFill(self):
        if self.index < self.lengthen:
            # 过去pid和type的值
            pid = str(self.data[self.index][0])
            type = str(self.data[self.index][2])
            # 设置相应的lineEdit值
            self.Tid_LineEdit.setText(pid)
            self.Ttype_LineEdit.setText(type)
            pidtype = type + pid
            self.Tra_Num_Line.setText(pidtype)
            return pid, type

    # 查询按钮槽信号
    def inquireSlot(self):
        # 获取火车tid
        tidType = self.Tra_Num_Line.text()

        # 获取火车tid和type
        type = tidType[0]
        tid = tidType[1:]

        # 给textLine赋值
        self.Tid_LineEdit.setText(tid)
        self.Ttype_LineEdit.setText(type)

        # 修改索引
        self.index = int(tid[2])
        print(self.index)

        # 查询火车记录
        self.queryTrain(tid, type)

    # 按钮使能
    def buttonEnable(self):
        if self.index == 0:
            # 第一个和上一个按钮不能使用
            self.first.setEnabled(False)
            self.front.setEnabled(False)
            self.last.setEnabled(True)
            self.next.setEnabled(True)
        elif self.index == self.lengthen - 1:
            self.last.setEnabled(False)
            self.next.setEnabled(False)
            self.first.setEnabled(True)
            self.front.setEnabled(True)
        else:
            # 最后一个和下一个按钮不能使用
            self.first.setEnabled(True)
            self.front.setEnabled(True)
            self.last.setEnabled(True)
            self.next.setEnabled(True)

    # 查询火车记录
    def queryTrain(self, tid, type):
        try:
            # 执行的sql语句
            sql1 = "select * from trains where tid=" + tid
            result = self.db.selectOne(sql1)

            # 起始站、终点站
            startStationId = result[3]
            endStationId = result[4]

            # 获取起始站名字
            sql2 = "select sname from stations where sid=" + str(startStationId)
            result2 = self.db.selectOne(sql2)
            startStationName = result2[0]

            # 获取终点站名字
            sql3 = "select sname from stations where sid=" + str(endStationId)
            result3 = self.db.selectOne(sql3)
            endStationName = result3[0]

            # 移除之前表格里的信息
            self.tableWidget.removeRow(0)

            # 将数据装入表格
            self.tableWidget.insertRow(0)
            self.tableWidget.setItem(0, 0, QTableWidgetItem(tid))
            self.tableWidget.setItem(0, 1, QTableWidgetItem(type))
            self.tableWidget.setItem(0, 2, QTableWidgetItem(startStationName))
            self.tableWidget.setItem(0, 3, QTableWidgetItem(endStationName))

            # 按钮使能
            self.buttonEnable()

        except:
            print("车次不存在")

    # 第一条按钮槽信号
    def firstSlot(self):
        self.index = 0
        pid, type = self.LineFill()
        self.queryTrain(pid, type)

    # 前一条条按钮槽信号
    def frontSlot(self):
        self.index = self.index - 1
        pid, type = self.LineFill()
        self.queryTrain(pid, type)


    # 下一条按钮槽信号
    def nextSlot(self):
        self.index = self.index + 1
        pid, type = self.LineFill()
        self.queryTrain(pid, type)

    # 最后一条按钮槽信号
    def lastSlot(self):
        self.index = self.lengthen - 1
        pid, type = self.LineFill()
        self.queryTrain(pid, type)

    # 详细按钮
    def detailSlot(self):
        # 获取tid信息
        try:
            tid = self.Tid_LineEdit.text()
            # 查询stations_train_pass表
            sql = "select * from stations_train_pass where tid=" + tid
            length, data = self.db.select(sql)
            # 没有记录时，提醒
            if length == 0:
                QMessageBox.warning(self, "error", "not find")
            else:
                # 设置表格属性
                self.tw.setColumnCount(5)
                self.tw.setHorizontalHeaderLabels(['Trips','Arrival time', 'place', 'shift' ,'Start time'])

                # 将表格设置为禁止编辑模式
                self.tw.setEditTriggers(QAbstractItemView.NoEditTriggers)
                # 设置表格整行选中
                self.tw.setSelectionBehavior(QAbstractItemView.SelectRows)
                # 将每个条目扩展到充满容器
                self.tw.horizontalHeader().setStretchLastSection(True)
                # 设置表项的行数
                self.tw.setRowCount(length)
                # 填充数据
                for i, item in enumerate(data):
                    for j, jtem in enumerate(item):
                        jtem = str(jtem)
                        if j == 0:
                            self.tw.setItem(i, j, QTableWidgetItem(jtem))
                        if j in [2, 3, 4, 5]:
                            j = j-1
                            self.tw.setItem(i, j, QTableWidgetItem(jtem))

        except:
            pass

