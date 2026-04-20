import streamlit as st
import ui_parts as ui

# 1. 页面配置
st.set_page_config(page_title="Guardian App", page_icon="🐾", layout="centered")
ui.inject_stitch_style()

# 2. 初始化页面状态（如果第一次打开，进入 Onboarding）
if 'page' not in st.session_state:
    st.session_state.page = "Onboarding"

# --- 路由指挥部 ---

# A. 欢迎/开屏页
if st.session_state.page == "Onboarding":
    ui.render_stitch_component(ui.get_onboarding_ui(), height=650)
    if st.button("Begin Journey ✨", use_container_width=True):
        st.session_state.page = "Dashboard"
        st.rerun()

# B. 主页 (Guardian Dashboard)
elif st.session_state.page == "Dashboard":
    ui.render_header("Guardian Sanctuary")
    ui.render_stitch_component(ui.get_dashboard_ui(), height=450)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📈 View Logs", use_container_width=True):
            st.session_state.page = "Log"
            st.rerun()
    with col2:
        if st.button("🔄 Social Sync", use_container_width=True):
            st.session_state.page = "Sync"
            st.rerun()

# C. 能源日志页
elif st.session_state.page == "Log":
    ui.render_header("Energy Log")
    ui.render_stitch_component(ui.get_log_ui(), height=500)
    if st.button("← Back to Sanctuary", use_container_width=True):
        st.session_state.page = "Dashboard"
        st.rerun()

# D. 社交同步页
elif st.session_state.page == "Sync":
    ui.render_header("Social Sync")
    ui.render_stitch_component(ui.get_sync_ui(), height=500)
    if st.button("← Back to Sanctuary", use_container_width=True):
        st.session_state.page = "Dashboard"
        st.rerun()

# 统一底部
ui.render_bottom_nav()
