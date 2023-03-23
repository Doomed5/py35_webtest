import tkinter as tk
import tkinter.tix
from tkinter import filedialog
from tkinter import *
import hashlib
import time
import office

LOG_LINE_NUM = 0


class MY_GUI:
    def __init__(self, my_window):
        self.my_window = my_window

    # 设置窗口
    def set_init_window(self):
        self.my_window.title("测试工具集合_v1.0")  # 窗口名
        # self.my_window.geometry('320x160+10+10')
        # #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.my_window.geometry('1068x681+10+10')
        # self.my_window["bg"] = "pink"                                    
        # self.my_window.attributes("-alpha",0.9)
        # #虚化，值越小虚化程度越高

        self.log_label = Label(self.my_window, text="日志")
        self.log_label.grid(row=12, column=0)
        # 文本框
        self.log_data_Text = Text(self.my_window, width=66, height=9)  # 日志框
        self.log_data_Text.grid(row=13, column=0, columnspan=10)

        # 按钮
        self.word_trans_to_pdf_button = Button(self.my_window, text="word转pdf", bg="pink", width=10,
                                               command=self.word_trans_to_pdf)  # 调用内部方法  加()为直接调用
        self.word_trans_to_pdf_button.grid(row=1, column=11)

    # 功能函数

    def word_trans_to_pdf(self):
        root = tk.Tk()
        root.withdraw()
        #FilePath = filedialog.askopenfilename()
        FloderPath = filedialog.askdirectory()

        path = FloderPath  # path这里，填写你存放word文件的位置，例如：C:/app/workbook
        office.word.docx2pdf(path=path)  # 程序就可以自动将该目录下的所有word文档，自动转换成pdf文档了

    # 获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        return current_time

    # 日志动态打印

    def write_log_to_Text(self,logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) +" " + str(logmsg) + "\n"      #换行
        if LOG_LINE_NUM <= 7:
            self.log_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0,2.0)
            self.log_data_Text.insert(END, logmsg_in)



def gui_start():
    init_window = tk.Tk()  # 实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()  # 父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


gui_start()
