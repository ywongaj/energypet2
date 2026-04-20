import streamlit as st
import streamlit.components.v1 as components

def inject_stitch_style():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
        #MainMenu, footer, header {visibility: hidden;}
        .stApp { background: #f6faf8; font-family: 'Plus Jakarta Sans', sans-serif; }
        .stButton button {
            background: #006c53 !important; color: white !important;
            border-radius: 2rem !important; font-weight: 800 !important; border: none !important;
        }
        .stTextInput input {
            background: #e1eae7 !important; border-radius: 1.5rem !important; border: none !important;
        }
    </style>
    """, unsafe_allow_html=True)

def render_stitch_component(html_content, height=500):
    full_code = f'''
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300..800&display=swap" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1" rel="stylesheet"/>
    <body class="bg-transparent m-0 p-0 font-['Plus_Jakarta_Sans'] overflow-hidden">
        {html_content}
    </body>
    '''
    components.html(full_code, height=height)

def render_header(title):
    st.markdown(f'''
    <div style="display: flex; justify-content: space-between; align-items: center; padding-bottom: 20px;">
        <h2 style="font-weight: 800; color: #2b3433; margin: 0;">{title}</h2>
        <div style="width: 40px; height: 40px; background: #8ff6d0; border-radius: 50%; display: flex; align-items: center; justify-content: center; border: 2px solid white;">
            <span class="material-symbols-outlined" style="color: #006c53;">pets</span>
        </div>
    </div>
    ''', unsafe_allow_html=True)

# --- 页面片段 ---

def get_register_ui():
    return '<div class="text-center pt-10"><div class="text-6xl mb-4">🛡️</div><h1 class="text-3xl font-extrabold text-[#2b3433]">Join Sanctuary</h1><p class="text-gray-500">Protect your energy.</p></div>'

def get_pet_selection_ui():
    return '<div class="bg-white/40 p-8 rounded-[3rem] text-center"><p class="text-sm font-bold text-emerald-800 uppercase mb-6">Choose Your Guardian</p><div class="flex justify-around text-5xl"><span>😺</span><span>🐶</span><span>🐰</span></div></div>'

def get_dashboard_ui(energy, pet):
    icons = {"Cat": "😺", "Dog": "🐶", "Bunny": "🐰"}
    icon = icons.get(pet, "😺")
    return f'''
    <div class="bg-white/60 backdrop-blur-3xl rounded-[3rem] p-10 border border-white/20 shadow-sm relative">
        <span class="bg-[#006c53]/10 text-[#006c53] text-[10px] font-black px-3 py-1 rounded-full uppercase">Battery</span>
        <h2 class="text-7xl font-bold text-[#2b3433] mt-4">{energy}%</h2>
        <div class="absolute right-8 top-12 text-7xl">{icon}</div>
        <div class="mt-8 h-3 bg-gray-100 rounded-full overflow-hidden">
            <div class="bg-[#006c53] h-full" style="width: {energy}%"></div>
        </div>
    </div>
    '''

def get_calendar_ui():
    return '''
    <div class="bg-white/60 rounded-[2.5rem] p-6">
        <h3 class="font-extrabold text-xl mb-4">October 2026</h3>
        <div class="grid grid-cols-7 gap-2 text-center text-[10px] text-gray-400 font-bold mb-4">
            <div>M</div><div>T</div><div>W</div><div>T</div><div>F</div><div>S</div><div>S</div>
        </div>
        <div class="grid grid-cols-7 gap-2">
            <div class="w-8 h-8 rounded-full bg-emerald-400 mx-auto"></div>
            <div class="w-8 h-8 rounded-full bg-emerald-200 mx-auto"></div>
            <div class="w-8 h-8 rounded-full bg-orange-400 mx-auto"></div>
            <div class="w-8 h-8 rounded-full bg-emerald-400 mx-auto"></div>
        </div>
    </div>
    '''

def get_empty_sync_ui():
    return '<div class="text-center p-10 bg-white/40 rounded-3xl border-2 border-dashed border-gray-200"><span class="material-symbols-outlined text-4xl text-gray-300">group_add</span><p class="text-gray-400 mt-2">No friends yet.</p></div>'

def get_friend_card_ui(email, energy):
    return f'''
    <div class="bg-white/60 p-4 rounded-3xl flex justify-between items-center mb-2 border border-white/20">
        <div class="flex items-center gap-3"><div class="w-10 h-10 bg-emerald-100 rounded-full flex items-center justify-center">😺</div>
        <p class="text-xs font-bold">{email}</p></div>
        <span class="font-black text-emerald-600">{energy}%</span>
    </div>
    '''
