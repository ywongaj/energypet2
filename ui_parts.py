# ui_parts.py 关键新增部分

def get_register_ui():
    return '''
    <div class="text-center pt-10">
        <div class="w-20 h-20 bg-[#8ff6d0] rounded-3xl mx-auto mb-6 flex items-center justify-center text-4xl shadow-lg">🛡️</div>
        <h1 class="text-3xl font-extrabold text-[#2b3433]">Create Account</h1>
        <p class="text-[#57615f] mt-2 px-10 text-sm">Join the sanctuary to protect your social energy.</p>
    </div>
    '''

def get_pet_selection_ui():
    return '''
    <div class="p-6 text-center">
        <div class="bg-white/40 p-6 rounded-[2.5rem] border border-white/20">
            <p class="text-[#57615f] text-sm mb-4">Tap a guardian to bond with them</p>
            <div class="flex justify-around text-4xl">
                <span>😺</span><span>🐶</span><span>🐰</span>
            </div>
        </div>
    </div>
    '''

def get_empty_sync_ui():
    return '''
    <div class="p-10 text-center">
        <div class="w-16 h-16 bg-gray-100 rounded-full mx-auto mb-4 flex items-center justify-center">
            <span class="material-symbols-outlined text-gray-400">person_add</span>
        </div>
        <h3 class="font-bold text-[#2b3433]">No Friends Yet</h3>
        <p class="text-xs text-gray-400 mt-2">Connect with others to see their energy levels.</p>
    </div>
    '''

def get_friend_card_ui(email, energy):
    color = "emerald-500" if energy > 50 else "orange-400"
    return f'''
    <div class="bg-white/60 backdrop-blur-xl p-4 rounded-3xl border border-white/20 flex items-center justify-between mb-2">
        <div class="flex items-center gap-3">
            <div class="w-10 h-10 bg-[#8ff6d0] rounded-full flex items-center justify-center text-xl">😺</div>
            <div>
                <p class="text-xs font-bold text-[#2b3433]">{email}</p>
                <p class="text-[10px] text-gray-400 uppercase tracking-tighter">Connected</p>
            </div>
        </div>
        <div class="text-right">
            <p class="text-sm font-black text-{color}">{energy}%</p>
            <div class="w-12 h-1 bg-gray-100 rounded-full mt-1">
                <div class="bg-{color} h-full" style="width: {energy}%"></div>
            </div>
        </div>
    </div>
    '''

# 更新后的 Dashboard 增加宠物显示
def get_dashboard_ui(energy, pet_type):
    icons = {"Cat": "😺", "Dog": "🐶", "Bunny": "🐰"}
    pet_icon = icons.get(pet_type, "😺")
    return f'''
    <div class="bg-white/60 backdrop-blur-3xl rounded-[3rem] p-10 border border-white/20 shadow-sm relative overflow-hidden">
        <div class="flex justify-between items-start">
            <div>
                <span class="bg-[#006c53]/10 text-[#006c53] text-[10px] font-black px-3 py-1 rounded-full uppercase tracking-widest">Guardian Active</span>
                <h2 class="text-7xl font-bold text-[#2b3433] mt-4">{int(energy)}%</h2>
            </div>
            <div class="text-7xl">{pet_icon}</div>
        </div>
        <div class="mt-8 h-3 bg-gray-200/50 rounded-full overflow-hidden">
            <div class="bg-[#006c53] h-full transition-all duration-700" style="width: {energy}%"></div>
        </div>
    </div>
    '''
