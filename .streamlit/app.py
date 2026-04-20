
import streamlit as st
from ui_parts import inject_stitch_style, render_header, render_bottom_nav

# 页面基本设置
st.set_page_config(page_title="Social Battery", layout="centered")
inject_stitch_style() # 注入 Stitch 的全局样式

# --- 路由逻辑 (Routing) ---
# 模拟页面切换
if 'page' not in st.session_state:
    st.session_state.page = "Dashboard"

# --- 页面函数定义 ---

def show_onboarding():
    """复现 Stitch 的 Onboarding 页面"""
    st.markdown('<div style="text-align: center; padding: 40px 0;">', unsafe_allow_html=True)
    st.image("https://lh3.googleusercontent.com/aida-public/AB6AXuAnyoG_2wBz3As43gXd6xdJpky9mbtFGK3XwrXhpufSTnqfaVMrZpfLY_7ZFfTkrClEOvDcd8JUvMP7yOas2MeW6Ou67e6RMgY09YETAMpSTSPQnT8gjuWSyDsYYivAfBo85D70Hucr3w2BAd82yl6P0HLEK32TjgVsekkKSrtq55eq8EgbJpNouWBHFzRzDIWnOry7-To1QN6ruksKsOonISgBavJGfJDxEYXeDlsidr42oPZUUX4ptlqRmV-SKm2pvAyhwtNhXRI", width=150) # 替换为你的宠物图
    st.markdown("## Welcome, Guardian")
    st.markdown("<p style='color: #57615f;'>Your journey to social mindfulness starts here.</p>", unsafe_allow_html=True)
    if st.button("Begin Journey", use_container_width=True):
        st.session_state.page = "Dashboard"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

def show_dashboard():
    """复现 Stitch 的 Dashboard (Guardian) 页面"""
    render_header()
    # 宠物状态卡片 (Marshmallow Mint Style)
    st.markdown(f"""
    <div class="glass-card">
        <div style="display: flex; align-items: center; gap: 20px;">
            <span style="font-size: 50px;">😸</span>
            <div>
                <h3 style="margin: 0;">Mochi is sleeping</h3>
                <p style="font-size: 12px; color: #006c53; font-weight: 800;">RECHARGING...</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 电量显示
    st.write("### Your Battery")
    st.progress(85)

def show_energy_log():
    """复现 Stitch 的 Energy Log 页面"""
    render_header("Energy Log")
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    activity = st.text_input("What happened?", placeholder="Long meeting...")
    impact = st.slider("Battery Impact", -50, 50, 0)
    if st.button("Save Entry", use_container_width=True):
        st.success("Logged!")
    st.markdown('</div>', unsafe_allow_html=True)

# --- 页面渲染控制器 ---
if st.session_state.page == "Onboarding":
    show_onboarding()
elif st.session_state.page == "Dashboard":
    show_dashboard()
elif st.session_state.page == "Log":
    show_energy_log()

# --- 注入底部导航 ---
# 我们在底栏加几个隐藏的按钮来切换页面
st.markdown("<br><br><br>", unsafe_allow_html=True) # 留出空间
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🐾 Home"): st.session_state.page = "Dashboard"; st.rerun()
with col2:
    if st.button("📈 Log"): st.session_state.page = "Log"; st.rerun()
with col3:
    if st.button("✨ Reset"): st.session_state.page = "Onboarding"; st.rerun()