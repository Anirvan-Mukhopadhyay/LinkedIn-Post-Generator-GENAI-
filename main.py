import streamlit as st
from few_shot import FewShotPosts
from post_gene import generate_post

# Set Page Configurations
st.set_page_config(page_title="✍️LinkedIn Post Generator✍️", layout="centered")

# Custom CSS for Styling
st.markdown(
    """
   <style>
    /* Global Styles */
    body {
        background-color: white;
        color: #FFFFFF;
    }

    /* Title Styling */
    .stApp {
        border-left: 10px solid #BB86FC;
        border-right: 10px solid #BB86FC;
        background-color: black;
    }

    h1 {
        text-align: center;
        font-weight: bold;
        color: white;
        border-bottom: 3px solid #BB86FC;
        padding-bottom: 10px;
    }

    /* Select Box Styling */
    div[data-baseweb="select"] {
        background: rgba(255, 255, 255, 0.1);
        border: 2px solid #BB86FC;
        border-radius: 10px;
        padding: 5px;
        font-weight: bold;
        transition: all 0.3s ease-in-out;
    }

    /* Hover Animation on Dropdown */
    div[data-baseweb="select"]:hover {
        box-shadow: 0px 0px 10px #BB86FC;
        transform: scale(1.02);
        cursor: pointer
    }

    /* Button Styling */
    .stButton>button {
        background: linear-gradient(45deg, #BB86FC, #3700B3);
        color: white;
        font-size: 22px;
        font-weight: bold;
        border-radius: 12px;
        padding: 12px 25px;
        border: none;
        transition: 0.3s;
        display: block;
        margin: auto;
        width: 250px;
        cursor: pointer;
    }

    .stButton>button:hover {
        background: linear-gradient(45deg, #3700B3, #BB86FC);
        transform: scale(1.05);
        cursor: pointer;
    }

    /* White text for labels */
    div[data-testid="stSelectbox"] label {
        color: white !important;
        font-size: 16px;
        font-weight: bold;
    }

    /* Dropdown Animation */
    div[data-testid="stSelectbox"] .css-1dimb5e-singleValue {
        opacity: 0;
        animation: fadeIn 0.5s ease-in-out forwards;
    }

    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(-10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    /* Cursor Pointer for Specific Items */
    div[data-testid="stSelectbox"] div[role="option"] {
        cursor: pointer !important;
    }

    /* Output Post Styling */
    .post-box {
        background: rgba(255, 255, 255, 0.1);
        border: 2px solid #BB86FC;
        border-radius: 10px;
        padding: 20px;
        margin-top: 20px;
        font-size: 18px;
        font-weight: bold;
        color: white !important;
        text-align: center;
        box-shadow: 0px 0px 15px #BB86FC;
    }
   div[role="checkbox"], div[role="radio"], input[type="checkbox"], input[type="radio"] {
    cursor: pointer !important;
}

}
</style>

    """,
    unsafe_allow_html=True
)

length_options = ["Short(50 to 60 words)", "Medium(100 to 150 words)", "Long(200 to 230 words)"]
language_options = ["English", "Hindi(written in English)"]

def main():
    st.markdown(
    "<h1 style='text-align: center; color: white; background-color: black; padding: 10px; border-bottom: 3px solid #BB86FC;'>✍️LinkedIn Post Generator✍️</h1>",
    unsafe_allow_html=True
        )

    col1, col2, col3 = st.columns(3)
    fs = FewShotPosts()

    with col1:
        selected_tag = st.selectbox("🔹 Title", options=fs.get_tags())
    with col2:
        length = st.selectbox("📏 Length", options=length_options)
    with col3:
        language = st.selectbox("🌍 Language", options=language_options)

    if st.button("🚀 Generate Post"):
        post = generate_post(length, language, selected_tag)
        st.markdown(f'<div class="post-box">{post}</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
