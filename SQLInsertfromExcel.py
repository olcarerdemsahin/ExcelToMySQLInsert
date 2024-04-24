import pandas as pd

# Define Dataset
df = pd.read_excel('Example Dataset.xlsx')

# # Change NaN values empty string
df.fillna('', inplace=True)

# Define Table Names and Columns
sql_insert = "INSERT INTO `tablename` (`column1`, `column2`, `column3`, `column4`, `column5`) VALUES "

# Create SQL Values
sql_values = []
for index, row in df.iterrows():
    ExcelColumn1 = row['ExcelColumn1']
    ExcelColumn2 = row['ExcelColumn2']
    ExcelColumn3 = row['ExcelColumn3']
    ExcelColumn4 = row['ExcelColumn4']
    ExcelColumn5 = row['ExcelColumn5']

    values = f"('{ExcelColumn1}', '{ExcelColumn2}', '{ExcelColumn3}', '{ExcelColumn4}', '{ExcelColumn5}')"
    sql_values.append(values)

# Combine SQL Values
sql_insert += ", ".join(sql_values)

# Create MySQL Insert Query
with open('InsertMySQLQuery.sql', 'w') as file:
    file.write(sql_insert)
