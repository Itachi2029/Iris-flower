import streamlit as st
import pickle
import numpy
def open_model():
    with open('model_pickup','rb') as f:
          model=pickle.load(f)
    return model 
mo=open_model()


def show_predict():
    st.title('FLOWER PREDICTION CATEGORIES')
    st.write('We required some from you Sir!')
    sepal_lenth = int(st.number_input('sepal_length'))
    sepal_width = int(st.number_input('sepal_width'))
    petal_length =int(st.number_input('petal_length'))
    petal_width = int(st.number_input('pertal_width'))
    print(sepal_lenth,sepal_width)
    ok=st.button("Classify flower")
    if ok:
      x=numpy.array([[sepal_lenth,sepal_width,petal_length,petal_width]])
      t=mo.predict(x)
      print(t[0])
      
      st.subheader(f"the type of flower type is {t[0]}")
