import pandas as pd
import streamlit as st

# Streamlit 
st.title("📚 Personal Library Manager")

# Try to read CSV
try:
    df = pd.read_csv("books.csv")
except FileNotFoundError:
    df = pd.DataFrame(columns=["Title", "Author", "Genre", "Status"])

st.write("### 📖 Books details")
st.dataframe(df)

# Input fields
title = st.text_input("📖 Book Title")
author = st.text_input("✍️ Author Name")
genre = st.text_input("📂 Genre")
status = st.selectbox("📌 Status:", ["Reading", "Completed", "Wishlist"])

# Add Book
if st.button("➕ Add Book"):
    new_book = pd.DataFrame([[title, author, genre, status]], columns=df.columns)
    df = pd.concat([df, new_book], ignore_index=True)
    df.to_csv("books.csv", index=False)
    st.success("✅ Added New Book!")
    st.rerun()

# Delete Book
if st.button("❌ Delete Book"):
    df = df[~((df['Title'] == title) & (df['Author'] == author))]
    df.to_csv("books.csv", index=False)
    st.success("🗑️ Book Deleted!")
    st.rerun()