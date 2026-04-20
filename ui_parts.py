# ui_parts.py
import streamlit as st
import streamlit.components.v1 as components

def inject_stitch_style():
    """注入 Stitch 的全局样式和字体"""
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
        .block-container { padding-top: 1rem; padding-bottom: 5rem; }
    </style>
    """, unsafe_allow_html=True)

def render_stitch_component(html_content, height=600):
    """通用的 Tailwind HTML 渲染器"""
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
    """对应 app.py 中的 render_header"""
    st.markdown(f"""
    <div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 0; margin-bottom: 20px;">
        <div>
            <p style="font-size: 10px; font-weight: 800; color: #006c53; text-transform: uppercase; margin: 0;">Social Battery</p>
            <h1 style="font-size: 24px; font-weight: 800; color: #2b3433; margin: 0;">{title}</h1>
        </div>
        <div style="width: 48px; height: 48px; background: #8ff6d0; border-radius: 50%; display: flex; align-items: center; justify-content: center; border: 2px solid white; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
            <span class="material-symbols-outlined" style="color: #006c53;">pets</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_bottom_nav():
    """对应 app.py 中的 render_bottom_nav"""
    # 在 Streamlit 中，底部导航通常通过 st.columns 配合 CSS 固定定位实现
    st.markdown("""
    <div style="position: fixed; bottom: 0; left: 0; width: 100%; background: rgba(255,255,255,0.6); 
                backdrop-filter: blur(20px); display: flex; justify-content: space-around; 
                padding: 15px 0 30px 0; border-top-left-radius: 2.5rem; border-top-right-radius: 2.5rem;
                box-shadow: 0 -10px 30px rgba(43,52,51,0.05); z-index: 100;">
    </div>
    """, unsafe_allow_html=True)

# --- 具体的页面 HTML 片段 ---
def get_dashboard_ui():
    return """
    <div class="bg-white/60 backdrop-blur-xl rounded-[2.5rem] p-8 shadow-sm mb-6 relative overflow-hidden">
        <span class="bg-emerald-100 text-emerald-700 text-[10px] font-black px-3 py-1 rounded-full uppercase">Mochi is Resting</span>
        <h2 class="text-4xl font-bold mt-4 mb-2 text-[#2b3433]">85%</h2>
        <p class="text-gray-500 text-sm">Your battery is looking healthy!</p>
    </div>
    """