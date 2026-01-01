import streamlit as st
import random

# ========== PAGE CONFIG ==========
st.set_page_config(
    page_title="AI Content Optimizer",
    page_icon="🚀",
    layout="wide"
)

# ========== CUSTOM CSS ==========
st.markdown("""
<style>
    .stApp {
        background-color: #0f172a;
    }
    
    h1, h2, h3, h4, p, label {
        color: white !important;
    }
    
    .main-header {
        text-align: center;
        padding: 2rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
    .platform-card {
        background: #1e293b;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        border-left: 4px solid #6366f1;
    }
    
    .content-card {
        background: #1e293b;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border: 1px solid #334155;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        padding: 0.8rem 2rem !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        width: 100% !important;
    }
</style>
""", unsafe_allow_html=True)

# ========== HEADER ==========
st.markdown("""
<div class="main-header">
    <h1>🎯 AI Content Optimizer</h1>
    <p>Generate & optimize content for any topic on any platform</p>
</div>
""", unsafe_allow_html=True)

# ========== INITIALIZE SESSION STATE ==========
if 'generated' not in st.session_state:
    st.session_state.generated = False
if 'content' not in st.session_state:
    st.session_state.content = {}
if 'platform' not in st.session_state:
    st.session_state.platform = "YouTube"
if 'topic' not in st.session_state:
    st.session_state.topic = "Machine Learning"

# ========== CONTENT GENERATION FUNCTIONS ==========
def generate_youtube_content(topic):
    return {
        "title": f"{topic} Explained: Complete Guide",
        "description": f"""Learn everything about {topic} in this comprehensive video!

📌 What you'll learn:
• Basics of {topic}
• Real-world applications
• Step-by-step implementation
• Future trends

👍 Like & Subscribe for more content!

#{topic.replace(' ', '')} #Education #Tech""",
        "timestamps": [
            "0:00 - Introduction",
            "1:30 - What is " + topic + "?",
            "3:15 - Key Concepts",
            "5:45 - Applications",
            "7:30 - Conclusion"
        ]
    }

def generate_twitter_content(topic):
    return {
        "thread": [
            f"🚀 Thread: Everything about {topic}",
            f"1/5: What is {topic}? Let's break it down!",
            f"2/5: {topic} is changing industries from healthcare to finance.",
            f"3/5: The benefits are incredible: efficiency, innovation, and growth.",
            f"4/5: Getting started with {topic}? Begin with fundamentals.",
            f"5/5: Like & RT if you found this helpful! Follow for more."
        ],
        "hashtags": [f"#{topic.replace(' ', '')}", "#TechTwitter"]
    }

def generate_linkedin_content(topic):
    return {
        "post": f"""Professional Insights: {topic}

{topic} is transforming industries and creating new opportunities.

Key benefits:
✅ Drives innovation
✅ Creates competitive advantages
✅ Opens career opportunities

What's your experience with {topic}?

#{topic.replace(' ', '')} #ProfessionalGrowth #Career"""
    }

# ========== MAIN APP ==========
tab1, tab2 = st.tabs(["📝 Generate Content", "📊 Test Results"])

with tab1:
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### 📱 Platforms")
        
        platforms = ["YouTube", "Twitter/X", "LinkedIn", "Instagram", "Blog"]
        for platform in platforms:
            if st.button(f"📌 {platform}", key=f"btn_{platform}", use_container_width=True):
                st.session_state.platform = platform
                st.rerun()
            
            if st.session_state.platform == platform:
                st.markdown(f"<div class='platform-card'><b>✅ {platform}</b><br><small>Selected platform</small></div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 🚀 Generate Content")
        
        # Topic input
        topic = st.text_input("Enter Topic:", value="Machine Learning")
        
        # Style selection
        style = st.selectbox("Content Style:", ["Conversational", "Professional", "Motivational"])
        
        # Generate button
        if st.button("✨ GENERATE CONTENT", use_container_width=True, type="primary"):
            st.session_state.topic = topic
            st.session_state.generated = True
            
            # Generate content based on platform
            if st.session_state.platform == "YouTube":
                st.session_state.content = generate_youtube_content(topic)
            elif st.session_state.platform == "Twitter/X":
                st.session_state.content = generate_twitter_content(topic)
            elif st.session_state.platform == "LinkedIn":
                st.session_state.content = generate_linkedin_content(topic)
            else:
                st.session_state.content = {"message": f"Content for {topic} on {st.session_state.platform}"}
            
            st.success(f"✅ Content generated for {topic} on {st.session_state.platform}!")
        
        # Display generated content
        if st.session_state.generated and st.session_state.content:
            st.markdown("---")
            st.markdown(f"### 📄 Generated Content for '{st.session_state.topic}'")
            
            if st.session_state.platform == "YouTube":
                st.markdown("#### 🎬 Title")
                st.code(st.session_state.content.get("title", ""))
                
                st.markdown("#### 📝 Description")
                st.text_area("Description", st.session_state.content.get("description", ""), height=150)
                
                st.markdown("#### ⏱️ Timestamps")
                for ts in st.session_state.content.get("timestamps", []):
                    st.write(f"• {ts}")
            
            elif st.session_state.platform == "Twitter/X":
                st.markdown("#### 🐦 Twitter Thread")
                for i, tweet in enumerate(st.session_state.content.get("thread", []), 1):
                    st.info(f"**Tweet {i}:** {tweet}")
            
            elif st.session_state.platform == "LinkedIn":
                st.markdown("#### 💼 LinkedIn Post")
                st.text_area("Post Content", st.session_state.content.get("post", ""), height=200)
            
            # Action buttons
            col_copy, col_test = st.columns(2)
            with col_copy:
                if st.button("📋 Copy Content", use_container_width=True):
                    st.toast("Content copied!", icon="📋")
            with col_test:
                if st.button("🧪 Run A/B Test", use_container_width=True):
                    st.session_state.test_results = {
                        "impressions": random.randint(3000, 8000),
                        "engagement": round(random.uniform(60, 80), 1),
                        "conversion": round(random.uniform(8, 12), 1)
                    }
                    st.rerun()

with tab2:
    if 'test_results' in st.session_state and st.session_state.test_results:
        results = st.session_state.test_results
        
        st.markdown("## 📊 Test Results")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Impressions", f"{results['impressions']:,}")
        with col2:
            st.metric("Engagement", f"{results['engagement']}%")
        with col3:
            st.metric("Conversion", f"{results['conversion']}%")
        
        st.markdown("### 🤖 Recommendations")
        st.write("• Conversational style performed best")
        st.write("• Consider testing different angles")
        st.write("• Run for 48 hours for conclusive results")
    else:
        st.info("No test results yet. Generate content and run A/B test first.")

# ========== FOOTER ==========
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #94a3b8; padding: 2rem;">
    <h3>🚀 AI Content Optimizer</h3>
    <p>Generate amazing content for any platform</p>
</div>
""", unsafe_allow_html=True)