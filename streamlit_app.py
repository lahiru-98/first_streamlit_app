import streamlit
import pandas

import requests
fruityvice_response = requestes.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

streamlit.title("My Parents new healthy Diner")
streamlit.header("Breakfast Menu")
streamlit.text(" 🥣 Omega 3 and BlueBerry Oat meal")
streamlit.text(" 🥗 Kale, Spinach & Rocket Smothie")
streamlit.text(" 🐔 Hard Boild Free-Ramge-Egg")
streamlit.text(" 🥑🍞 Avacado toast")

streamlit.header("🍌🥭 Build Your Own Fruit Smoothie 🥝🍇")

#Reading the csv file from a S3 bucket
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#set the index as Fruit Name
my_fruit_list = my_fruit_list.set_index('Fruit')

#Allow user to select set of fruits that they want to include
fruits_selected = streamlit.multiselect("Pick Some Fruits : ", list(my_fruit_list.index) , ['Avocado', 'Apple'])

fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show) 
