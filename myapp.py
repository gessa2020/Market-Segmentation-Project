
from sklearn import preprocessing 
import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

filename = 'final_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
df = pd.read_csv("Clustered_Customer_Data.csv")
st.set_option('deprecation.showPyplotGlobalUse', False)

st.markdown('<style>body{background-color: Blue;}</style>',unsafe_allow_html=True)
st.title("Bank customer Segmentation")

with st.form("my_form"):
    age=st.number_input(label='Age',step=1)
    
    income=st.number_input(label='Income',step=1)
    
    debtIncomeRatio=st.number_input(label='DebtIncomeRatio',step=0.01,format="%.2f")
    
    education=st.number_input(label='Education',step=1)
    
    years_employed=st.number_input(label='Years Employed',step=1)
    
    data=[[age,income,debtIncomeRatio,education,years_employed]]

    submitted = st.form_submit_button("Submit")

    if submitted:
        clust=loaded_model.predict(data)[0]
        print('Data Belongs to Cluster',clust)

        cluster_df1=df[df['Cluster']==clust]
        cluster_df1.drop(['Unnamed: 0','Cluster'], axis=1, inplace=True)  # drop the unnamed column
        cluster_stats = cluster_df1.describe()

        st.write("Cluster value:", clust)
        st.write("Statistical Information of the Cluster:")
        st.write(cluster_stats.style.set_properties(**{'font-size': '16px'}))  # increase font size
        
        st.experimental_set_query_params()  # reset the form
        


