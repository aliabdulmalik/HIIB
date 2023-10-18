import streamlit as st
import matplotlib.pyplot as plt

# Title and Description
st.title("Visualizing Inaccuracies due to biased training Data")
st.header(" Accuracy Pie Chart")
sizes = [100, 0]
explode = (0, 0) 

# d1 &  -> s0 = 100, d1&d2 = 0 -> d2 == 100s0 = 65
divider = st.slider(label="Skin Color",min_value=0.0,max_value=100.0)  / 6.25
divider2 = st.slider(label="Gender",min_value=0.0,max_value=100.0)    /  6.25

sizes[0] = sizes[0] - divider -divider2
sizes[1] = sizes[1] + divider + divider2

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode,  autopct='%1.1f%%',labels=["Accuracy", "Inaccuracy"],
        shadow=False, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig1)
st.header(f" Accuracy: {sizes[0]:.2f}%")

