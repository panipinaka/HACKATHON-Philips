from pandas import DataFrame
import pandas as pd
#import numpy as np

import glob
import os

path = r'E:\new' 
all_files = glob.glob(path + "/*.psv")
f_name=os.path.splitext(os.path.basename("p000001.psv"))[0]
data_collection = pd.read_csv("p000001.psv",sep='|',index_col=None, header=0)                 
data_collection['hours']=data_collection.index                                              
data_collection['identifier']=f_name 
##data_collection.loc['NAN_VALUE'] =(data_collection.isna().sum()/data_collection.shape[0])*100
#print(data_collection)

for filename in all_files:  
    if filename!="p000001.psv":                                                                             
        data = pd.read_csv(filename,sep='|',index_col=None, header=0)
        f_name=os.path.splitext(os.path.basename(filename))[0]                 
        data['hours']=data.index
        data['identifier']=f_name  
        data_collection = data_collection.append(data)
new=data_collection.copy()  
new.loc['NAN_VALUE'] = (new.isna().sum()/new.shape[0])*100   

#        else:
#            continue
#        #num=(data_collection.isna().sum()/data_collection.shape[0])*100
#        #data_collection = data_collection.append(num) 
#        #value:data_collection.loc['num']= (data_collection.isna().sum()/data_collection.shape[0])*100
#       # data_collection.loc['mean'] = data_collection.mean()
#        #print(data_collection[data_collection["value"]<40])
#
#
#dfdfdfd
##data=df.fillna(0)'''
