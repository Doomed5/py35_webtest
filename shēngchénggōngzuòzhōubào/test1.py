import pandas as pd

#df = pd.DataFrame({"id":[1,2,3],})
df = pd.DataFrame({"id":[1,2,3],'name':["zhangsan",'lisi','wangwu'],'arg':[28,42,10]})
df = df.set_index("id")
print(df)
df.to_excel('people.xlsx')
