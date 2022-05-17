import streamlit

streamlit.title("My Parents new healthy Diner")
streamlit.header("Breakfast Menu")
streamlit.text(" 🥣 Omega 3 and BlueBerry Oat meal")
streamlit.text(" 🥗 Kale, Spinach & Rocket Smothie")
streamlit.text(" 🐔 Hard Boild Free-Ramge-Egg")
streamlit.text(" 🥑🍞 Avacado toast")

streamlit.header("🍌🥭 Build Your Own Fruit Smoothie 🥝🍇")

#Reading the csv file from a S3 bucket
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list) 
