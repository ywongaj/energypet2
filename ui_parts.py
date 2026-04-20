# ui_parts.py
import streamlit as st
import streamlit.components.v1 as components

def inject_stitch_style():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stApp { background: #f6faf8; font-family: 'Plus Jakarta Sans', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

def render_stitch_component(html_content, height=700):
    """将 Stitch 的完整 HTML 注入 Streamlit"""
    full_code = f'''
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1" rel="stylesheet"/>
    <body class="bg-transparent m-0 p-0 font-['Plus_Jakarta_Sans'] overflow-hidden">
        {html_content}
    </body>
    '''
    components.html(full_code, height=height, scrolling=True)

# --- 从 Stitch 的 code.html 中提取的片段 ---

def get_onboarding_ui():
    return """
    <div class="min-h-screen bg-gradient-to-b from-[#f6faf8] to-[#e1eae7] p-8 flex flex-col items-center">
        <div class="mt-20 w-32 h-32 bg-[#8ff6d0] rounded-full flex items-center justify-center text-6xl shadow-inner">😸</div>
        <h1 class="text-4xl font-extrabold text-[#2b3433] mt-8">Hello, Guardian</h1>
        <p class="text-[#57615f] mt-4 text-center max-w-xs">Ready to track your energy and care for your companion?</p>
    </div>
    """

def get_dashboard_ui(energy=85):
    return f"""
    <div class="p-6">
        <div class="bg-white/60 backdrop-blur-2xl rounded-[3rem] p-10 border border-white/20 shadow-sm relative overflow-hidden">
            <div class="relative z-10">
                <span class="bg-[#006c53]/10 text-[#006c53] text-[10px] font-black px-3 py-1 rounded-full uppercase">Resting</span>
                <h2 class="text-6xl font-bold text-[#2b3433] mt-4">{energy}%</h2>
                <p class="text-[#57615f] text-sm mt-2">Mochi is feeling peaceful in this space.</p>
            </div>
            <div class="absolute -right-4 -bottom-4 text-8xl opacity-20">🐈</div>
        </div>
    </div>
    """

def get_log_ui():
    return """
    <div class="p-6 space-y-4">
        <h3 class="font-bold text-[#2b3433] text-xl px-2">Recent Logs</h3>
        <div class="bg-white/40 p-5 rounded-[2rem] border border-white/20 flex justify-between items-center">
            <div class="flex items-center gap-4">
                <div class="w-10 h-10 bg-red-100 rounded-full flex items-center justify-center text-red-500">
                    <span class="material-symbols-outlined">group</span>
                </div>
                <div><p class="font-bold text-[#2b3433]">Work Meeting</p><p class="text-[10px] text-gray-400">2h ago</p></div>
            </div>
            <span class="text-red-500 font-black">-15%</span>
        </div>
    </div>
    """

def get_sync_ui():
    return """
    <div class="p-6">
        <div class="bg-[#006c53] rounded-[3rem] p-10 text-white shadow-xl">
            <span class="material-symbols-outlined text-4xl animate-spin">sync</span>
            <h2 class="text-2xl font-bold mt-4">Social Sync</h2>
            <p class="text-emerald-100/70 text-sm mt-2">Connecting to your calendar to predict energy drains...</p>
        </div>
    </div>
    """
