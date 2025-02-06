import streamlit as st
import os
from PIL import Image

# Set App Title
st.title("Stelo Vienas Armor Generator")
st.subheader("Customize your armor and heraldry")

# Sidebar: Armor Customization
st.sidebar.header("Customize Your Armor")

# Armor Customization Options
under_armor = st.sidebar.selectbox("Under Armor", ["None", "Arming Doublet", "Chainmail Hauberk", "Leather Jerkin", "Brigandine"])
armor_material = st.sidebar.selectbox("Armor Material", ["Steel", "Bronze", "Gold", "Blackened Iron"])
helmet = st.sidebar.selectbox("Helmet", ["None", "Great Helm", "Bascinet", "Sallet", "Visored Helm"])
shoulder_armor = st.sidebar.selectbox("Shoulder Armor", ["None", "Spaulders", "Pauldrons", "Scaled Shoulders"])
over_armor = st.sidebar.multiselect("Over Armor", ["None", "Hooded Cloak", "Flowing Cape", "Heraldic Surcoat", "Fur-Lined Mantle"])
engraving_style = st.sidebar.selectbox("Engraving Style", ["None", "Floral", "Runes", "Geometric"])
design = st.sidebar.selectbox("Decorative Design", ["None", "Floral Engravings", "Geometric Patterns", "Heraldic Symbols", "Mythical Creatures"])

# Heraldic Customization
st.sidebar.header("Heraldic Creator")
shield_shape = st.sidebar.selectbox("Shield Shape", ["Heater", "Round", "Kite", "Escutcheon", "Pavise"])
heraldic_symbol = st.sidebar.selectbox("Heraldic Symbol", ["None", "Lion Rampant", "Fleur-de-lis", "Cross Pattee", "Double-headed Eagle", "Stag", "Dragon"])
shield_color = st.sidebar.color_picker("Shield Background Color", "#FFFFFF")
border_color = st.sidebar.color_picker("Border Color", "#000000")
symbol_color = st.sidebar.color_picker("Heraldic Symbol Color", "#FFD700")
pattern = st.sidebar.selectbox("Heraldic Pattern", ["None", "Quartered", "Checkered", "Diagonal Bands", "Stripes"])

# Color Customization
st.sidebar.header("Color Customizations")
base_layer_color = st.sidebar.color_picker("Base Layer Color (Tunic/Gambeson)", "#B87333")
armor_accent_color = st.sidebar.color_picker("Armor Accent Color", "#FFD700")
cloak_color = st.sidebar.color_picker("Cloak or Cape Color", "#5B84B1")

# AI Prompt Generator
st.header("Generated AI Prompt")
prompt = f"A warrior clad in {armor_material.lower()} armor. "
if under_armor != "None":
    prompt += f"Underneath, they wear a {under_armor.lower()} dyed {base_layer_color}. "
if over_armor and "None" not in over_armor:
    prompt += f"Over the armor, they wear {', '.join(over_armor).lower()}, dyed {cloak_color}. "
if helmet != "None":
    prompt += f"They wear a {helmet.lower()} on their head. "
if shoulder_armor != "None":
    prompt += f"Their shoulders are protected by {shoulder_armor.lower()}. "
if design != "None":
    prompt += f"The armor is adorned with {design.lower()} designs. "
if engraving_style != "None":
    prompt += f"The engravings feature {engraving_style.lower()} patterns. "
prompt += f"The armor is accented with {armor_accent_color}."

st.text_area("AI Prompt", value=prompt, height=150)

# Function to Generate Heraldic Shield
def generate_heraldic_shield():
    width, height = 400, 500
    image = Image.new("RGBA", (width, height), shield_color)
    draw = ImageDraw.Draw(image)

    # Add border
    border_width = 10
    draw.rectangle([border_width, border_width, width - border_width, height - border_width], outline=border_color, width=border_width)

    # Add Patterns
    if pattern == "Quartered":
        draw.line([(width//2, 0), (width//2, height)], fill=border_color, width=5)
        draw.line([(0, height//2), (width, height//2)], fill=border_color, width=5)
    elif pattern == "Checkered":
        for i in range(0, width, width//8):
            for j in range(0, height, height//8):
                if (i+j) % 2 == 0:
                    draw.rectangle([(i, j), (i+width//8, j+height//8)], fill=border_color)
    elif pattern == "Diagonal Bands":
        for i in range(0, width, width//6):
            draw.line([(i, 0), (0, i)], fill=border_color, width=5)
            draw.line([(width, i), (i, height)], fill=border_color, width=5)
    elif pattern == "Stripes":
        for i in range(0, height, height//6):
            draw.rectangle([(0, i), (width, i+height//12)], fill=border_color)

    # Placeholder for Heraldic Symbol
    if heraldic_symbol != "None":
        draw.ellipse([(width//3, height//3), (2*width//3, 2*height//3)], fill=symbol_color)

    return image

# Display Heraldic Shield
st.header("Your Custom Heraldic Shield")
shield_image = generate_heraldic_shield()
st.image(shield_image, caption="Generated Heraldry", use_column_width=True)

# Download Button for Heraldic Shield
img_bytes = shield_image.tobytes()
st.download_button("Download Heraldic Shield", data=img_bytes, file_name="heraldic_shield.png", mime="image/png")
