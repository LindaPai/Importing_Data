#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


file = "MMH Data Breakdown.csv"


# In[3]:


data = pd.read_csv(file, sep= ",",nrows = 50, header =[1], na_values ="Nothing")  # Header = [0] will be "MMH Data Breakdown" title
data


# In[4]:


data.columns


# In[5]:


df = data[["ID", "Gender","Age", 'Weight (lb.)','Height (in.)']]
df


# In[6]:


bmi = (data["Weight (lb.)"].values / data["Height (in.)"].values / data["Height (in.)"].values) * 703


# In[7]:


bmi = pd.DataFrame(bmi).rename(columns = {0 :"BMI"})


# In[8]:


bmi.head()


# In[9]:


df_concat = pd.concat([df,bmi], axis=1)

print(df_concat)


# In[11]:


color = []
for x in df_concat["BMI"]:
    if x > 30:
        col=["red"]
    else:
        col=["blue"]
    color.append(col)


# In[12]:


bmi_col = pd.DataFrame(color).rename(columns = {0 :"Colors"})


# In[17]:


df_all = pd.concat([df,bmi,bmi_col], axis=1)
df_all.head()


# In[14]:


plt.plot(df_concat["Gender"],df_concat["BMI"])


# In[18]:


plt.scatter(x =df_concat["BMI"] ,y = df_concat["Age"], s = np.array(bmi)*5, c = df_all["Colors"], alpha = 0.8)
#plt.xscale('log')
plt.xlabel("BMI")
plt.ylabel("Age")
plt.title("MMH Patients BMI Analysis")
plt.grid(True)


# In[19]:


plt.hist(df_concat["BMI"], bins = 10)
plt.grid(True)


# In[ ]:





# In[ ]:




