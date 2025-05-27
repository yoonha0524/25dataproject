import streamlit as st 
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# 페이지 설정
st.set_page_config(page_title="서초구 고등학교 지도", layout="centered")

# 타이틀
st.title("📍 서초구 고등학교 위치 지도")

# 고등학교 데이터 (예시)
data = {
    "학교명": [
        "서울고등학교",
        "세화고등학교",
        "세화여자고등학교",
        "서문여자고등학교",
        "양재고등학교"
    ],
    "주소": [
        "서울특별시 서초구 반포대로 222",
        "서울특별시 서초구 사임당로23길 25",
        "서울특별시 서초구 사임당로23길 25",
        "서울특별시 서초구 서초중앙로 81",
        "서울특별시 서초구 양재천로 67"
    ],
    "위도": [37.5006, 37.4931, 37.4929, 37.4896, 37.4775],
    "경도": [127.0117, 127.0125, 127.0127, 127.0155, 127.0374]
}
df = pd.DataFrame(data)

# 지도 중심 설정 (서초구 중심 좌표)
map_center = [37.4836, 127.0326]
m = folium.Map(location=map_center, zoom_start=13)

# 학교별 마커 추가
for _, row in df.iterrows():
    folium.Marker(
        location=[row["위도"], row["경도"]],
        popup=f"<b>{row['학교명']}</b><br>{row['주소']}",
        tooltip=row["학교명"],
        icon=folium.Icon(color='blue', icon='graduation-cap', prefix='fa')
    ).add_to(m)

# 지도 출력
st_folium(m, width=700, height=500)

# 표 출력 (선택사항)
with st.expander("📄 고등학교 목록 보기"):
    st.dataframe(df[["학교명", "주소"]], use_container_width=True)
