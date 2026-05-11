import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Simple dataset (expand later)
codes = [
    "print('hello')",
    "def add(a,b): return a+b",
    "#include<iostream>",
    "cout << 'hi';",
    "public static void main",
    "System.out.println('hi');",
    "console.log('hi')",
    "function test(){}"
]

labels = [
    "Python","Python","C++","C++",
    "Java","Java","JavaScript","JavaScript"
]

vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(3,6))
X = vectorizer.fit_transform(codes)

model = LogisticRegression(max_iter=1000)
model.fit(X, labels)

pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model saved")