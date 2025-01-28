import streamlit as st

# Set Page Configuration (called once at the very top)
st.set_page_config(page_title="Velocity Nodes", page_icon="🚀", layout="centered")

# ==================== Home Page ====================
def home():
    st.sidebar.radio("Select a page", ["Home"])

    col1, col2 = st.columns([1, 2])  # Adjust the ratio to control the width of columns

    with col1:
        st.image("https://i.ibb.co/McNrwYq/11zon-cropped.png", width=200)

    with col2:
        st.markdown(
            """
            <p style="font-size:50px; font-weight:bold;">
                <span style="color:#CC9966;">Velocity</span>
                <span style="color:#1E90FF;">Nodes</span>
            </p>
            """,
            unsafe_allow_html=True
        )

    st.image("https://i.imgur.com/BTMaNKG.png")
    st.markdown(
        """
        ### Velocity | Free Hosting 24/7  
        🔥 **#1 World's First Free Hosting with Quality**  
        🚀 **Welcome to Velocity Hosting 🚀**

        ---
        **🔹 Affordable Pricing:**  
        Enjoy premium-quality Discord server hosting at just $2 per month—perfect for personal or community use!  
        <br><br>
        **🔹 Free Minecraft Hosting:**  
        Get your own Minecraft server hosted for free! Whether you're building a world with friends or hosting a community, we provide smooth and reliable server hosting.  
         <br><br>
        **🔹 24/7 Uptime:**  
        With reliable server performance, your Discord and Minecraft servers stay up and running, day and night.  
         <br><br>
        **🔹 Easy Setup:**  
        Our user-friendly platform makes it simple to get your Discord and Minecraft servers online in minutes!  
        <br><br>
        **🔹 Support Team:**  
        Need help? Our support team is available to assist you with any questions or issues.  
         <br><br>
        Ready to level up your Discord and Minecraft experience?  
        Visit our website and get started today! 🌐
        """,
        unsafe_allow_html=True
    )

# ==================== Join Page ====================
def join():
    st.title("🌟 How to Create a Minecraft Server")
    st.subheader("Your journey to hosting the ultimate Minecraft experience starts here! 👇")

    st.markdown("""
    ### 📋 Step-by-Step Guide
    1. **Click the button below** to access our step-by-step guide for creating your Minecraft server.
    2. **Join our Discord server** for access to tutorials, FAQs, and community support.
    3. **Contact our support team** via Discord, email, or phone for personalized assistance.
    4. **Customize your server settings** to match your vision, from game modes to mods and plugins.
    5. **Launch your server** and invite your friends to start your Minecraft adventure!
    """)

    if st.button("🚀 Start Creating Your Server"):
        st.success("Awesome! Join our Discord server or contact us for next steps.")
        st.markdown("[Velocity nodes panel](https://Velcotynodes.xyz)")

    st.markdown("### 🛠️ Why Choose Velocity Nodes?")
    st.markdown("""
    - **24/7 Uptime**: Our servers are optimized for reliability and minimal downtime.
    - **Affordable Plans**: Get premium hosting without breaking the bank.
    - **User-Friendly Interface**: Simple tools for beginners and advanced customization for pros.
    - **Community Support**: A vibrant Discord community to help you every step of the way.
    - **Secure Servers**: State-of-the-art security to keep your server safe and secure.
    """)

    st.markdown("### 📞 Get in Touch")
    st.markdown("""
    - **Discord**: Join our friendly community [here](#).  
    - **Email**: Reach us at **support@velocitynodes.com** for inquiries.  
    - **Phone**: Call us directly at **+91-12345-67890** for quick assistance.  
    """)

    st.markdown("### 🚀 Velocity Nodes Features")
    st.markdown("""
    Hosting your Minecraft server has never been easier! Here's what you can expect:
    - **Powerful Hardware**: High-performance servers for smooth gameplay.
    - **Global Accessibility**: Players from anywhere can join without lag.
    - **Custom Mod Support**: Easily install and manage mods or plugins.
    - **Scalability**: Upgrade your plan as your server grows.
    - **Instant Setup**: Get your server up and running in minutes!
    """)

    st.markdown("### 🔗 Join the Velocity Nodes Community")
    st.markdown("""
    Become a part of our growing Minecraft community!  
    - Share ideas, mods, and gameplay tips with fellow server owners.  
    - Learn from experts and access exclusive resources.  
    - **For username and password access**, contact us via Discord, email, or phone.
    """)

    st.markdown("---")
    st.markdown("""
    Made with ❤️ by **Velocity Nodes Team**.  
    Join us to create, play, and build memories in the world of Minecraft.  
    **Stay tuned for more updates and features!**
    """)

    st.sidebar.header("🌐 Explore More")
    st.sidebar.markdown("""
    - [📖 Documentation](#)  
    - [👥 Discord Community](#)  
    - [💸 Pricing Plans](#)
    """)

