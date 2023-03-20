import streamlit as st
import requests
import pandas as pd

st.title("프로그래머스 파이썬 문제 검색기")

# 프로그래머스의 파이썬 문제들을 긁어오는 api를 직접 참조해서
# 전체 데이터를 df와 시킬 것
# url = "https://school.programmers.co.kr/api/v1/school/challenges/?perPage=20&languages[]=python3&order=recent&page=1"
page_url = lambda x: f"https://school.programmers.co.kr/api/v1/school/challenges/?perPage=20&languages[]=python3&order=recent&page={x}"

# res = requests.get(page_url(2))
# st.write(res.status_code)
# st.write(res.text)

#1. page을 호출해서 total page만 받는다
res = requests.get(page_url(1))
json = res.json()
total_pages = json['totalPages']
# st.write(total_pages)

get_tests = lambda x: requests.get(page_url(x)).json()['result']

#2. total page -> for문으로 전체 문제 크롤링 -> df
# for i in range(total_pages):
#     st.write(get_tests(i+1))

df = pd.concat([pd.DataFrame(get_tests(i+1), dtype=str) for i in range(total_pages)])
df = df[['id', 'title']].sort_values(
    by='id', key=lambda x: x.astype(int)
    ).reset_index(drop=True)
# st.write(df)

#3. df write

# 글씨를 입력하는 창 -> 입력 -> df -> contains. 노출 -> 링크까지

st.text_input(label="검색어 입력", key='search')
