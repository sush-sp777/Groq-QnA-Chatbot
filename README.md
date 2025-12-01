# 🤖 Q&A Chatbot using Groq + LangChain + Streamlit

A fast and lightweight **AI Question-Answer Chatbot**, powered by **Groq's ultra-fast inference**, served through a clean **Streamlit UI**, and built using **LangChain**.


---

## Demo
[Click here to view the deployed app](https://ska5akvvnjwvwswptle5yu.streamlit.app/)

---

## 🖱 How to Use

1. **Enter your Groq API Key**  
   - Open the app and enter your personal Groq API key in the sidebar.  
   - This key is required for the chatbot to generate responses.

2. **Select a Groq Model**  
   - Choose from available models like `llama-3.1-8b-instant`, `llama-3.3-70b-versatile`, or `openai/gpt-oss-20b`.  
   - Different models may produce slightly different answers and response times.

3. **Adjust Response Settings**  
   - **Temperature:** Controls creativity of responses (0.0 = precise, 1.0 = creative).  
   - **Max Tokens:** Maximum length of the generated response.

4. **Ask a Question**  
   - Type your question in the main input box.  
   - The chatbot will provide a professional and helpful answer in the response section.

5. **View the Response**  
   - Scroll down to see the chatbot’s answer.  
   - You can ask follow-up questions as needed.
---

## 🚀 Features

- ⚡ Ultra-fast responses powered by Groq LLMs  
- 🎯 Ask any question and get accurate, helpful answers  
- 🔄 Switch between different Groq models  
- 🎛 Adjustable temperature + max token sliders  
- 🧩 Clean and modular LangChain pipeline  
- 🔐 Secure API key handling using `.env`  
- ☁️ Fully deployable on Streamlit Cloud  

---

## 🛠 Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Groq API** | LLM inference |
| **LangChain** | Prompt templates & chains |
| **Streamlit** | Front-end web UI |
| **Python-dotenv** | Environment variable management |
| **Python 3.10+**| Programming language |

---

## 📁 Project Structure

```bash
QnA-Groq-Chatbot/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
└── .gitignore
```
---
## ⚙️ Installation & Setup

- 1️⃣ Clone the repository
```bash
git clone https://github.com/sush-sp777/Groq-QnA-Chatbot.git
cd Groq-QnA-Chatbot
```
- 2️⃣ Create a virtual environment
```bash
python -m venv venv
```
Activate it:
```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```
- 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
---
- 🔐 Environment Variables

Create a .env file in the project root (for local testing):
```bash
GROQ_API_KEY=your_groq_api_key
LANGCHAIN_API_KEY=your_langchain_api_key # Internal key for LangChain tracing
```
---
- ▶️ Running the App
```bash
streamlit run app.py
```
Your app will open automatically at:
```bash
http://localhost:8501
```




