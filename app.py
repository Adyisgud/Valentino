import streamlit as st
import random

# Set page config
st.set_page_config(
    page_title="Be My Valentine? 💕",
    page_icon="💘",
    layout="centered",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None
    }
)

# Initialize session state
if 'clicked_yes' not in st.session_state:
    st.session_state.clicked_yes = False
if 'no_button_top' not in st.session_state:
    st.session_state.no_button_top = 8  # Position 8 (right of center in middle row)
if 'previous_positions' not in st.session_state:
    st.session_state.previous_positions = [8]

# Custom CSS for styling and button positioning
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #ffeef8 0%, #ffe0f0 100%);
    }
    .center-text {
        text-align: center;
        font-size: 3em;
        color: #d91d87;
        font-weight: bold;
        margin: 20px 0;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.3);
    }
    .success-message {
        text-align: center;
        font-size: 2em;
        color: #c71585;
        padding: 40px;
        background: white;
        border-radius: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 20px;
        animation: fadeIn 0.5s;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: scale(0.9); }
        to { opacity: 1; transform: scale(1); }
    }
    div[data-testid="column"] {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .stButton > button {
        font-size: 1.2em;
        padding: 15px 40px;
        border-radius: 25px;
        font-weight: bold;
        transition: all 0.3s;
    }
    .stButton > button:hover {
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# Main content
if not st.session_state.clicked_yes:
    st.markdown("<h1 class='center-text'>💕 Will You Be My Valentine? 💕</h1>", unsafe_allow_html=True)
    
    # Display image in its own centered section (much larger)
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.image("Valentinopic.jpg", use_column_width=True)
    
    st.write("")
    st.write("")
    
    # Define grid positions (3 rows x 5 columns = 15 positions for buttons only)
    # Yes button at position 6 (middle row, left of center)
    yes_position = 6
    
    # No button starts at position 8 (middle row, right of center)
    no_position = st.session_state.no_button_top % 15
    
    # Make sure no_position doesn't overlap with yes
    if no_position == yes_position:
        no_position = 8
    
    # Create 3 rows of 5 columns each for buttons
    for row in range(3):
        cols = st.columns(5)
        for col_idx in range(5):
            current_position = row * 5 + col_idx
            
            with cols[col_idx]:
                if current_position == yes_position:
                    if st.button("❤️ YES! ❤️", key="yes_button", use_container_width=True):
                        st.session_state.clicked_yes = True
                        st.rerun()
                elif current_position == no_position:
                    if st.button("😢 No", key=f"no_button_{st.session_state.no_button_top}", use_container_width=True):
                        # Generate new position anywhere except yes_position and recent positions
                        forbidden_positions_list = [yes_position] + st.session_state.previous_positions[-3:]
                        new_position = random.randint(0, 14)
                        while new_position in forbidden_positions_list:
                            new_position = random.randint(0, 14)
                        st.session_state.previous_positions.append(new_position)
                        st.session_state.no_button_top = new_position
                        st.rerun()
                else:
                    st.write("")  # Empty space

else:
    # Success message
    st.balloons()
    st.markdown("""
        <div class='success-message'>
            <h1 style='color: #c71585;'>🎉 Yay! 🎉</h1>
            <h2 style='color: #c71585;'>Congrats! I'll see you on the 14th! 💕</h2>
            <p style='font-size: 1.2em; margin-top: 20px; color: #c71585;'>❤️ Can't wait! ❤️</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Optional: Add a cute GIF
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("https://media.giphy.com/media/3o6Zt6ML6BklcajjsA/giphy.gif", 
                 use_column_width=True)
