
from sklearn.feature_extraction.text import TfidfVectorizer

def get_matching_rate(text1 , text2):
    try:
        from sklearn.metrics.pairwise import cosine_similarity
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform([text1, text2])
        cosine_similarity = cosine_similarity(vectors[0], vectors[1]).flatten()
        return cosine_similarity[0]
    except:
        return 0.0