#本程序对特征表进行排序，并从0开始进行排序，如需增加或修改功能请自行更改
import pandas as pd


def specialize(name,path):
    data = pd.read_excel(path)
    #此方法可使目标文件的顺序不变且按照升序进行排序
    data[name] = data[name].replace([i for i in data.sort_values(name)[name].unique()],[j for j in range(len(data[name].unique()))])
    data.to_excel(path,index=False)
    print("完成")
