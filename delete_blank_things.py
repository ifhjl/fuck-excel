import pandas as pd    
import re
 
def clear(name,path):
    data=pd.read_excel(path)
    sg.Print(path)
    count=0
    boo=1
    for i in data[name]:
        length=len(i)
        if(i[length-1]==" "):
            data[name][count]=i[:length-1]
            sg.Print("名字后有空格的为：{}".format(i))
            boo=0
        count=count+1
    data.to_excel(path)
    if(boo==1):
        print("数据正常，无需修改",index=False)
    else:
        print("已完成，修改后的文件为{}".format(path))

