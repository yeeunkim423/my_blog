import streamlit as st
import random

st.set_page_config(page_title="Daelicent Fic Ideas", layout="centered")

st.title("🖋️ Daelicent Fic Notes & Ideas")
st.caption("Organize your fic universe and keep your imagination flowing.")

# 📓 탭 생성
tab1, tab2 = st.tabs(["📓 Fic Notebook", "💡 Fic Prompts"])

# 📓 메모장 탭
with tab1:
    st.subheader("📓 Your Fic Notebook")

    # 세션 초기화
    if "fic_notes" not in st.session_state:
        st.session_state.fic_notes = []

    # 폼으로 새 노트 추가
    with st.form("fic_form", clear_on_submit=True):
        new_note = st.text_area("💭 Add a new idea or scene:", height=100)
        submitted = st.form_submit_button("➕ Add")

        if submitted and new_note.strip():
            st.session_state.fic_notes.append(new_note.strip())
            st.success("Note added!")

    # 저장된 노트 보여주기
    st.markdown("---")
    if st.session_state.fic_notes:
        for i, note in enumerate(reversed(st.session_state.fic_notes), 1):
            st.markdown(f"**{len(st.session_state.fic_notes) - i + 1}.** {note}")
    else:
        st.info("No notes yet. Start writing!")

    # 초기화 옵션
    with st.expander("⚙️ Clear all notes"):
        if st.button("🗑️ Delete All"):
            st.session_state.fic_notes = []
            st.success("Notebook cleared.")

# 💡 아이디어 정리 탭
with tab2:
    st.subheader("💡 Fic Prompt Ideas")

    default_prompts = [
        "👶 Single dad Daemon AU with Alicent as the teacher at Milo’s daycare.",
        "🧳 Enemies-to-lovers AU where Alicent is Daemon’s new PR manager.",
        "🎓 Daemon as a grumpy professor and Alicent as his sunshine TA.",
        "👑 Royal AU where Alicent is queen and Daemon is her sworn sword.",
        "🏢 Modern CEO AU with Daemon as Alicent’s fake boyfriend for the press.",
        "🍼 Single mom Alicent AU with Daemon as her kid’s pediatrician.",
        "💍 Alicent is Daemon’s ex who shows up at his brother’s wedding.",
        "🥐 Daemon and Alicent as rival bakery owners in the same street.",
        "📚 College AU where Daemon is the tattooed philosophy lecturer.",
        "👨‍👩‍👧‍👦 Co-parents after a one-night stand turned into joint custody.",
        "💒 Alicent has to plan Daemon’s wedding—until he calls it off.",
        "🐉 Daemon as a dragonrider, Alicent as the healer who patches him up.",
        "🎭 Alicent is a princess in disguise, Daemon sees through her act.",
        "🗂️ Office AU where Daemon and Alicent are forced to share a desk.",
        "👯 Daemon is Helaena’s brother, Alicent is her best friend.",
        "🍸 Drunk in Vegas, Daemon and Alicent accidentally get married.",
        "⏰ Alicent is a kindergarten teacher, Daemon is the hot single dad.",
        "🎙️ Daemon is a podcast host, Alicent is the viral guest.",
        "⚖️ Alicent is Otto’s protégée, Daemon is the reckless rival.",
        "🕵️ They’re forced to go undercover as a couple on the run.",
        "🧛 Daemon is a vampire, Alicent is the journalist exposing him.",
        "👶 Reunited exes at their kids’ school events.",
        "🎩 Alicent is an etiquette coach; Daemon is the feral prince.",
        "🎨 Daemon is the brooding artist upstairs, Alicent bakes too much.",
        "💔 Daemon crashes Alicent’s blind date claiming to be her ex."
    ]

    # 세션 상태 초기화
    if "saved_prompts" not in st.session_state:
        st.session_state.saved_prompts = []
    if "custom_prompts" not in st.session_state:
        st.session_state.custom_prompts = []

    # 무작위 프롬프트 추천
    if st.button("🎲 Prompt me!"):
        all_prompts = default_prompts + st.session_state.custom_prompts
        st.session_state.random_prompt = random.choice(all_prompts)

    if "random_prompt" in st.session_state:
        st.markdown(f"**🔹 Prompt:** {st.session_state.random_prompt}")
        if st.button("❤️ Save this idea"):
            if st.session_state.random_prompt not in st.session_state.saved_prompts:
                st.session_state.saved_prompts.append(st.session_state.random_prompt)
                st.success("Prompt saved!")

    # 사용자 정의 프롬프트 추가
    st.markdown("---")
    st.subheader("📝 Add Your Own Prompt")
    with st.form("custom_prompt_form", clear_on_submit=True):
        custom_input = st.text_input("Enter your idea:")
        custom_submit = st.form_submit_button("➕ Add Prompt")
        if custom_submit and custom_input.strip():
            st.session_state.custom_prompts.append(custom_input.strip())
            st.success("Custom prompt added!")

    # 저장된 프롬프트 보기
    st.markdown("---")
    st.subheader("📁 Saved Prompts")
    if st.session_state.saved_prompts:
        for i, prompt in enumerate(st.session_state.saved_prompts, 1):
            st.markdown(f"**{i}.** {prompt}")
        if st.button("🗑️ Clear Saved Prompts"):
            st.session_state.saved_prompts = []
            st.success("Saved prompts cleared.")
    else:
        st.info("No saved prompts yet. Try generating one!")
