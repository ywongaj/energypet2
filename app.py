import streamlit as st
import ui_parts as ui

# 初始化
st.set_page_config(page_title="Guardian App", page_icon="🐾")
ui.inject_stitch_style()

# 页面导航状态
if 'page' not in st.session_state:
    st.session_state.page = "Onboarding"

# 页面渲染逻辑
if st.session_state.page == "Onboarding":
    ui.render_stitch_component(ui.get_onboarding_ui(), height=450)
    if st.button("Begin Journey ✨", use_container_width=True):
        st.session_state.page = "Dashboard"
        st.rerun()

elif st.session_state.page == "Dashboard":
    ui.render_header("Sanctuary")
    ui.render_stitch_component(ui.get_dashboard_ui(), height=350)
    if st.button("View Energy Log 📈", use_container_width=True):
        st.session_state.page = "Log"
        st.rerun()

elif st.session_state.page == "Log":
    ui.render_header("Energy Log")
    ui.render_stitch_component(ui.get_log_ui(), height=450)
    if st.button("← Back Home", use_container_width=True):
        st.session_state.page = "Dashboard"
        st.rerun()

ui.render_bottom_nav()
