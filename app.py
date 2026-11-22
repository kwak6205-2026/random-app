import random
import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="가위바위보 게임", page_icon="🎮")

# 1. 화면 상단에 멋진 제목과 안내 문구 배치
st.title("🎮 두근두근! 인공지능과 가위바위보 게임")
st.write("아래 버튼 중 하나를 골라 컴퓨터와 승부를 겨뤄보세요! 과연 이길 수 있을까요?")
st.divider()

# 2. [✌️ 가위], [✊ 바위], [✋ 보] 버튼 3개를 나란히 배치
col1, col2, col3 = st.columns(3)

user_choice = None

with col1:
    if st.button("✌️ 가위", use_container_width=True):
        user_choice = "✌️ 가위"

with col2:
    if st.button("✊ 바위", use_container_width=True):
        user_choice = "✊ 바위"

with col3:
    if st.button("✋ 보", use_container_width=True):
        user_choice = "✋ 보"

# 3. 사용자가 버튼을 누르면 대결 진행
if user_choice:
    choices = ["✌️ 가위", "✊ 바위", "✋ 보"]
    computer_choice = random.choice(choices)

    st.divider()
    
    # 나와 컴퓨터의 선택을 나란히 보여주기
    res_col1, res_col2 = st.columns(2)
    with res_col1:
        st.subheader("🙋‍♂️ 나의 선택")
        st.info(user_choice)
    with res_col2:
        st.subheader("🤖 컴퓨터의 선택")
        st.info(computer_choice)

    # 4. 승패 판정 및 결과 출력
    if user_choice == computer_choice:
        st.warning("🤝 비겼습니다! 다시 한 번 도전해 보세요.")
    elif (
        (user_choice == "✌️ 가위" and computer_choice == "✋ 보") or
        (user_choice == "✊ 바위" and computer_choice == "✌️ 가위") or
        (user_choice == "✋ 보" and computer_choice == "✊ 바위")
    ):
        st.balloons()  # 승리 시 풍선 축하 효과
        st.success("🎉 축하합니다! 당신이 이겼습니다!")
    else:
        st.error("😭 아쉽네요! 컴퓨터가 이겼습니다.")
