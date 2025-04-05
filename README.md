# 🎓 Personalized Learning Path Recommender System

An intelligent recommendation system that suggests the **best learning path** based on:
- ✅ Your current skills
- 🎯 Your target goal (technology/topic)
- 🌟 Course ratings and relevance

This AI-based tool helps students and professionals get personalized course recommendations with ratings, making their learning journey focused and efficient.

---

## 🚀 Features

- 🔍 Input your existing skills (e.g., Python, HTML, Excel)
- 🎯 Choose what you want to learn (e.g., Data Science, Full Stack Development)
- 🎓 Get a personalized list of **top-rated courses**
- 📊 Each course includes:
  - Platform name (e.g., Coursera, Udemy)
  - Course rating
  - Description & duration
- 🧠 Smart recommendation engine (content-based + NLP filtering)
- 🌐 Simple web interface using **Flask**

---

## 📂 Project Structure


learning-path-recommender/ ├── templates/ # HTML frontend │ └── index.html ├── static/ # CSS / styling ├── data/ │ └── courses_dataset.csv # Dataset of courses with tags, ratings ├── app.py # Flask backend ├── recommender.py # Skill-to-course matching logic ├── utils.py # NLP preprocessing ├── requirements.txt └── README.md


---

## 💡 How It Works

### 1. Input:
- **Skills**: Python, SQL, Excel
- **Goal**: Become a Data Analyst

### 2. Process:
- NLP filtering & cosine similarity
- Match skills with course prerequisites
- Filter and sort by rating + relevance

### 3. Output:
- A list of personalized courses with:
  - ⭐ Ratings
  - 🎓 Course title
  - 📍 Platform
  - 🔗 Link to course

---

## 🛠 Tech Stack

- **Python 3.9+**
- **Flask** – Web framework
- **Pandas / NumPy** – Data processing
- **NLTK / scikit-learn** – NLP & ML logic
- **HTML/CSS** – Frontend interface

---

## 🧪 Demo

### Example Input:

 Skills: Python, Excel Goal: Data Science

### Example Output:

📚 "Data Science with Python" – Coursera (⭐ 4.7)

📘 "Excel for Data Analysis" – Udemy (⭐ 4.6)

📖 "Statistics for DS" – edX (⭐ 4.8)


---

## 📈 Future Improvements

- 🔄 User login & profile save
- 📊 Track progress and completed courses
- 🔗 API integration with real platforms (Coursera, edX)
- 📱 Mobile UI

