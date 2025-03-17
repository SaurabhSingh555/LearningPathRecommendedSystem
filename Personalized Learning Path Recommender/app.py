from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
import nltk
import os

# Download stopwords if not already downloaded
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Initialize Flask app
app = Flask(__name__)

# Load course data
def load_data():
    try:
        return pd.read_csv('coursera_courses.csv')
    except Exception as e:
        print(f"❌ Error loading coursera_courses.csv: {e}")
        return pd.DataFrame()

# Load user-course ratings (optional - not used in current logic)
def load_ratings():
    try:
        return pd.read_csv('user_course_ratings.csv')
    except Exception as e:
        print(f"❌ Error loading user_course_ratings.csv: {e}")
        return pd.DataFrame()

# Preprocess data
def preprocess_data(courses):
    if not courses.empty:
        courses['features'] = (
            courses['course_title'].fillna('') + ' ' +
            courses['course_organization'].fillna('') + ' ' +
            courses['course_Certificate_type'].fillna('') + ' ' +
            courses['course_difficulty'].fillna('')
        )
        courses['features'] = courses['features'].str.lower()
    return courses

# Content-based filtering
def content_based_filtering(courses, course_title):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(courses['features'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    idx = courses[courses['course_title'] == course_title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    course_indices = [i[0] for i in sim_scores]
    return courses.iloc[course_indices]

# Skill gap analysis
def skill_gap_analysis(user_skills, required_skills, courses):
    missing_skills = required_skills - user_skills
    recommendations = {}
    for skill in missing_skills:
        skill_courses = courses[courses['features'].str.contains(skill, case=False, na=False)]
        if not skill_courses.empty:
            recommendations[skill] = skill_courses[['course_title', 'course_organization', 'course_rating', 'course_difficulty']]
    return recommendations

# Home route
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_skills = set(request.form['user_skills'].lower().split(','))
        required_skills = set(request.form['required_skills'].lower().split(','))

        courses = load_data()
        courses = preprocess_data(courses)

        recommendations = skill_gap_analysis(user_skills, required_skills, courses)

        return render_template('index.html', recommendations=recommendations)

    return render_template('index.html')

# Run the app
if __name__ == '__main__':
    print("🚀 Starting Flask app on http://127.0.0.1:5000", flush=True)
    app.run(debug=True)
