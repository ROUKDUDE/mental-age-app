import streamlit as st

st.set_page_config(page_title="Mental Age Guesser", page_icon="🧠", layout="centered")

st.title("🎉 Mental Age Guesser 🎉")
st.write("Answer these 5 fun questions to discover your mental age!")

score = 0

# Question 1
q1 = st.radio("1. What's your favorite weekend activity?", 
              ['Reading books', 'Partying all night', 'Playing video games'])
if q1 == 'Reading books':
    score += 30
elif q1 == 'Partying all night':
    score += 20
else:
    score += 10

# Question 2
q2 = st.radio("2. Pick a dessert:", 
              ['Ice cream', 'Fruit salad', 'Chocolate cake'])
if q2 == 'Ice cream':
    score += 10
elif q2 == 'Fruit salad':
    score += 30
else:
    score += 20

# Question 3
q3 = st.radio("3. Which pet would you choose?", 
              ['Cat', 'Dog', 'Fish'])
if q3 == 'Cat':
    score += 20
elif q3 == 'Dog':
    score += 10
else:
    score += 30

# Question 4
q4 = st.radio("4. Choose a holiday destination:", 
              ['Beaches', 'Mountains', 'Historical cities'])
if q4 == 'Beaches':
    score += 10
elif q4 == 'Mountains':
    score += 20
else:
    score += 30

# Question 5
q5 = st.radio("5. How do you prefer to spend an evening?", 
              ['Watching movies', 'Sleeping early', 'Hanging out with friends'])
if q5 == 'Watching movies':
    score += 20
elif q5 == 'Sleeping early':
    score += 30
else:
    score += 10

# Button to show result
if st.button("Guess My Mental Age"):
    if score <= 60:
        mental_age = 16
    elif 61 <= score <= 90:
        mental_age = 25
    elif 91 <= score <= 120:
        mental_age = 40
    else:
        mental_age = 60

    st.success(f"🧠 Your estimated mental age is: {mental_age} years!")
    st.markdown("**✨ CREATED BY HADHI ✨**")
