import os

def save_uploaded_file(image):
    os.makedirs('./app/uploads', exist_ok=True)
    file_path = os.path.join('./app/uploads', image.filename)
    image.save(file_path)
    return file_path

def clean_up_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

def recomendation(hair_type, face_type):
    # Definisi tabel gaya rambut dan penjelasan
    hairstyle_table = {
        "Rectangular": {
            "Straight": [
                ("Textured crops", "Adds volume and softness to balance angular features."),
                ("Side part with a fade", "Creates a structured yet versatile look."),
                ("Layered cuts", "Softens sharp angles and adds dimension."),
            ],
            "Wavy": [
                ("Medium length wavy styles (Bro Flow)", "Accentuates natural waves for a relaxed style."),
                ("Messy quiffs", "Adds volume to elongate the face."),
            ],
            "Curly": [
                ("Faded sides with curls on top", "Keeps the curls defined while reducing bulk."),
                ("Short afros", "Provides a clean, balanced look."),
            ],
            "Dreadlocks": [
                ("Medium length dreadlocks", "Elongates the face while maintaining a trendy style."),
                ("Low fade with dreadlocks", "Combines modern fades with the classic dreadlock look."),
            ],
            "Kinky": [
                ("Tapered styles to reduce volume", "Keeps a neat shape while balancing proportions."),
                ("Short tapered afro", "A clean style that highlights natural texture."),
            ],
        },
        "Square": {
            "Straight": [
                ("Buzz cuts", "Highlights strong jawlines for a bold look."),
                ("Crew cuts", "A classic style that complements angular features."),
                ("Slick backs", "Adds sleekness to a structured face shape."),
            ],
            "Wavy": [
                ("Side parts", "Balances sharp angles with soft waves."),
                ("Layered cuts", "Adds texture and volume to enhance the look."),
            ],
            "Curly": [
                ("Tapered curls", "Keeps curls neat while adding height."),
                ("Short textured cuts", "Highlights curls with a modern edge."),
            ],
            "Dreadlocks": [
                ("Short dreadlocks with fade", "Blends natural locks with clean fades."),
                ("Neat medium length locks", "Offers a balanced, structured appearance."),
            ],
            "Kinky": [
                ("Defined angular afro", "Creates sharp, bold lines for impact."),
                ("Tapered frohawk", "Adds height and texture for a striking look."),
            ],
        },
        "Oval": {
            "Straight": [
                ("Pompadours", "Adds height and draws attention upward."),
                ("Ivy League", "Combines sophistication with ease of maintenance."),
                ("Slick backs", "Highlights the symmetry of an oval face."),
            ],
            "Wavy": [
                ("Medium length wavy styles (Bro Flow)", "Enhances natural waves for a polished look."),
                ("Layered cuts", "Adds texture to complement balanced features."),
                ("Comb overs", "A timeless style that flatters oval shapes."),
            ],
            "Curly": [
                ("Tapered curls", "Keeps curls neat and defined."),
                ("Short textured cuts", "Adds volume and structure to curly hair."),
                ("Medium afros", "Balances volume while highlighting texture."),
            ],
            "Dreadlocks": [
                ("Medium length dreadlocks", "Frames the face with natural locks."),
                ("Side swept dreadlocks", "Adds asymmetry for a dynamic look."),
            ],
            "Kinky": [
                ("Rounded afro", "A balanced look that complements oval shapes."),
                ("Tapered styles to reduce volume", "Keeps a neat, manageable shape."),
            ],
        },
        "Round": {
            "Straight": [
                ("Pompadours", "Adds height to elongate the face."),
                ("Slick backs", "Creates a sleek, vertical effect."),
                ("Side part with a fade", "Balances round features with clean lines."),
            ],
            "Wavy": [
                ("Quiffs", "Adds volume and structure for a sharp appearance."),
                ("Textured crops", "Creates a modern, edgy style."),
            ],
            "Curly": [
                ("High fade with curly top", "Elongates the face with added height."),
                ("Short afros", "Keeps curls neat and proportional."),
            ],
            "Dreadlocks": [
                ("High fade with dreadlocks", "Adds height and contrast to the face."),
                ("Undercut with long locks", "Balances length with a modern undercut."),
            ],
            "Kinky": [
                ("Rounded afro", "Creates symmetry while maintaining natural texture."),
                ("Flat top", "Elongates the face with a bold statement."),
            ],
        },
    }

    # Validasi input
    if face_type not in hairstyle_table:
        return f"Face type '{face_type}' is not recognized."
    if hair_type not in hairstyle_table[face_type]:
        return f"Hair type '{hair_type}' is not recognized."

    # Hasil klasifikasi
    recommended_styles_with_explanations = hairstyle_table[face_type][hair_type]

    # Format output
    result = []
    for style, explanation in recommended_styles_with_explanations:
        result.append({"style": style, "explanation": explanation})

    return result

