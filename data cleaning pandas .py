#!/usr/bin/env python
# coding: utf-8
1.Introduction
      This assignment will help you to consolidate the concepts learnt in the session.
2.Problem Statement
      It happens all the time: someone gives you data containing malformed strings,
Python, lists and missing data. How do you tidy it up so you can get on with the
analysis?    
      Take this monstrosity as the DataFrame to use in the following puzzles:
        df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN','londON_StockhOlm','Budapest_PaRis', 'Brussels_londOn'],
        'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
        'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
        'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
        '12. Air France', '"Swiss Air"']})
# In[1]:


import pandas as pd
import numpy as np


# In[3]:


df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm', 'Budapest_PaRis',  'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )', '12. Air France', '"Swiss Air"']})


# In[4]:


df

1. Some values in the the FlightNumber column are missing. These numbers are
   meant to increase by 10 with each row so 10055 and 10075 need to be put in
   place. Fill in these missing numbers and make the column an integer column
   (instead of a float column).
# In[5]:


df['FlightNumber'].fillna(value=df['FlightNumber'][0]+10, limit=1, inplace=True)
df['FlightNumber'].fillna(value=df['FlightNumber'][2]+10, limit=1, inplace=True)


# In[6]:


df


# In[7]:


df['FlightNumber'].dtype


# In[8]:


df['FlightNumber'] = df['FlightNumber'].astype(np.int64)
df['FlightNumber'].dtype


# In[9]:


df

2. The From_To column would be better as two separate columns! Split each
   string on the underscore delimiter _ to give a new temporary DataFrame with
   the correct values. Assign the correct column names to this temporary
   DataFrame.
# In[11]:


temp_data = pd.DataFrame(df['From_To'].str.split('_', 1).to_list(), columns = ['From','To'])
temp_data

3. Notice how the capitalisation of the city names is all mixed up in this
   temporary DataFrame. Standardise the strings so that only the first letter is
   uppercase (e.g. "londON" should become "London".)
# In[15]:


temp_data['From'] = temp_data['From'].str.capitalize()
temp_data['To'] = temp_data['To'].str.capitalize()


# In[16]:


temp_data

4. Delete the From_To column from df and attach the temporary DataFrame
   from the previous questions.
# In[17]:


df.drop(['From_To'], inplace=True, axis=1)
df


# In[18]:


df = pd.concat([temp_data, df], axis=1, sort=False)
df

5. In the RecentDelays column, the values have been entered into the
   DataFrame as a list. We would like each first value in its own column, each
   second value in its own column, and so on. If there isn't an Nth value, the value
   should be NaN.
   
   Expand the Series of lists into a DataFrame named delays, rename the columns
   delay_1, delay_2, etc. and replace the unwanted RecentDelays column in df
   with delays.
# In[19]:


delays = pd.DataFrame(df['RecentDelays'].to_list(), columns = ['delay_1', 'delay_2', 'delay_3'])
delays


# In[20]:


df.drop(['RecentDelays'], inplace=True, axis=1)
df


# In[21]:


df.insert(loc = 3, column='delay_1' , value=delays['delay_1'])
df.insert(loc = 4, column='delay_2' , value=delays['delay_2'])
df.insert(loc = 5, column='delay_3' , value=delays['delay_3'])
df

