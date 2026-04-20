# app.py 示例
import streamlit as st
import ui_parts as ui

ui.inject_stitch_style()

if 'page' not in st.session_state:
    st.session_state.page = "Home"

if st.session_state.page == "Home":
    ui.render_stitch_component(ui.get_dashboard_ui())
    if st.button("Open Log"):
        st.session_state.page = "Log"
        st.rerun()
else:
    ui.render_stitch_component(ui.get_log_ui())
    if st.button("Back Home"):
        st.session_state.page = "Home"
        st.rerun()