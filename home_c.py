from sklearn.datasets import fetch_openml
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import plotly.express as px
import streamlit as st
import numpy as np
#######st.title&label
st.title("home")
cmd=st.selectbox(label="feature_name",options=["ocean_proximity","population"])
if st.button("test"):
    st.text(cmd)
######database
database=fetch_openml(data_id= 43705)
df=pd.DataFrame(database.data,columns=database.feature_names)
####encodeing
encoder=LabelEncoder()
df["ocean_proximity_encod"]=encoder.fit_transform(df["ocean_proximity"])
#####st.plot
st.write(df)
if cmd=="ocean_proximity":
 grouped=df.groupby('ocean_proximity')['median_house_value'].mean().reset_index()
 fig=px.bar(grouped,
           x='ocean_proximity',
           y='median_house_value',
           color='ocean_proximity',
           text='median_house_value')
 st.plotly_chart(fig)

if cmd=="population":
 grouped1=df.groupby("population")['median_house_value'].mean().reset_index()
 fig = px.bar(grouped1,
              x="population",
              y='median_house_value',
              color="population",
              text='median_house_value')
 st.plotly_chart(fig)