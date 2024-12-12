import streamlit as st

st.logo("https://storage.googleapis.com/hairmatch-frontend-asset/assets/black-logo.png")

st.title("Contact Us")
st.subheader("Meet our team who contributed in this Project!")

contacts = [
    {
        "name": "Robby Agustino",
        "photo": "https://storage.googleapis.com/hairmatch-frontend-asset/assets/PP_Robby.jpg",
        "description": "Project Leader & Cloud Engineer - Led the team in successfully planning and executing the project. Designed and developed the entire web structure, built APIs, and created responsive front-end applications. Skilled in cloud computing, web development, and DevOps.",
        "contact": """
            <a href="mailto:robby.agn@gmail.com"><i class="fas fa-envelope"></i></a>
            <a href="https://github.com/rotinoo" target="_blank"><i class="fab fa-github"></i></a>
            <a href="https://www.linkedin.com/in/robby-agustino/" target="_blank"><i class="fab fa-linkedin"></i></a>
        """
    },
    {
        "name": "Timothy Mulya Cahyana",
        "photo": "https://storage.googleapis.com/hairmatch-frontend-asset/assets/PP_Timothy.jpg",
        "description": "Machine Learning Engineer - Developed and trained machine learning models for accurate face shape recognition and hair type classification. Expertise in data preprocessing, model optimization, and implementing cutting-edge algorithms to enhance predictive accuracy.",
        "contact": """
            <a href="mailto:timothymulyacahyana@gmail.com"><i class="fas fa-envelope"></i></a>
        """
    },
    {
        "name": "Chornelius Aneba Moza Ikratama",
        "photo": "https://storage.googleapis.com/hairmatch-frontend-asset/assets/PP_Moza_2.jpg",
        "description": "Data Scientist - Specialized in collecting, analyzing, and interpreting data using advanced statistical techniques. Played a crucial role in gathering data for hairstyle recommendation",
        "contact": """
            <a href="mailto:choeliusmoza@gmail.com"><i class="fas fa-envelope"></i></a>
        """
    },
    {
        "name": "Siti Nur Hasanah",
        "photo": "https://storage.googleapis.com/hairmatch-frontend-asset/assets/PP_Siti.jpg",
        "description": "Assisted in creating basic documentation and helped organize project files. Contributed to team communication and task tracking.",
        "contact": """
            <a href="mailto:sitiinuurhasanah@gmail.com"><i class="fas fa-envelope"></i></a>
        """
    },
    {
        "name": "Jordan Adzani",
        "photo": "https://storage.googleapis.com/hairmatch-frontend-asset/assets/PP_Jordan.png",
        "description": "Machine Learning Cohort - Tried on designing and developing the hairtype Classification model",
        "contact": """
            <a href="mailto:jordan.adzani23@gmail.com"><i class="fas fa-envelope"></i></a>
        """
    },
    {
        "name": "Muhammad Rivan Prawira Gustha",
        "photo": "https://storage.googleapis.com/hairmatch-frontend-asset/assets/PP_Rivan.jpeg",
        "description": "Cloud Computing Cohort - Assisted with frontend development in the project.",
        "contact": """
            <a href="mailto:prawiraa.rivan@gmail.com"><i class="fas fa-envelope"></i></a>
        """
    },
]

# Zigzag layout with clickable links
for i, contact in enumerate(contacts):
    st.markdown(
        f"""
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
        <style>
            .contact-container {{
                display: flex;
                align-items: center;
                flex-direction: row;
                margin-bottom: 30px;
            }}
            .contact-container img {{
                width: 150px;
                height: 150px;
                border-radius: 50%;
                margin: 0 20px;
            }}
            .contact-container div {{
                text-align: left;
            }}
            @media (max-width: 768px) {{
                .contact-container {{
                    flex-direction: column;
                    align-items: center;
                }}
                .contact-container img {{
                    margin: 0 0 20px 0;
                }}
                .contact-container div {{
                    text-align: center;
                }}
            }}
        </style>
        <div class="contact-container">
            <img src="{contact['photo']}" alt="Photo of {contact['name']}">
            <div>
                <h3 style="font-size:20px; margin:0;">{contact['name']}</h3>
                <p style="font-size:16px; margin-bottom: 10px;">{contact['description']}</p>
                <p style="font-size:25px; margin:0; margin-bottom: 15px ;text-align: right;">{contact['contact']}</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
