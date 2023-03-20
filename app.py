import streamlit as st
import requests

st.title("프로그래머스 파이썬 문제 검색기")

# 프로그래머스의 파이썬 문제들을 긁어오는 api를 직접 참조해서
# 전체 데이터를 df와 시킬 것
url = "https://school.programmers.co.kr/api/v1/school/challenges"
qs = {
    "order": "recent",
    "page": 1
} 
res = requests.get(url, data=qs)
st.write(res.text)

# 글씨를 입력하는 창 -> 입력 -> df -> contains. 노출 -> 링크까지