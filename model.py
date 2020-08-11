import numpy as np 
import pandas as pd
import pickle 


data = pd.read_csv("dataset.csv")

data = data.drop(labels='EMPTY_COLUMN',axis=1)
data = data.drop(labels='HOUSEHOLD_SIZE',axis=1) 

for i in range (len(data)) :
  if data['INCOME_CLASSIFIER'][i] != 0 and data['INCOME_CLASSIFIER'][i] != 1 : 
    data = data.drop(i,axis=0)

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy ='mean')
l=data.iloc[:,10:11].values
imputer.fit(l)
data['AGE_HEAD_OF_HOUSEHOLD']=imputer.transform(l)

data['ACCESS_TO_TOILET_FINAL'] = data['ACCESS_TO_TOILET_FINAL'].fillna('not known')
data['NUM_ADULT_IN_HOUSEHOLD'] = data['HOUSE_HOLD_SIZE']-data['NUM_CHILD_IN_HOUSEHOLD'] 

data  = data.drop(labels='FAVORITE_NUMBER' , axis=1)

l =[18,60,89,278,176914,176928,176962,249675,249691]
for i in range (len(data)) :
  if i not in l :
    if data['TOTAL_NUM_ROOMS'][i] > 16 :
      data['TOTAL_NUM_ROOMS'][i] = 16 

data = pd.get_dummies(data, columns=["OWN_COMPUTER","OWN_TV"],drop_first=True)

l =[18,60,89,278,176914,176928,176962,249675,249691]
for i in range (len(data)) :
  if i not in l :
    if data['HOUSE_HOLD_SIZE'][i] > 11 :
      data['HOUSE_HOLD_SIZE'][i] = 11

l =[18,60,89,278,176914,176928,176962,249675,249691]
for i in range (len(data)) :
  if i not in l :
    if data['NUM_CHILD_IN_HOUSEHOLD'][i] > 8 :
      data['NUM_CHILD_IN_HOUSEHOLD'][i] = 8
    
data = pd.get_dummies(data,columns=['TENURE_STATUS_FINAL','TYPE_LIVING_QUARTERS','ACCESS_TO_TOILET_FINAL','ACCESS_TO_PIPE_WATER_FINAL','INTERNET_ACCESS_FINAL','HEAD_OF_HOUSEHOLD','EMPLOYEMENT_HEAD_HOUSEHOLD_FINAL'],drop_first=True)

y = data.iloc[:,5:6].values
data  = data.drop(labels='INCOME_CLASSIFIER' , axis=1)
id = data['SN_ID'] 
data  = data.drop(labels='SN_ID' , axis=1)
X = data.iloc[:,:].values

# Training XGBoost on the Training set
from xgboost import XGBClassifier
classifier = XGBClassifier(max_depth=8)
classifier.fit(X, y)

pickle.dump(classifier, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
