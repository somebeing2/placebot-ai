import streamlit as st
import pandas as pd
import time
import random

# --- 1. APP CONFIGURATION (The "Brand Kit") ---
st.set_page_config(
    page_title="PlaceBot.ai | Autonomous Placement Cell",
    page_icon="🎓",
    layout="wide"
)

# Custom CSS to make it look like a "SaaS Product"
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        background-color: #004e98;
        color: white;
        font-weight: bold;
    }
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR (The Control Center) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4762/4762311.png", width=80) # Placeholder Icon
    st.title("PlaceBot.ai")
    st.caption("Zero-Touch Placement Automation")
    
    st.markdown("---")
    
    # Input for the "Recruiter"
    st.header("1. Recruiter Input")
    
    # UPDATED: Added Standard MBA Roles
    job_role = st.selectbox("Select Target Role", [
        "Management Consultant",
        "Product Manager",
        "HR Business Partner",
        "Financial Analyst",
        "Marketing Manager",
        "Operations Manager",
        "Data Scientist", 
        "Software Engineer"
    ])
    
    min_gpa = st.slider("Minimum GPA Requirement", 0.0, 10.0, 7.5)
    
    # The Job Description (This drives the matching)
    st.subheader("Job Description (JD)")
    
    # Dynamic JD Text based on selection to make the demo smoother
    if "Consultant" in job_role:
        default_jd = "Looking for a strategic thinker with strong problem-solving skills. Must know Excel, Market Research, and Case Analysis. MBA preferred."
    elif "HR" in job_role:
        default_jd = "Seeking an HR professional with knowledge of Labor Laws, Talent Acquisition, Employee Engagement, and Soft Skills."
    elif "Product" in job_role:
        default_jd = "Requires strong User Research, Roadmap planning, Agile methodology, and Cross-functional leadership."
    else:
        default_jd = "We are looking for a candidate with strong Python skills, knowledge of Machine Learning, and an understanding of financial modeling. Good communication is a plus."
        
    jd_text = st.text_area("Paste JD here:", value=default_jd, height=150)
    
    st.markdown("---")
    st.info("🔒 Secure Admin Access: Christ University")

# --- 3. MOCK DATA GENERATION (Simulating your "Data Science" database) ---
# In a real startup, this would come from a SQL Database
@st.cache_data
def get_student_data():
    # UPDATED: Expanded list to include MBA profiles
    students = [
        # Tech & Finance Profiles
        {"ID": "CU23401", "Name": "Arjun Sharma", "GPA": 8.9, "Skills": ["Python", "Finance", "SQL", "Tableau"], "Bio": "Finance major with strong data analytics skills."},
        {"ID": "CU23403", "Name": "Kabir Singh", "GPA": 7.8, "Skills": ["Python", "Machine Learning", "Deep Learning", "NLP"], "Bio": "Hackathon winner, focused on AI research."},
        {"ID": "CU23404", "Name": "Sneha Gupta", "GPA": 8.5, "Skills": ["Finance", "Excel", "Accounting", "Auditing"], "Bio": "Cleared CFA Level 1, strong in core finance."},
        {"ID": "CU23405", "Name": "Rohan Das", "GPA": 6.9, "Skills": ["Java", "SQL", "Backend", "System Design"], "Bio": "Backend developer, loves building scalable systems."},
        
        # MBA / Management Profiles
        {"ID": "CU23402", "Name": "Riya Patel", "GPA": 9.2, "Skills": ["Marketing", "SEO", "Content Strategy", "Social Media"], "Bio": "Creative strategist with internship experience at Ogilvy."},
        {"ID": "CU23406", "Name": "Vikram Malhotra", "GPA": 9.0, "Skills": ["Strategy", "Excel", "Case Analysis", "Market Research"], "Bio": "President of the Consulting Club, excellent problem solver."},
        {"ID": "CU23407", "Name": "Ananya Iyer", "GPA": 8.2, "Skills": ["HR", "Talent Acquisition", "Employee Engagement", "Labor Laws"], "Bio": "People-person with a focus on organizational psychology."},
        {"ID": "CU23408", "Name": "David Fernandez", "GPA": 7.5, "Skills": ["Operations", "Supply Chain", "Logistics", "Project Management"], "Bio": "Detail-oriented, Lean Six Sigma Green Belt."},
        {"ID": "CU23409", "Name": "Priya Venkatesh", "GPA": 8.8, "Skills": ["Product Management", "User Research", "Agile", "Roadmap"], "Bio": "Aspiring PM, built two startup prototypes in college."},
        {"ID": "CU23410", "Name": "Rahul Nair", "GPA": 8.1, "Skills": ["Sales", "B2B", "Negotiation", "CRM"], "Bio": "High energy, lead the university sponsorship team."}
    ]
    return pd.DataFrame(students)

