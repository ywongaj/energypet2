import streamlit as st
import ui_parts as ui

# --- 1. 基础配置与初始化 ---
st.set_page_config(page_title="Guardian", page_icon="🐾", layout="centered")
ui.inject_stitch_style()

# 核心：只在第一次运行且不在 session_state 时初始化
if 'energy' not in st.session_state:
    st.session_state.energy = 100
if 'page' not in st.session_state:
    st.session_state.page = "Register"
if 'registered_emails' not in st.session_state:
    # 模拟已注册的数据库，用来测试“找不到用户”的功能
    st.session_state.registered_emails = ["test@gmail.com", "lily@bank.com"] 
if 'friends' not in st.session_state:
    st.session_state.friends = []

# --- 2. 页面路由 ---

# 页面 A: 注册 (将邮箱存入模拟数据库)
if st.session_state.page == "Register":
    ui.render_stitch_component(ui.get_register_ui(), height=400)
    email = st.text_input("Enter Email", placeholder="yourname@example.com")
    if st.button("Continue", use_container_width=True):
        if "@" in email:
            st.session_state.user_email = email
            if email not in st.session_state.registered_emails:
                st.session_state.registered_emails.append(email) # 模拟注册成功
            st.session_state.page = "ChoosePet"
            st.rerun()
        else:
            st.error("Please enter a valid email.")

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

# 页面 C: 主系统
else:
    ui.render_header(st.session_state.page)

    if st.session_state.page == "Home":
        ui.render_stitch_component(ui.get_dashboard_ui(st.session_state.energy, st.session_state.chosen_pet), height=400)
        
        # --- 能量输入区域 (修复消失问题 & 加入 0% 报错) ---
        st.markdown("### Record Energy")
        with st.container():
            event = st.text_input("What happened?", placeholder="Client Meeting...")
            col_s, col_n = st.columns([3, 1])
            with col_s:
                v_slider = st.slider("Impact", -100, 100, 0, key="slider", label_visibility="collapsed")
            with col_n:
                v_num = st.number_input("Val", -100, 100, value=v_slider, key="num", label_visibility="collapsed")
            
            final_impact = v_num if v_num != v_slider else v_slider
            
            if st.button("Log Event ✨", use_container_width=True):
                new_energy = st.session_state.energy + final_impact
                # 校验：如果电量归零或更低，触发错误弹窗
                if new_energy <= 0:
                    st.error("⚠️ CRITICAL ERROR: Your social battery is depleted! Please rest immediately.")
                    st.session_state.energy = 0 # 强制设为 0
                else:
                    st.session_state.energy = min(100, new_energy)
                    st.success(f"Logged: {event}")
                st.rerun()

    elif st.session_state.page == "Calendar":
        ui.render_stitch_component(ui.get_calendar_ui(), height=650)

    elif st.session_state.page == "SocialSync":
        # 好友列表
        if not st.session_state.friends:
            ui.render_stitch_component(ui.get_empty_sync_ui(), height=300)
        else:
            for friend in st.session_state.friends:
                ui.render_stitch_component(ui.get_friend_card_ui(friend['email'], friend['energy']), height=100)
        
        # --- 添加好友 (加入“找不到用户”校验) ---
        with st.expander("➕ Add Friend"):
            f_email = st.text_input("Enter friend's email")
            if st.button("Find User"):
                # 校验：是否在模拟的“注册数据库”中
                if f_email in st.session_state.registered_emails:
                    if f_email not in [f['email'] for f in st.session_state.friends]:
                        st.session_state.friends.append({"email": f_email, "energy": 70})
                        st.success(f"Found {f_email} and added to list!")
                    else:
                        st.info("User already in your list.")
                else:
                    # 弹出你要求的错误信息
                    st.error("Unable to find this user")

    # 底部导航
    st.write("---")
    nav1, nav2, nav3 = st.columns(3)
    with nav1:
        if st.button("🏠 Home"): st.session_state.page = "Home"; st.rerun()
    with nav2:
        if st.button("📅 Calendar"): st.session_state.page = "Calendar"; st.rerun()
    with nav3:
        if st.button("👥 Sync"): st.session_state.page = "SocialSync"; st.rerun()
