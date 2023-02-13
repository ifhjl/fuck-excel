#本程序对特征表进行排序，并从0到1进行排序，如需增加或修改功能请自行更改
import pandas as pd


def specialize(name,path):
    data = pd.read_excel(path)
    print("改列的元素按排序的结果为:{}，将按照由0开始的排序对其进行特征化。".format(sorted(data[name].unique())))
    data[name] = sorted(data[name])
    for i in range(len(data[name].unique())):
        data[name] = data[name].replace({data[name].unique()[i]:i})
    data.to_excel(path,index=False)
    print("完成")
