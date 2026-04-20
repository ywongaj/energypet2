# ui_parts.py
import streamlit as st
import streamlit.components.v1 as components

def inject_stitch_style():
    """注入 Stitch 设计系统的视觉灵魂"""
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
        
        /* 隐藏 Streamlit 装饰 */
        #MainMenu, footer, header {visibility: hidden;}
        
        /* 全局背景与字体 */
        .stApp { 
            background: linear-gradient(180deg, #f6faf8 0%, #e1eae7 100%);
            font-family: 'Plus Jakarta Sans', sans-serif; 
        }
        
        /* 美化输入框：Stitch 'No Border' 规则 */
        .stTextInput input, .stNumberInput input {
            background-color: #e1eae7 !important;
            border: none !important;
            border-radius: 1.5rem !important;
            padding: 12px 20px !important;
            color: #2b3433 !important;
            font-weight: 600;
        }

        /* 美化按钮：Marshmallow Mint 梯度 */
        .stButton button {
            background: #006c53 !important;
            color: white !important;
            border-radius: 2.5rem !important;
            border: none !important;
            font-weight: 800 !important;
            padding: 0.75rem 2rem !important;
            transition: all 0.2s ease;
        }
        .stButton button:hover {
            transform: scale(0.98);
            box-shadow: 0 4px 15px rgba(0, 108, 83, 0.2);
        }
    </style>
    """, unsafe_allow_html=True)

def render_stitch_component(html_content, height=600):
    """HTML 渲染容器"""
    full_code = f'''
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1" rel="stylesheet"/>
    <body class="bg-transparent m-0 p-0 font-['Plus_Jakarta_Sans'] overflow-hidden">
        {html_content}
    </body>
    '''
    components.html(full_code, height=height, scrolling=False)

def render_header(title):
    st.markdown(f'''
    <div style="display: flex; justify-content: space-between; align-items: center; padding: 15px 0;">
        <h2 style="font-weight: 800; color: #2b3433; margin: 0; font-size: 1.5rem;">{title}</h2>
        <div style="width: 45px; height: 45px; background: #8ff6d0; border-radius: 50%; display: flex; align-items: center; justify-content: center; border: 2px solid white; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
            <span class="material-symbols-outlined" style="color: #006c53;">pets</span>
        </div>
    </div>
    ''', unsafe_allow_html=True)

# --- 模块化 UI 片段 ---

def get_onboarding_ui():
    return '''
    <div class="text-center pt-16">
        <div class="w-32 h-32 bg-[#8ff6d0] rounded-full mx-auto mb-8 flex items-center justify-center text-6xl shadow-xl border-4 border-white">😸</div>
        <h1 class="text-4xl font-extrabold text-[#2b3433] tracking-tight">Hello, Guardian</h1>
        <p class="text-[#57615f] mt-4 px-12 leading-relaxed">Let's balance your social energy and grow with your companion.</p>
    </div>
    '''

def get_dashboard_ui(energy):
    # 表情联动逻辑
    mood = "😸" if energy >= 70 else "😐" if energy >= 30 else "😿"
    status_text = "Resting" if energy >= 70 else "Need Space" if energy >= 30 else "Exhausted"
    
    return f'''
    <div class="bg-white/60 backdrop-blur-3xl rounded-[3rem] p-10 border border-white/20 shadow-sm relative overflow-hidden">
        <div class="flex justify-between items-start">
            <div>
                <span class="bg-[#006c53]/10 text-[#006c53] text-[10px] font-black px-3 py-1 rounded-full uppercase tracking-widest">{status_text}</span>
                <h2 class="text-7xl font-bold text-[#2b3433] mt-4">{int(energy)}%</h2>
            </div>
            <div class="text-7xl drop-shadow-sm">{mood}</div>
        </div>
        <div class="mt-8 h-3 bg-gray-200/50 rounded-full overflow-hidden">
            <div class="bg-[#006c53] h-full transition-all duration-700" style="width: {energy}%"></div>
        </div>
    </div>
    '''

def render_bottom_nav():
    st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)
