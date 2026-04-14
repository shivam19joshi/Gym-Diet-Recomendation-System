import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import folium
from streamlit_folium import st_folium

# Page config
st.set_page_config(page_title="AI Gym Diet Planner", page_icon="💪", layout="wide")

st.title("💪 AI Gym Diet Planner + Fitness Dashboard")

# Sidebar Inputs
st.sidebar.header("👤 User Details")

name = st.sidebar.text_input("Name")
age = st.sidebar.number_input("Age", 10, 100)
height = st.sidebar.number_input("Height (cm)", 100.0, 250.0)
weight = st.sidebar.number_input("Weight (kg)", 30.0, 200.0)

# BMI Calculation
def calculate_bmi(weight, height):
    height_m = height / 100
    return round(weight / (height_m ** 2), 2)

# Diet Plan Logic
def diet_plan(bmi):
    if bmi < 18.5:
        return "Underweight", ["High protein", "Nuts & shakes", "5-6 meals/day"]
    elif 18.5 <= bmi < 24.9:
        return "Normal", ["Balanced diet", "Fruits & veggies", "Stay hydrated"]
    elif 25 <= bmi < 29.9:
        return "Overweight", ["Low carbs", "High protein", "Daily cardio"]
    else:
        return "Obese", ["Calorie deficit", "Avoid junk", "Strict workout"]

# Main Button
if st.sidebar.button("Analyze"):
    if name and height and weight:
        bmi = calculate_bmi(weight, height)
        category, plan = diet_plan(bmi)

        # Layout
        col1, col2 = st.columns(2)

        # LEFT SIDE → USER RESULT
        with col1:
            st.subheader(f"👋 Hello {name}")
            st.metric("Your BMI", bmi)
            st.metric("Category", category)

            st.write("### 🥗 Recommended Diet Plan")
            for p in plan:
                st.write(f"✅ {p}")

        # RIGHT SIDE → BMI GRAPH
        with col2:
            st.subheader("📊 BMI Visualization")

            bmi_range = np.linspace(10, 40, 100)
            categories = []

            for x in bmi_range:
                if x < 18.5:
                    categories.append("Underweight")
                elif x < 24.9:
                    categories.append("Normal")
                elif x < 29.9:
                    categories.append("Overweight")
                else:
                    categories.append("Obese")

            df = pd.DataFrame({
                "BMI": bmi_range,
                "Category": categories
            })

            fig = px.line(df, x="BMI", y=[1]*len(df), color="Category",
                          title="BMI Category Range")

            fig.add_vline(x=bmi, line_dash="dash", line_color="red")

            st.plotly_chart(fig, use_container_width=True)

        st.markdown("---")

        # 📍 MAP SECTION
        st.subheader("📍 Nearby Gyms (Demo Map)")

        # Default location (Nagpur)
        lat, lon = 21.1458, 79.0882

        gym_map = folium.Map(location=[lat, lon], zoom_start=13)

        # Sample gym markers
        gyms = [
            ("Gym A", 21.150, 79.090),
            ("Gym B", 21.140, 79.085),
            ("Gym C", 21.155, 79.095)
        ]

        for gym in gyms:
            folium.Marker(
                location=[gym[1], gym[2]],
                popup=gym[0],
                icon=folium.Icon(color="blue", icon="info-sign")
            ).add_to(gym_map)

        # User marker
        folium.Marker(
            [lat, lon],
            popup="You are here",
            icon=folium.Icon(color="red")
        ).add_to(gym_map)

        st_folium(gym_map, width=700, height=400)

    else:
        st.error("Please fill all details")

# Footer
st.markdown("---")
st.caption("🔥 Built for Fitness Entrepreneurs using Streamlit")
