import pandas as pd 
  
# read an excel file and convert  
# into a dataframe object 
df = pd.DataFrame(pd.read_excel("Population Density.xlsx")) 
  
# show the dataframe 
df.to_csv('PopDensity.csv',index=True,header=False)

print(df) 