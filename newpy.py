import numpy as np 
import pandas as pd 
Q1= np.array([2,np.nan,6,7,3,2])
Q2=np.nansum(Q1)
Q3=pd.Series([4,5,2,np.nan,1,np.nan])
Q4=Q3.isnull()
a=pd.Series([4,5,2,np.nan,1,np.nan])
Q5=a[a.notnull()]
b=pd.Series([4,5,2,np.nan,1,np.nan])
Q6=b.fillna(100)


c=pd.DataFrame([[4,5,2,9,1,8],
                  [5, 6, np.nan,3,np.nan,2],
                  [6,np.nan,7,np.nan,4,3]])
Q7=c.fillna(100)
d=pd.Series([4,5,2,np.nan,1,np.nan])
Q8=d.dropna()
e=pd.DataFrame([[4,5,2,9,1,8],
                  [5, 6, np.nan,3,np.nan,2],
                  [6,np.nan,7,np.nan,4,3]])
Q9=e.dropna(axis=1)
f=pd.DataFrame([[4,5,2,9,1,8],
                  [5, 6, np.nan,3,np.nan,2],
                  [6,np.nan,7,np.nan,4,3]])
Q10=f.dropna(axis=0)
g=pd.DataFrame([[4,5,2,9,1,8],
                  [5, 6, np.nan,3,np.nan,2],
                  [6,np.nan,7,np.nan,4,3]])
Q11=g.dropna(axis='rows', thresh=5)
Q12=pd.DataFrame([[4,5,2,9,1,8],
                  [5, 6, np.nan,3,np.nan,2],
                  [6,np.nan,7,np.nan,4,3]])
Q12[6]=np.nan
