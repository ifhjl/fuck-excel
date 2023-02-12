import pandas as pd
def change_time(name,path):
    data = pd.read_excel(path,parse_dates=[name])
    data.to_excel(path)
#例子
change_time("时间","information.xlsx",index=False)
