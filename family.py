import streamlit as st
import streamlit.components.v1 as components


conn = st.connection('familydb', type='sql')
rows = conn.query("SELECT * FROM members", ttl=0)
st.dataframe(rows)
members = conn.query("SELECT firstname, lastname, phone, created_at FROM members ORDER BY created_at DESC", ttl="0")
st.dataframe(members)
# 🔧 Styling
st.markdown("""
    <style>
        .main {
            background-color: #f0f2f6;
            font-family: 'Segoe UI', sans-serif;
        }
        .title {
            color: #2e4053;
            text-align: center;
            font-size: 2.5em;
            margin-bottom: 0.5em;
        }
        .info-box {
            padding: 10px;
            border: 2px solid #aaa;
            border-radius: 10px;
            background-color: #ffffff;
        }
        .footer {
            font-size: 0.9em;
            color: gray;
            text-align: center;
            margin-top: 30px;
        }
        .section-title {
            font-size: 1.6em;
            margin-top: 30px;
            color: #1c3e57;
        }
    </style>
""", unsafe_allow_html=True)

# 🚀 Session state for login
if 'user_entered' not in st.session_state:
    st.session_state.user_entered = False

# 🔐 Login Page
if not st.session_state.user_entered:
    st.markdown("<div class='title'>Welcome! Please enter your details</div>", unsafe_allow_html=True)

    name = st.text_input("Enter your first name")
    lstname = st.text_input("Enter your last name")
    number = st.text_input("Enter your phone number")

    allowed_lastnames = ["khali", "vasisth"]

    if st.button("Submit"):
        if name and number and lstname:
            if lstname.lower() in allowed_lastnames:
                st.session_state.user_entered = True
                st.session_state.name = name
                st.session_state.number = number
                st.session_state.lstname = lstname
                st.experimental_rerun()
            else:
                st.warning("🚫 Access Denied: Your last name is not allowed.")
        else:
            st.warning("⚠️ Please fill in all fields.")

# 🏡 Main Page
else:
    st.title(f"Hello, {st.session_state.name.title()} {st.session_state.lstname.title()}!")
    st.success("✅ Welcome to the family page!")

    st.image(
        "https://c8.alamy.com/comp/T5W55F/the-village-of-khal-jhuni-in-the-saryu-valley-of-uttarakhand-in-northern-india-T5W55F.jpg",
        use_column_width=True,
        caption="Khal Village – Our Roots"
    )

    st.markdown("<div class='section-title'>📌 Page Info</div>", unsafe_allow_html=True)
    st.markdown("""
        - This portal is for viewing and updating your **family chart**.
        - Currently showing **Kashi Ram's side**.
        - Click below to view or edit your tree.
    """)

    # ℹ️ Info Box
    components.html("""
        <div class="info-box">
            <h3 style="color:#2e86c1;">About this portal</h3>
            <p>This is a private website for members of the <strong>Khal</strong> family.</p>
            <p>Only those with last name <strong>Khali</strong> or <strong>Vasisth</strong> are currently allowed.</p>
            <p>More family branches and features coming soon!</p>
        </div>
    """, height=220)

    # 👁 Family Tree Viewer
    st.markdown("<div class='section-title'>🌳 View Family Tree</div>", unsafe_allow_html=True)
    components.html("""
        <iframe 
            src="https://www.familyecho.com/?p=AELY4&c=ofkzym9wksxud2ht&f=209934363209316139&lang=en"
            width="100%" height="1000"
            style="border: 2px solid #ccc; border-radius: 10px;"
            allow="autoplay" allowfullscreen="true">
        </iframe>
    """, height=1000, scrolling=True)

    # ✏ Edit Button
    st.markdown("<div class='section-title'>✏️ Edit Your Family Tree</div>", unsafe_allow_html=True)
    st.markdown("""
        <a href="https://www.familyecho.com/?p=START&c=2gw93plx8pwokrh4&f=209934363209316139&lang=en" target="_blank">
            <button style="background-color:#2e86c1;color:white;padding:10px 20px;border:none;border-radius:5px;font-size:16px;cursor:pointer;">
                ➕ Open FamilyEcho Editor
            </button>
        </a>
    """, unsafe_allow_html=True)

    # Footer
    st.markdown("<div class='footer'>Made with ❤️ by SK | Powered by Streamlit</div>", unsafe_allow_html=True)
