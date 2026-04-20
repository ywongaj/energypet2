# app.py
import streamlit as st
import ui_parts as ui

# 基础设置
st.set_page_config(page_title="Guardian", page_icon="🐾")
ui.inject_stitch_style()

# 初始化页面状态
if 'page' not in st.session_state:
    st.session_state.page = "Onboarding"

# --- 页面路由 ---

if st.session_state.page == "Onboarding":
    ui.render_stitch_component(ui.get_onboarding_ui())
    if st.button("BEGIN JOURNEY", use_container_width=True):
        st.session_state.page = "Dashboard"
        st.rerun()

elif st.session_state.page == "Dashboard":
    ui.render_stitch_component(ui.get_dashboard_ui(85)) # 这里的 85 可以改成你的变量
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📈 Log", use_container_width=True):
            st.session_state.page = "Log"; st.rerun()
    with col2:
        if st.button("🔄 Sync", use_container_width=True):
            st.session_state.page = "Sync"; st.rerun()

elif st.session_state.page == "Log":
    ui.render_stitch_component(ui.get_log_ui())
    if st.button("← Back", use_container_width=True):
        st.session_state.page = "Dashboard"; st.rerun()

elif st.session_state.page == "Sync":
    ui.render_stitch_component(ui.get_sync_ui())
    if st.button("← Back", use_container_width=True):
        st.session_state.page = "Dashboard"; st.rerun()
