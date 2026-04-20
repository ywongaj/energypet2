# app.py
import streamlit as st
import ui_parts as ui

# 初始化
st.set_page_config(page_title="Social Battery", page_icon="🔋")
ui.inject_stitch_style()

if 'page' not in st.session_state:
    st.session_state.page = "Dashboard"

# 根据页面状态显示内容
if st.session_state.page == "Dashboard":
    ui.render_header("Guardian Dashboard")
    ui.render_stitch_component(ui.get_dashboard_ui(), height=300)
    if st.button("View Energy Log →", use_container_width=True):
        st.session_state.page = "Log"
        st.rerun()

elif st.session_state.page == "Log":
    ui.render_header("Energy Log")
    ui.render_stitch_component(ui.get_log_ui(), height=400)
    if st.button("← Back to Home", use_container_width=True):
        st.session_state.page = "Dashboard"
        st.rerun()

ui.render_bottom_nav()
