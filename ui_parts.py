# ui_parts.py 核心修改点

def get_pet_selection_ui(pet_name):
    return f'''
    <div class="bg-white/40 p-8 rounded-[3rem] text-center">
        <p class="text-sm font-bold text-emerald-800 uppercase mb-4">Choose a Guardian for {pet_name}</p>
        <div class="flex justify-around text-5xl">
            <span>😺</span><span>🐶</span><span>🐰</span>
        </div>
    </div>
    '''

def get_dashboard_ui(energy, pet_type, pet_name):
    # 表情联动逻辑：根据电量切换 Emoji
    if energy > 70:
        moods = {"Cat": "😸", "Dog": "🐶", "Bunny": "🐰"}
        status = "Feeling Great"
    elif energy >= 40:
        moods = {"Cat": "😐", "Dog": "🦮", "Bunny": "🤔"}
        status = "Getting Tired"
    else:
        moods = {"Cat": "😿", "Dog": "🐕‍🦺", "Bunny": "😞"}
        status = "Needs Rest"
    
    icon = moods.get(pet_type, "😺")
    
    return f'''
    <div class="bg-white/60 backdrop-blur-3xl rounded-[3rem] p-10 border border-white/20 shadow-sm relative">
        <div class="flex justify-between items-start">
            <div>
                <span class="bg-[#006c53]/10 text-[#006c53] text-[10px] font-black px-3 py-1 rounded-full uppercase tracking-widest">{status}</span>
                <h2 class="text-7xl font-bold text-[#2b3433] mt-4">{int(energy)}%</h2>
                <p class="text-xs text-gray-400 mt-2 font-bold">{pet_name} is watching over you</p>
            </div>
            <div class="text-7xl transition-all duration-500">{icon}</div>
        </div>
        <div class="mt-8 h-3 bg-gray-200/50 rounded-full overflow-hidden">
            <div class="bg-[#006c53] h-full transition-all duration-700" style="width: {energy}%"></div>
        </div>
    </div>
    '''
