import streamlit as st
from dotenv import load_dotenv
import os
from google import genai

# Load environment variables
load_dotenv()

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

# Check API key
if not api_key:
    st.error("GEMINI_API_KEY not found. Please check your .env file.")
    st.stop()

# Create Gemini client
client = genai.Client(api_key=api_key)

# Page configuration
st.set_page_config(
    page_title="Gemini AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}

.block-container {
    max-width: 800px;
    padding-top: 3rem;
    padding-bottom: 3rem;
}

h1 {
    text-align: center;
    color: #8b5cf6;
    font-size: 45px !important;
    font-weight: 700;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    color: #cbd5e1;
    font-size: 18px;
    margin-bottom: 30px;
}

textarea {
    background-color: #1e293b !important;
    color: white !important;
    border: 2px solid #475569 !important;
    border-radius: 12px !important;
    font-size: 16px !important;
}

textarea:focus {
    border-color: #8b5cf6 !important;
    box-shadow: 0 0 10px rgba(139, 92, 246, 0.4) !important;
}

.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #7c3aed, #8b5cf6);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 12px;
    font-size: 17px;
    font-weight: 600;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #6d28d9, #7c3aed);
}

.response-box {
    background-color: #1e293b;
    border-left: 5px solid #8b5cf6;
    border-radius: 10px;
    padding: 20px;
    margin-top: 20px;
    color: #f8fafc;
    line-height: 1.7;
}

.footer {
    text-align: center;
    color: #64748b;
    margin-top: 40px;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)

# UI
st.title("🤖 Gemini AI Chatbot")

st.markdown(
    '<div class="subtitle">Ask Gemini anything!</div>',
    unsafe_allow_html=True
)

# User prompt
prompt = st.text_area(
    "Enter your prompt:",
    placeholder="Explain Artificial Intelligence in simple words..."
)

# Generate response
if st.button("✨ Generate Response"):

    if prompt.strip():

        try:
            with st.spinner("Gemini is thinking..."):

                response = client.models.generate_content(
                    model="gemini-3.5-flash-lite",
                    contents=prompt
                )

            st.success("Response generated!")

            st.markdown(
                f"""
                <div class="response-box">
                    {response.text}
                </div>
                """,
                unsafe_allow_html=True
            )

        except Exception as e:
            st.error(f"Error: {e}")

    else:
        st.warning("Please enter a prompt.")

# Footer
st.markdown(
    '<div class="footer">Powered by Google Gemini ✨</div>',
    unsafe_allow_html=True
)