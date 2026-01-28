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
    st.session_state.no_button_top = 23  # Position 23 (right of center in bottom row)
if 'previous_positions' not in st.session_state:
    st.session_state.previous_positions = [23]

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
    
    # Define grid positions (5 rows x 5 columns = 25 positions)
    # Image occupies positions 6, 7, 8, 11, 12, 13, 16, 17, 18 (center 3x3 of 5x5 grid)
    image_positions = {6, 7, 8, 11, 12, 13, 16, 17, 18}
    
    # Yes button at position 21 (bottom row, left of center)
    yes_position = 21
    
    # No button starts at position 23 (bottom row, right of center)
    no_position = st.session_state.no_button_top
    
    # Make sure no_position doesn't overlap with yes or image
    forbidden_positions = image_positions | {yes_position}
    if no_position in forbidden_positions:
        no_position = 23
    
    # Create 5 rows of 5 columns each
    for row in range(5):
        cols = st.columns(5)
        for col_idx in range(5):
            current_position = row * 5 + col_idx
            
            with cols[col_idx]:
                if current_position in image_positions:
                    # Display image only once in the center position
                    if current_position == 12:  # Center of the image block
                        st.image("Valentinopic.jpg", 
                                width=1200)
                    else:
                        st.write("")  # Empty space for image area
                elif current_position == yes_position:
                    if st.button("❤️ YES! ❤️", key="yes_button", use_container_width=True):
                        st.session_state.clicked_yes = True
                        st.rerun()
                elif current_position == no_position:
                    if st.button("😢 No", key=f"no_button_{st.session_state.no_button_top}", use_container_width=True):
                        # Generate new position anywhere except yes_position and image_positions
                        forbidden_positions_list = list(forbidden_positions) + st.session_state.previous_positions[-3:]
                        new_position = random.randint(0, 24)
                        while new_position in forbidden_positions_list:
                            new_position = random.randint(0, 24)
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
