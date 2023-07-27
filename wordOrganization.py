
import pandas as pd
import openpyxl

df = pd.read_excel("book1.xlsx")


df.sort_values(by=['name'],ascending=True, inplace=True)
#df.sort_values(by='name')
print(df)
df.to_excel('book1.xlsx', sheet_name='Sheet 2')


#if " "== "☒":

