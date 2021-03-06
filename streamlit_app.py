import streamlit
import pandas
import snowflake.connector
import requests
from urllib.error import URLError


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

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"kiwi")
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized 

streamlit.header("FruityVice Fruit Advice")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?' , 'kiwi')
  if not fruit_choice:
    streamlit.error("Please Select a Fruit to get the information")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
    
except URLError as e:
  streamlit.error()
  
def get_fruit_load_list():
	with my_cnx.cursor() as my_cur:
		my_cur_execute("select * from fruit_load_list")
		return my_cur.fetchall()
def insert_row_snowflake(new_fruit):
	with my_cnx.cursor() as my_cur:
		my_cur.execute("insert into fruit_load_list values('from streamlit')")
		return "Thanks For Adding " + new_fruit

if streamlit.button('Get Fruit Load List'):
	my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
	my_data_rows = get_fruit_load_list()
	streamlit.dataframe(my_data_rows)

add_my_fruit = streamlit.text_input('what fruit do you like to add?')
if streamlit.button('Add a Fruit to The List'):
	my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
	back_from_function = insert_row_snowflake(fruit_choice)
	streamlit.text(back_from_function)
