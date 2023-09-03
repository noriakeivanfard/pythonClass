import math
from functools import partial
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

op = 0
num_1 = 0
num_2 = 0

def stylesheet():
    main_window.Button_0.setStyleSheet('''QPushButton {font: 700 italic 14pt "Segoe UI";
                                       background-color:rgb(0, 85, 0);
                                       color: rgb(255, 255, 255);}''')
    
    main_window.Button_1.setStyleSheet('''QPushButton {font: 700 italic 14pt "Segoe UI";
                                       background-color:rgb(0, 85, 0);
                                       color: rgb(255, 255, 255);}''')
    
    main_window.Button_2.setStyleSheet('''QPushButton {font: 700 italic 14pt "Segoe UI";
                                       background-color:rgb(0, 85, 0);
                                       color: rgb(255, 255, 255);}''')
    
    main_window.Button_3.setStyleSheet('''QPushButton {font: 700 italic 14pt "Segoe UI";
                                       background-color:rgb(0, 85, 0);
                                       color: rgb(255, 255, 255);}''')
    
    main_window.Button_4.setStyleSheet('''QPushButton {font: 700 italic 14pt "Segoe UI";
                                       background-color:rgb(0, 85, 0);
                                       color: rgb(255, 255, 255);}''')
    
    main_window.Button_5.setStyleSheet('''QPushButton {font: 700 italic 14pt "Segoe UI";
                                       background-color:rgb(0, 85, 0);
                                       color: rgb(255, 255, 255);}''')
    
    main_window.Button_6.setStyleSheet('''QPushButton {font: 700 italic 14pt "Segoe UI";
                                       background-color:rgb(0, 85, 0);
                                       color: rgb(255, 255, 255);}''')
    
    main_window.Button_7.setStyleSheet('''QPushButton {font: 700 italic 14pt "Segoe UI";
                                       background-color:rgb(0, 85, 0);
                                       color: rgb(255, 255, 255);}''')
    
    main_window.Button_8.setStyleSheet('''QPushButton {font: 700 italic 14pt "Segoe UI";
                                       background-color:rgb(0, 85, 0);
                                       color: rgb(255, 255, 255);}''')
    
    main_window.Button_9.setStyleSheet('''QPushButton {font: 700 italic 14pt "Segoe UI";
                                       background-color: rgb(0, 85, 0);
                                       color: rgb(255, 255, 255);}''')

    main_window.Button_sqrt.setStyleSheet('''QPushButton {font: 700 italic 14pt "Segoe UI";
                                          background-color: rgb(48, 124, 0);
                                          color: rgb(6, 6, 6);}''')
    
    main_window.Button_cos.setStyleSheet('''QPushButton {font:  700 italic 14pt "Segoe UI";
                                         ;background-color: rgb(48, 124, 0);
                                         color: rgb(6, 6, 6);}''')
    
    main_window.Button_tan.setStyleSheet('''QPushButton {font: 700 italic 14pt "Segoe UI";
                                         background-color: rgb(48, 124, 0);
                                         color: rgb(6, 6, 6);}''')
    
    main_window.Button_cot.setStyleSheet('''QPushButton {font:  700 italic 14pt "Segoe UI";
                                         background-color:  rgb(48, 124, 0);
                                         color: rgb(6, 6, 6);}''')
    
    main_window.Button_abs.setStyleSheet('''QPushButton {font:  700 italic 14pt "Segoe UI";
                                         background-color:  rgb(48, 124, 0);
                                         color: rgb(6, 6, 6);}''')
    
    main_window.Button_fac.setStyleSheet('''QPushButton {font:  700 italic 14pt "Segoe UI";
                                         background-color:  rgb(48, 124, 0);
                                         color: rgb(6, 6, 6);}''')
    
    main_window.Button_mod.setStyleSheet('''QPushButton {font:  700 italic 14pt "Segoe UI";
                                         background-color:  rgb(48, 124, 0);
                                         color: rgb(6, 6, 6);}''')
    
    main_window.Button_sqrt.setStyleSheet('''QPushButton {font:  700 italic 14pt "Segoe UI";
                                          background-color:  rgb(48, 124, 0);
                                          color: rgb(6, 6, 6);}''')

    main_window.Button_sum.setStyleSheet('''QPushButton {font:  700 italic 14pt "Segoe UI";
                                         background-color: rgb(0, 170, 127);
                                         color:  rgb(6, 6, 6);}''')
    
    main_window.Button_min.setStyleSheet('''QPushButton {font:  700 italic 14pt "Segoe UI";
                                         background-color: rgb(0, 170, 127);
                                         color:  rgb(6, 6, 6);}''')
    
    main_window.Button_div.setStyleSheet('''QPushButton {font:  700 italic 14pt "Segoe UI";
                                         background-color: rgb(0, 170, 127);
                                         color:  rgb(6, 6, 6);}''')
    
    main_window.Button_eql.setStyleSheet('''QPushButton {font:  700 italic 14pt "Segoe UI";
                                         background-color: rgb(0, 170, 127);
                                         color:  rgb(6, 6, 6);}''')
    
    main_window.Button_mul.setStyleSheet('''QPushButton {font:  700 italic 14pt "Segoe UI";
                                         background-color: rgb(0, 170, 127);
                                         color:  rgb(6, 6, 6);}''')
    
    main_window.Button_dot.setStyleSheet('''QPushButton {font:  700 italic 14pt "Segoe UI";
                                         background-color: rgb(0, 170, 127);
                                         color:  rgb(6, 6, 6);}''')
    
    main_window.Button_pow.setStyleSheet('''QPushButton {font:  700 italic 14pt "Segoe UI";
                                         background-color: rgb(0, 170, 127);
                                         color:  rgb(6, 6, 6);}''')
    
    main_window.Button_pi.setStyleSheet('''QPushButton {font:  700 italic 14pt "Segoe UI";
                                        background-color: rgb(0, 170, 127);
                                        color:  rgb(6, 6, 6);}''')

