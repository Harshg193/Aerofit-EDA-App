#Import Libra
import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns 
import matplotlib.pyplot as plt

#Setting the page configuration of Stramlit Dashboard
st.set_page_config(page_title ="Aeropfit Treadmill Analysis",layout="wide")
st.title("Aerofit Treadmill Data Analysis Dashboard")

#upload
uploaded_file = st.file_uploader("Please upload your dataset", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    #Basic Data Analysis
    st.subheader("Dataset Preview")
    st.dataframe(df.head())
    
    #Shap of the dataset
    st.subheader("Shape of the Dataset")
    st.write("Number of rows and columns in the dataset are: ",df.shape)
    st.write("Column names of my dataset are: ",df.columns.tolist())
    
    #checkboxes 
    st.subheader("Data Statistics")
    data_info = st.checkbox("Show dataset information")
    missing_values = st.checkbox("Show Missing Values")
    statistics = st.checkbox("Show the Statistical Summary of the Dataset")
    data_info=st.radio("Select Option", ("Data Types", "Missing Values", "Statistics Summary"))
    
    if data_info:
        st.write("Statistics of the Dataset are: ",df.info())
        
    if missing_values:
        st.write("Missing values of the Dataset are: ",df.isna().sum(axis = 0))
        
    if statistics:
        st.write("Statisics of the Dataset are: ",df.describe())
        
   
    if data_info == "Data Types":
        st.write("Datatypes are :", df.dtypes)
        
    elif data_info == "Missing Values":
        st.write("Missing Values are :", df.isnull().sum())
        
    elif data_info == "Statistics Summary":
        st.write("Statistics summary is :", df.describe())   
        
    # Visual Analysis of our Dataset
    # Column Selector
    numeric_cols = df.select_dtypes(include = ["int64","float64"]).columns.tolist() 
    categorical_cols = df.select_dtypes(include = ["int64","float64"]).columns.tolist()
    st.write(numeric_cols)
    st.write(categorical_cols)
    
    # Un-variate Analysis
    # Count Plot
    st.subheader("Count Plot")
    selected_cols = st.selectbox("select a numeric column: ",numeric_cols)
    fig,ax = plt.subplots()
    sns.countplot( x = df[selected_cols],ax = ax)
    st.pyplot(fig)  
    
    # Count Plot for categorical Data
    st.subheader("Count Plot for categorical Data")
    cat_cols = st.selectbox("Select a categorical column ", categorical_cols)
    fig, ax = plt.subplots()
    sns.countplot(y=df[cat_cols], ax=ax)
    st.pyplot(fig)
    
    #Box Plot for numerical Coluns 
    st.subheader("Box Plots for checking the Outliers")
    box_cols = st.selectbox("select a numeric columns: ",numeric_cols)
    fig,ax = plt.subplots()
    sns.boxplot(x = df[box_cols],ax = ax)
    st.pyplot(fig)
    
    #Historical Plot for numerical Coluns 
    st.subheader("Histogram for Distribution of Numeric Columns")
    hist_cols = st.selectbox("Select a numeric column for histogram:", numeric_cols, key="hist_col")
    fig, ax = plt.subplots()
    sns.histplot(x=df[hist_cols], kde=True, ax=ax)
    st.pyplot(fig)
    
    #Bi-variate Analysis
    st.subheader("Bi-variate Analysis of our dataset: Categorical vs Numerical")
    num_cols = st.selectbox("Select a numeric column: ",numeric_cols,key = "num1")
    category_cols = st.selectbox("selecty categoricsl column: ",categorical_cols,key ="cat1" )
    fig,ax = plt.subplots()
    sns.boxplot(x=df[num_cols], y=df[category_cols], ax=ax)
    st.pyplot(fig)
    
    
    #Muti-variate Analysis 
    #Heat map our dataset to check correlation
    st.subheader("Co-relation Heatmap")
    fig,ax = plt.subplots(figsize = (10,6))
    sns.heatmap(df[numeric_cols].corr(),annot=True,cmap ="magma", ax=ax)
    st.pyplot(fig)
    
    #Pair - plot
    st.subheader("Pair plot our dataset")
    fig = sns.pairplot(df[numeric_cols])
    st.pyplot(fig)
    
else:
    st.write("Please upload the Dataset first for the exploratory dada analysis")