
# 🛒 E-Commerce Chatbot using Groq, ChromaDB, SQLite3 & Semantic Router

This project is an intelligent e-commerce chatbot that helps users navigate products, ask questions, and receive accurate, conversational responses in real-time. It uses **Groq LLMs** for fast response generation, **ChromaDB** for vector-based document search, **SQLite3** for structured product storage, and **Semantic Router** for intent-based routing.

---

## 🔧 Tech Stack

- **[Groq](https://groq.com/)** – Ultra-fast inference with LLMs like LLaMA and Mistral.
- **[ChromaDB](https://www.trychroma.com/)** – Vector store for embedding-based retrieval of unstructured data.
- **SQLite3** – Lightweight relational database for storing structured product info (name, price, category, etc).
- **[Semantic Router](https://github.com/semanticroter/semantic-router)** – Intent classification and routing layer for organizing chatbot workflows.

---

## ✨ Features

- 🛍️ **Product Search & Info:** Ask about product details using natural language.
- 💬 **Conversational Interface:** Human-like interactions powered by Groq LLMs.
- 🧠 **Context-Aware Retrieval:** Uses ChromaDB to pull relevant FAQ/product content.
- 🗂️ **Structured & Unstructured Data:** Combines SQLite3 (catalog data) with ChromaDB (FAQs/docs).
- 🛤️ **Semantic Routing:** Handles various user intents like product search, order tracking, and returns.

---



## ⚙️ How It Works

1. **Intent Detection:**  
   User input is passed through **Semantic Router** to detect the intent (e.g., "search product", "ask FAQ", "track order").

2. **Structured Query (SQLite):**  
   If intent is catalog-related, a SQL query is run on the `SQLite3` database to fetch product details.

3. **Unstructured Query (ChromaDB):**  
   If intent is FAQ-based or requires long-form content, relevant context is retrieved from ChromaDB.

4. **LLM Generation (Groq):**  
   The retrieved context and user query are passed to **Groq-hosted LLaMA/Mistral models** for generating the final response.

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/devpatel45/RAG-Project2.git
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set environment variables

Create a `.env` file with your Groq API key:

```
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=your_selected_model
```

### 4. Run the chatbot

```bash
python main.py
```

---

## 🧪 Example Prompts

- "Do you have any shoes with rating more than 3.5?"
- "Can I return my order after 10 days?"


  ## I have only implemented a small amount of FAQ data and as I don't have the full access to an E-Commerce data base I have given only a small shoes data base with links
