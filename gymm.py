import streamlit as st

# Page config
st.set_page_config(page_title="Gym Diet Planner", page_icon="💪")

st.title("💪 Gym Diet Planner & BMI Calculator")

# User Inputs
name = st.text_input("Enter your Name")
age = st.number_input("Enter your Age", min_value=10, max_value=100)
height = st.number_input("Enter your Height (in cm)", min_value=100.0, max_value=250.0)
weight = st.number_input("Enter your Weight (in kg)", min_value=30.0, max_value=200.0)

# BMI Calculation Function
def calculate_bmi(weight, height):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

# Diet Plan Function
def diet_plan(bmi):
    if bmi < 18.5:
        return "Underweight", """
        🍽️ Diet Plan:
        - High protein (eggs, chicken, paneer)
        - Healthy fats (nuts, peanut butter)
        - Milk, banana shakes
        - Eat 5-6 meals/day
        - Strength training recommended
        """
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight", """
        🍽️ Diet Plan:
        - Balanced diet (protein + carbs + fats)
        - Fruits and vegetables
        - Whole grains
        - Stay hydrated
        - Maintain regular workouts
        """
    elif 25 <= bmi < 29.9:
        return "Overweight", """
        🍽️ Diet Plan:
        - Low carbs, high protein
        - Avoid sugar & junk food
        - Green vegetables, salads
        - Cardio exercises daily
        """
    else:
        return "Obese", """
        🍽️ Diet Plan:
        - Strict calorie deficit
        - High fiber foods
        - Avoid fried & processed food
        - Intermittent fasting (optional)
        - Regular cardio + gym training
        """

# Button
if st.button("Calculate BMI & Get Diet Plan"):
    if name and height and weight:
        bmi = calculate_bmi(weight, height)
        category, plan = diet_plan(bmi)

        st.success(f"Hello {name}! 👋")
        st.subheader(f"Your BMI: {bmi}")
        st.subheader(f"Category: {category}")
        st.markdown(plan)
    else:
        st.error("Please fill all details!")

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
