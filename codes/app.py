import streamlit as st

st.set_page_config(page_title="Streamlit Chatbot")

st.title("🤖 Streamlit Chatbot")

# 대화 기록 저장
if "messages" not in st.session_state:
    st.session_state.messages = []

# 이전 메시지 출력
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 사용자 입력
prompt = st.chat_input("메시지를 입력하세요")

if prompt:
    # 사용자 메시지 저장
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )
    with st.chat_message("user"):
        st.markdown(prompt)

    # 챗봇 응답 (Echo)
    response = f"당신이 입력한 메시지: **{prompt}**"
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )
    with st.chat_message("assistant"):
        st.markdown(response)
