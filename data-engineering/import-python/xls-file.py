# Import package
import pandas as pd

# Assign url of file: url
url =  'http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'

# Read in all sheets of Excel file: xls
dict = pd.read_excel(url, sheet_name=None)

# Print the sheetnames to the shell
print(dict.keys())

# Print the head of the first sheet (using its name, NOT its index)
print(dict['1700'].head())
