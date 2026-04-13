# 🦊 GitLab Handbook Assistant

An AI-powered chatbot that helps employees and aspiring employees easily access information from GitLab's Handbook and Direction pages — built with **Hybrid RAG + HyDE retrieval**.

## 🌐 Live Demo
🔗 [https://app-handbook-chatbot.streamlit.app/](https://app-handbook-chatbot.streamlit.app/)

## 👤 Author
**V Sai Kiran Reddy**  
GitHub: [https://github.com/skar-23/gitlab-handbook-chatbot](https://github.com/skar-23/gitlab-handbook-chatbot)

---

## 🧠 How It Works

This chatbot uses an **Advanced Hybrid RAG** pipeline to improve accuracy and grounded responses:

1. **Query Expansion**: Enriches the user query with GitLab-specific terms.
2. **HyDE**: Gemini generates a hypothetical ideal answer to improve retrieval quality.
3. **Hybrid Search**: Combines semantic search (ChromaDB) + keyword matching.
4. **Dual Retrieval**: Searches Handbook and Direction content separately.
5. **Grounded Generation**: Gemini synthesizes an answer using only retrieved context and provides citations.

---

## ✨ Features

- 💬 Natural conversation with multi-turn memory.
- 📚 Large indexed knowledge base from GitLab public docs.
- 🔍 Hybrid RAG + HyDE retrieval.
- 📖 Source citations in final answers.
- 🎨 Multiple UI themes in Streamlit.
- 🛡️ Basic guardrails for off-topic handling.
- ⚡ Model fallback strategy for quota handling.

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Frontend | Streamlit |
| LLM | Google Gemini 2.0 Flash |
| Embeddings | `sentence-transformers` (`all-MiniLM-L6-v2`) |
| Vector Store | ChromaDB |
| Data Ingestion | Git (Handbook) + BeautifulSoup (Direction pages) |

---

## 🗂️ Project Structure

```text
gitlab-handbook-chatbot/
├── app.py
├── src/
│   ├── rag_engine.py
│   ├── ingest_handbook.py
│   ├── ingest_direction.py
│   ├── build_vectorstore.py
│   ├── clear_db.py
│   └── debug_search.py
├── requirements.txt
└── runtime.txt
```

---

## 🚀 Setup & Run Locally

### Prerequisites

- Python 3.10+
- Gemini API key (Google AI Studio)

### 1) Clone and install

```bash
git clone https://github.com/skar-23/gitlab-handbook-chatbot.git
cd gitlab-handbook-chatbot
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Environment variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
HF_TOKEN=your_huggingface_token_if_needed
```

### 3) Run the app

```bash
streamlit run app.py
```

---

## ☁️ Deploy on Streamlit Community Cloud (separate deployment)

1. Push your code to your GitHub repository (already done).
2. Go to [https://share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
3. Click **Create app** and select:
   - Repository: `skar-23/gitlab-handbook-chatbot`
   - Branch: `main`
   - Main file path: `app.py`
4. In app **Settings → Secrets**, add:

```toml
GEMINI_API_KEY = "your_gemini_api_key_here"
HF_TOKEN = "your_huggingface_token_if_needed"
```

5. Deploy the app.

Notes:
- `requirements.txt` is already present, so Streamlit Cloud installs dependencies automatically.
- First startup may take extra time while the vector DB is downloaded.

---

## 📝 Update README after deployment

After Streamlit gives your new app URL, replace the Live Demo link in this README:

```md
## 🌐 Live Demo
🔗 https://your-app-name.streamlit.app/
```

Then commit and push:

```bash
git add README.md
git commit -m "docs: add Streamlit deployment instructions and live demo link"
git push
```

---

## 🎯 Example Questions

- What are GitLab's core CREDIT values?
- How does GitLab handle unlimited PTO?
- How do I prepare for a technical interview at GitLab?
