import streamlit as st
import random
from datetime import datetime, date

# ==========================================
# 1. 系統設定 (第一性原理：零摩擦力啟動)
# ==========================================
st.set_page_config(
    page_title="2026 長濱部落深度旅遊 (大地慢活版)",
    page_icon="⛰️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==========================================
# 2. CSS 美學 (UIUX-CRF v9.0 認知鎖定：大地色系主題)
# ==========================================
st.markdown("""
    <style>
    /* 1. 全站背景為暖沙黃，字體為深咖啡色 */
    .stApp {
        background-color: #F4F1EA;
        font-family: "Microsoft JhengHei", sans-serif;
        color: #4A3F35 !important;
    }
    
    /* 2. 強制所有一般文字元素為深咖啡色 */
    p, div, span, h1, h2, h3, h4, h5, h6, label, .stMarkdown {
        color: #4A3F35 !important;
    }

    /* === 3. 核心修復：強制輸入框與選單在深色模式下維持「白底深字」 === */
    div[data-baseweb="select"] > div, 
    div[data-baseweb="input"] > div, 
    div[data-baseweb="base-input"] {
        background-color: #ffffff !important;
        border: 1px solid #C19A6B !important;
        color: #4A3F35 !important;
    }
    input, div[data-baseweb="select"] span, li[data-baseweb="option"] {
        color: #4A3F35 !important;
    }
    ul[data-baseweb="menu"] { background-color: #ffffff !important; }
    svg { fill: #4A3F35 !important; color: #4A3F35 !important; }

    /* === 4. 特別加強：日期選單高亮 (山林大地風) === */
    div[data-testid="stDateInput"] > label {
        color: #6B4E31 !important; 
        font-size: 24px !important; 
        font-weight: 900 !important;
        text-shadow: 0px 0px 5px rgba(107, 78, 49, 0.2);
        margin-bottom: 10px !important;
        display: block;
    }
    div[data-testid="stDateInput"] div[data-baseweb="input"] {
        border: 3px solid #8B5A2B !important; 
        background-color: #E8DCC4 !important;
        border-radius: 10px !important;
        box-shadow: 0 0 15px rgba(139, 90, 43, 0.1); 
    }

    /* 隱藏官方元件 */
    header {visibility: hidden;}
    footer {display: none !important;}
    
    /* 標題區：大地與原木漸層 */
    .header-box {
        background: linear-gradient(135deg, #5D4037 0%, #8D6E63 50%, #A1887F 100%);
        padding: 30px 20px;
        border-radius: 0 0 30px 30px;
        color: white !important;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(93, 64, 55, 0.3);
        margin-top: -60px;
    }
    .header-box h1, .header-box div, .header-box span { color: white !important; }
    .header-title { font-size: 28px; font-weight: bold; text-shadow: 1px 1px 3px rgba(0,0,0,0.5); }
    
    /* 輸入卡片 */
    .input-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        border: 1px solid #E8DCC4;
        margin-bottom: 20px;
    }
    
    /* 按鈕：深胡桃木色 */
    .stButton>button {
        width: 100%;
        background-color: #6B4E31;
        color: white !important;
        border-radius: 50px;
        border: none;
        padding: 12px 0;
        font-weight: bold;
        transition: 0.3s;
        font-size: 18px;
    }
    .stButton>button:hover { background-color: #4A3F35; }
    
    /* 資訊看板 */
    .info-box {
        background-color: #E8DCC4;
        border-left: 5px solid #8B5A2B;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 20px;
    }
    
    /* 時間軸 */
    .timeline-item {
        border-left: 3px solid #8D6E63;
        padding-left: 20px;
        margin-bottom: 20px;
        position: relative;
    }
    .timeline-item::before {
        content: '⛰️';
        position: absolute;
        left: -13px;
        top: 0;
        background: #F4F1EA;
        border-radius: 50%;
    }
    .day-header {
        background: #D7CCC8;
        color: #5D4037 !important;
        padding: 5px 15px;
        border-radius: 15px;
        display: inline-block;
        margin-bottom: 15px;
        font-weight: bold;
    }
    .spot-title { font-weight: bold; color: #5D4037 !important; font-size: 18px; }
    .spot-tag { 
        font-size: 12px; background: #C19A6B; color: white !important; 
        padding: 2px 8px; border-radius: 10px; margin-right: 5px; font-weight: bold;
    }
    
    /* 住宿卡片 */
    .hotel-card {
        background: #FFFFFF;
        border-left: 5px solid #6B4E31;
        padding: 10px;
        border-radius: 8px;
        margin-bottom: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    .hotel-tag {
        font-size: 11px;
        background: #8D6E63;
        color: white !important;
        padding: 2px 6px;
        border-radius: 8px;
        margin-right: 5px;
    }
    
    /* 景點名錄小卡 */
    .mini-card {
        background: white;
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #E8DCC4;
        font-size: 14px;
        margin-bottom: 8px;
        border-left: 3px solid #A1887F;
    }
    .feature-badge {
        background: #8B5A2B; color: white !important; padding: 1px 5px; border-radius: 4px; font-size: 11px; margin-left: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. 核心資料庫 (新增：南溪部落)
# ==========================================
all_spots_db = [
    # --- 海岸線 (打卡、海景、地質) ---
    {"name": "金剛大道", "region": "海岸", "type": "絕景", "feature": "山海一線", "fee": "免門票", "desc": "長光部落的無電線桿大道，直通太平洋，宛如東海岸的伯朗大道。"},
    {"name": "八仙洞遺址", "region": "海岸", "type": "文化", "feature": "史前遺跡", "fee": "停車費", "desc": "台灣最古老的舊石器時代長濱文化遺址，海蝕洞奇觀。"},
    {"name": "樟原船型教堂", "region": "海岸", "type": "建築", "feature": "諾亞方舟", "fee": "免門票", "desc": "阿美族部落裡的特色教堂，外觀如一艘大船停泊海岸。"},
    {"name": "星龍營業所", "region": "海岸", "type": "美食", "feature": "無敵海景", "fee": "低消一杯", "desc": "隱身在海岸山脈半山腰的秘境咖啡廳，俯瞰太平洋。"},
    {"name": "烏石鼻漁港", "region": "海岸", "type": "生態", "feature": "火山岩", "fee": "免門票", "desc": "全台最大的柱狀火山岩體，安靜純樸的小漁港。"},

    # --- 部落秘境 (新增南溪部落) ---
    {"name": "南溪部落", "region": "部落", "type": "秘境", "feature": "苦茶油/生態", "fee": "需預約", "desc": "隱身長濱最深山的布農族與阿美族混居聚落，體驗純粹的苦茶油產業、無光害星空與豐富的山林生態。"},
    {"name": "南竹湖部落", "region": "部落", "type": "體驗", "feature": "白螃蟹故鄉", "fee": "需預約", "desc": "充滿皮雕與月桃編織工藝的阿美族部落，提供部落深度導覽。"},
    {"name": "真柄部落 (梯田)", "region": "部落", "type": "秘境", "feature": "山海梯田", "fee": "免門票", "desc": "馬武窟溪畔，擁有壯麗的海岸梯田景觀，最適合慢步。"},
    {"name": "長光部落", "region": "部落", "type": "文化", "feature": "敲打樹皮", "fee": "需預約", "desc": "嚴長壽推薦的部落，可體驗傳統樹皮布製作與阿美族醃肉。"},
    {"name": "永福部落", "region": "部落", "type": "體驗", "feature": "海鹽爺爺", "fee": "需預約", "desc": "傳承古法手工炒海鹽，體驗東海岸純粹的海之味。"},

    # --- 山林慢食 (無菜單、在地食材) ---
    {"name": "Sinasera 24", "region": "山海", "type": "慢食", "feature": "法式無菜單", "fee": "$3000起", "desc": "南法米其林三星主廚返台開設，結合長濱在地24節氣食材 (極難訂位)。"},
    {"name": "齒草埔", "region": "山海", "type": "慢食", "feature": "料理人的家", "fee": "需預約", "desc": "隱密空間內的細緻無菜單料理，專注於食材與感官的對話。"},
    {"name": "長濱吳神父腳底按摩", "region": "山海", "type": "療癒", "feature": "正宗發源地", "fee": "依項目", "desc": "長濱天主堂內，純正吳神父足部健康法，消除旅途疲勞。"},
    {"name": "邱爸爸海味", "region": "山海", "type": "美食", "feature": "海鮮無菜單", "fee": "約$500/人", "desc": "在地漁港現撈海產，沒有菜單，看老闆今天捕到什麼吃什麼。"}
]

hotels_db = [
    {"name": "畫日風尚 Sinasera Resort", "region": "海岸", "tag": "奢華渡假", "price": 6000, "desc": "Sinasera 24 餐廳所在，法式優雅與太平洋的結合。"},
    {"name": "陽光佈居", "region": "山海", "tag": "靈修慢活", "price": 3500, "desc": "位於半山腰，無電視干擾，提倡純粹寧靜與星空。"},
    {"name": "聽風說故事", "region": "海岸", "tag": "無敵海景", "price": 4200, "desc": "每間房都能看日出，擁有大片草皮的質感民宿。"},
    {"name": "竹湖山居", "region": "山林", "tag": "生態體驗", "price": 3800, "desc": "被果園與森林包圍，生態極為豐富的隱世山居。"},
    {"name": "真柄禾多露營區", "region": "部落", "tag": "梯田露營", "price": 1200, "desc": "背山面海，在金黃色稻浪與滿天星斗中入眠。"}
]

# ==========================================
# 4. 邏輯核心：動態路由演算
# ==========================================
def generate_dynamic_itinerary(days_str, group):
    coast_spots = [s for s in all_spots_db if s['region'] == "海岸"]
    tribe_spots = [s for s in all_spots_db if s['region'] == "部落"]
    food_spots = [s for s in all_spots_db if s['region'] == "山海"]
    
    if "一日" in days_str: day_count = 1
    elif "二日" in days_str: day_count = 2
    else: day_count = 3
    
    itinerary = {}
    
    # --- Day 1: 經典東海岸與地質奇觀 ---
    d1_spot1 = next((s for s in coast_spots if s['name'] == "金剛大道"), coast_spots[0])
    d1_spot2 = next((s for s in coast_spots if s['name'] == "星龍營業所"), coast_spots[1])
    itinerary[1] = [d1_spot1, d1_spot2]
    
    # --- Day 2: 深入部落 (確保南溪部落的高權重曝光) ---
    if day_count >= 2:
        # 強制將南溪部落作為重點推薦之一，或從部落池隨機抽選
        d2_spot1 = next((s for s in tribe_spots if s['name'] == "南溪部落"), random.choice(tribe_spots))
        d2_spot2 = next((s for s in food_spots if s['name'] == "長濱吳神父腳底按摩"), food_spots[0])
        itinerary[2] = [d2_spot1, d2_spot2]

    # --- Day 3: 史前遺跡與返程採買 ---
    if day_count == 3:
        d3_spot1 = next((s for s in coast_spots if s['name'] == "八仙洞遺址"), coast_spots[2])
        used_names = [s['name'] for day in itinerary.values() for s in day]
        remaining_food = [s for s in food_spots if s['name'] not in used_names]
        d3_spot2 = remaining_food[0] if remaining_food else {"name": "長濱市區採買", "region": "山海", "type": "採買", "feature": "伴手禮", "fee": "自費", "desc": "採購長濱米、手炒海鹽與部落手工藝品。"}
        itinerary[3] = [d3_spot1, d3_spot2]

    titles = {
        "情侶/夫妻": "🍷 大地氣息的浪漫慢食之旅",
        "親子家庭": "🌿 走入南溪：山林童趣與生態紀實",
        "長輩同行": "🍵 苦茶油香與吳神父的無壓慢活",
        "熱血獨旅": "🏍️ 擁抱山海交界的深度尋幽"
    }
    status_title = titles.get(group, "⛰️ 長濱大地慢活之旅")
    
    return status_title, itinerary

# ==========================================
# 5. 頁面內容渲染
# ==========================================
st.markdown("""
    <div class="header-box">
        <div class="header-title">⛰️ 2026 長濱鄉深度導覽</div>
        <div class="header-subtitle">聽見土地的呼吸，走進山林秘境 🌿</div>
    </div>
""", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="input-card">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        travel_date = st.date_input("📅 預計抵達日期", value=date.today())
    with col2:
        days_str = st.selectbox("🕒 停留天數", ["一日遊 (海岸快閃)", "二日遊 (部落留宿)", "三日遊 (深度慢活)"])
        group = st.selectbox("👥 旅伴屬性", ["情侶/夫妻", "親子家庭", "長輩同行", "熱血獨旅"])
    
    if st.button("🚀 生成大地系專屬行程"):
        st.session_state['generated'] = True
    st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.get('generated'):
    status_title, itinerary = generate_dynamic_itinerary(days_str, group)
    
    st.markdown(f"""
    <div class="info-box">
        <h4>{status_title}</h4>
        <p>為您演算 <b>{travel_date.strftime('%Y/%m/%d')}</b> 啟程的 <b>{group}</b> 專屬路線！</p>
    </div>
    """, unsafe_allow_html=True)

    for day, spots in itinerary.items():
        st.markdown(f'<div class="day-header">Day {day}</div>', unsafe_allow_html=True)
        
        for i, spot in enumerate(spots):
            time_label = "☀️ 上午" if i == 0 else "🌤️ 下午"
            
            tags_html = f'<span class="spot-tag">{spot["type"]}</span>'
            tags_html += f'<span class="spot-tag">{spot["feature"]}</span>'
            if spot['region'] == "部落": 
                tags_html += '<span class="spot-tag" style="background:#5D4037;color:white!important;">原民文化</span>'
            
            st.markdown(f"""
            <div class="timeline-item">
                <div class="spot-title">{time_label}：{spot['name']}</div>
                <div style="margin: 5px 0;">{tags_html}</div>
                <div style="font-size: 14px; color: #555;">
                    💰 {spot['fee']} <br>
                    📝 {spot['desc']}
                </div>
            </div>
            """, unsafe_allow_html=True)

    if "一日" not in days_str:
        st.markdown("### 🏨 長濱秘境宿單 (防呆推薦)")
        if group == "親子家庭" or group == "長輩同行":
            rec_hotels = [h for h in hotels_db if h['tag'] not in ["梯田露營"]] 
        else:
            rec_hotels = hotels_db
            
        for h in random.sample(rec_hotels, min(3, len(rec_hotels))):
            st.markdown(f"""
            <div class="hotel-card">
                <div style="font-weight:bold; color:#5D4037;">{h['name']} <span class="hotel-tag">{h['tag']}</span></div>
                <div style="font-size:13px; color:#666; margin-top:3px;">
                    💲 {h['price']}起 | {h['desc']}
                </div>
            </div>
            """, unsafe_allow_html=True)

with st.expander("📖 展開長濱鄉全境資源矩陣 (All Spots)"):
    st.markdown("#### 大地生態與海岸大數據庫")
    for region in ["海岸", "部落", "山海"]:
        st.markdown(f"**【{region}線】**")
        region_spots = [s for s in all_spots_db if s['region'] == region]
        cols = st.columns(2)
        for i, s in enumerate(region_spots):
            with cols[i % 2]:
                st.markdown(f"""
                <div class="mini-card">
                    <b>{s['name']}</b> <span class="feature-badge">{s['feature']}</span><br>
                    <span style="color:#888; font-size:12px;">{s['desc']}</span>
                </div>
                """, unsafe_allow_html=True)
