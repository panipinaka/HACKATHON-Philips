from pandas import DataFrame
import pandas as pd
#import numpy as np
import glob
import os

path = r'E:\new' 
all_files = glob.glob(path + "/*.psv")
f_name=os.path.splitext(os.path.basename("p000001.psv"))[0]
data_collection = pd.read_csv("p000001.psv",sep='|',index_col=None, header=0)                 #cantains all file name
data_collection['hours']=data_collection.index                                              #adding hours coloumn
data_collection['identifier']=f_name 
data_collection=((data_collection[].isna.sum())/data_collection.shape[])*100
print(data_collection)

 
for filename in all_files:  
    if filename!="p000001.psv":                                                #loop over the filenames
        data = pd.read_csv(filename,sep='|',index_col=None, header=0)
        f_name=os.path.splitext(os.path.basename(filename))[0]                 #filename without extintion file
        data['hours']=data.index                                              #adding hours coloumn
        data['identifier']=f_name  
                                                    #adding identifier coloumn
        data_collection = data_collection.append(data) 
print( data_collection)


#data=df.fillna(0)
