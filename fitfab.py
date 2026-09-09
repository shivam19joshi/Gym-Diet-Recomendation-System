import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Gym Diet Planner",
    page_icon="💪",
    layout="centered"
)

st.title("💪 Gym Diet Planner")
st.write("Enter your details to get your BMI and a personalized diet plan.")

# -----------------------------
# User Inputs
# -----------------------------
name = st.text_input("Name")

age = st.number_input(
    "Age",
    min_value=15,
    max_value=80,
    value=25
)

height = st.number_input(
    "Height (cm)",
    min_value=100.0,
    max_value=220.0,
    value=175.0
)

weight = st.number_input(
    "Weight (kg)",
    min_value=30.0,
    max_value=200.0,
    value=65.0
)

goal = st.selectbox(
    "Your Goal",
    ["Weight Gain", "Maintain Weight", "Weight Loss"]
)

activity = st.selectbox(
    "Activity Level",
    [
        "Lightly Active",
        "Moderately Active",
        "Very Active"
    ]
)

# -----------------------------
# Button
# -----------------------------
if st.button("Generate My Diet Plan", use_container_width=True):

    if name.strip() == "":
        st.warning("Please enter your name.")
        st.stop()

    # -----------------------------
    # BMI Calculation
    # -----------------------------
    height_m = height / 100

    bmi = weight / (height_m ** 2)

    if bmi < 18.5:
        bmi_category = "Underweight"
    elif bmi < 25:
        bmi_category = "Normal Weight"
    elif bmi < 30:
        bmi_category = "Overweight"
    else:
        bmi_category = "Obese"

    # -----------------------------
    # BMR Calculation
    # Mifflin-St Jeor (male example)
    # -----------------------------
    bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5

    # -----------------------------
    # Activity Multiplier
    # -----------------------------
    if activity == "Lightly Active":
        multiplier = 1.375
    elif activity == "Moderately Active":
        multiplier = 1.55
    else:
        multiplier = 1.725

    maintenance_calories = bmr * multiplier

    # -----------------------------
    # Goal Calories
    # -----------------------------
    if goal == "Weight Gain":
        target_calories = maintenance_calories + 300
    elif goal == "Weight Loss":
        target_calories = maintenance_calories - 400
    else:
        target_calories = maintenance_calories

    target_calories = int(target_calories)

    # -----------------------------
    # Display Results
    # -----------------------------
    st.success(f"Hello {name}! Your plan is ready.")

    st.subheader("📊 Your BMI")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("BMI", f"{bmi:.1f}")

    with col2:
        st.metric("Category", bmi_category)

    st.subheader("🔥 Daily Calorie Target")

    st.metric(
        "Recommended Calories",
        f"{target_calories} kcal/day"
    )

    # -----------------------------
    # Diet Plan
    # -----------------------------
    st.subheader("🍽️ Your Diet Plan")

    if goal == "Weight Gain":

        st.markdown("""
        ### 🌅 Breakfast
        - 4 eggs / paneer
        - 2-3 roti or 2 slices whole wheat bread
        - 1 banana
        - 1 glass milk

        ### 🥤 Mid-Morning Shake
        - 1 banana
        - 30g oats
        - 2 tbsp peanut butter
        - 300-350ml milk

        ### 🍛 Lunch
        - 4 roti
        - Dal
        - Vegetable
        - Paneer
        - Curd

        ### ☕ Evening Snack
        - Peanut butter sandwich
        - Fruit
        - Milk

        ### 🏋️ Pre/Post Workout
        - Banana
        - Milk
        - Eggs / paneer

        ### 🌙 Dinner
        - Rice
        - Dal
        - Paneer / vegetables
        - Curd

        ### 🥛 Before Bed
        - 1 glass milk
        """)

    elif goal == "Weight Loss":

        st.markdown("""
        ### 🌅 Breakfast
        - 2-3 eggs / paneer
        - Oats
        - 1 fruit

        ### 🍎 Mid-Morning
        - Apple / orange
        - Curd

        ### 🍛 Lunch
        - 2-3 roti
        - Dal
        - Lots of vegetables
        - Salad

        ### ☕ Evening
        - Roasted chana
        - Green tea / tea without excess sugar

        ### 🌙 Dinner
        - 2 roti
        - Dal
        - Vegetables
        - Paneer/tofu
        """)

    else:

        st.markdown("""
        ### 🌅 Breakfast
        - Eggs / paneer
        - Oats
        - 1 banana
        - Milk

        ### 🥤 Mid-Morning
        - Banana-oats shake

        ### 🍛 Lunch
        - 3-4 roti
        - Dal
        - Vegetables
        - Paneer
        - Curd

        ### ☕ Evening
        - Sandwich
        - Fruit

        ### 🌙 Dinner
        - Rice
        - Dal
        - Vegetables
        - Paneer/tofu
        """)

    st.info(
        "💡 This is a general fitness plan. Individual calorie and nutrition "
        "requirements can vary."
    )
