import streamlist as st
import pandas as pd
import numpy as np

st.title("Pineapple Garden")

# User inputs latitude and longitude
latitude = st.number_input("Enter Latitude", value=5.4141)
longitude = st.number_input("Enter Longitude", value=100.3288)

# Display the location on the map
location_data = pd.DataFrame({'lat': [latitude], 'lon': [longitude]})
st.map(location_data)
