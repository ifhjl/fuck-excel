import PySimpleGUI as sg 
import pandas as pd
 
def clear(path1,path2,name1,name2):
    data1 = pd.read_excel(path1)
    data2 = pd.read_excel(path2)
    data1.set_index(name1)
    data2.set_index(name2)
    id1 = data1.index.unique()
    id2 = data2.index.unique()
    sg.Print("差异为：{}".format(id1.difference(id2)))

sg.theme('SandyBeach')

layout=[
        [sg.Text('正在读取的文件1是：',font=("微软雅黑", 12)),sg.Text('',key='filename1',size=(50,1),font=("微软雅黑", 10),text_color='blue')],
        [sg.Text('正在读取的文件2是：',font=("微软雅黑", 12)),sg.Text('',key='filename2',size=(50,1),font=("微软雅黑", 10),text_color='blue')],
        [sg.Text("输入列1的头名称："),sg.Input(key="name1",size=(15,1),text_color='blue')],
        [sg.Text("输入列2的头名称："),sg.Input(key="name2",size=(15,1),text_color='blue')],
        [sg.FileBrowse('选择文件',key='file1',target="filename1"),sg.FileBrowse('选择文件',key='file2',target="filename2"),sg.Button("执行"),sg.Button("关闭程序"),sg.Button("备注")]
       ]

window=sg.Window("Excel处理",layout,font=("微软雅黑",15),default_element_size=(500,100))

while True:
    event,values=window.read()
    if event in (None,"关闭程序"):
        break
    if event in ("执行"):
        clear(values["file1"],values["file2"],values["name1"],values["name2"])
    elif event in ("备注"):
        sg.Print("备注")
        sg.Print("这个是模板")
window.close()