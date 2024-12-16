import streamlit as st

def main():
    st.title("Percentage to Inches calc ")

    st.write("### Enter Your Input")
    length = st.number_input("Enter the Length", min_value=0.0, step=0.1)
    percentage = st.number_input("Enter the Percentage (e.g., 2 for 2%)", min_value=0.0, step=0.01)

    if length > 0 and percentage > 0:
        result = length * (percentage / 100) / 0.08

        st.write("### Result")
        st.write(f"For {percentage}% and length {length}, the total in inches is: **{result:.4f} inches**")

if __name__ == "__main__":
    main()
# Add the footer
add_created_by(
    email_address="nicholas.nabholz@bexar.org",
    app_name="Percent to Inches",
    author_name="NN"
)
