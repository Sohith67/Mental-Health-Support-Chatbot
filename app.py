import streamlit as st
import google.generativeai as genai
from textblob import TextBlob
from dotenv import load_dotenv
import os

# === Load API Key ===
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ GEMINI_API_KEY not found. Please check your .env file.")
    st.stop()

# === Configure Gemini API ===
genai.configure(api_key=api_key)

# === Initialize Model and Chat Session ===
try:
    model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
    chat_session = model.start_chat(history=[])
except Exception as e:
    st.error(f"❌ Failed to start Gemini model: {e}")
    st.stop()


# === Streamlit Page Settings ===
st.set_page_config(page_title="🧠 Mental Health Chatbot", layout="centered")
st.title("🧠 Mental Health Support Chatbot")

st.markdown("""
<div style='margin-bottom: 15px; font-size: 16px;'>
This chatbot is designed to provide emotional support using AI.<br>
If you're in a crisis, please contact a professional or emergency services.
</div>
""", unsafe_allow_html=True)

# === Initialize Chat History in Session ===
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# === Input Section ===
with st.form("chat_form"):
    user_input = st.text_input("You:", placeholder="How are you feeling today?", key="user_input")
    submit = st.form_submit_button("Send")

# === On Message Submit ===
if submit and user_input:
    st.session_state.chat_history.append(("You", user_input))

    # Analyze sentiment
    blob = TextBlob(user_input)
    polarity = blob.sentiment.polarity
    sentiment = "😊 Positive" if polarity > 0.1 else "😐 Neutral" if -0.1 <= polarity <= 0.1 else "😞 Negative"

    # Generate AI response
    try:
        gemini_reply = chat_session.send_message(user_input)
        full_response = gemini_reply.text.strip() + f"\n\n(Sentiment: {sentiment}, Polarity: {polarity:.2f})"
    except Exception as e:
        full_response = f"❌ Error generating response: {e}"

    st.session_state.chat_history.append(("Bot", full_response))

# === Chat Display ===
for sender, msg in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {msg}")

# === Sidebar Resources ===
with st.sidebar:
    st.header("📘 Mental Health Resources")
    st.markdown("""
- 📞 **National Suicide Prevention Lifeline:** 1-800-273-8255  
- 💬 **Crisis Text Line:** Text **'HELLO'** to **741741**  
- 🌐 [More Resources](https://www.mentalhealth.gov/get-help/immediate-help)
""")
    st.markdown("""<hr style="margin: 10px 0;">""", unsafe_allow_html=True)
    st.caption("This chatbot is for informational and emotional support only. It is not a substitute for professional help.")
