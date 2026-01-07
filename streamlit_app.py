import streamlit as st
import pandas as pd
import datetime

# 設定網頁標題
st.set_page_config(page_title="Ling 減脂紀錄", page_icon="🏃‍♀️")

st.title("🏃‍♀️ Ling 的數據追蹤中心")

# --- 數據儲存邏輯 (簡單版) ---
if 'fitness_data' not in st.session_state:
    # 預設一筆你照片中的數據
    st.session_state.fitness_data = pd.DataFrame({
        "日期": ["2026-01-07"],
        "時段": ["早晨"],
        "體重": [68.6],
        "體脂": [38.5],
        "內臟脂肪": [11.0]
    })

# --- 輸入區 ---
with st.expander("➕ 新增今日紀錄"):
    col1, col2 = st.columns(2)
    with col1:
        new_date = st.date_input("選擇日期", datetime.date.today())
        new_time = st.selectbox("選擇時段", ["早晨", "晚間"])
    with col2:
        new_w = st.number_input("體重 (kg)", step=0.1, value=68.6)
        new_f = st.number_input("體脂 (%)", step=0.1, value=38.5)
        new_vf = st.number_input("內臟脂肪", step=0.5, value=11.0)
    
    if st.button("確認儲存"):
        new_row = pd.DataFrame({"日期": [str(new_date)], "時段": [new_time], "體重": [new_w], "體脂": [new_f], "內臟脂肪": [new_vf]})
        st.session_state.fitness_data = pd.concat([st.session_state.fitness_data, new_row], ignore_index=True)
        st.success("紀錄成功！")

# --- 圖片上傳區 ---
st.subheader("📷 上傳小米報告截圖")
uploaded_file = st.file_uploader("拍下今日數據照片", type=["jpg", "png", "jpeg"])
if uploaded_file:
    st.image(uploaded_file, caption="今日紀錄存檔", use_container_width=True)

# --- 圖表區 ---
st.subheader("📈 體重變化趨勢")
st.line_chart(st.session_state.fitness_data.set_index("日期")["體重"])

st.subheader("📋 歷史數據表")
st.dataframe(st.session_state.fitness_data, use_container_width=True)

# --- AI 自動反饋 (根據你照片的數值) ---
st.divider()
last_weight = st.session_state.fitness_data["體重"].iloc[-1]
last_vf = st.session_state.fitness_data["內臟脂肪"].iloc[-1]

st.subheader("🤖 AI 健康導師建議")
if last_vf >= 10:
    st.error(f"⚠️ 當前內臟脂肪為 {last_vf}，屬於「極高」等級。建議減少攝取含糖飲料與油炸物，增加每天 20 分鐘的有氧運動。")
else:
    st.success("✅ 內臟脂肪控制在標準範圍，請繼續保持！")
