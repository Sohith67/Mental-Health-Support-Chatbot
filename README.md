
# 🧠 Mental Health Support Chatbot

This project is a Mental Health Support Chatbot built using **Streamlit** and **Google's Gemini API** (`gemini-1.5-flash`). It provides mental health support through a chat interface, offering **sentiment analysis**, **mood tracking**, and **personalized coping strategies** based on user input.

---

## ✨ Features

* **Chat Interface**: Interact with the chatbot in a user-friendly web interface.
* **Sentiment Analysis**: Analyze the emotional tone of user messages using TextBlob.
* **Mood Tracking**: Visualize mood trends over time with line charts.
* **Coping Strategies**: Get personalized coping tips based on emotional states.
* **Session Summaries**: Review chat history and mood logs during the session.
* **Helpful Resources**: Quick links to mental health support organizations.

## 📸 Screenshot

Here's a preview of the chatbot in action:
![Uploading Screenshot (175).png…]()


---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Vikranth3140/Mental-Health-Support-Chatbot.git
cd Mental-Health-Support-Chatbot
```

### 2. Create a virtual environment and activate it

```bash
python -m venv env
# On Windows:
.\env\Scripts\activate
# On macOS/Linux:
source env/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up Gemini API Key

1. Go to [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
2. Generate an API key.
3. Create a `.env` file in the project root and add:

```
GEMINI_API_KEY=your_api_key_here
```

---

## 💻 Usage

```bash
streamlit run app.py
```

Then, open your browser at [http://localhost:8501](http://localhost:8501)

### How to Interact

* Type your feelings or concerns in the chat input.
* The chatbot responds with helpful and empathetic replies.
* Sentiment is analyzed and coping strategies are suggested.
* Mood trend is shown in a live chart.
* A summary can be accessed in the sidebar.

---

## 📁 Project Structure

```
Mental-Health-Support-Chatbot/
│
├── app.py              # Main chatbot application
├── requirements.txt    # Python package dependencies
└── .env                # Environment file with Gemini API key (excluded from Git)
```

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🙏 Acknowledgements

* [Streamlit](https://streamlit.io)
* [Google Gemini API](https://makersuite.google.com/)
* [TextBlob](https://textblob.readthedocs.io/en/dev/)

---

## 🆘 Resources

If you are in crisis or need immediate support, please contact:

* 📞 **National Suicide Prevention Lifeline**: 1-800-273-8255
* 💬 **Crisis Text Line**: Text 'HELLO' to 741741
* 🌐 [More Resources](https://www.mentalhealth.gov/get-help/immediate-help)

