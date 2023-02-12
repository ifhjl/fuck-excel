import pandas as pd
#name->list's name  path->excel_file's path
def delete_same(name,path):
  data = pd.read_excel(path)
  data = data.drop_duplicates(subset=[name],keep="first")
  data.to_excel(path,index=False)
  
