# app.py
import streamlit as st

def find_largest(num1, num2, num3):
    return max(num1, num2, num3)

def main():
    st.title("Find the Largest Number App")

    # User input for three numbers
    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")
    num3 = st.number_input("Enter the third number:")

    # Perform the check when the user clicks the button
    if st.button("Find Largest"):
        largest_number = find_largest(num1, num2, num3)
        st.success(f"The largest number among {num1}, {num2}, and {num3} is {largest_number}")

if __name__ == "__main__":
    main()
