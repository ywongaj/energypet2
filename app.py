import streamlit as st
import ui_parts as ui

# 1. 基础配置
st.set_page_config(page_title="Guardian App", page_icon="🐾", layout="centered")
ui.inject_stitch_style()

# 2. 初始化全局状态
if 'page' not in st.session_state:
    st.session_state.page = "Register"
if 'user_email' not in st.session_state:
    st.session_state.user_email = ""
if 'chosen_pet' not in st.session_state:
    st.session_state.chosen_pet = None
if 'friends' not in st.session_state:
    st.session_state.friends = [] # 存储好友对象: {"email": "", "energy": 80}
if 'energy' not in st.session_state:
    st.session_state.energy = 85

# --- 页面路由逻辑 ---

# 页面 1: 注册
if st.session_state.page == "Register":
    ui.render_stitch_component(ui.get_register_ui(), height=450)
    email = st.text_input("Enter your email to join", placeholder="example@bank.com")
    if st.button("Continue", use_container_width=True):
        if "@" in email:
            st.session_state.user_email = email
            st.session_state.page = "ChoosePet"
            st.rerun()
        else:
            st.error("Please enter a valid email.")

# 页面 2: 选择宠物
elif st.session_state.page == "ChoosePet":
    ui.render_header("Choose Your Guardian")
    ui.render_stitch_component(ui.get_pet_selection_ui(), height=300)
    
    col1, col2, col3 = st.columns(3)
    with col1: 
        if st.button("Cat 😺"): 
            st.session_state.chosen_pet = "Cat"; st.session_state.page = "Dashboard"; st.rerun()
    with col2: 
        if st.button("Dog 🐶"): 
            st.session_state.chosen_pet = "Dog"; st.session_state.page = "Dashboard"; st.rerun()
    with col3: 
        if st.button("Bunny 🐰"): 
            st.session_state.chosen_pet = "Bunny"; st.session_state.page = "Dashboard"; st.rerun()

# 页面 3: 主系统 (带底部导航栏)
else:
    # 顶部导航 (可选)
    ui.render_header(f"{st.session_state.page}")

    # A. 首页
    if st.session_state.page == "Dashboard":
        ui.render_stitch_component(ui.get_dashboard_ui(st.session_state.energy, st.session_state.chosen_pet), height=400)
        # 日志记录按钮放在首页底部，方便操作
        if st.button("➕ Log New Activity", use_container_width=True):
            st.session_state.page = "Log" # 虽然不在底部导航，但作为主要操作保留
            st.rerun()

    # B. 日历页 (Insights)
    elif st.session_state.page == "Calendar":
        ui.render_stitch_component(ui.get_energy_log_ui(), height=650)

    # C. 社交同步页 (好友列表)
    elif st.session_state.page == "SocialSync":
        if not st.session_state.friends:
            ui.render_stitch_component(ui.get_empty_sync_ui(), height=300)
        else:
            for friend in st.session_state.friends:
                ui.render_stitch_component(ui.get_friend_card_ui(friend['email'], friend['energy']), height=100)
        
        # 添加好友功能
        with st.expander("➕ Add Friend"):
            f_email = st.text_input("Friend's Email")
            if st.button("Send Request"):
                st.session_state.friends.append({"email": f_email, "energy": 75})
                st.success("Friend added!")
                st.rerun()
    
    # D. 临时 Log 页 (记录能量)
    elif st.session_state.page == "Log":
        # (此处保留你之前的 -100 到 100 的双向输入逻辑)
        if st.button("← Back"): st.session_state.page = "Dashboard"; st.rerun()

    # 固定底部工具栏
    st.markdown("---")
    nav_col1, nav_col2, nav_col3 = st.columns(3)
    with nav_col1:
        if st.button("🏠 Home"): st.session_state.page = "Dashboard"; st.rerun()
    with nav_col2:
        if st.button("📅 Calendar"): st.session_state.page = "Calendar"; st.rerun()
    with nav_col3:
        if st.button("👥 Sync"): st.session_state.page = "SocialSync"; st.rerun()
