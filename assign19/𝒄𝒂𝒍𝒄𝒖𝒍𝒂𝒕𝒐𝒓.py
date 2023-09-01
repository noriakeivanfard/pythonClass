import math
from functools import partial
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

s = 0

def stylesheet():
    main_window.Button_0.setStyleSheet(''' QPushButton {font: 700 italic 14pt "Segoe UI";background-color:rgb(0, 85, 0);color: rgb(255, 255, 255);}''')
    main_window.Button_1.setStyleSheet(''' QPushButton {font: 700 italic 14pt "Segoe UI";background-color:rgb(0, 85, 0);color: rgb(255, 255, 255);}''')
    main_window.Button_2.setStyleSheet(''' QPushButton {font: 700 italic 14pt "Segoe UI";background-color:rgb(0, 85, 0);color: rgb(255, 255, 255);}''')
    main_window.Button_3.setStyleSheet(''' QPushButton {font: 700 italic 14pt "Segoe UI";background-color:rgb(0, 85, 0);color: rgb(255, 255, 255);}''')
    main_window.Button_4.setStyleSheet(''' QPushButton {font: 700 italic 14pt "Segoe UI";background-color:rgb(0, 85, 0);color: rgb(255, 255, 255);}''')
    main_window.Button_5.setStyleSheet(''' QPushButton {font: 700 italic 14pt "Segoe UI";background-color:rgb(0, 85, 0);color: rgb(255, 255, 255);}''')
    main_window.Button_6.setStyleSheet(''' QPushButton {font: 700 italic 14pt "Segoe UI";background-color:rgb(0, 85, 0);color: rgb(255, 255, 255);}''')
    main_window.Button_7.setStyleSheet(''' QPushButton {font: 700 italic 14pt "Segoe UI";background-color:rgb(0, 85, 0);color: rgb(255, 255, 255);}''')
    main_window.Button_8.setStyleSheet(''' QPushButton {font: 700 italic 14pt "Segoe UI";background-color:rgb(0, 85, 0);color: rgb(255, 255, 255);}''')
    main_window.Button_9.setStyleSheet(''' QPushButton {font: 700 italic 14pt "Segoe UI";background-color:rgb(0, 85, 0);color: rgb(255, 255, 255);}''')

    main_window.Button_sqrt.setStyleSheet(''' QPushButton {font: 700 italic 14pt "Segoe UI";";background-color: rgb(48, 124, 0);color: rgb(6, 6, 6);}''')
    main_window.Button_cos.setStyleSheet(''' QPushButton {font:  700 italic 14pt "Segoe UI";;background-color:  rgb(48, 124, 0);color: rgb(6, 6, 6);}''')
    main_window.Button_tan.setStyleSheet(''' QPushButton {font:  700 italic 14pt "Segoe UI";;background-color:  rgb(48, 124, 0);color: rgb(6, 6, 6);}''')
    main_window.Button_cot.setStyleSheet(''' QPushButton {font:  700 italic 14pt "Segoe UI";;background-color:  rgb(48, 124, 0);color: rgb(6, 6, 6);}''')
    main_window.Button_abs.setStyleSheet(''' QPushButton {font:  700 italic 14pt "Segoe UI";;background-color:  rgb(48, 124, 0);color: rgb(6, 6, 6);}''')

    main_window.Button_sum.setStyleSheet(''' QPushButton {font:  700 italic 14pt "Segoe UI";background-color: rgb(0, 170, 127);color:  rgb(6, 6, 6);}''')
    main_window.Button_sub.setStyleSheet(''' QPushButton {font:  700 italic 14pt "Segoe UI";background-color: rgb(0, 170, 127);color:  rgb(6, 6, 6);}''')
    main_window.Button_div.setStyleSheet(''' QPushButton {font:  700 italic 14pt "Segoe UI";background-color: rgb(0, 170, 127);color:  rgb(6, 6, 6);}''')
    main_window.Button_eql.setStyleSheet(''' QPushButton {font:  700 italic 14pt "Segoe UI";background-color: rgb(0, 170, 127);color:  rgb(6, 6, 6);}''')
    main_window.Button_mul.setStyleSheet(''' QPushButton {font:  700 italic 14pt "Segoe UI";background-color: rgb(0, 170, 127);color:  rgb(6, 6, 6);}''')
    main_window.Button_dot.setStyleSheet(''' QPushButton {font:  700 italic 14pt "Segoe UI";background-color: rgb(0, 170, 127);color:  rgb(6, 6, 6);}''')

