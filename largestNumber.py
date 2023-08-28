import streamlit as st

def find_largest(*args):
    """Finds the largest number in a list of numbers."""
    return max(args)

def main():
    """Finds the largest number entered by the user."""
    st.title("Find the Largest Number")

    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")
    num3 = st.number_input("Enter the third number:")

    largest = find_largest(num1, num2, num3)
    st.write(f"The largest number is: {largest}")

if __name__ == "__main__":
    main()
