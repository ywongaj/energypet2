import streamlit as st
import ui_parts as ui

# --- 1. 基础配置与初始化 ---
st.set_page_config(page_title="Guardian", page_icon="🐾", layout="centered")
ui.inject_stitch_style()

# 确保数据持久化，只在初次运行时设置
if 'energy' not in st.session_state:
    st.session_state.energy = 100
if 'page' not in st.session_state:
    st.session_state.page = "Register"
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""
if 'pet_name' not in st.session_state:
    st.session_state.pet_name = ""
if 'registered_users' not in st.session_state:
    st.session_state.registered_users = ["Lily", "Alpha", "Guardian_Master"] 
if 'friends' not in st.session_state:
    st.session_state.friends = []

# --- 2. 页面路由逻辑 ---

# 页面 A: 注册 (用户名 & 宠物命名)
if st.session_state.page == "Register":
    ui.render_stitch_component(ui.get_register_ui(), height=450)
    u_name = st.text_input("Your Name", placeholder="e.g., Lily")
    p_name = st.text_input("Name your Guardian", placeholder="e.g., Mochi")
    
    if st.button("Begin Journey ✨", use_container_width=True):
        if u_name and p_name:
            st.session_state.user_name = u_name
            st.session_state.pet_name = p_name
            if u_name not in st.session_state.registered_users:
                st.session_state.registered_users.append(u_name)
            st.session_state.page = "ChoosePet"
            st.rerun()
        else:
            st.warning("Please tell us both names!")

# 页面 B: 挑选宠物种类
elif st.session_state.page == "ChoosePet":
    ui.render_header(f"Welcome, {st.session_state.user_name}")
    ui.render_stitch_component(ui.get_pet_selection_ui(st.session_state.pet_name), height=350)
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Cat 😺"): st.session_state.chosen_pet = "Cat"; st.session_state.page = "Home"; st.rerun()
    with col2:
        if st.button("Dog 🐶"): st.session_state.chosen_pet = "Dog"; st.session_state.page = "Home"; st.rerun()
    with col3:
        if st.button("Bunny 🐰"): st.session_state.chosen_pet = "Bunny"; st.session_state.page = "Home"; st.rerun()

# 页面 C: 主系统
else:
    ui.render_header(f"{st.session_state.page}")

    if st.session_state.page == "Home":
        ui.render_stitch_component(ui.get_dashboard_ui(st.session_state.energy, st.session_state.chosen_pet, st.session_state.pet_name), height=400)
        
        st.markdown(f"### Record {st.session_state.pet_name}'s Energy")
        
        # 强绑定输入框与滑动条
        # 使用 session_state 来存储临时数值，确保两者同步
        if 'impact_val' not in st.session_state:
            st.session_state.impact_val = 0

        event = st.text_input("What happened?", placeholder="Client meeting, Afternoon tea...")
        
        col_s, col_n = st.columns([3, 1])
        with col_s:
            v_slider = st.slider("Impact", -100, 100, st.session_state.impact_val, key="v_slider", label_visibility="collapsed")
        with col_n:
            v_num = st.number_input("Val", -100, 100, value=v_slider, key="v_num", label_visibility="collapsed")
        
        # 实时更新同步值
        st.session_state.impact_val = v_num

        if st.button("Log Event ✨", use_container_width=True):
            new_energy = st.session_state.energy + st.session_state.impact_val
            if new_energy <= 0:
                st.error(f"⚠️ CRITICAL ERROR: {st.session_state.pet_name} is exhausted! Please rest.")
                st.session_state.energy = 0
            else:
                st.session_state.energy = min(100, new_energy)
                st.success(f"Logged: {event}")
                st.session_state.impact_val = 0 # 重置
            st.rerun()

    elif st.session_state.page == "Calendar":
        ui.render_stitch_component(ui.get_calendar_ui(), height=650)

    elif st.session_state.page == "SocialSync":
        if not st.session_state.friends:
            ui.render_stitch_component(ui.get_empty_sync_ui(), height=300)
        else:
            for friend in st.session_state.friends:
                ui.render_stitch_component(ui.get_friend_card_ui(friend['name'], friend['energy']), height=100)
        
        with st.expander("➕ Add Friend"):
            f_name = st.text_input("Enter friend's user name")
            if st.button("Find User"):
                if f_name in st.session_state.registered_users:
                    if f_name not in [f['name'] for f in st.session_state.friends]:
                        st.session_state.friends.append({"name": f_name, "energy": 65})
                        st.success(f"Found {f_name}!")
                    else:
                        st.info("Already in your list.")
                else:
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
