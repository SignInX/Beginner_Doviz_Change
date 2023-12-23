import requests
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QDateTime


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setWindowTitle("Currency App")       
        Form.setFixedSize(279, 419)
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(140, 50, 111, 41))
        self.lcdNumber.setObjectName("USD")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_3.setGeometry(QtCore.QRect(140, 110, 111, 41))
        self.lcdNumber_3.setObjectName("EUR")
        self.lcdNumber_5 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_5.setGeometry(QtCore.QRect(140, 180, 111, 41))
        self.lcdNumber_5.setObjectName("GBP")
        self.lcdNumber_7 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_7.setGeometry(QtCore.QRect(140, 240, 111, 41))
        self.lcdNumber_7.setObjectName("CHF")
        self.lcdNumber_9 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_9.setGeometry(QtCore.QRect(140, 300, 111, 41))
        self.lcdNumber_9.setObjectName("CAD")
        self.lcdNumber_4 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_4.setGeometry(QtCore.QRect(140, 360, 111, 41))
        self.lcdNumber_4.setObjectName("AUD")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(35, 55, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(35, 115, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(35, 185, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(35, 245, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(35, 305, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(35, 365, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.labelTime = QtWidgets.QLabel(Form)
        self.labelTime.setGeometry(QtCore.QRect(40, 10, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelTime.setFont(font)
        self.labelTime.setObjectName("labelTime")



        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.retranslateUi(Form)

        self.doviz(Form)
        self.saat(Form)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        


    def doviz(self, Form):
        
       
        url = "http://data.fixer.io/api/latest?access_key="
        api_key = "API_KEY"

        try:
            res = requests.get(url + api_key)
            if res.status_code == 200:
                json_veri = res.json()

                res = requests.get(url + api_key)
                json_veri = res.json()


                
                usd_rate = json_veri["rates"]["USD"]
                eur_rate = json_veri["rates"]["EUR"]
                gbp_rate = json_veri["rates"]["GBP"]
                chf_rate = json_veri["rates"]["CHF"]
                cad_rate = json_veri["rates"]["CAD"]
                aud_rate = json_veri["rates"]["AUD"]
                try_rate = json_veri["rates"]["TRY"]
                
         
                
                self.lcdNumber.display(try_rate / usd_rate)
                self.lcdNumber_7.display(try_rate / chf_rate)
                self.lcdNumber_5.display(try_rate / gbp_rate)
                self.lcdNumber_9.display(try_rate / cad_rate)
                self.lcdNumber_4.display(try_rate / aud_rate)
                self.lcdNumber_3.display(try_rate / eur_rate)
                
                           

        except requests.RequestException as e:
            print("Error:", e)


          

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "USD"))
        self.label_2.setText(_translate("Form", "EUR"))
        self.label_3.setText(_translate("Form", "GBP"))
        self.label_4.setText(_translate("Form", "CHF"))
        self.label_5.setText(_translate("Form", "CAD"))
        self.label_7.setText(_translate("Form", "AUD"))


    def saat(self, Form):
        current_time = QDateTime.currentDateTime().toString("dd.MM.yyyy\thh:mm:ss")
        self.labelTime.setText(current_time)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
