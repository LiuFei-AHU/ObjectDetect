import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from pyqt5_plugins.examplebuttonplugin import QtGui
from detect import detect_obj
from generate import generate_random_image
from MainWindow import Ui_MainWindow


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.openImage)
        self.generateButton.clicked.connect(self.generateImage)
        self.showInfo.setText("")
        self.showImg.setText("")

    def openImage(self):
        imgPath, _ = QFileDialog.getOpenFileName(self.centralwidget, "选择图片", "./", "*.png;;*.jpg;;All Files(*)")
        print(imgPath)
        self.showImage(imgPath)

    def generateImage(self):
        img = generate_random_image(save=True, save_path='./resource')
        self.showImage(img)

    def showImage(self, imgPath):
        r_info, r_img_name = detect_obj(imgPath)
        print(r_img_name)
        img = QtGui.QPixmap(r_img_name).scaled(self.showImg.width(), self.showImg.height())
        self.showImg.setPixmap(img)
        text = ""
        for info in r_info:
            text = text + str(info[1]).strip() + ' ' + info[2] + ' ;'
        self.showInfo.setText(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())
