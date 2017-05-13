import csv as csv
import numpy as np
import pandas as pd

df = pd.read_csv('train.csv') 
dd = pd.read_csv('user.csv')
ds = pd.read_csv('position.csv')
da = pd.read_csv('ad.csv')

data = pd.merge(df, dd, on=['userID'], how='left') 
data = data[['userID', 'label', 'clickTime', 'conversionTime', 'creativeID', 'positionID', 'connectionType', 'telecomsOperator', 'age', 'gender', 'education', 'marriageStatus' ,'haveBaby' ,'hometown' ,'residence']]

data = pd.merge(data, ds, on=['positionID'], how = 'left')
data = data[['userID', 'label', 'clickTime', 'conversionTime', 'creativeID', 'positionID', 'connectionType', 'telecomsOperator', 'age', 'gender', 'education', 'marriageStatus' ,'haveBaby' ,'hometown' ,'residence', 'sitesetID', 'positionType']]

data = pd.merge(data, da, on=['creativeID'], how = 'left')
data = data[['userID', 'label', 'clickTime', 'conversionTime', 'creativeID', 'positionID', 'connectionType', 'telecomsOperator', 'age', 'gender', 'education', 'marriageStatus' ,'haveBaby' ,'hometown' ,'residence', 'adID', 'camgaignID', 'appID', 'appPlatform' , 'sitesetID', 'positionType']]


print data.head(5)

data.to_csv(r'data.csv', encoding='gbk')


