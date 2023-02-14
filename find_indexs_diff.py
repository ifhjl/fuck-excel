
import pandas as pd
 
def clear(path1,path2,name1,name2):
    data1 = pd.read_excel(path1)
    data2 = pd.read_excel(path2)
    data1.set_index(name1)
    data2.set_index(name2)
    id1 = data1.index.unique()
    id2 = data2.index.unique()
    print("差异为：{}".format(id1.difference(id2)))

