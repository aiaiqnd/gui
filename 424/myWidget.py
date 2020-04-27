import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from human import Human

from ui_Widget import Ui_Widget


class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.boy = Human('Boy', 16)

        self.boy.nameChanged.connect(self.do_nameChanged)
        self.boy.ageChanged.connect(self.do_ageChanged_int)
        self.boy.ageChanged[str].connect(self.do_ageChanged_str)

    def on_sliderSetage_valueChanged(self, value):
        self.boy.setAge(value)

    def on_btnSetName_clicked(self):
        hisName = self.ui.editNameIput.text()
        self.boy.setName(hisName)

    def do_nameChanged(self, name):
        self.ui.editNameHello.setText('hello,' + name)

    @pyqtSlot(int)
    def do_ageChanged_int(self, age):
        self.ui.editAgeint.setText(str(age))

    @pyqtSlot(str)
    def do_ageChanged_str(self, info):
        self.ui.editAgeistr.setText(info)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    icon = QIcon(':/icons/images/tips.ico')
    app.setWindowIcon(icon)
    abc = QmyWidget()
    abc.show()
    sys.exit(app.exec_())
