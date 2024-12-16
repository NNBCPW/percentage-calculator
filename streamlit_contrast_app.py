import streamlit as st

def main():
    st.title("Percentage Inches Calculator")

    st.write("### Enter Your Input")
    length = st.number_input("Enter the Length", min_value=0.0, step=0.1)
    percentage = st.number_input("Enter the Percentage (e.g., 2 for 2%)", min_value=0.0, step=0.01)

    if length > 0 and percentage > 0:
        result = length * (percentage / 100) / 0.08

        st.write("### Result")
        st.write(f"For {percentage}% and length {length}, the total in inches is: **{result:.4f} inches**")

    st.write("---")
    st.write("Created by: NN")
    st.markdown(
        "For support, please [email me](mailto:nicholas.nabholz@bexar.org?subject=Support%20for%20Percentage%20to%20Length%20and%20Inches%20Calculator)."
    )

if __name__ == "__main__":
    main()
