import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


# Title and Description
st.title("Visualizing Inaccuracies due to biased training Data")
st.header(" Accuracy Pie Chart")
sizes = [100, 0]
explode = (0, 0) 


class_matrix_f = np.array(([92.3, 90.1, 92.5, 91.8, 92.1, 95.1, 90.6,], # Amazon
                           [82.2, 76.6, 82.4, 85.2, 84.3, 86.3, 83.9],  # Microsoft
                           [88.8, 80.5, 87.6, 88.4, 86.5, 77.0, 82.2]   # Face ++
                           ))

class_matrix_m = np.array(([96.6, 95.5, 94.9, 91.4, 98.7, 97.9, 98.3,], # Amazon
                           [77.7, 71.7, 77.5, 79.4, 84.8, 79.0, 77.2 ],  # Microsoft
                           [95.9, 94.4, 90.4, 89.7, 98.1, 96.8, 97.8 ],   # Face ++
                           ))

gender = ["Female","Male" ]
groups = ["White", "Black", "East Asian", "SE Asian", "Latino", "Indian", "Mid Eastern"]
software = ["Amazon","Microsoft", "Face++"]

sel_gender = st.select_slider(options=gender,value="Female",label="Gender")
sel_group = st.select_slider(options=groups, label="Group",value="Mid Eastern")
sel_software = st.radio(options=software, label="Software",horizontal=True)


if sel_gender == "Female":
    class_matrix = class_matrix_f
else:
    class_matrix = class_matrix_m
sizes[0] = class_matrix[software.index(sel_software),groups.index(sel_group)]
sizes[1] = 100 -sizes[0]

fig1, ax1 = plt.subplots()
pie = ax1.pie(sizes, explode=explode,  autopct='%1.1f%%',labels=["Accuracy", "Inaccuracy"],
        shadow=False, startangle=90)
pie[0][1].set_alpha(0)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig1)
st.header(f" Accuracy: {sizes[0]:.2f}%")

