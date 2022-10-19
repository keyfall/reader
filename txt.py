# Python开发学习笔记:Python开发简单的GUI文本编辑器

# 导入需要的包
from tkinter import *  # GUI包
from tkinter.scrolledtext import ScrolledText  # 可滚动的多行文本区域控件


# 定义按钮使用到的事件函数;函数必须定义在调用之前,否则会报函数未定义的错误
# with open() as:文本文件操作方法;打开文本文件
def load():
    if (filename.get() != ""):  # 判断当前文件路径是否为空
        try:  # 获取路径为空的异常
            with open(filename.get(), encoding='utf-8') as file:
                contents.delete('1.0', END)  # 1.0:第一行第一个字符;END:文本结尾
                contents.insert(INSERT, file.read())
        except FileNotFoundError:
            contents.insert(INSERT, "当前文件" + filename.get() + "不存在")
    else:
        filename.insert(INSERT, "请在此输入文件完整路径或和程序同一文件路径的文件名称")


# 参数w代表write(写入)
def save():
    with open(filename.get(), 'w') as file:  # 默认保存路径为程序所在路径
        file.write(contents.get('1.0', END))


# 实例化对应的控件对象同时绑定需要的事件

form = Tk()  # 实例化窗体对象
form.title("简单的文本编辑器")  # 窗体标题

# anchor:

# 　　　　N:北  下

# 　　　　E:东  右

# 　　　　S:南 下

# 　　　　W:西 左

# 　　　　CENTER:中间

# Label控件如果不设置anchor属性只设置side属性,当程序运行时Label控件会根据side占满顶级窗口
# 就算设置expand=False属性也没用

Label(form, bg='red', text='文件路径:', height=1).pack(side=LEFT, anchor=NE)

contents = ScrolledText()  # 实例化富文本控件
contents.pack(side=BOTTOM, expand=True, fill=BOTH)  # 设置控件的相关属性

filename = Entry()  # 实例化单行文本框控件
filename.pack(side=LEFT, expand=True, fill=X)  # 设置单行文本框相关属性

# 实例化按钮控件并设置按钮的文本及事件
Button(text='打开', command=load).pack(side=LEFT)
Button(text='保存', command=save).pack(side=LEFT)

# 调用mainloop函数以进入主事件循环
mainloop()