import streamlit as st
import time
import datetime
from datetime import datetime, date, time
import requests

form = st.sidebar.form("my_form")

form.markdown('''# Taxi Fare NYC prediction
Hey let's give me some data to perform a prediction :kappa:
''')
date_input = form.date_input('Date')
time_input = form.time_input('Time')

pick_up_lon = form.number_input('pickup longitude', min_value=0)
pick_up_lat = form.number_input('pickup latitude',min_value=0)
drop_off_lon = form.number_input('dropoff longitude',min_value=0)
drop_off_lat = form.number_input('dropoff latitude', min_value=0)

passengers = form.number_input('Passengers', min_value=1)
# ###Now add a submit button to the form:
form.form_submit_button("Submit")
pick_up = str(date_input) +' ' +str(time_input)

dict_params = {
    'pickup_datetime': pick_up,
    'pickup_longitude': pick_up_lon,
    'pickup_latitude': pick_up_lat,
    'dropoff_longitude': drop_off_lon,
    'dropoff_latitude': drop_off_lat,
    'passenger_count': passengers
}

r = requests.get('https://taxifare.lewagon.ai/predict', params = dict_params)
st.sidebar.write('My fare will be around', r.json()['prediction'],'$')


st.components.v1.html("""
<html>
<head>
<meta charset="utf-8">
<title>Display a map on a webpage</title>
<meta name="viewport" content="initial-scale=1,maximum-scale=1,user-scalable=no">
<link href="https://api.mapbox.com/mapbox-gl-js/v2.4.1/mapbox-gl.css" rel="stylesheet">
<script src="https://api.mapbox.com/mapbox-gl-js/v2.4.1/mapbox-gl.js"></script>
<style>
body { margin: 0; padding: 0; }
#map { position: absolute; top: 0; bottom: 0; width: 100%; }
</style>
</head>
<body>
<div id="map"></div>
<script>
	mapboxgl.accessToken = 'pk.eyJ1IjoiYW9zeHh4IiwiYSI6ImNrc3VmZjdrdTAydDAycHMzcWw0ZWQ4Z3cifQ.lt_PAlq_hnf4ToB70mX5VQ';
const map = new mapboxgl.Map({
container: 'map', // container ID
style: 'mapbox://styles/mapbox/streets-v11', // style URL
center: [-73.968565, 40.779897], // starting position [lng, lat]
zoom: 9 // starting zoom
});
</script>

</body>
</html>""",
                      height=800,
                      width=1000)
