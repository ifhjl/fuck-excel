# fuck-excel
第二课的作业中第一个的的第三小问的后面几步有点无聊就没做了  
第二个的最后一个顺序不对才做的出来，不知道为什么，答案代码如下：  
idx = pd.IndexSlice  
exclude = ['France', 'Canada', 'Amsterdam', 'Belgium']  
res = df.set_index(['Review Date', 'Company Location']).sort_index(level=0)  
res.loc[idx[2012:,~res.index.get_level_values(1).isin(exclude)],:].head(3)  
