
import numpy as np
import pickle
import pandas as pd
import streamlit as st 

from PIL import Image

pickle_in = open("carPrice.pkl","rb")
classifier=pickle.load(pickle_in)

st.set_page_config(layout="wide")

def predict_price(Year,Present_Price,Kms_Driven,Fuel_Type,Seller_Type,Transmission):
   
    prediction=classifier.predict([[Year,Present_Price,Kms_Driven,Fuel_Type,Seller_Type,Transmission]])
    print(prediction)
    return prediction



def main():
    html_temp = """
    <div style="background-color:brown;padding:10px">
    <h2 style="color:white;text-align:center;">Vehicle price Prediction </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    st.subheader("Please Enter the details below to get an estimated value of your vehicle")
    
    Year=st.slider("Year of purchase",2000,2020)
    Kms_Driven=st.slider("Kms Driven",500,500000)
    Fuel_Type=st.selectbox("Type of fuel",["Petrol","Diesel","CNG"])
    if(Fuel_Type=="Petrol"):
        Fuel_Type=2
    if(Fuel_Type=="Diesel"):
        Fuel_Type=1
    else:
        Fuel_Type=0
    Seller_Type=st.selectbox("Seller type",["Individual","Dealer"])
    if(Seller_Type=="Individual"):
        Seller_Type=1
    else:
        Seller_Type=0
    Transmission=st.selectbox("Transmission type",["Manual","Automatic"])
    if(Transmission=="Manual"):
        Transmission=1
    else:
        Transmission=0
    Present_Price=st.text_input("Buying price (Lakhs)")
    
    result=""
    if st.button("Predict"):
        result=predict_price(Year,Present_Price,Kms_Driven,Fuel_Type,Seller_Type,Transmission)
        result=str(result)[1:-1]+ " Lakhs"
        st.header(result)
    
    
    if st.button("About"):
        st.text("This web application is created to help user get an estimated selling value of their vehicle by analyzing different features.")

if __name__=='__main__':
    main()
    
    
    