def num(n):
    num_1 = main_window.line_edit.text()
    num_2 = num_1 + n 
    main_window.line_edit.setText(num_2)
       
def cos():
    num_1 = main_window.line_edit.text()
    num_2 = float(num_1)
    num_3 = math.radians(num_2)
    result = math.cos(num_3)
    main_window.line_edit.setText(str(result))
    
def cot():
    num_1 = main_window.line_edit.text()
    num_2 = float(num_1)
    num_3 = math.radians(num_2)
    result = math.atan(num_3)
    main_window.line_edit.setText(str(result))

def log():
    num_1 = main_window.line_edit()
    num_2 = float(num_1)
    num_3 = math.radians(num_2)
    result = math.log(num_3)
    main_window.line_edit.setText(str(result))
    
def tan():
    num_1 = main_window.line_edit()
    num_2 = float(num_1)
    num_3 = math.radians(num_2)
    result = math.tan(num_3)
    main_window.line_edit.setText(str(result))
    
def AC():
    main_window.line_edit.setText("")
    
def C():
    num_1 = main_window.line_edit()
    num_2 = num_1[:-1]
    main_window.line_edit.setText(num_2)
    
def sqrt():
    num_1 = main_window.line_edit.text()
    num_2 = float(num_1)
    result = math.sqrt(num_2)
    main_window.line_edit.setText(str(result))
    
def abs():
    num_1 = main_window.text_line.text()
    num_2 = float(num_1)
    result = abs(num_2)
    main_window.text_line.setText(str(result))

def dot():
    num = main_window.line_edit()
    if "." not in num:
        main_window.line_edit.setText(main_window.line_edit.text() + ".")

def sum():
    global op , num_1
    op = "+"
    num = main_window.line_edit.text()
    num_1 = float(num)
    main_window.line_edit.setText("")
    
def sub(): 
    global op , num_1
    op = "-"
    num = main_window.line_edit.text()
    num_1 = float(num)
    main_window.line_edit.setText("")
    
def mul():
    global op , num_1
    op = "*"
    num = main_window.line_edit.text()
    num_1 = float(num)
    main_window.line_edit.setText("")

def div():
    global op , num_1
    op = "/"
    num = main_window.line_edit.text()
    num_1 = float(num)
    main_window.line_edit.setText("")
    
def eql():
    if op == "+":
        eq_sum()
    elif op == "-":
        eq_sub()
    elif op == "*":
        eq_mul()
    elif op == "/":
        eq_div()
def eq_sum():
    num_2 = float(main_window.line_edit.text())
    main_window.line_edit.setText("")
    result = num_1 + num_2
    main_window.line_edit.setText(str(result))
def eq_sub():
    num_2 = float(main_window.lineEdit.text())
    main_window.line_edit.setText("")
    result = num_1 - num_2
    main_window.line_edit.setText(str(result))

def eq_mul():
    num_2 = float(main_window.line_edit.text())
    main_window.line_edit.setText("")
    result = num_1 * num_2
    main_window.line_edit.setText(str(result))

def eq_div():
    try:
        num_2 = float(main_window.line_edit.text())
        main_window.line_edit.setText("")
        result = num_1 / num_2
        main_window.line_edit.setText(str(result))
    except:
        main_window.line_edit.setText("you can not divition by zero!")


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
main_window.Button_sub.clicked.connect(partial(num, "-"))
main_window.Button_mul.clicked.connect(partial(num, "*"))
main_window.Button_div.clicked.connect(partial(num, "/"))
main_window.Button_sqrt.clicked.connect(partial(sqrt))
main_window.Button_tan.clicked.connect(partial(tan))
main_window.Button_cos.clicked.connect(partial(cos))
main_window.Button_cot.clicked.connect(partial(cot))
main_window.Button_abs.clicked.connect(partial(abs))
main_window.Button_eql.clicked.connect(partial(eql))

app.exec_()
