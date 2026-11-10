
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Cancer Prediction",
    page_icon="🎗️",
    layout="wide"
)

st.title("🎗️ Cancer Prediction System")
st.write("Decision Tree Machine Learning Model")

# Load saved model
@st.cache_resource
def load_model():
    return joblib.load("cancer_decision_tree_model.pkl")

try:
    model_data = load_model()
    model = model_data['model']
    le = model_data['label_encoder']
    features = model_data['feature_names']

    st.success("Model loaded successfully!")

except Exception as e:
    st.error(f"Model loading failed: {e}")
    st.stop()

st.subheader("Upload Cancer Dataset CSV")

uploaded_file = st.file_uploader(
    "Upload CSV file containing model input features",
    type=["csv"]
)

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    # Remove unnecessary columns if present
    data = data.drop(
        columns=['id', 'Unnamed: 32', 'diagnosis'],
        errors='ignore'
    )

    missing_cols = [col for col in features if col not in data.columns]

    if missing_cols:
        st.error(f"Missing required columns: {missing_cols}")

    else:
        X = data[features]

        if X.isnull().any().any():
            st.error("Your CSV contains missing values. Please clean the data.")
        elif not all(pd.api.types.is_numeric_dtype(X[c]) for c in features):
            st.error("All model input features must be numeric.")
        else:
            predictions = model.predict(X)

            result = data.copy()
            result['Predicted Diagnosis'] = le.inverse_transform(
                predictions.astype(int)
            )

            st.subheader("Prediction Results")
            st.dataframe(result, use_container_width=True)

            counts = result['Predicted Diagnosis'].value_counts()

            st.subheader("Prediction Summary")
            st.write(counts)

            st.download_button(
                "Download Prediction Results",
                data=result.to_csv(index=False).encode('utf-8'),
                file_name="cancer_predictions.csv",
                mime="text/csv"
            )
