import streamlit as st
import pyperclip

st.title("🎈 AtCoder 標準入力受け取り")

if st.button("N"):
    pyperclip.copy("input()")
#N = input()
st.button("N,M")
#N, M = map(int, input().split())
st.button("A1 A2 A3...An")
