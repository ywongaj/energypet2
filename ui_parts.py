# ui_parts.py
import streamlit as st
import streamlit.components.v1 as components

def inject_stitch_style():
    """注入全局 CSS 样式"""
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stApp {
            background: linear-gradient(180deg, #f6faf8 0%, #e1eae7 100%);
            font-family: 'Plus Jakarta Sans', sans-serif;
        }
    </style>
    """, unsafe_allow_html=True)

def render_stitch_component(html_content, height=500):
    """渲染 HTML/Tailwind 组件"""
    full_code = f"""
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1" rel="stylesheet"/>
    <body class="bg-transparent m-0 p-0 font-['Plus_Jakarta_Sans']">
        {html_content}
    </body>
    """
    components.html(full_code, height=height, scrolling=False)

def render_header(title="Guardian"):
    """显示页头"""
    st.markdown(f"""
    <div style="display: flex; justify-content: space-between; align-items: center; padding: 20px 0;">
        <h1 style="font-size: 24px; font-weight: 800; color: #2b3433; margin: 0;">{title}</h1>
        <div style="width: 45px; height: 45px; background: #8ff6d0; border-radius: 50%; display: flex; align-items: center; justify-content: center;">
            <span class="material-symbols-outlined" style="color: #006c53;">pets</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

def get_dashboard_ui():
    """首页的 HTML 片段"""
    return """
    <div class="bg-white/60 backdrop-blur-xl rounded-[2.5rem] p-8 shadow-sm border border-white/20">
        <span class="text-[10px] font-black text-emerald-700 uppercase tracking-widest">Battery Level</span>
        <h2 class="text-5xl font-bold text-[#2b3433] mt-2">85%</h2>
        <p class="text-gray-500 text-sm mt-2">Mochi is feeling energetic!</p>
    </div>
    """

def get_log_ui():
    """日志页的 HTML 片段"""
    return """
    <div class="space-y-4">
        <div class="bg-white/40 p-5 rounded-3xl border border-white/20 flex justify-between items-center">
            <div>
                <p class="font-bold text-[#2b3433]">Lunch with Team</p>
                <p class="text-xs text-gray-500">Social Interaction</p>
            </div>
            <span class="text-red-500 font-bold">-15%</span>
        </div>
        <div class="bg-white/40 p-5 rounded-3xl border border-white/20 flex justify-between items-center">
            <div>
                <p class="font-bold text-[#2b3433]">Solo Reading</p>
                <p class="text-xs text-gray-500">Recharging</p>
            </div>
            <span class="text-emerald-600 font-bold">+20%</span>
        </div>
    </div>
    """

def render_bottom_nav():
    """底部导航栏占位（防止遮挡）"""
    st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)
