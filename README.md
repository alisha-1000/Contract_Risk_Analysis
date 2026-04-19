# ⚖️ Intelligent Contract Risk Analysis & Agentic Legal Assistance

## 🚀 From NLP-Based Risk Detection to Agentic AI Legal Reasoning

---

## 📌 Project Overview

This project presents an **AI-powered system for analyzing legal contracts** and identifying potential risks at the clause level.

The system is developed in two phases:

* **Milestone 1:** Classical NLP + Machine Learning-based clause classification
* **Milestone 2:** Retrieval-Augmented Generation (RAG) + Agentic AI system for autonomous reasoning

The final system integrates **ML, RAG, LLMs, and Agentic workflows** to generate structured contract risk reports.

---

## 🧠 Key Features

* 📄 Upload contract (PDF/Text)
* 🔍 Clause-level analysis
* ⚠️ Risk classification (High / Medium / Low)
* 📚 Context retrieval using RAG (FAISS)
* 🧠 LLM-based reasoning (Groq API)
* 🔁 Agentic workflow using LangGraph
* 📊 Structured risk report generation
* 🌐 Live deployment (Streamlit Cloud)

---

## 🚀 How It Works

1. Upload contract (PDF/Text)
2. System splits text into clauses
3. RAG retrieves similar legal clauses
4. LLM analyzes clause risk
5. Agent compiles structured report

---

## 🧩 System Architecture

```
Input (PDF/Text)
        ↓
Clause Segmentation (utils/parser.py)
        ↓
RAG Retrieval (rag/retriever.py)
        ↓
LLM Reasoning (rag/llm_rag.py)
        ↓
Agent Workflow (agent/graph.py)
        ↓
Final Risk Report
```

---

## 📊 Milestone 1: ML-Based Risk Classification

### 🔹 Objective

Detect risky clauses using classical NLP techniques.

### 🔹 Implementation

* Text preprocessing (cleaning, tokenization)
* Feature extraction using **TF-IDF**
* Model: **Logistic Regression**
* Files:

  * `risk_model.pkl`
  * `label_encoder.pkl`
  * `tfidf_vectorizer.pkl`

### 🔹 Output

* Clause-level risk prediction
* Evaluation using accuracy and F1-score

---

## 🚀 Milestone 2: Agentic AI Legal Assistant

### 🔹 1. Clause Segmentation

* Implemented in `utils/parser.py`
* Regex-based splitting
* Structured clause extraction

---

### 🔹 2. RAG Pipeline

* Embeddings: `sentence-transformers`
* Vector Store: `FAISS`
* Files:

  * `faiss.index`
  * `metadata.pkl`
  * `build_index.py`

```
Query → Embedding → Similar Clauses → Context
```

---

### 🔹 3. LLM Reasoning

* Implemented in `rag/llm_rag.py`
* Uses **Groq API**
* Generates:

  * Risk level
  * Explanation

---

### 🔹 4. Agentic Workflow (LangGraph)

Implemented in `agent/graph.py`

```
Extract → Analyze → Loop → Report
```

* Stateful execution
* Iterative clause analysis
* Final structured output

---

### 🔹 5. Output

* Clause-level:

  * Risk Level
  * Explanation
* Final contract risk report

---

## 🖥️ User Interface

Built using **Streamlit** (`app.py`)

Features:

* Upload PDF
* View clauses
* Risk dashboard
* Download report

---

## 🌐 Deployment

Deployed using **Streamlit Cloud**

🔗 **Live App:** [https://your-app-link.streamlit.app](https://contractriskanalysis-l3qvfbvsojfij8hek3khzk.streamlit.app/)

---

## ⚙️ Tech Stack

### 🔹 NLP & ML

* scikit-learn
* nltk
* TF-IDF

### 🔹 RAG

* sentence-transformers
* FAISS

### 🔹 Agentic AI

* LangGraph
* LangChain

### 🔹 LLM

* Groq API

### 🔹 Frontend

* Streamlit

### 🔹 Other

* PyPDF
* pandas, numpy

---

## 📁 Project Structure

```
Contract_Risk_Analysis/
│
├── app.py
├── requirements.txt
├── README.md
│
├── agent/
│   └── graph.py
│
├── rag/
│   ├── retriever.py
│   ├── llm_rag.py
│   ├── build_index.py
│   ├── faiss.index
│   └── metadata.pkl
│
├── utils/
│   └── parser.py
│
├── risk_model.pkl
├── label_encoder.pkl
├── tfidf_vectorizer.pkl
```

---

## 🔐 Environment Setup

Create `.streamlit/secrets.toml`:

```
GROQ_API_KEY = "your_api_key_here"
```

---

## ▶️ Run Locally

```
pip install -r requirements.txt
streamlit run app.py
```

---

## 📊 Evaluation Alignment

This project satisfies evaluation criteria:

* ✔ RAG implementation
* ✔ Agentic AI (LangGraph)
* ✔ LLM-based reasoning
* ✔ Clean modular structure
* ✔ Deployment with UI
* ✔ Explainable outputs

---

## ⚠️ Disclaimer

This system provides AI-generated insights and **does not constitute legal advice**.

---

## 👥 Team Members

* Your Name
Ganaga Raghuwanshi
Anuradha Raghuwanshi
Bulbul Agarwalla
Alisha Gupta


---

## 🎯 Future Work

* Clause type classification
* Highlight risky clauses in document
* Multi-contract comparison
* Fine-tuned legal LLM

---

## 🧠 Key Insight

> This project demonstrates the transition from traditional NLP systems to **agentic AI workflows with retrieval-augmented reasoning**, enabling more reliable and explainable legal analysis.

---


