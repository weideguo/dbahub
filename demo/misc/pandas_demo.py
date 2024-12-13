import pandas as pd

data = {'Name': ['Alice1', 'Bob1', 'Charlie1'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)

writer = pd.ExcelWriter('output.xlsx',mode='a')    # 即使使用追加模式也不能同个sheet再次写
df.to_excel(writer, sheet_name='Sheet1', index=False)

writer.close()
