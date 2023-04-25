
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import math

class Progress(QDialog):
    precent = 0
    def __init__(self):
        super(Progress,self).__init__()

        self.setWindowFlags(Qt.FramelessWindowHint)     # 去掉窗体边框
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗体背景透明

        self.Timer = Timer()    # 调用计时器
        self.Timer.signal.connect(self.percentUpdate)   # 绑定计时器信号
        self.Timer.start()      # 启动该类的run函数
        width,height = 230,230
        self.resize(width,height)   # 设置主窗体宽度

        self.circle = Circle((width,height),self)   # 这个self一定要加，不然画笔绑定不到这个窗体(Qt树概念)
        self.water = Water(self)

        # QMetaObject.connectSlotsByName(self)    # 绘制窗体渐变事件
        # self.anim = Animation(self)    # 绘制窗体渐变事件

    def percentUpdate(self):
        self.precent += 1   # 百分比+1
        self.water.update_percent(self.precent)
        self.water.paintEvent(None)
        self.circle.update_percent(self.precent)    # 根据百分比刷新percent


class Timer(QThread):
    signal = Signal()
    def run(self):
        for i in range(100):
            self.signal.emit()
            self.msleep(50)

class Circle(QWidget):
    def __init__(self,wh,parent=None):
        super(Circle, self).__init__(parent)
        print(wh)
        self.resize(*wh)
        self.width,self.height = wh
        self.setWindowFlags(Qt.FramelessWindowHint)  # 去边框
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.percent = 0
        self.pen = QPen()
        # 添加渐变效果
        gradient = QConicalGradient(0,0,90)    # 设置锥形渐变的x,y坐标点，起始角度
        gradient.setColorAt(0,Qt.red)   # 设置起始角度的颜色
        gradient.setColorAt(0.2,Qt.yellow)   # 设置起始角度的颜色
        gradient.setColorAt(0.4,Qt.blue)   # 设置起始角度的颜色
        gradient.setColorAt(0.6,Qt.green)   # 设置起始角度的颜色
        gradient.setColorAt(0.8,Qt.black)   # 设置起始角度的颜色
        gradient.setColorAt(1,Qt.red)   # 设置的颜色180度时颜色为红色

        # 将渐变效果添加至画刷
        self.pen.setBrush(gradient)
        self.pen.setWidth(8)
        self.pen.setCapStyle(Qt.RoundCap)
    def paintEvent(self, event):
        rectf = QRectF(10,10,self.width-20,self.height-20)    # 获取绘制的举行范围
        painter = QPainter(self)
        rotateAngle = 360*self.percent/100  # 绘制角度

        # 绘制准备工作
        painter.setRenderHints(QPainter.Antialiasing)   # 启用反锯齿
        painter.setPen(self.pen)    # 设置画笔
        painter.drawArc(rectf, 90*16, -rotateAngle*16)  # 画一个圆弧，指定圆弧的矩形范围，圆弧起始角度，圆弧扫过的角度
        # painter.setPen(QColor())
        painter.drawText(rectf,Qt.AlignCenter,'%d%%' % self.percent)    # 显示当前进度
        self.update()
    def update_percent(self,percent):
        self.percent = percent

class Water(QWidget):
    def __init__(self,parent=None):
        super(Water, self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint)     # 窗体去边框
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.resize(230,230)    # 设置窗口大小

        self.bg_color = QColor("#95BBFF")   # 设置进度条颜色
        self.water_offset = 0.005   # 设置偏移量，值越大，波形振幅越高
        self.offset = 50
        self.percent = 0

    def paintEvent(self, event):
        painter = QPainter()    # 绘制事件
        painter.setRenderHints(QPainter.Antialiasing)   # 启用反锯齿
        painter.begin(self)     # 启动绘制
        painter.setPen(Qt.NoPen)    # 设置无画笔

        percentage = 1 - self.percent/100   # 设置百分比
        # 水波走向：正弦函数 y = A(wx+l) + k
        w = 2 * math.pi / 230   # w表示周期，值越大密度越大
        A = 230 * self.water_offset # A表示振幅，理解为水波的上下振幅
        k = 230 *percentage     # k表示y的偏移量，可以理解为进度

        water1 = QPainterPath() # 绘制器路径，可以在封闭的子路径中将构建块连接起来
        water2 = QPainterPath()

        # 指定起始点
        water1.moveTo(5,230)
        water2.moveTo(5,230)
        self.offset += 0.6

        if self.offset > 230/2: # 不知道有什么用
            self.offset = 0
        i = 5

        rectf = QRectF(10,10,230-20,230-20) # 获取绘制的矩形大小
        while i<230-5:
            waterY1 = A*math.sin(w*i + self.offset) + k
            waterY2 = A*math.sin(w*i + self.offset + 230/2*w) + k

            water1.lineTo(i,waterY1)
            water2.lineTo(i,waterY2)
            i += 1

        water1.lineTo(230-5,230)
        water2.lineTo(230-5,230)

        totalpath = QPainterPath()
        painter.drawRect(self.rect())   # 画一个矩形
        painter.save()
        totalpath.addEllipse(rectf)     # 将矩形添加如一个椭圆
        # totalpath.intersected(water1)
        painter.setPen(Qt.NoPen)

        #设置水波的透明度
        watercolor1 =QColor(self.bg_color)
        watercolor1.setAlpha(100)
        watercolor2 = QColor(self.bg_color)
        watercolor2.setAlpha(150)
        path = totalpath.intersected(water1)
        painter.setBrush(watercolor1)
        painter.drawPath(path)


        path = totalpath.intersected(water2)
        painter.setBrush(watercolor2)
        painter.drawPath(path)
        painter.restore()
        painter.end()
    def update_percent(self, p):
        self.percent = p
        if self.water_offset < 0.05:
            self.water_offset += 0.001
        return p

def Animation(parent, type=b"windowOpacity", from_value=0, to_value=1, ms=1000, connect=None):

    anim = QPropertyAnimation(parent, type)
    anim.setDuration(ms)
    anim.setStartValue(from_value)
    anim.setEndValue(to_value)
    if connect:
        anim.finished.connect(connect)
    anim.start()
    return anim

if __name__ == '__main__':
    app = QApplication([])
    obj = Progress()
    obj.show()
    app.exec_()



