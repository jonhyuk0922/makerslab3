import streamlit as st

st.set_page_config(
    page_title="서울 점심 추천 – Minions Edition",
    page_icon="🍌",
    layout="wide",
)

# =========================
# 스타일 (Minions 느낌으로 변경)
# =========================
st.markdown(
    """
<style>
:root {
    --minion-yellow: #ffe75c;
    --minion-yellow-soft: #fff5a8;
    --minion-blue: #1c6fd9;
    --minion-blue-soft: #d3e4ff;
    --minion-gray: #4f4f4f;
}

/* 전체 배경 */
[data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at top, #fff9c4 0, #fffde7 35%, #fff9c4 70%, #fffce0 100%);
}

/* 상단 헤더 영역 투명하게 */
[data-testid="stHeader"] {
    background: rgba(255,255,255,0);
}

/* 컨텐츠 영역 살짝 가운데로 */
.block-container {
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}

/* 입력창 / 셀렉트박스 / 버튼 공통 느낌 */
.stTextInput > div > div > input {
    border-radius: 999px;
    padding: 0.6rem 1.1rem;
    border: 2px solid var(--minion-blue-soft);
    background-color: #ffffffaa;
}

.stSelectbox > div > div {
    border-radius: 999px;
    border: 2px solid var(--minion-blue-soft);
    background-color: #ffffffdd;
}

/* 버튼 - 미니언즈 블루 */
.stButton > button {
    border-radius: 999px;
    border: none;
    padding: 0.6rem 1.3rem;
    background: var(--minion-blue);
    color: white;
    font-weight: 700;
    box-shadow: 0 4px 10px rgba(0,0,0,0.12);
    transition: transform 0.05s ease-out, box-shadow 0.05s ease-out, background 0.15s;
}

.stButton > button:hover {
    background: #1653a7;
    transform: translateY(-1px);
    box-shadow: 0 6px 14px rgba(0,0,0,0.18);
}

.stButton > button:active {
    transform: translateY(1px);
    box-shadow: 0 3px 6px rgba(0,0,0,0.2);
}

/* 슬라이더 색감 */
[data-baseweb="slider"] > div > div {
    background-color: var(--minion-blue-soft);
}
[data-baseweb="slider"] [role="slider"] {
    background-color: var(--minion-blue);
}

/* 왼쪽 필터 카드 느낌 */
.css-1r6slb0, .css-1d391kg {  /* Streamlit 버전에 따라 필터 박스 감싸는 div */
    border-radius: 18px !important;
    background: #ffffffbb;
    padding: 1rem 1.2rem;
}

/* 검색바 커스텀 (위에서 st.text_input 옆에 설명용 div) */
.search-bar input {
    border-radius: 999px !important;
    padding: 0.75rem 1.25rem !important;
    border: 2px solid var(--minion-blue-soft) !important;
}

/* 레스토랑 카드 */
.restaurant-card {
    background: linear-gradient(135deg, var(--minion-yellow-soft), #ffffff);
    border-radius: 20px;
    padding: 18px;
    margin-bottom: 14px;
    display: flex;
    gap: 16px;
    border: 2px solid #ffe082;
    box-shadow: 0 6px 14px rgba(0,0,0,0.06);
    position: relative;
    overflow: hidden;
}

/* 카드 상단에 살짝 도트 패턴 느낌 */
.restaurant-card::before {
    content: "";
    position: absolute;
    right: -30px;
    top: -30px;
    width: 120px;
    height: 120px;
    background-image: radial-gradient(circle, #ffeb3b55 2px, transparent 2px);
    background-size: 12px 12px;
    opacity: 0.6;
}

/* 카드 이미지 – 미니언즈 얼굴 느낌 */
.card-image {
    width: 140px;
    height: 100px;
    border-radius: 18px;
    background: radial-gradient(circle at 30% 30%, #fffde7 0, #ffe75c 40%, #ffd54f 75%);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 34px;
    color: #2b4b6f;
    flex-shrink: 0;
    border: 3px solid var(--minion-blue);
    position: relative;
}

/* 미니언즈 고글(눈) 표현 */
.card-image::before, .card-image::after {
    content: "";
    position: absolute;
    top: 38%;
    width: 24px;
    height: 24px;
    border-radius: 50%;
    border: 3px solid #616161;
    background: #fafafa;
}
.card-image::before {
    left: 24px;
}
.card-image::after {
    right: 24px;
}

/* pupils */
.card-image span {
    position: relative;
}
.card-image span::before, .card-image span::after {
    content: "";
    position: absolute;
    top: -6px;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #424242;
}
.card-image span::before {
    left: -26px;
}
.card-image span::after {
    right: -26px;
}

.card-content {
    flex: 1;
}

.card-title-row {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 4px;
}

.card-title-row h3 {
    margin: 0;
    font-size: 18px;
    color: #3c3c3c;
    font-weight: 800;
}

/* 영업중 뱃지 – 연두색 */
.card-status {
    font-size: 12px;
    padding: 2px 8px;
    border-radius: 999px;
    background-color: #e6f4ea;
    color: #137333;
    font-weight: 600;
}

/* 평점/정보 줄 */
.card-rating {
    font-size: 14px;
    color: #424242;
    margin-bottom: 4px;
}

/* 태그 줄 – 파란 pill 느낌 */
.card-tags {
    font-size: 12px;
    color: #1b3c78;
    margin-bottom: 6px;
}

.card-tags span {
    display: inline-block;
    padding: 2px 8px;
    border-radius: 999px;
    background: var(--minion-blue-soft);
    margin-right: 4px;
    margin-bottom: 2px;
}

/* 리뷰 한 줄 */
.card-snippet {
    font-size: 13px;
    color: #555;
    font-style: italic;
}

/* info 박스 */
.stAlert {
    border-radius: 16px;
    background-color: #fffde7;
    border: 1px solid #ffe082;
}

/* 작은 캡션류 글자 */
small {
    color: var(--minion-gray);
}

</style>
""",
    unsafe_allow_html=True,
)

