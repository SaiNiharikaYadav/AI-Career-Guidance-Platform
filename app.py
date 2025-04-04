from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
CORS(app)

df = pd.read_csv("jobs_data.csv")
df['tags'] = df['Skills'] + " " + df['Domain']
vectorizer = TfidfVectorizer()
vector_matrix = vectorizer.fit_transform(df['tags'])

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    skills = data.get('skills', '')
    interests = data.get('interests', '')
    user_input = skills + " " + interests

    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, vector_matrix)
    top_indices = similarity[0].argsort()[-5:][::-1]
    recommendations = df.iloc[top_indices][['Job Title', 'Description']].to_dict(orient='records')
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
