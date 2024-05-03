import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
df = pd.read_csv(r"C:\Users\ANKIT SINGH\OneDrive\Desktop\covid.csv")
data = df["covid"] + "" + df["fever"]
X = data.astype(str) 
y = df['flu'] 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, 
random_state = 42)
vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(X_train)
X_test_counts = vectorizer.transform(X_test)
classifier = MultinomialNB()
classifier.fit(X_train_counts, y_train)
data1 = pd.read_csv(r"C:\Users\ANKIT SINGH\OneDrive\Desktop\test.csv")
new_data = data1["covid"] + "" + data1["fever"]
new_data_counts = vectorizer.transform(new_data.astype(str))
predictions = classifier.predict(new_data_counts)
new_data = predictions
print(new_data)
accuracy = accuracy_score(y_test, classifier.predict(X_test_counts))
print(f"\nAccuracy: {accuracy:.2f}")
print("Classification Report: ")
print(classification_report(y_test, classifier.predict(X_test_counts)))
predictions_df = pd.DataFrame(predictions, columns = ['flu_prediction'])
data1 = pd.concat([data1, predictions_df], axis = 1)