# =========================
# 데이터
# =========================
RESTAURANTS = [
    {
        "name": "선샤인 숯불구이",
        "area": "종로",
        "cuisine": "한식",
        "price": "₩₩ - ₩₩₩",
        "rating": 4.9,
        "reviews": 40,
        "meal_types": ["점심식사", "저녁식사"],
        "tags": ["고기", "직장인맛집", "단체석"],
        "status": "영업 중",
        "snippet": "“유독... 내가 가본 고깃집 중에 최고였어요...”",
    },
    {
        "name": "다움 숯불구이 명동점",
        "area": "명동",
        "cuisine": "한식",
        "price": "₩₩ - ₩₩₩",
        "rating": 4.9,
        "reviews": 5587,
        "meal_types": ["점심식사", "저녁식사"],
        "tags": ["고기", "관광객 인기", "가성비"],
        "status": "영업 중",
        "snippet": "“고기도 맛있고 직원분들도 친절했어요.”",
    },
    {
        "name": "멘야산다이메",
        "area": "강남",
        "cuisine": "일식",
        "price": "₩₩",
        "rating": 4.6,
        "reviews": 320,
        "meal_types": ["점심식사", "저녁식사"],
        "tags": ["라멘", "직장인 점심", "혼밥"],
        "status": "영업 중",
        "snippet": "“국물이 진하고 부담스럽지 않았어요.”",
    },
    {
        "name": "버거랩 랩",
        "area": "홍대",
        "cuisine": "양식",
        "price": "₩₩",
        "rating": 4.5,
        "reviews": 210,
        "meal_types": ["점심식사", "브런치"],
        "tags": ["수제버거", "감자튀김", "캐주얼"],
        "status": "영업 중",
        "snippet": "“패티가 두툼해서 점심 한 끼로 든든해요.”",
    },
    {
        "name": "쌀국수 공방",
        "area": "합정",
        "cuisine": "아시아 음식",
        "price": "₩",
        "rating": 4.3,
        "reviews": 180,
        "meal_types": ["점심식사", "저녁식사"],
        "tags": ["쌀국수", "가벼운식사", "국물"],
        "status": "영업 중",
        "snippet": "“점심에 부담 없이 먹기 좋은 쌀국수 집.”",
    },
    {
        "name": "비건 포크",
        "area": "을지로",
        "cuisine": "채식주의자 친화",
        "price": "₩₩",
        "rating": 4.7,
        "reviews": 95,
        "meal_types": ["점심식사"],
        "tags": ["비건", "헬시푸드", "한끼식사"],
        "status": "영업 중",
        "snippet": "“고기도 안 들어갔는데 왜 이렇게 맛있죠?”",
    },
    {
        "name": "카레코코",
        "area": "성수",
        "cuisine": "일식",
        "price": "₩₩",
        "rating": 4.4,
        "reviews": 150,
        "meal_types": ["점심식사", "저녁식사"],
        "tags": ["카레", "직장인맛집", "매운맛선택"],
        "status": "영업 중",
        "snippet": "“매운 단계 조절 가능해서 좋았어요.”",
    },
    {
        "name": "파스타리아",
        "area": "신촌",
        "cuisine": "양식",
        "price": "₩₩ - ₩₩₩",
        "rating": 4.2,
        "reviews": 260,
        "meal_types": ["점심식사", "저녁식사", "데이트"],
        "tags": ["파스타", "분위기좋음", "와인"],
        "status": "영업 중",
        "snippet": "“점심 세트 구성이 꽤 알찼습니다.”",
    },
]

