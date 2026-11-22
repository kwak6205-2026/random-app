import streamlit as st

# 1. [함수] 벽 자재와 색상을 받아서 건축 스타일 이름을 정해주는 함수 (snake_case 준수)
def get_architect_style(wall_material, wall_color):
    # 2. [선택구조] 자재와 색상 조합에 따라 건축 스타일 판정
    if wall_material == "노출 콘크리트" and wall_color in ["화이트", "그레이"]:
        style_name = "모던 미니멀 스타일"
    elif wall_material == "친환경 원목" or wall_color == "우드 브라운":
        style_name = "따뜻한 내추럴 우드 스타일"
    elif wall_material == "붉은 벽돌":
        style_name = "클래식 브릭 하우스 스타일"
    else:
        style_name = "개성 있는 믹스매치 스타일"
    
    return style_name

# --- 화면 구성 ---
st.title("🏡 나만의 단독주택 만들기")
st.write("기본 **30평형 단독주택**을 기준으로 원하는 층수, 벽 자재, 벽 색상을 골라 나만의 집을 완성해 보세요!")
st.divider()

# 사용자 입력 (직관적인 3가지 선택)
floor_choice = st.selectbox("1. 건물 층수를 선택하세요", ["1층 (단층 주택)", "2층 (복층 주택)", "3층 (다층 주택)"])
material_choice = st.selectbox("2. 외벽 자재를 선택하세요", ["붉은 벽돌", "노출 콘크리트", "친환경 원목"])
color_choice = st.selectbox("3. 외벽 메인 색상을 선택하세요", ["화이트", "그레이", "우드 브라운"])

# 버튼 클릭 시 실행
if st.button("✨ 나만의 단독주택 완성하기", use_container_width=True):
    # 3. [리스트] 사용자가 고른 3가지 건축 요소를 리스트에 저장
    selected_options = [
        f"건물 규모: {floor_choice} (30평 고정)",
        f"외벽 자재: {material_choice}",
        f"외벽 색상: {color_choice}"
    ]

    # 함수 호출해서 건축 스타일 이름 받아오기
    final_style = get_architect_style(material_choice, color_choice)

    st.divider()
    # 판정된 건축 스타일 크게 보여주기
    st.metric(label="완성된 나의 단독주택 스타일", value=final_style)

    st.subheader("📋 내가 선택한 주택 설계 요약")
    # 4. [반복구조] 리스트에 담긴 3가지 요소를 하나씩 꺼내서 화면에 출력
    for option in selected_options:
        st.info(option)

    # 층수에 따른 간단한 건축 팁 추가 출력
    if "1층" in floor_choice:
        st.success("💡 1층 주택은 계단이 없어 이동이 편리하고 마당과 연결하기 좋습니다!")
    elif "2층" in floor_choice:
        st.success("💡 2층 주택은 1층은 거실, 2층은 침실로 공간을 분리하기 가장 좋습니다!")
    else:
        st.success("💡 3층 주택은 옥상 테라스를 활용하고 멋진 전망을 확보할 수 있습니다!")
