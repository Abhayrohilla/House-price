import streamlit as st
import pandas as pd
import joblib

# Load the saved model from a file
model_filename = r"C:\Users\abhay\AI model\House_predicition.pkl"  # Update with the correct path to your model file
regression_model = joblib.load(model_filename)


# Display text in the center with custom color
st.markdown(
    "<h1><div style='text-align: center;'>Unlock the Future of Real Estate: Predict House Prices with Precision</div></h1>",
    unsafe_allow_html=True
)

# Display text in the center with custom color
st.markdown(
    "<h1><div style='text-align: center;'>Bharat Intern</div></h1>",
    unsafe_allow_html=True
)

# Create a Streamlit app
st.title("House Price Prediction")

# Sidebar for user input
st.sidebar.header("User Input")
lotsize = st.sidebar.number_input("Lot Size", min_value=None, step=1)
bedrooms = st.sidebar.number_input("Number of Bedrooms", min_value=None, step=1)
bathrms = st.sidebar.number_input("Number of Bathrooms", min_value=None, step=1)
stories = st.sidebar.number_input("Number of Stories", min_value=None, step=1)
driveway = st.sidebar.radio("Driveway", ("Yes", "No"))
recroom = st.sidebar.radio("Recreation Room", ("Yes", "No"))
fullbase = st.sidebar.radio("Full Basement", ("Yes", "No"))
gashw = st.sidebar.radio("Gas Hot Water", ("Yes", "No"))
airco = st.sidebar.radio("Air Conditioning", ("Yes", "No"))
garagepl = st.sidebar.number_input("Number of Garage Places", min_value=None, step=1)
prefarea = st.sidebar.radio("Preferred Area", ("Yes", "No"))

# Convert categorical inputs to 1 or 0
categorical_inputs = {
    'driveway': 1 if driveway == "Yes" else 0,
    'recroom': 1 if recroom == "Yes" else 0,
    'fullbase': 1 if fullbase == "Yes" else 0,
    'gashw': 1 if gashw == "Yes" else 0,
    'airco': 1 if airco == "Yes" else 0,
    'prefarea': 1 if prefarea == "Yes" else 0,
}

# Create a DataFrame with the correct column order
input_data = {
    'lotsize': [lotsize],
    'bedrooms': [bedrooms],
    'bathrms': [bathrms],
    'stories': [stories],
    'driveway': [categorical_inputs['driveway']],
    'recroom': [categorical_inputs['recroom']],
    'fullbase': [categorical_inputs['fullbase']],
    'gashw': [categorical_inputs['gashw']],
    'airco': [categorical_inputs['airco']],
    'garagepl': [garagepl],
    'prefarea': [categorical_inputs['prefarea']],
}

# Manual Min-Max scaling
def min_max_scaling(value, min_value, max_value):
    return (value - min_value) / (max_value - min_value)

# Example usage
X = lotsize  # Your original value
X_min = 1650  # Minimum value of the feature
X_max = 16200  # Maximum value of the feature

scaled_value = min_max_scaling(X, X_min, X_max)


# Scale the 'lotsize' feature using MinMaxScaler
input_data['lotsize'] = float(f"{scaled_value:.6f}")

input_df = pd.DataFrame(input_data)


# Display the input data
st.subheader("User Input Data")
st.write(input_df)

# Make predictions
if st.button("Predict"):
    prediction = regression_model.predict(input_df)
    st.write("Predicted House Price:", int(prediction[0]))
