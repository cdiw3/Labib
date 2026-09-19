import streamlit as st
import streamlit.components.v1 as components

# قراءة ملف HTML
with open("labib0001.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# تضمينه في تطبيق Streamlit باستخدام مكوّن iframe
components.html(html_content, height=800, scrolling=True)