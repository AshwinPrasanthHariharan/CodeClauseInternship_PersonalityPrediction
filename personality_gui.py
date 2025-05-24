import tkinter as tk
from tkinter import filedialog, messagebox
import docx
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

train_docs = [
    "Led multiple teams and delivered results on tight deadlines.",
    "Worked on individual projects with attention to detail and analysis.",
]
train_labels = ["Extrovert", "Introvert"]

vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(train_docs)
model = LogisticRegression()
model.fit(X_train, train_labels)

def extract_text_from_docx(file_path):
    try:
        doc = docx.Document(file_path)
        return ' '.join([para.text for para in doc.paragraphs])
    except:
        return ""

def predict(cv_path):
    text = extract_text_from_docx(cv_path)
    if not text.strip():
        messagebox.showerror("Error", "Empty or unreadable file.")
        return
    X_test = vectorizer.transform([text])
    prediction = model.predict(X_test)[0]
    messagebox.showinfo("Prediction", f"Predicted Personality: {prediction}")

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("DOCX files", "*.docx")])
    if file_path:
        predict(file_path)

root = tk.Tk()
root.title("Personality Prediction from Resume")
root.geometry("400x200")

tk.Label(root, text="Upload a DOCX CV to predict personality", font=("Arial", 12)).pack(pady=20)
tk.Button(root, text="Browse", command=browse_file, bg="lightblue", font=("Arial", 12)).pack(pady=10)

root.mainloop()