def num(n):
    num_1 = main_window.lineEdit.text()
    num_2 = num_1 + n
    main_window.lineEdit.setText(num_2)
       
def cos():
    num_1 = main_window.lineEdit.text()
    num_2 = float(num_1)
    num_3 = math.radians(num_2)
    result = math.cos(num_3)
    main_window.lineEdit.setText(str(result))
    
def cot():
    num_1 = main_window.lineEdit.text()
    num_2 = float(num_1)
    num_3 = math.radians(num_2)
    result = math.atan(num_3)
    main_window.lineEdit.setText(str(result))

def log():
    num_1 = main_window.lineEdit.text()
    num_2 = float(num_1)
    num_3 = math.radians(num_2)
    result = math.log(num_3)
    main_window.lineEdit.setText(str(result))
    
def tan():
    num_1 = main_window.lineEdit.text()
    num_2 = float(num_1)
    num_3 = math.radians(num_2)
    result = math.tan(num_3)
    main_window.lineEdit.setText(str(result))
    
def AC():
    main_window.lineEdit.setText("")
    
def C():
    num_1 = main_window.lineEdit.text()
    num_2 = num_1[:-1]
    main_window.lineEdit.setText(num_2)
    
def sqrt():
    num_1 = main_window.lineEdit.text()
    num_2 = float(num_1)
    num_3 = math.radians(num_2)
    result = math.sqrt(num_3)
    main_window.lineEdit.setText(str(result))
    
def abs():
    num_1 = main_window.lineEdit.text()
    num_2 = float(num_1)
    result = abs(num_2)
    main_window.lineEdit.setText(str(result))
    
def pow():
    num_1 = main_window.lineEdit.text()
    num_2 = float(num_1)
    num_3 = num_2 ** 2
    main_window.lineEdit.setText(str(num_3))
    
def pi():
    num_1 = main_window.lineEdit.text()
    main_window.lineEdit.setText(num_1 + "3.14")

def fac():
    num_1 = main_window.lineEdit.text()
    num_2 = str(num_1)
    num_3 = math.radians(num_2)
    result = math.factorial(num_3)
    main_window.lineEdit.setText(str(result))
    
def mod():
    num_1 = main_window.lineEdit.text()
    num_2 = float(num_1)
    result = math.modf(num_2)
    main_window.lineEdit.setText(str(result))
    
def dot():
    num = main_window.lineEdit.text()
    if "." not in num:
        main_window.lineEdit.setText(main_window.line_edit.text() + ".")
        
def eql(op):
    if op == "+":
        eql_sum()
    elif op == "-":
        eql_sub()
    elif op == "*":
        eql_mul()  
    elif op == "/":
        eql_div()

def eql_sum():
    num_2 = float(main_window.lineEdit.text())
    main_window.lineEdit.setText("")
    result = num_1 + num_2
    main_window.lineEdit.setText(str(result))
def eql_sub():
    num_2 = float(main_window.lineEdit.text())
    main_window.lineEdit.setText("")
    result = num_1 - num_2
    main_window.lineEdit.setText(str(result))

def eql_mul():
    num_2 = float(main_window.lineEdit.text())
    main_window.lineEdit.setText("")
    result = num_1 * num_2
    main_window.lineEdit.setText(str(result))

def eql_div():
    try:
        num_2 = float(main_window.lineEdit.text())
        main_window.lineEdit.setText("")
        result = num_1 / num_2
        main_window.lineEdit.setText(str(result))
    except:
        main_window.lineEdit.setText("can not divition by zero!")

app = QApplication([])
loader = QUiLoader()

main_window = loader.load("calculator.ui")
stylesheet()
main_window.show()

main_window.Button_0.clicked.connect(partial(num, "0"))
main_window.Button_1.clicked.connect(partial(num, "1"))
main_window.Button_2.clicked.connect(partial(num, "2"))
main_window.Button_3.clicked.connect(partial(num, "3"))
main_window.Button_4.clicked.connect(partial(num, "4"))
main_window.Button_5.clicked.connect(partial(num, "5"))
main_window.Button_6.clicked.connect(partial(num, "6"))
main_window.Button_7.clicked.connect(partial(num, "7"))
main_window.Button_8.clicked.connect(partial(num, "8"))
main_window.Button_9.clicked.connect(partial(num, "9"))
main_window.Button_dot.clicked.connect(partial(num, "."))

main_window.Button_C.clicked.connect(C)
main_window.Button_AC.clicked.connect(AC)

main_window.Button_sum.clicked.connect(partial(num, "+"))
main_window.Button_min.clicked.connect(partial(num, "-"))
main_window.Button_mul.clicked.connect(partial(num, "*"))
main_window.Button_div.clicked.connect(partial(num, "/"))
main_window.Button_sqrt.clicked.connect(partial(sqrt))
main_window.Button_tan.clicked.connect(partial(tan))
main_window.Button_cos.clicked.connect(partial(cos))
main_window.Button_cot.clicked.connect(partial(cot))
main_window.Button_abs.clicked.connect(partial(abs))
main_window.Button_pow.clicked.connect(partial(pow))
main_window.Button_pi.clicked.connect(partial(pi))
main_window.Button_fac.clicked.connect(partial(fac))
main_window.Button_mod.clicked.connect(partial(mod))
main_window.Button_eql.clicked.connect(partial(eql, op))

app.exec_()
