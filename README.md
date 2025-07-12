# 🧠 Text-to-SQL with Vector Context

Traditional text-to-SQL solutions work well for small databases. However, when working with **large databases** containing **thousands of tables**, LLMs struggle due to **token limitations** — they often lack the context needed to identify relevant tables and generate accurate queries.

This project aims to solve that problem by **integrating a Vector Database** to **store synthetic metadata** about the database structure. This metadata provides **strategic context** to the LLM, enabling it to generate SQL queries using the **correct tables and columns**.

---

## 🚀 Project Goals

- Summarize and embed **synthetic metadata** about database tables (e.g., column names, types, purpose, timestamps).
- Use a **vector database** to allow fast and semantic retrieval of relevant table context.
- Enable **LLMs** to receive this context and generate accurate SQL queries even in large-scale databases.

---

## 📁 Project Structure

```
project-root/
│
├── app/                  # Application folder
│   ├── front/            # Streamlit frontend for interaction
│   └── back/             # FastAPI backend for embeddings and query generation
│
├── notebooks/            # Exploratory notebooks for testing prompts and results
└── README.md             # Project overview and usage instructions
```

---

## 🧪 Running the Project

### 🔧 App (Frontend + Backend)

To run the full app (Streamlit + FastAPI), navigate to the `app` folder and run:

```bash
cd app
docker-compose up
```

> Make sure you have Docker and Docker Compose installed.

---

### 📓 Notebooks

To run the exploratory notebooks locally, you'll need Jupyter:

```bash
pip install notebook
jupyter notebook
```

Or, if using a preferred environment (e.g., VSCode, JupyterLab), ensure the appropriate kernel is available.

---

## 🧱 Next Steps

- Enhance the metadata extraction with schema sampling and column value descriptions.
- Improve prompt engineering to maximize SQL generation accuracy.
- Integrate support for schema evolution over time.

---

## 📬 Contributing

Feel free to open issues, suggest improvements, or contribute via pull requests.

---

## 📄 License

MIT License