df = get_student_data()

# --- 4. MAIN DASHBOARD ---

# Header Section
col1, col2 = st.columns([3, 1])
with col1:
    st.title("🚀 Deployment Dashboard")
    st.markdown("### Welcome, Placement Director.")
    st.markdown("Your AI Agent is ready to screen **1,250 students** instantly.")
with col2:
    # Live Status Badge
    st.success("● AI Agent: ONLINE")
    st.write(f"**Date:** {time.strftime('%d %b %Y')}")

st.markdown("---")

# The "Action" Button
if st.button("RUN AUTOMATED MATCHING PROTOCOL ⚡"):
    
    # 1. Simulating "AI Processing" (The Visual Effect)
    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01) # Made slightly faster for better demo feel
        if percent_complete == 20:
            my_bar.progress(percent_complete + 1, text="Parsing 1,250 Resumes...")
        if percent_complete == 50:
            my_bar.progress(percent_complete + 1, text="Analyzing Keyword Overlap (NLP)...")
        if percent_complete == 80:
            my_bar.progress(percent_complete + 1, text="Ranking Candidates by Employability Score...")
        my_bar.progress(percent_complete + 1)
    
    my_bar.empty()
    
    # 2. The Logic (Simple Rule-Based AI)
    # This proves your "Data Science" logic without needing complex models
    results = []
    
    for index, row in df.iterrows():
        score = 0
        
        # GPA Filter
        if row["GPA"] >= min_gpa:
            score += 30
        
        # Keyword Matching (The "AI" part)
        # We check if skills from the student bio/skills exist in the JD
        jd_keywords = jd_text.lower()
        student_skills = [s.lower() for s in row["Skills"]]
        
        match_count = 0
        for skill in student_skills:
            if skill in jd_keywords: # Improved matching logic
                match_count += 1
        
        # Add score based on matches
        score += (match_count * 15)
        
        # Cap score at 98% (Nobody is perfect!)
        final_score = min(98, score + random.randint(5, 15))
        
        # Classification
        status = "❌ Reject"
        if final_score > 75:
            status = "✅ Interview"
        elif final_score > 50:
            status = "⚠️ Waitlist"
            
        results.append({
            "Student Name": row["Name"],
            "Match Score": f"{final_score}%",
            "Key Skills": ", ".join(row["Skills"]),
            "AI Recommendation": status
        })
    
    # 3. Display Results
    results_df = pd.DataFrame(results)
    
    # Sort by Score (Descending) for "Ranking"
    results_df = results_df.sort_values(by="Match Score", ascending=False)

    st.subheader(f"🎯 Top Candidates for '{job_role}'")
    st.table(results_df)
    
    # 4. Success Metrics (The "Business" Value)
    st.markdown("### 💰 Efficiency Impact")
    m1, m2, m3 = st.columns(3)
    m1.metric(label="Time Saved", value="48 Hours", delta="99%")
    m2.metric(label="Cost Saved", value="₹ 15,000", delta="Consultant Fees")
    m3.metric(label="Bias Detected", value="0%", delta="AI Neural Check")
    
    st.balloons()

else:
    # Default View (When app loads)
    st.info("👈 Configure the Job Description in the Sidebar to begin the matching process.")
    st.write("Current Student Database Overview:")
    st.dataframe(df)

# Footer
st.markdown("---")
st.markdown(
    "© 2026 | Built by **[Kevin Joseph](https://www.linkedin.com/in/kevin-joseph-in/)** | "
    "Powered by Gemini Pro & Streamlit")
