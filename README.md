# 🧠 LangChain SQL Bot

A smart and friendly Streamlit chatbot powered by LangChain + OpenAI that lets you ask questions over your SQLite database — just like you're talking to a data analyst.

---

## 💡 What It Does

- 🗂 Upload your own `.db` file (like a mock Salesforce or CRM DB)
- 💬 Ask natural questions like:
  - “What is the total opportunity value?”
  - “List tasks due this week”
- 🧠 Behind the scenes, it converts your question to raw SQL
- 📊 Shows the query, the answer, and even visualizes your schema!

---

## ⚙️ How to Set It Up

### 1. Clone the repo
```bash
git clone https://github.com/your-username/langchain-sql-bot.git
cd langchain-sql-bot
```

### 2. Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set your OpenAI API Key
```bash
export OPENAI_API_KEY=your-key-here
```

### 5. Run the app
```bash
streamlit run streamlit_app.py
```

---

## 🗂 Folder Structure

```
├── data/                   # Put your .db files here
├── sql_agent.py            # LangChain agent setup and schema diagram logic
├── streamlit_app.py        # Streamlit UI and chat interface
├── utils/                  # Query splitter and helper modules
├── requirements.txt
└── README.md
```

---

## 🛠 Tech Stack

- [LangChain](https://github.com/langchain-ai/langchain)
- [OpenAI GPT-3.5/4](https://platform.openai.com/)
- [Streamlit](https://streamlit.io/)
- [SQLite](https://www.sqlite.org/)
- [Graphviz](https://graphviz.org/)

---

## 🚀 Coming Soon

- PostgreSQL & MySQL support
- Export to Excel or CSV
- Query history
- Copyable raw SQL output
- Chart visualizations for numeric answers

---

## 📜 License

MIT
