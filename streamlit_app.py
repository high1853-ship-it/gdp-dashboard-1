import streamlit as st
import pandas as pd
import datetime

# --- 1. 專業網頁設定 ---
st.set_page_config(page_title="Ling's Fitness Pro", page_icon="🔥", layout="wide")

# 套用自定義 CSS 讓顏色更豐富
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; border-radius: 20px; background: linear-gradient(45deg, #FF4B2B, #FF416C); color: white; border: none; }
    .metric-card { background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); border-left: 5px solid #FF416C; }
    h1 { color: #2C3E50; font-family: 'Helvetica Neue', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 標題與數據導航 ---
st.title("🏃‍♀️ Ling Pro 數據監控中心")
st.write(f"最後更新：{datetime.date.today()}")

# 模擬最新數據 (這部分之後可串接資料庫)
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div class="metric-card"><h4>體重</h4><h2>68.6 <small>kg</small></h2></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="metric-card"><h4>體脂率</h4><h2>38.5 <small>%</small></h2></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="metric-card"><h4>內臟脂肪</h4><h2>11.0</h2></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="metric-card"><h4>身體年齡</h4><h2>28 <small>歲</small></h2></div>', unsafe_allow_html=True)

st.divider()

# --- 3. 互動區域 ---
tab1, tab2, tab3 = st.tabs(["📊 趨勢分析", "📸 照片存檔", "✍️ 手動輸入"])

with tab1:
    st.subheader("核心指標變化趨勢")
    # 建立更有質感的範例數據
    chart_data = pd.DataFrame({
        '日期': pd.date_range(start='2026-01-01', periods=7),
        '體重': [70.2, 69.8, 69.5, 69.2, 68.9, 68.7, 68.6],
        '體脂': [39.5, 39.2, 39.0, 38.8, 38.6, 38.5, 38.5]
    }).set_index('日期')
    
    st.line_chart(chart_data, color=["#FF416C", "#3498db"])

with tab2:
    st.subheader("小米報告存檔")
    uploaded_file = st.file_uploader("點擊或拖曳上傳今日報告截圖", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        st.image(uploaded_file, use_container_width=True)

with tab3:
    with st.form("data_form"):
        c1, c2 = st.columns(2)
        w = c1.number_input("今日體重", value=68.6)
        f = c2.number_input("今日體脂", value=38.5)
        submitted = st.form_submit_button("同步最新數據")
        if submitted:
            st.toast("數據已同步至雲端！", icon='✅')

# --- 4. 底部 AI 反饋區 ---
st.sidebar.header("🤖 AI 專屬回饋")
st.sidebar.info("Ling，你目前的肌肉量分佈非常平均。建議加強軀幹部位的有氧訓練，以針對內臟脂肪進行改善。")
st.sidebar.progress(45, text="目標體重達成度：45%")
