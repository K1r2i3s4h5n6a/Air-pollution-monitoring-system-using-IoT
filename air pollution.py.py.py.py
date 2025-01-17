# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cL7V1VQ6SGH9WAPa9sqKo3-kfoyw4JWE
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
import datetime
import matplotlib.dates as md

filepath = "pollution.csv"
searchpath = "/pollution.csv"

df=pd.read_csv('/pollution.csv')
df.head()

#finding out the time when max. pollution occurs at Chadni Chowk
df[df['Chadni Chowk']==3.0235897439999997].drop(['Gariahat','Dharmatala'],axis=1)

#finding out the time when max. pollution occurs at Gariahat
df[df['Gariahat']==3.0235897439999997].drop(['Chadni Chowk','Dharmatala'],axis=1)

#finding out the time when max. pollution occurs at Dharmatala
df[df['Dharmatala']==3.0235897439999997].drop(['Chadni Chowk','Gariahat'],axis=1)

#finding out pollution level at Chadni Chowk by hourly update
plt.figure(figsize=(12,8))
plt.rcParams.update({'font.size':15})
x =pd.to_datetime(df['created_at'])
y=df['Chadni Chowk']
plt.plot_date(x, y)
plt.xlabel("Data & Hour")
plt.ylabel("Pollution Level")
plt.title("Hourly Pollution Level at Chadni Chowk")

#finding out pollution level at Gariahat by hourly update
plt.figure(figsize=(12,8))
plt.rcParams.update({'font.size':15})
x =pd.to_datetime(df['created_at'])
y=df['Gariahat']
plt.plot_date(x, y,color='green')
plt.xlabel("Data & Hour")
plt.ylabel("Pollution Level")
plt.title("Hourly Pollution Level at Gariahat")

#finding out pollution level at Dharmatala by hourly update
plt.figure(figsize=(12,8))
plt.rcParams.update({'font.size':15})
x =pd.to_datetime(df['created_at'])
y=df['Dharmatala']
plt.plot_date(x, y,color='red')
plt.xlabel("Data & Hour")
plt.ylabel("Pollution Level")
plt.title("Hourly Pollution Level at Dharmatala")

#pairplotting
sns.set(font_scale=1.5)
g=sns.pairplot(df,hue="Chadni Chowk")
g.fig.set_size_inches(15,15)

sns.jointplot(x="Chadni Chowk",y="Gariahat",data=df,color='green')

sns.jointplot(x="Chadni Chowk",y="Dharmatala",data=df,color='red')

sns.jointplot(x="Dharmatala",y="Gariahat",data=df,color='k')