
import pandas as pd
import json
import csv
import statsmodels.api as sm
#import InsertToDb 



def GetPreDict(df_pre):
    #build model
    df= pd.read_csv('..\Marketing_Leads_India.csv')
    df_y = df['Converted']
    X_train_sm =preparedata(df)
    logm3 = sm.GLM(df_y,X_train_sm, family = sm.families.Binomial())
    res3 = logm3.fit()
    
    #predict
    df= pd.read_csv('..\Marketing_Leads_India.csv')
    df= df.drop(['Converted'], axis=1)
    df=pd.concat([df,df_pre])
    df=preparedata(df)
    y_train_pred= res3.predict(df[-1:])
    y_train_pred = y_train_pred.values
    score=int(y_train_pred*100) 
    #print("score : ",score)

    return score

def preparedata(df):
    with open('..\ModelColumns.txt') as f:
        lines = f.readlines()
    col=lines[0].split(",")
    df = df.drop(['Lead Number'], axis=1)
    df['Lead Source'] = df['Lead Source'].replace(['bing','Click2call','Press_Release','Social Media','Live Chat','youtubechannel'
                        ,'testone','Pay per Click Ads','welearnblog_Home','WeLearn','blog','NC_EDM'],'Other_Source')
    df["Do Not Email"] = df["Do Not Email"].map({'Yes': 1, "No": 0})
    df["Do Not Call"] = df["Do Not Call"].map({'Yes': 1, "No": 0})
    dummy1 = pd.get_dummies(df[['Lead Origin', 'Lead Source', 'Last Activity', 'Specialization','What is your current occupation',
                                     'Tags','Lead Quality','City','Last Notable Activity']], drop_first=True)
    df = pd.concat([df, dummy1], axis=1)
    X_t =df[df[col].columns]
    X_t_sm = sm.add_constant(X_t)
    X_t_sm = sm.add_constant(X_t_sm[col])
    return X_t_sm


import sqlalchemy as db
from sqlalchemy import create_engine



json_file=open('data.json','r')
csv_file=open('data_file.csv','w')

json_data_to_python_dict=json.load(json_file)
write=csv.writer(csv_file)

write.writerow(json_data_to_python_dict.keys())
write.writerow(json_data_to_python_dict.values())
json_file.close()
csv_file.close()
df= pd.read_csv('data_file.csv')
score=GetPreDict(df)
lead=df['Lead Number'][0]
#InsertToDb.connect_and_insert_to_postgres(lead,score)
print("Lead Number: ",lead,"Score : ",score)

