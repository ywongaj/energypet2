
# ui_parts.py
import streamlit as st
import streamlit.components.v1 as components

def inject_stitch_style():
    """
    注入 Stitch 的 'Marshmallow Mint' 全局样式。
    包含：自定义字体、禁止滚动条显示、以及全局背景梯度。
    """
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
        
        /* 隐藏 Streamlit 默认的装饰元素 */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* 全局背景：根据 DESIGN.md 采用 Mint Growth 梯度 */
        .stApp {
            background: linear-gradient(180deg, #f6faf8 0%, #e1eae7 100%);
            font-family: 'Plus Jakarta Sans', sans-serif;
        }

        /* 移除组件之间的默认边距，实现 Stitch 的紧凑感 */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 5rem;
        }
    </style>
    """, unsafe_allow_html=True)

def render_stitch_component(html_content, height=600):
    """
    这是一个万能包装器。它把 Stitch 的 HTML 代码放入一个 iframe 中，
    并自动加载 Tailwind CSS 以确保样式生效。
    """
    full_code = f"""
    <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1" rel="stylesheet"/>
    
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        'primary': '#006c53',
                        'primary-container': '#8ff6d0',
                        'secondary': '#6a5f35',
                        'on-surface': '#2b3433',
                        'surface-variant': '#57615f'
                    }}
                }}
            }}
        }}
    </script>

    <body class="bg-transparent m-0 p-0 font-['Plus_Jakarta_Sans']">
        {html_content}
    </body>
    """
    components.html(full_code, height=height, scrolling=False)

# --- 以下是各个页面的具体 HTML 片段（基于你上传的 code.html） ---

def get_dashboard_ui():
    """返回 Dashboard 页面的 HTML 内容"""
    # 这里我精简了你 zip 包里 dashboard/code.html 的核心部分
    return """
    <div class="p-6">
        <header class="flex justify-between items-center mb-8">
            <div>
                <p class="text-xs font-bold text-primary uppercase tracking-widest">Good Morning</p>
                <h1 class="text-2xl font-extrabold text-on-surface">Guardian Lily</h1>
            </div>
            <div class="w-12 h-12 bg-primary-container rounded-full flex items-center justify-center border-2 border-white shadow-sm">
                <span class="material-symbols-outlined text-primary">pets</span>
            </div>
        </header>

        <div class="bg-white/60 backdrop-blur-xl rounded-[2.5rem] p-8 shadow-sm mb-6 relative overflow-hidden">
            <div class="relative z-10">
                <span class="bg-primary/10 text-primary text-[10px] font-black px-3 py-1 rounded-full uppercase">Mochi is Resting</span>
                <h2 class="text-3xl font-bold mt-4 mb-2 text-on-surface">85%</h2>
                <p class="text-surface-variant text-sm">Social Battery level is optimal</p>
            </div>
            <div class="absolute -right-10 -top-10 w-40 h-40 bg-primary-container/30 rounded-full blur-3xl"></div>
        </div>

        <div class="grid grid-cols-2 gap-4">
            <div class="bg-primary-container/20 p-6 rounded-[2rem] text-center">
                <span class="material-symbols-outlined text-primary mb-2">add_circle</span>
                <p class="text-xs font-bold text-primary">Log Interaction</p>
            </div>
            <div class="bg-secondary/10 p-6 rounded-[2rem] text-center">
                <span class="material-symbols-outlined text-secondary mb-2">auto_awesome</span>
                <p class="text-xs font-bold text-secondary">View Insights</p>
            </div>
        </div>
    </div>
    """

def get_log_ui():
    """返回 Energy Log 页面的 HTML 内容"""
    return """
    <div class="p-6">
        <h2 class="text-xl font-bold text-on-surface mb-6">Recent Interactions</h2>
        <div class="space-y-4">
            <div class="flex items-center gap-4 bg-white/40 p-4 rounded-2xl">
                <div class="w-10 h-10 bg-red-100 rounded-full flex items-center justify-center text-red-600">
                    <span class="material-symbols-outlined text-sm">trending_down</span>
                </div>
                <div class="flex-1">
                    <p class="text-sm font-bold text-on-surface">Team Meeting</p>
                    <p class="text-xs text-surface-variant">2 hours ago</p>
                </div>
                <p class="text-sm font-black text-red-600">-15%</p>
            </div>
        </div>
    </div>
    """