import streamlit as st
from PIL import Image
import time

#side bar specification
if "s1" not in st.session_state:
   st.session_state["s1"]=0
   
if "s2" not in st.session_state:
   st.session_state["s2"]=0
st.sidebar.title("SELECT A PAGE")
options=st.sidebar.radio("",["Login","Upload","Result"],key="radio_option")
def update():
        st.session_state["s1"]=1
        st.session_state.radio_option="Upload"
        

#Login page details
if options=="Login":
    
    image3=Image.open(r"D:\Satellite image detection\Pages\kct.png")
    st.title("Satellite image change detection")
    st.image(image3,width=700)
    u=st.text_input("Username")
    p=st.text_input("Password",type="password")
    
    c=st.button("Submit")
    if c:
        if u=="@123" and p=="@123":
            st.success("Logged in successfully")
            st.button("Next",on_click=update)
            
            
        else:
            st.error("Username or Password incorrect")
def next1():
    st.session_state["s2"]=1
    st.session_state["radio_option"]="Result"         
#Upload page decription          
if options=="Upload":
    if st.session_state["s1"]==1:
        st.title("Please load the two image of the same location")
        image1=st.file_uploader(label="enter image 1",type=['jpg','png'])
        image2 =st.file_uploader(label="enter image 2",type=['jpg','png'])
        a=st.button("Upload image")
        if a:
            if image1 and image2:
                st.button("View Result",on_click=next1)
            else:
                st.error("Please upload the image")
    else:
        st.error("Please Login ")
    

#result
if options=="Result":
    if st.session_state["s1"]==1:
        if st.session_state["s2"]==1:
            st.title("The Detected Change")  
            image1=Image.open(r"D:\New folder (2)\image\result.png")
            st.image(image1,width=950)
        else:
            st.error("Please upload the images")
        
    else:
        st.error("Please Login")