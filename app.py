import streamlit as st

st.set_page_config(
    page_title="서울 점심 추천 – TripAdvisor 스타일",
    page_icon="🍽️",
    layout="wide",
)

# =========================
# 스타일 (Tripadvisor 비슷하게)
# =========================
st.markdown(
    """
<style>
.main {
    background-color: #f5f5f5;
}

.search-bar input {
    border-radius: 999px !important;
    padding: 0.75rem 1.25rem !important;
    border: 1px solid #c0c0c0 !important;
}

.restaurant-card {
    background-color: #ffffff;
    border-radius: 12px;
    padding: 16px;
    margin-bottom: 12px;
    display: flex;
    gap: 16px;
    border: 1px solid #e0e0e0;
}

.card-image {
    width: 140px;
    height: 100px;
    border-radius: 8px;
    background: linear-gradient(135deg, #e8f3ff, #d6e5ff);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 28px;
    color: #2b4b6f;
    flex-shrink: 0;
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
}

.card-status {
    font-size: 12px;
    padding: 2px 6px;
    border-radius: 4px;
    background-color: #e6f4ea;
    color: #137333;
}

.card-rating {
    font-size: 14px;
    color: #222;
    margin-bottom: 4px;
}

.card-tags {
    font-size: 13px;
    color: #555;
    margin-bottom: 4px;
}

.card-snippet {
    font-size: 13px;
    color: #555;
    font-style: italic;
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
st.markdown("### 서울 음식점")
st.write("서울의 인기 점심 음식점")

top_left, top_mid, top_right = st.columns([4, 2, 2])

with top_left:
    search_text = st.text_input(
        "", placeholder="검색 (가게 이름, 지역, 태그 등)", label_visibility="collapsed"
    )
    st.markdown('<div class="search-bar"></div>', unsafe_allow_html=True)

with top_mid:
    sort_option = st.selectbox(
        "정렬", ["추천", "평점 높은순", "리뷰 많은순", "가격 낮은순", "가격 높은순"], index=0
    )

with top_right:
    # 🔥 여기서 다른 페이지로 이동
    if st.button("🍽️ 점심 메뉴 추천 받기"):
        # Streamlit 1.25+ 에서 지원
        st.switch_page("pages/1_점심_추천_결과.py")

# =========================
# 좌측 필터 / 우측 리스트
# =========================
left, right = st.columns([1, 3])

with left:
    st.subheader("음식점 타입")
    selected_cuisine = st.multiselect(
        "요리",
        options=sorted({r["cuisine"] for r in RESTAURANTS}),
        default=sorted({r["cuisine"] for r in RESTAURANTS}),
    )

    st.subheader("식사 유형")
    selected_meal = st.multiselect(
        "식사",
        options=["아침식사", "브런치", "점심식사", "저녁식사"],
        default=["점심식사"],
    )

    st.subheader("가격대")
    selected_price = st.multiselect(
        "가격",
        options=["₩", "₩₩", "₩₩ - ₩₩₩", "₩₩₩"],
        default=["₩", "₩₩", "₩₩ - ₩₩₩", "₩₩₩"],
    )

    st.subheader("평점")
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
    st.write(f"{len(filtered_list)}개의 결과")

    if not filtered_list:
        st.info("조건에 맞는 가게가 없어요. 필터를 조금 완화해볼까?")
    else:
        for r in filtered_list:
            st.markdown(
                f"""
<div class="restaurant-card">
  <div class="card-image">
    🍽️
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
      {" · ".join(r["tags"])} · {", ".join(r["meal_types"])}
    </div>
    <div class="card-snippet">
      {r['snippet']}
    </div>
  </div>
</div>
""",
                unsafe_allow_html=True,
            )
