import pandas as pd
df = pd.DataFrame({'A':[34, 78, 54], 'B':[12, 67, 43],'C':[9,8,7]},index=['r1', 'r2', 'r3'])
print(df.iloc[:,:3])