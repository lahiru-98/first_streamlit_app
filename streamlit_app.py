import streamlit
import pandas
import snowflake.connector



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

streamlit.header("FruityVice Fruit Advice")
fruit_choice = streamlit.text_input('What fruit would you like information about?' , 'kiwi')
streamlit.write('The user Entered' , fruit_choice)


import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"kiwi")
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("Hello from Snowflake:")
streamlit.dataframe(my_data_rows)

add_my_fruit = streamlit.text_input('what fruit do you like to add?')
streamlit.write('Thanks for adding ' , add_my_fruit)
