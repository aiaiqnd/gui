import sys
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal


class Human(QObject):
    nameChanged = pyqtSignal(str)
    ageChanged =pyqtSignal([int], [str])

    def __init__(self, name='Mike', age = 10, parent =None):
        super().__init__(parent)
        self.setAge(age)
        self.setName(name)

    def setAge(self, age):
        self.__age = age
        self.ageChanged.emit(self.__age) #send int singnal
        if age <= 18:
            ageInfo = '你是 少年'
        elif 18< age <= 35:
            ageInfo = '你是 年轻人'
        elif 35 < age <=55:
            ageInfo = '你是 中年人'
        elif 55< age <= 80:
            ageInfo = '您是 老人'
        else:
            ageInfo = '您是 寿星啊'
        self.ageChanged[str].emit(ageInfo)

    def setName(self, name):
        self.__name = name
        self.nameChanged.emit(self.__name)

class Responsor(QObject):
    @pyqtSlot(int)
    def do_ageChanged_int(self, age):
        print('你的年龄是:' +str(age))

    @pyqtSlot(str)
    def do_ageChanged_str(self, ageInfo):
        print(ageInfo)

    @pyqtSlot(str)
    def do_nameChanged(self, name):
        print("hello," + name)

if __name__ == '__main__':
    print("**创建对象时**")
    boy = Human('Boy', 16)
    resp = Responsor()
    boy.nameChanged.connect(resp.do_nameChanged)
    boy.ageChanged.connect(resp.do_ageChanged_int)
    boy.ageChanged[str].connect(resp.do_ageChanged_str)

    print('\n **建立关联后**')
    boy.setAge(35)
    boy.setName('Jack')

    boy.ageChanged[str].disconnect(resp.do_ageChanged_str)
    print("\n **断开ageChanged[str]的关联后**")
    boy.setAge(10)



















