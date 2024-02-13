import streamlit as st
import plotly.express as px
from backend import get_data


# Adding title, texxt input, slider, selectbox and subheader
st.title("Weather Forecast for the upcoming Days")
place = st.text_input("Place: ", placeholder = "Give Place Name here")
days = st.slider("Forecast Days", min_value = 1, max_value = 5,
                 help = "Select the number of forecasted days")
option = st.selectbox("Select data to veiw", ("Temperature", "Sky"),
                       placeholder = "Please Select")

st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        # Getting the Temperature and Sky data
        filtered_data= get_data(place, days)

        if option == "Temperature":
            # Creating a temperature plot
            temperature = [(dict["main"]["temp"] / 10) for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x = dates, y = temperature, labels = {"x": "Date", "y": "Temperature (c)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width = 115)
    except KeyError:
        st.write("This place doesn't exist")