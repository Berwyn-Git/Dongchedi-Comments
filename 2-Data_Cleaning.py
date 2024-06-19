import pandas as pd


data = pd.read_csv("Result.csv", header=None, names=['content', 'post_link'])
keywords = ['汇款', '付款', '扣款', '月供', '贷款', '还款', '利率']

filtered_data = data[data.iloc[:, 0].astype(str).str.contains('|'.join(keywords), na=False)]

filtered_data = filtered_data.drop_duplicates()
filtered_data = filtered_data.dropna()

filtered_data.to_csv('filterd_data.csv', index=False, header=False)