PRICE_ORDER = {"₩": 1, "₩₩": 2, "₩₩ - ₩₩₩": 2.5, "₩₩₩": 3}

# =========================
# 헤더 + 검색 + 버튼
# =========================
st.markdown("## 🐥 서울 점심 미니언즈 추천")
st.write("노랑노랑 귀여운 서울 점심 맛집 리스트야. 오늘 점심 뭐 먹을지 같이 골라보자! 🍌")

top_left, top_mid, top_right = st.columns([4, 2, 2])

with top_left:
    search_text = st.text_input(
        "",
        placeholder="검색 (가게 이름, 지역, 태그 등)",
        label_visibility="collapsed",
    )
    st.markdown('<div class="search-bar"></div>', unsafe_allow_html=True)

with top_mid:
    sort_option = st.selectbox(
        "정렬", ["추천", "평점 높은순", "리뷰 많은순", "가격 낮은순", "가격 높은순"], index=0
    )

with top_right:
    if st.button("🍽️ 점심 메뉴 추천 받기"):
        # Streamlit 1.25+ 에서 지원
        st.switch_page("pages/1_점심_추천_결과.py")

# =========================
# 좌측 필터 / 우측 리스트
# =========================
left, right = st.columns([1, 3])

with left:
    st.subheader("🍌 음식점 타입")
    selected_cuisine = st.multiselect(
        "요리",
        options=sorted({r["cuisine"] for r in RESTAURANTS}),
        default=sorted({r["cuisine"] for r in RESTAURANTS}),
    )

    st.subheader("🍽️ 식사 유형")
    selected_meal = st.multiselect(
        "식사",
        options=["아침식사", "브런치", "점심식사", "저녁식사"],
        default=["점심식사"],
    )

    st.subheader("💸 가격대")
    selected_price = st.multiselect(
        "가격",
        options=["₩", "₩₩", "₩₩ - ₩₩₩", "₩₩₩"],
        default=["₩", "₩₩", "₩₩ - ₩₩₩", "₩₩₩"],
    )

    st.subheader("⭐ 최소 평점")
    min_rating = st.slider("최소 평점", 0.0, 5.0, 4.0, 0.1)


def filter_restaurants():
    filtered = []
    for r in RESTAURANTS:
        # 요리
        if r["cuisine"] not in selected_cuisine:
            continue
        # 식사 유형 (하나라도 겹치면 통과)
        if not any(m in r["meal_types"] for m in selected_meal):
            continue
        # 가격
        if not any(p in r["price"] for p in selected_price):
            continue
        # 평점
        if r["rating"] < min_rating:
            continue
        # 검색어
        if search_text:
            text = search_text.lower()
            if (
                text not in r["name"].lower()
                and text not in r["area"].lower()
                and all(text not in tag.lower() for tag in r["tags"])
            ):
                continue
        filtered.append(r)

    # 정렬
    if sort_option == "평점 높은순":
        filtered.sort(key=lambda x: x["rating"], reverse=True)
    elif sort_option == "리뷰 많은순":
        filtered.sort(key=lambda x: x["reviews"], reverse=True)
    elif sort_option == "가격 낮은순":
        filtered.sort(
            key=lambda x: min(
                PRICE_ORDER.get(part.strip(), 2)
                for part in x["price"].split("-")
            )
        )
    elif sort_option == "가격 높은순":
        filtered.sort(
            key=lambda x: max(
                PRICE_ORDER.get(part.strip(), 2)
                for part in x["price"].split("-")
            ),
            reverse=True,
        )
    else:  # 추천
        filtered.sort(key=lambda x: x["rating"] * x["reviews"], reverse=True)

    return filtered


with right:
    filtered_list = filter_restaurants()
    st.write(f"🔍 {len(filtered_list)}개의 결과가 있어요")

    if not filtered_list:
        st.info("조건에 맞는 가게가 없어요. 필터를 조금 완화해볼까? 🥲")
    else:
        for r in filtered_list:
            # 태그/식사 타입을 pill 형태로 보여주도록 감싸기
            tags_html = "".join(
                f"<span>{tag}</span>" for tag in r["tags"]
            )
            meals_html = "".join(
                f"<span>{m}</span>" for m in r["meal_types"]
            )

            st.markdown(
                f"""
<div class="restaurant-card">
  <div class="card-image">
    <span></span>
  </div>
  <div class="card-content">
    <div class="card-title-row">
      <h3>{r['name']}</h3>
      <span class="card-status">{r['status']}</span>
    </div>
    <div class="card-rating">
      ⭐ {r['rating']} · {r['reviews']}건의 리뷰 · {r['price']} · {r['cuisine']} · {r['area']}
    </div>
    <div class="card-tags">
      {tags_html}{meals_html}
    </div>
    <div class="card-snippet">
      {r['snippet']}
    </div>
  </div>
</div>
""",
                unsafe_allow_html=True,
            )
