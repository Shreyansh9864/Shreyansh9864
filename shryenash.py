import streamlit as st

# Page Navigation with Sidebar
page = st.sidebar.radio("Select a page", ["Home"])

if page == "Home":
    # Create two columns for content layout
    col1, col2 = st.columns([1, 2])  # Adjust the ratio to control the width of columns

    # Add the image to the first column
    with col1:
        st.image("https://i.ibb.co/McNrwYq/11zon-cropped.png", width=200)

    # Add styled text to the second column with different colors for words
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

    # Add description and bold first 4 lines
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
