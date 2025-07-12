import streamlit as st
import pandas as pd



st.title("Streamlit Elements Demo")
st.subheader("Dataframe")

#datframe section
df = pd.DataFrame({
    'Name' : ['Arnab','Bob','Sayan','David'],
    'Age': [25,35,45,15],
    'occupation': ['Engineer','Doctor','Teacher','Lawyer']
})

st.dataframe(df)

#data editor section
st.subheader("data editor")
editable_df = st.data_editor(df)
print(editable_df)

#Static Table Section
st.subheader("static tables")
st.table(df)

#Metrics section
st.subheader("Metrics")
st.metric(label="Total Rows", value=len(df))
st.metric(label="Average Age", value=round(df['Age'].mean(),1))