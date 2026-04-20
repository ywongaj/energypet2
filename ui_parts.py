# ui_parts.py
import streamlit as st
import streamlit.components.v1 as components

def inject_stitch_style():
    """注入 Stitch 的 Marshmallow Mint 设计系统样式"""
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
        .block-container { padding: 1rem; }
    </style>
    """, unsafe_allow_html=True)

def render_stitch_component(html_content, height=600):
    """通用的 Tailwind HTML 渲染器"""
    full_code = f'''
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1" rel="stylesheet"/>
    <body class="bg-transparent m-0 p-0 font-['Plus_Jakarta_Sans']">
        {html_content}
    </body>
    '''
    components.html(full_code, height=height, scrolling=False)

def render_header(title="Guardian"):
    st.markdown(f"""
    <div style="display: flex; justify-content: space-between; align-items: center; padding: 15px 0;">
        <h2 style="font-size: 20px; font-weight: 800; color: #2b3433; margin: 0;">{title}</h2>
        <div style="width: 40px; height: 40px; background: #8ff6d0; border-radius: 50%; display: flex; align-items: center; justify-content: center; border: 2px solid white;">
            <span class="material-symbols-outlined" style="color: #006c53;">pets</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- 具体的页面 HTML 片段 (基于 Stitch 源码) ---

def get_onboarding_ui():
    """复现 onboarding/code.html"""
    return """
    <div class="flex flex-col items-center justify-center p-8 text-center">
        <div class="w-24 h-24 bg-emerald-100 rounded-full mb-6 flex items-center justify-center text-4xl">😺</div>
        <h1 class="text-3xl font-extrabold text-[#2b3433] mb-4">Hello, Guardian</h1>
        <div class="bg-white/40 p-6 rounded-[2rem] border border-white/20 mb-8">
            <p class="text-sm text-gray-600">Ready to track your energy and care for your digital companion?</p>
        </div>
    </div>
    """

def get_dashboard_ui():
    """复现 dashboard/code.html"""
    return """
    <div class="bg-white/60 backdrop-blur-xl rounded-[2.5rem] p-8 shadow-sm border border-white/20 relative overflow-hidden">
        <span class="bg-emerald-100 text-emerald-700 text-[10px] font-black px-3 py-1 rounded-full uppercase">Battery Level</span>
        <h2 class="text-5xl font-bold text-[#2b3433] mt-4">85%</h2>
        <p class="text-gray-500 text-sm mt-2 italic">Mochi is feeling peaceful.</p>
    </div>
    """

def get_log_ui():
    """复现 energy_log/code.html"""
    return """
    <div class="space-y-4">
        <div class="bg-white/40 p-5 rounded-3xl border border-white/20 flex justify-between items-center">
            <div class="flex items-center gap-3">
                <span class="material-symbols-outlined text-red-400">group</span>
                <div><p class="font-bold text-[#2b3433]">Social Event</p><p class="text-[10px] text-gray-400">Today</p></div>
            </div>
            <span class="text-red-500 font-bold">-15%</span>
        </div>
    </div>
    """

def render_bottom_nav():
    st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)
