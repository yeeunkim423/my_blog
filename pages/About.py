import streamlit as st
import base64
import os
from streamlit_timeline import timeline  # 타임라인용 라이브러리

st.title("House of the Dragon Fanpage")

IMAGE_FOLDER = "data"

# daemon, alicent 딕셔너리 및 show_gif, show_character 함수는 그대로 유지

# 타임라인 이벤트 (최근 요구한 상세 버전)
timeline_events = {
    "events": [
        {
            "start_date": {"year": "81 AC"},
            "text": {
                "headline": "Daemon Targaryen born",
                "text": "Daemon Targaryen was born in 81 AC."
            }
        },
        {
            "start_date": {"year": "130 AC"},
            "text": {
                "headline": "Daemon dies",
                "text": "Daemon died at Gods Eye in 130 AC at age 49."
            }
        },
        {
            "start_date": {"year": "88 AC"},
            "text": {
                "headline": "Alicent Hightower born",
                "text": "Alicent Hightower was born in 88 AC."
            }
        },
        {
            "start_date": {"year": "Unknown"},
            "text": {
                "headline": "Alicent marries King Viserys I",
                "text": "Alicent became the wife of King Viserys I Targaryen."
            }
        },
        {
            "start_date": {"year": "133 AC"},
            "text": {
                "headline": "Alicent dies",
                "text": "Alicent died in King's Landing in 133 AC."
            }
        }
    ]
}

character_choice = st.sidebar.selectbox(
    "Choose a section",
    ("Daemon Targaryen", "Alicent Hightower", "Timeline")
)

if character_choice == "Daemon Targaryen":
    show_character(daemon)
elif character_choice == "Alicent Hightower":
    show_character(alicent)
else:
    st.header("Timeline")
    timeline(timeline_events)
