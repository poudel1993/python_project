#!/usr/bin/env python
# coding: utf-8

# In[39]:


import numpy as np
np.random.seed(12)
arrays=[[1,1,2,2,3,3],['a','b','a','b','a','b']]
fg=pd.MultiIndex.from_arrays(arrays)
# df = pd.DataFrame([[1,'a'],[1,'b'],[2,'a'],[2,'b'],[3,'a'],[3,'b']],columns=['A','B'])
V=np.random.randint(0,9,size=(6,2))
gg=pd.DataFrame(data=V,columns=['A','B'],index=fg)
gg

# arrays = [np.array(["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"]),np.array(["one", "two", "one", "two", "one", "two", "one", "two"]),]
# df = pd.DataFrame(np.random.randn(8, 4), index=arrays,column) 
# df


# In[ ]:


arrays=[["ONE","ONE","TWO","TWO","THREE","THREE"],["one","two","one","two","one","two"]]


# In[ ]:




