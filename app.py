import streamlit as st
import ui_parts as ui

# 1. 初始化设置
st.set_page_config(page_title="Guardian", page_icon="🐾", layout="centered")
ui.inject_stitch_style()

# 2. 初始化全局数据状态
if 'page' not in st.session_state:
    st.session_state.page = "Register"
if 'user_email' not in st.session_state:
    st.session_state.user_email = ""
if 'chosen_pet' not in st.session_state:
    st.session_state.chosen_pet = None
if 'energy' not in st.session_state:
    st.session_state.energy = 85
if 'friends' not in st.session_state:
    st.session_state.friends = []

# --- 路由逻辑 ---

# 页面 A: 注册 (Email)
if st.session_state.page == "Register":
    ui.render_stitch_component(ui.get_register_ui(), height=400)
    email = st.text_input("Enter Email", placeholder="yourname@example.com", label_visibility="collapsed")
    if st.button("Continue", use_container_width=True):
        if "@" in email:
            st.session_state.user_email = email
            st.session_state.page = "ChoosePet"
            st.rerun()
        else:
            st.warning("Please enter a valid email.")

# 页面 B: 选择宠物
elif st.session_state.page == "ChoosePet":
    ui.render_header("Choose Guardian")
    ui.render_stitch_component(ui.get_pet_selection_ui(), height=350)
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Cat 😺"): st.session_state.chosen_pet = "Cat"; st.session_state.page = "Home"; st.rerun()
    with col2:
        if st.button("Dog 🐶"): st.session_state.chosen_pet = "Dog"; st.session_state.page = "Home"; st.rerun()
    with col3:
        if st.button("Bunny 🐰"): st.session_state.chosen_pet = "Bunny"; st.session_state.page = "Home"; st.rerun()

# 页面 C: 主系统 (带导航栏)
else:
    # 顶部标题栏
    ui.render_header(st.session_state.page)

    if st.session_state.page == "Home":
        ui.render_stitch_component(ui.get_dashboard_ui(st.session_state.energy, st.session_state.chosen_pet), height=400)
        # 快速记录按钮
        with st.expander("📝 Quick Energy Log"):
            event = st.text_input("What happened?")
            impact = st.slider("Impact", -100, 100, 0)
            if st.button("Record"):
                st.session_state.energy = max(0, min(100, st.session_state.energy + impact))
                st.toast("Logged!")
                st.rerun()

    elif st.session_state.page == "Calendar":
        ui.render_stitch_component(ui.get_calendar_ui(), height=650)

    elif st.session_state.page == "SocialSync":
        # 好友列表逻辑
        if not st.session_state.friends:
            ui.render_stitch_component(ui.get_empty_sync_ui(), height=300)
        else:
            for friend in st.session_state.friends:
                ui.render_stitch_component(ui.get_friend_card_ui(friend['email'], friend['energy']), height=100)
        
        # 添加好友 "+" 号
        with st.expander("➕ Add New Friend"):
            f_email = st.text_input("Friend's Email")
            if st.button("Send Invite"):
                st.session_state.friends.append({"email": f_email, "energy": 75})
                st.success(f"Added {f_email}!")
                st.rerun()

    # 固定底部导航栏
    st.write("---")
    nav1, nav2, nav3 = st.columns(3)
    with nav1:
        if st.button("🏠 Home"): st.session_state.page = "Home"; st.rerun()
    with nav2:
        if st.button("📅 Calendar"): st.session_state.page = "Calendar"; st.rerun()
    with nav3:
        if st.button("👥 Sync"): st.session_state.page = "SocialSync"; st.rerun()
