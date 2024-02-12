import streamlit as st

st.title("Weather Forecast for the upcoming Days")
place = st.text_input("Place: ", placeholder = "Give Place Name here")
days = st.slider("Forecast Days", min_value = 1, max_value = 5,
                 help = "Select the number of forecasted days")
option = st.selectbox("Select data to veiw", ("Temperature", "Sky"),
                       placeholder = "Please Select")

st.subheader(f"{option} for the next {days} days in {place}")