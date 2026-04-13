import streamlit as st

# Title
st.set_page_config(page_title="Gym Member Dashboard", page_icon="💪")
st.title("💪 Gym Member Health Tracker")

# User Inputs
st.header("Enter Your Details")

name = st.text_input("Name")
age = st.number_input("Age", min_value=10, max_value=100, step=1)
height = st.number_input("Height (in cm)", min_value=100.0, max_value=250.0)
weight = st.number_input("Weight (in kg)", min_value=30.0, max_value=200.0)

# Calculate BMI
if st.button("Calculate BMI"):

    if name == "":
        st.warning("Please enter your name")
    else:
        height_m = height / 100
        bmi = weight / (height_m ** 2)

        st.subheader(f"Hello {name} 👋")
        st.write(f"Your BMI is: **{bmi:.2f}**")

        # BMI Category + Diet Plan
        if bmi < 18.5:
            st.error("Category: Underweight")
            st.write("🍽️ Diet Plan:")
            st.write("""
            - Increase calorie intake
            - Eat protein-rich foods (eggs, chicken, paneer)
            - Include nuts and dry fruits
            - Drink milk & shakes
            - Eat 5-6 meals a day
            """)

        elif 18.5 <= bmi < 24.9:
            st.success("Category: Normal Weight")
            st.write("🍽️ Diet Plan:")
            st.write("""
            - Maintain balanced diet
            - Include fruits & vegetables
            - Protein intake (dal, eggs, chicken)
            - Stay hydrated
            - Avoid junk food
            """)

        elif 25 <= bmi < 29.9:
            st.warning("Category: Overweight")
            st.write("🍽️ Diet Plan:")
            st.write("""
            - Reduce sugar & carbs
            - Increase protein intake
            - Eat salads & fiber-rich foods
            - Avoid fried foods
            - Drink more water
            """)

        else:
            st.error("Category: Obese")
            st.write("🍽️ Diet Plan:")
            st.write("""
            - Strict low-calorie diet
            - High protein, low carbs
            - Avoid sugar completely
            - Eat more vegetables
            - Consider consulting a nutritionist
            """)

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
