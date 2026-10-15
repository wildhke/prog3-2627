import streamlit as st
import folium
import pandas as pd

st.title("Wetter app")
st.write("Live-Demo: Python-Grundlagen")

STATIONS = {"Kempten": {"longitude": 47.73, "latitude": 10.31, "elevation": 674},
            "Memmingen": {"longitude": 47.99, "latitude": 10.18, "elevation": 600}, 
            "Oberstdorf": {"longitude": 47.41, "latitude": 10.28, "elevation": 806}
}

stations = st.multiselect("Stations", list(STATIONS), ["Kempten"])

days = st.slider("Zeitraum in Tagen", min_value=1, max_value=60, value=30)

st.subheader("Temperaturverlauf")

st.subheader("Map")
map_data = pd.DataFrame([{"name": name,
                          "lon": STATIONS[name]["latitude"],
                          "lat": STATIONS[name]["longitude"]} for name in stations
])
st.map(map_data)