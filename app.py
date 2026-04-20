import streamlit as st
import ui_parts as ui

# --- 1. 基础配置与初始化 ---
st.set_page_config(page_title="Guardian", page_icon="🐾", layout="centered")
ui.inject_stitch_style()

# 初始化全局数据
if 'energy' not in st.session_state:
    st.session_state.energy = 100
if 'page' not in st.session_state:
    st.session_state.page = "Register"
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""
if 'pet_name' not in st.session_state:
    st.session_state.pet_name = ""
if 'registered_users' not in st.session_state:
    # 模拟用户数据库，包含用户名以供社交搜索
    st.session_state.registered_users = ["Lily", "Alpha", "Guardian_Master"] 
if 'friends' not in st.session_state:
    st.session_state.friends = []

# --- 2. 页面路由 ---

# 页面 A: 注册 (用户名 & 宠物名)
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

# 页面 B: 选择宠物种类
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
        # 传递电量和宠物类型，UI 会根据电量自动换脸
        ui.render_stitch_component(ui.get_dashboard_ui(st.session_state.energy, st.session_state.chosen_pet, st.session_state.pet_name), height=400)
        
        st.markdown(f"### Record {st.session_state.pet_name}'s Energy")
        with st.container():
            event = st.text_input("What happened?", placeholder="Client meeting, Afternoon tea...")
            
            # 实现输入框与滑块的强绑定
            col_s, col_n = st.columns([3, 1])
            with col_s:
                # 滑块绑定到 session_state.energy_val
                v_slider = st.slider("Impact", -100, 100, 0, key="v_slider", label_visibility="collapsed")
            with col_n:
                # 数字框也绑定到同一个值，实现“动一个，另一个也动”
                v_num = st.number_input("Val", -100, 100, value=v_slider, key="v_num", label_visibility="collapsed")
            
            # 最终取值
            final_impact = v_num

            if st.button("Log Event ✨", use_container_width=True):
                new_energy = st.session_state.energy + final_impact
                if new_energy <= 0:
                    st.error(f"⚠️ CRITICAL: {st.session_state.pet_name} is exhausted! Please rest.")
                    st.session_state.energy = 0
                else:
                    st.session_state.energy = min(100, new_energy)
                    st.success(f"Logged: {event}")
                st.rerun()

    elif st.session_state.page == "Calendar":
        ui.render_stitch_component(ui.get_calendar_ui(), height=650)

    elif st.session_state.page == "SocialSync":
        if not st.session_state.friends:
            ui.render_stitch_component(ui.get_empty_sync_ui(), height=300)
        else:
            for friend in st.session_state.friends:
                ui.render_stitch_component(ui.get_friend_card_ui(friend['name'], friend['energy']), height=100)
        
        with st.expander("➕ Add Friend by Name"):
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

    # 底部固定导航
    st.write("---")
    nav1, nav2, nav3 = st.columns(3)
    with nav1:
        if st.button("🏠 Home"): st.session_state.page = "Home"; st.rerun()
    with nav2:
        if st.button("📅 Calendar"): st.session_state.page = "Calendar"; st.rerun()
    with nav3:
        if st.button("👥 Sync"): st.session_state.page = "SocialSync"; st.rerun()
