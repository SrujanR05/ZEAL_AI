# 🚀 ZEAL AI – Smart Product Assistant

ZEAL AI is an intelligent product assistant web application that uses AI to answer user questions about products. It combines a Flask backend, a simple frontend UI, and an AI-based Visual Question Answering (VQA) model.

---

## 📌 Features

* 🧠 AI-powered question answering for products
* 🛍️ Product catalog with images and details
* 💬 Interactive chat interface
* 🗂️ Chat history stored using SQLite
* 🔍 Smart relevance checking for user queries
* 🛠️ Admin panel for managing queries

---

## 🏗️ Tech Stack

* **Backend:** Flask (Python)
* **Frontend:** HTML, CSS, JavaScript
* **Database:** SQLite
* **AI Model:** Custom VQA Model
* **Data Storage:** JSON (products)

---

## 📂 Project Structure

```
ZEAL_AI/
│── app.py
│── database.db
│── requirements.txt
│
├── data/
│   └── products.json
│
├── models/
│   └── vqa_model.py
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   ├── index.html
│   ├── product.html
│   ├── chat.html
│   └── admin.html
```

---

## ⚙️ Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com/your-username/zeal-ai.git
cd zeal-ai
```

2. **Create a virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the application**

```bash
python app.py
```

5. **Open in browser**

```
http://127.0.0.1:5000/
```

---

## 🧠 How It Works

* Products are loaded from a JSON file
* Users select a product and ask questions
* The system checks if the question is relevant
* AI model generates an answer
* Chat history is stored in SQLite database

---

## 🗄️ Database Tables

* **users** → Stores user details
* **chat_history** → Stores completed Q&A
* **pending_questions** → Stores unanswered queries

---

## 📸 Sample Use Case

1. Select a product (e.g., laptop or phone)
2. Ask a question like:

   * "What is the battery life?"
   * "Is this good for gaming?"
3. Get AI-generated answers instantly

---

## 🚧 Future Improvements

* 🔐 User authentication system
* 🌐 Deploy on cloud (AWS / Render / Heroku)
* 📊 Analytics dashboard
* 🤖 Improved AI accuracy
* 🛒 E-commerce integration

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork the repo and submit a pull request.

---

## 📄 License

This project is for educational purposes.

---

## 👨‍💻 Author

Developed as part of a project to build an AI-powered product assistant.

---