# ==================== Feedback Page ====================
def feedback():
    st.title("📢 Feedback Area")
    st.header("We'd Love to Hear from You!")
    st.subheader("If you're facing any issues, have bug reports, or need a membership refund, contact us here!")

    with st.form(key="feedback_form"):
        username = st.text_input("Username:")
        emails = st.text_input("Email:")
        phoneno = st.text_input("Phone number")
        details = st.text_area("Describe your issue or feedback in detail:")

        submit_button = st.form_submit_button("Submit")

        if submit_button:
            with open("feedbacks.txt", "a") as file:
                file.write(f"Username: {username}\n")
                file.write(f"Email: {emails}\n")
                file.write(f"Phone number: {phoneno}\n")
                file.write(f"Details: {details}\n")
                file.write("-" * 50 + "\n")

            st.success("Thank you for your feedback! Our team will get back to you soon.")

    st.markdown("""
    ### 🌟 Why Choose Velocity Nodes?
    - **24/7 Uptime**: Our servers are optimized for reliability and minimal downtime.
    - **Affordable Plans**: Get premium hosting without breaking the bank.
    - **User-Friendly Interface**: Simple tools for beginners and advanced customization for pros.
    - **Community Support**: A vibrant Discord community to help you every step of the way.
    - **Secure Servers**: State-of-the-art security to keep your server safe and secure.
    """)

    st.markdown("### 📞 How to Connect with Us")
    st.markdown("""
    - **Join our Discord Server**: Click [here](#) to join our active community. Get immediate assistance, updates, and support directly from our team and community members.  
    - **Phone Support**: Call us directly at **+91-12345-67890** for quick and personalized assistance.

    You can reach us at any time through these platforms. We aim to provide instant support through Discord or over the phone for urgent matters.
    """)

    st.markdown("""
    ### 📋 How to Get Started
    1. **Click the button below** to create your Minecraft server.
    2. **Join our Discord server** for access to tutorials, FAQs, and community support.
    3. **Contact our support team** via Discord or phone for personalized assistance.
    4. **Customize your server settings** to match your vision, from game modes to mods and plugins.
    5. **Launch your server** and invite your friends to start your Minecraft adventure!
    """)

    if st.button("🚀 Start Creating Your Server"):
        st.success("Awesome! Join our Discord server or contact us for next steps.")

    st.markdown("---")
    st.markdown("""
    Made with ❤️ by **Velocity Nodes Team**.  
    Join us to create, play, and build memories in the world of Minecraft.  
    **Stay tuned for more updates and features!**
    """)

    st.sidebar.header("🌐 Explore More")
    st.sidebar.markdown("""
    - [📖 Documentation](#)  
    - [👥 Discord Community](#)  
    - [💸 Pricing Plans](#)
    """)

# ==================== Login & Sign Up ====================
def login():
    USER_DATA_FILE = "users.txt"

    st.title("🚀 Welcome to Velocity Nodes!")
    st.subheader("Secure and Easy Login & Sign Up")

    with st.container():
        st.header("🔑 Login")

        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            login_button = st.form_submit_button("Login")

            if login_button:
                try:
                    with open(USER_DATA_FILE, "r") as file:
                        users = file.readlines()

                    valid_user = False
                    for user in users:
                        stored_username, _, stored_password = user.strip().split(",")
                        if username == stored_username and password == stored_password:
                            valid_user = True
                            break

                    if valid_user:
                        st.success("Successfully logged in!")
                    else:
                        st.error("Invalid username or password. Please try again.")
                except FileNotFoundError:
                    st.error("No user data found. Please sign up first.")

    with st.container():
        st.header("✨ Sign Up")

        with st.form("signup_form"):
            username_signup = st.text_input("Create Username")
            email_signup = st.text_input("Email Address")
            password_signup = st.text_input("Create Password", type="password")
            confirm_password_signup = st.text_input("Confirm Password", type="password")
            signup_button = st.form_submit_button("Sign Up")

            if signup_button:
                if password_signup == confirm_password_signup:
                    with open(USER_DATA_FILE, "a") as file:
                        file.write(f"{username_signup},{email_signup},{password_signup}\n")
                    st.success("Account created successfully! Please log in.")
                else:
                    st.error("Passwords do not match. Please try again.")

    with st.expander("❓ Need Help?"):
        st.markdown("""
        - **Forgot Password?**  
        Click [here](#) to reset your password.

        - **Already have an account?**  
        Click the **Login** button above.

        - **Need support?**  
        You can contact us via our **Discord** or by emailing support@velocitynodes.com.
        """)

    st.markdown("---")
    st.markdown("""
        Made with ❤️ by **Velocity Nodes Team**.  
        **Join us to create, play, and build memories in the world of Minecraft.**
    """)

# ==================== About Us ====================
def about():
    st.title("🚀 Welcome to Velocity Nodes")
    st.header("Your Gateway to Free 24/7 Minecraft Server Hosting")

    st.subheader("Founders & Vision")
    st.markdown("""
    **Velocity Nodes** was founded by **Script Evil** and **Dittebish**, two passionate individuals dedicated to empowering the Minecraft community.  
    Together, they provide affordable, reliable, and secure hosting services for Minecraft server owners,  
    making it easy for creators to thrive.
    """)

    st.markdown("### 🌟 Why Choose Velocity Nodes?")
    st.markdown("""
    - 🕒 **Free 24/7 Hosting** for Minecraft servers.
    - ⚙️ **Optimized Performance** for seamless gameplay.
    - 🛡️ **Secure Systems** to protect your data.
    - 💰 **Affordable Memberships** for premium features.
    """)

    st.image(
        "https://i.imgur.com/BTMaNKG.png",
        caption="Velocity Nodes - Empowering Minecraft Creators",
        use_column_width=True,
    )

    st.markdown("---")
    st.markdown("### 🔗 Get Started Now!")
    if st.button("Visit Our membership"):
        st.markdown("[Coming Soon!](https://yourwebsite.com)")

    st.markdown("---")
    st.markdown("""
    Made with ❤️ by **Script Evil** and **Dittebish**.
    """)

# ==================== Main Function ====================
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Join", "Login/Sign Up", "Feedback", "About Us"])

    if page == "Home":
        home()
    elif page == "Join":
        join()
    elif page == "Login/Sign Up":
        login()
    elif page == "Feedback":
        feedback()
    elif page == "About Us":
        about()

if __name__ == "__main__":
    main()
