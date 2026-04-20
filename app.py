import streamlit as st
import ui_parts as ui

# 1. 基础配置
st.set_page_config(page_title="Guardian App", page_icon="🐾", layout="centered")
ui.inject_stitch_style()

# 2. 初始化全局状态
if 'page' not in st.session_state:
    st.session_state.page = "Onboarding"
if 'energy' not in st.session_state:
    st.session_state.energy = 85  # 初始电量
if 'history' not in st.session_state:
    st.session_state.history = []

# --- 页面路由 ---

# A. Onboarding 欢迎页
if st.session_state.page == "Onboarding":
    ui.render_stitch_component(ui.get_onboarding_ui(), height=600)
    if st.button("Begin Journey ✨", use_container_width=True):
        st.session_state.page = "Dashboard"
        st.rerun()

# B. Dashboard 主页
elif st.session_state.page == "Dashboard":
    ui.render_header("Guardian Sanctuary")
    ui.render_stitch_component(ui.get_dashboard_ui(st.session_state.energy), height=400)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📈 Log Activity", use_container_width=True):
            st.session_state.page = "Log"
            st.rerun()
    with col2:
        if st.button("🔄 Social Sync", use_container_width=True):
            st.session_state.page = "Sync"
            st.rerun()

# C. Log 记录页 (双向输入核心)
elif st.session_state.page == "Log":
    ui.render_header("Energy Log")
    
    st.markdown('<div class="glass-card" style="padding:1rem; margin-bottom:1.5rem; background:rgba(255,255,255,0.4); border-radius:2rem;">', unsafe_allow_html=True)
    
    # 使用 Form 确保提交时统一处理数据
    with st.form("energy_entry_form", clear_on_submit=True):
        event_name = st.text_input("What happened?", placeholder="Lunch with team, Meditation...")
        
        st.write("Energy Impact (-100 to 100)")
        
        # 联动逻辑：滑动条与数字框
        col_slider, col_input = st.columns([3, 1])
        with col_slider:
            val_slider = st.slider("Adjust Impact", -100, 100, 0, label_visibility="collapsed")
        with col_input:
            val_num = st.number_input("Value", -100, 100, value=val_slider, label_visibility="collapsed")
            
        # 确定最终数值
        final_val = val_num if val_num != val_slider else val_slider
        
        submit = st.form_submit_button("Record Entry ✨", use_container_width=True)
        
        if submit and event_name:
            # 更新电量（限制在 0-100）
            st.session_state.energy = max(0, min(100, st.session_state.energy + final_val))
            # 记录历史
            st.session_state.history.insert(0, {"name": event_name, "val": final_val})
            st.toast(f"Logged: {event_name}")
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

    # 显示历史
    st.markdown("### Recent Activities")
    for item in st.session_state.history[:5]:
        color = "red-500" if item['val'] < 0 else "emerald-600"
        symbol = "trending_down" if item['val'] < 0 else "trending_up"
        log_html = f'''
        <div class="flex items-center justify-between bg-white/40 p-4 rounded-3xl mb-2 border border-white/10">
            <div class="flex items-center gap-3">
                <span class="material-symbols-outlined text-{color}">{symbol}</span>
                <span class="font-bold text-[#2b3433]">{item['name']}</span>
            </div>
            <span class="font-black text-{color}">{item['val']}%</span>
        </div>
        '''
        ui.render_stitch_component(log_html, height=80)

    if st.button("← Back Home", use_container_width=True):
        st.session_state.page = "Dashboard"
        st.rerun()

ui.render_bottom_nav()
