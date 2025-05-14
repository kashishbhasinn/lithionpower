import streamlit as st

# Page Configuration
st.set_page_config(page_title="Kashish Bhasin - Business Analyst Intern", layout="centered")

# Header
st.title("👩‍💼 Kashish Bhasin")
st.subheader("Aspiring Business Analyst Intern | BTech CSE - AI/ML")
st.write("📍 Noida | 📧 kashishbhasinn@gmail.com | 📱 +91 9811149303")
st.write("[LinkedIn](https://www.linkedin.com/in/kashish-bhasin) | [GitHub](https://github.com/kashishbhasinn)")

# About Section
st.header("📝 About Me")
st.write("""
I’m a BTech Computer Science student specializing in Artificial Intelligence and Machine Learning at Manipal University Jaipur, with a CGPA of 9.29. 
I’ve interned at DRDO and IIM Bangalore, worked on real-world AI applications, and bring a strong foundation in data-driven decision-making.
""")

# Skills
st.header("🧠 Skills")
skills = [
    "• Python, SQL, C, Excel, Tableau",
    "• Scikit-learn, TensorFlow, Hugging Face, LangChain",
    "• NLP, RAG, LLMs, Vector Databases (ChromaDB, FAISS, Pinecone)",
    "• Data Preprocessing, Feature Engineering, EDA",
    "• Agile Development, CI/CD, Cloud AI (AWS, Azure)"
]
for skill in skills:
    st.write(skill)

# Experience
st.header("💼 Experience")
st.subheader("AI Product Strategist Intern — Arogo AI, IIT Kharagpur")
st.write("- Led AI-driven mental health platform dev with CV + NLP.")
st.write("- Automated medical image analysis using Swin-UNETR, BLIP-2.")

st.subheader("AI Research Intern — DRDO DYSL-AI, Bangalore")
st.write("- Built RAG system using LangChain + ChromaDB for document retrieval.")
st.write("- Compared 15+ vector DBs, improved LLM workflows by 50%.")

st.subheader("Data Intern — IIM Bangalore")
st.write("- Automated scraping of 7–9 Cr records with Python.")
st.write("- Developed AI data pipelines, cut manual effort by 50%.")

# Projects
st.header("💡 Projects")
st.subheader("AI-Powered Resume Analysis System")
st.write("- Improved keyword match accuracy by 65%.")
st.write("- Tools: Python, Streamlit, Google Gemini API.")

st.subheader("AI Kitchen Assistant")
st.write("- Smart cooking assistant using voice and AI.")
st.write("- Tools: Streamlit, Gemini API, HuggingFace Transformers.")

st.subheader("Pre-Trained Image Classifier")
st.write("- Achieved 80% accuracy using PyTorch + pre-trained models.")

# Achievements
st.header("🏆 Achievements")
achievements = [
    "• AWS Udacity AI/ML Scholar – Top 2,000 globally",
    "• Treasurer, AI/ML Community – Boosted engagement by 200 attendees",
    "• PASCH Youth Scholar – 3-week scholarship in Germany"
]
for a in achievements:
    st.write(a)

# Why Me for Lithion Power
st.header("🚀 Why Me for Lithion Power?")
why_me = [
    "• BTech in AI/ML with Excel, Python skills",
    "• Built real-time dashboards using Streamlit, Gemini API",
    "• Interned at DRDO, IIM-B – used NLP, ChromaDB"
]
for point in why_me:
    st.write(point)

# Footer
st.markdown("---")
st.write("Feel free to connect or reach out via email. Ready to join immediately!")
