import streamlit as st
import streamlit.components.v1 as components

# ... (保留你之前的 inject_stitch_style 和 render_stitch_component) ...

def get_onboarding_ui():
    """Stitch 的 Onboarding 页面逻辑"""
    return """
    <div class="text-center p-8">
        <div class="w-24 h-24 bg-[#8ff6d0] rounded-full mx-auto mb-6 flex items-center justify-center text-4xl">😺</div>
        <h2 class="text-2xl font-extrabold text-[#2b3433] mb-4">Hello, Lily</h2>
        <div class="bg-white/40 p-6 rounded-[2rem] text-left mb-6 border border-white/20">
            <p class="text-sm text-[#57615f]">Ready to track your energy and care for your Guardian?</p>
        </div>
    </div>
    """

def get_dashboard_ui():
    """主页卡片样式"""
    return """
    <div class="bg-white/60 backdrop-blur-xl rounded-[2.5rem] p-8 shadow-sm border border-white/20 relative overflow-hidden">
        <div class="flex justify-between items-start">
            <div>
                <span class="bg-emerald-100 text-emerald-700 text-[10px] font-black px-3 py-1 rounded-full uppercase">Resting</span>
                <h2 class="text-5xl font-bold text-[#2b3433] mt-4">85%</h2>
            </div>
            <div class="text-6xl">🐈</div>
        </div>
        <p class="text-gray-500 text-sm mt-4 italic">"Mochi feels peaceful in this environment."</p>
    </div>
    """

def get_log_ui():
    """日志列表样式"""
    return """
    <div class="space-y-4">
        <div class="bg-white/40 p-5 rounded-3xl border border-white/20 flex justify-between items-center">
            <div class="flex items-center gap-3">
                <span class="material-symbols-outlined text-red-400">group</span>
                <div><p class="font-bold text-[#2b3433]">Meeting</p><p class="text-[10px] text-gray-400">2:00 PM</p></div>
            </div>
            <span class="text-red-500 font-bold">-20%</span>
        </div>
    </div>
    """

def get_sync_ui():
    """同步页面样式"""
    return """
    <div class="p-6 text-center">
        <div class="bg-primary-container/20 p-10 rounded-[3rem] border-2 border-dashed border-primary/20">
            <span class="material-symbols-outlined text-4xl text-primary animate-pulse">sync</span>
            <p class="mt-4 font-bold text-primary">Scanning Calendar...</p>
        </div>
    </div>
    """
