

# 🧠 LangChain SQL Bot

This is a Streamlit-based chatbot powered by LangChain and OpenAI that allows you to interact with your SQLite database using natural language.

---

## 💡 Features

- Upload your own `.db` file
- Ask questions like:
  - "What is the total amount of opportunities?"
  - "List all leads from California"
- See the actual SQL query generated
- View natural language answers
- Automatically visualizes the database schema with PK/FK annotations

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/langchain-sql-bot.git
cd langchain-sql-bot
```

### 2. Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
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

## 📂 Project Structure

```
├── streamlit_app.py        # Main Streamlit UI
├── sql_agent.py            # LangChain logic and schema diagram
├── requirements.txt        # Python dependencies
├── README.md               # Project overview
```

---

## 🧠 Built With

- [LangChain](https://github.com/hwchase17/langchain)
- [OpenAI API](https://platform.openai.com/)
- [Streamlit](https://streamlit.io/)
- [SQLite](https://www.sqlite.org/)
- [Graphviz](https://graphviz.org/)

---

## 🚀 Future Enhancements

- PostgreSQL/MySQL support
- Query saving and history
- Rich chart visualizations
- Download results

---

## 📜 License

MIT