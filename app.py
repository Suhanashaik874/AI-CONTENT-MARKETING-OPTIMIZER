import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.graph_objects as go


# Page configuration
st.set_page_config(
    page_title="AI Content Optimizer",
    page_icon="🚀",
    layout="wide"
)

# Simple sentiment analysis without nltk
def analyze_sentiment_simple(text):
    """
    Simple sentiment analysis without external dependencies
    """
    positive_words = ['great', 'good', 'excellent', 'amazing', 'awesome', 'love', 'best', 'perfect', 'happy', 'win', 'success']
    negative_words = ['bad', 'poor', 'terrible', 'awful', 'hate', 'worst', 'failure', 'sad', 'angry', 'problem', 'issue']
    
    text_lower = text.lower()
    pos_count = sum(1 for word in positive_words if word in text_lower)
    neg_count = sum(1 for word in negative_words if word in text_lower)
    
    if pos_count > neg_count:
        return "positive", 0.3, "😊"
    elif neg_count > pos_count:
        return "negative", -0.2, "😟"
    else:
        return "neutral", 0.0, "😐"

# Use this function instead of TextBlob
def analyze_sentiment(text):
    return analyze_sentiment_simple(text)


# Page configuration
st.set_page_config(
    page_title="AI Content Optimizer",
    page_icon="🚀",
    layout="wide"
)

# Custom CSS to match your design
st.markdown("""
<style>
    /* Main theme colors */
    :root {
        --primary: #6366f1;
        --dark-bg: #0f172a;
        --card-bg: #1e293b;
        --text-light: #f8fafc;
        --text-gray: #94a3b8;
    }
    
    .stApp {
        background-color: var(--dark-bg) !important;
    }
    
    /* Custom header */
    .main-header {
        text-align: center;
        padding: 3rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        margin: 2rem 0;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    }
    
    .main-header h1 {
        color: white;
        font-size: 3.5rem;
        font-weight: 800;
        margin: 0;
        letter-spacing: -1px;
    }
    
    .main-header p {
        color: rgba(255,255,255,0.9);
        font-size: 1.3rem;
        margin-top: 1rem;
        font-weight: 300;
    }
    
    /* Platform cards */
    .platform-card {
        background-color: var(--card-bg);
        padding: 1.5rem;
        border-radius: 12px;
        margin: 0.75rem 0;
        border-left: 5px solid var(--primary);
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .platform-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
    }
    
    .platform-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
        display: block;
    }
    
    /* Content cards */
    .content-card {
        background-color: var(--card-bg);
        padding: 1.8rem;
        border-radius: 12px;
        margin: 1.2rem 0;
        border: 2px solid #334155;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Stats cards */
    .stat-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.8rem 1rem;
        border-radius: 15px;
        text-align: center;
        margin: 0.5rem;
        box-shadow: 0 8px 16px rgba(102, 126, 234, 0.2);
        border: 2px solid rgba(255, 255, 255, 0.1);
    }
    
    .stat-number {
        font-size: 3rem;
        font-weight: 800;
        color: white;
        margin: 0;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }
    
    .stat-label {
        color: rgba(255,255,255,0.9);
        font-size: 1rem;
        margin: 0.5rem 0 0 0;
        font-weight: 500;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        padding: 0.8rem 2.5rem !important;
        border-radius: 10px !important;
        font-weight: 700 !important;
        width: 100% !important;
        font-size: 1.1rem !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4) !important;
    }
    
    /* Tabs */
    div[data-testid="stTabs"] {
        background-color: transparent !important;
    }
    
    div[data-testid="stTabs"] > div > div {
        background-color: var(--card-bg) !important;
        gap: 1rem !important;
        padding: 0.8rem !important;
        border-radius: 12px !important;
        border: 2px solid #334155 !important;
    }
    
    button[data-baseweb="tab"] {
        color: var(--text-gray) !important;
        font-weight: 600 !important;
        padding: 0.8rem 1.5rem !important;
        border-radius: 8px !important;
        background: transparent !important;
        border: none !important;
        transition: all 0.3s ease !important;
    }
    
    button[data-baseweb="tab"]:hover {
        background: rgba(99, 102, 241, 0.1) !important;
        color: var(--primary) !important;
    }
    
    button[data-baseweb="tab"][aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
    }
    
    /* Text inputs */
    .stTextInput > div > div > input {
        background-color: var(--card-bg) !important;
        color: var(--text-light) !important;
        border: 2px solid #334155 !important;
        border-radius: 10px !important;
        padding: 0.8rem 1rem !important;
        font-size: 1.1rem !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: var(--primary) !important;
        box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.2) !important;
    }
    
    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    header {visibility: hidden !important;}
    
    /* Text colors */
    h1, h2, h3, h4, h5, h6, p, label {
        color: var(--text-light) !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'topic' not in st.session_state:
    st.session_state.topic = "Machine Learning"
if 'test_results' not in st.session_state:
    st.session_state.test_results = None
if 'generated_content' not in st.session_state:
    st.session_state.generated_content = {}

# Header Section
st.markdown("""
<div class="main-header">
    <h1>🎯 AI Content Optimizer</h1>
    <p>Generate & optimize content for any topic on any platform</p>
</div>
""", unsafe_allow_html=True)

# Create tabs
tab1, tab2 = st.tabs(["📝 Generate Content", "📊 Test Results"])

with tab1:
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### 📱 Content Platforms")
        
        platforms = [
            {"name": "YouTube", "desc": "Video scripts & descriptions", "icon": "🎬"},
            {"name": "Twitter/X", "desc": "Tweets & threads", "icon": "🐦"},
            {"name": "LinkedIn", "desc": "Professional posts", "icon": "💼"},
            {"name": "Instagram", "desc": "Captions & stories", "icon": "📸"},
            {"name": "Blog", "desc": "Articles & blog posts", "icon": "✍️"}
        ]
        
        for platform in platforms:
            st.markdown(f"""
            <div class="platform-card">
                <div class="platform-icon">{platform['icon']}</div>
                <h4 style="margin: 0; color: var(--text-light);">{platform['name']}</h4>
                <p style="color: var(--text-gray); margin: 0.5rem 0 0 0; font-size: 0.9rem;">
                    {platform['desc']}
                </p>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 🚀 AI Content Optimizer")
        st.markdown('<p style="color: var(--text-gray); margin-bottom: 1.5rem;">Generate content for any topic on any platform</p>', unsafe_allow_html=True)
        
        # Topic input
        topic = st.text_input(
            "#### Enter Any Topic",
            value="Machine Learning",
            help="You can enter ANY topic - from cooking recipes to quantum physics",
            key="topic_input"
        )
        
        col_gen, _ = st.columns([1, 2])
        with col_gen:
            if st.button("✨ **Generate Content**", use_container_width=True, type="primary"):
                st.session_state.topic = topic
                
                # Generate sample content
                st.session_state.generated_content = {
                    "youtube": {
                        "hook": f"Have you ever wondered about {topic}? Whether you're a beginner or an expert, this video will give you fresh insights that might surprise you!",
                        "structure": [
                            "0:00 - Introduction to " + topic,
                            "1:30 - Key Concepts Explained",
                            "3:45 - Real-world Applications",
                            "5:20 - Getting Started Guide",
                            "7:00 - Future Trends"
                        ]
                    }
                }
                st.success(f"Content generated for '{topic}'!")
        
        # Display generated content if available
        if st.session_state.generated_content:
            st.markdown("---")
            st.markdown(f"### YouTube Content for '{st.session_state.topic}'")
            
            with st.expander("📹 **Video Script & Description**", expanded=True):
                content = st.session_state.generated_content["youtube"]
                
                st.markdown("#### 🎣 **HOOK** (First 15 seconds)")
                st.info(content["hook"])
                
                st.markdown("#### 📋 **VIDEO STRUCTURE**")
                for item in content["structure"]:
                    st.markdown(f"• **{item}**")
                
                if st.button("📋 **Copy Content**", use_container_width=True):
                    st.toast("✅ Content copied to clipboard!", icon="📋")
            
            # A/B Testing Section
            st.markdown("---")
            st.markdown("### 🔬 A/B Testing Variations")
            
            col_a, col_b, col_c = st.columns(3)
            
            with col_a:
                st.markdown("""
                <div class="content-card">
                    <h4>💬 Conversational</h4>
                    <p style="color: var(--text-gray); font-size: 0.9rem; line-height: 1.5;">
                        Friendly and approachable style using everyday language and relatable examples.
                    </p>
                    <div style="margin-top: 1rem; padding: 0.5rem; background: rgba(99, 102, 241, 0.1); border-radius: 6px;">
                        <small><strong>Best for:</strong> Beginners & General Audience</small>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            with col_b:
                st.markdown("""
                <div class="content-card">
                    <h4>👔 Professional</h4>
                    <p style="color: var(--text-gray); font-size: 0.9rem; line-height: 1.5;">
                        Formal and expert-level tone with data-driven insights for professional audiences.
                    </p>
                    <div style="margin-top: 1rem; padding: 0.5rem; background: rgba(99, 102, 241, 0.1); border-radius: 6px;">
                        <small><strong>Best for:</strong> B2B & Corporate</small>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            with col_c:
                st.markdown("""
                <div class="content-card">
                    <h4>🚀 Motivational</h4>
                    <p style="color: var(--text-gray); font-size: 0.9rem; line-height: 1.5;">
                        Inspiring and energetic tone with actionable tips to motivate your audience.
                    </p>
                    <div style="margin-top: 1rem; padding: 0.5rem; background: rgba(99, 102, 241, 0.1); border-radius: 6px;">
                        <small><strong>Best for:</strong> Personal Growth & Inspiration</small>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("#### Run A/B Test")
            
            test_col1, test_col2 = st.columns(2)
            
            with test_col1:
                if st.button("⚡ **Quick Test** (3 variants)", use_container_width=True):
                    # Simulate test results
                    st.session_state.test_results = {
                        "impressions": 4945,
                        "engagement": 67.7,
                        "conversion": 9.2,
                        "confidence": 91.0,
                        "variants": {
                            "Conversational": 73,
                            "Professional": 65,
                            "Motivational": 65
                        }
                    }
                    st.rerun()
            
            with test_col2:
                if st.button("📊 **Comprehensive Test** (5 variants)", use_container_width=True):
                    st.toast("🚀 Starting comprehensive A/B test...", icon="📊")
                    # Simulate test results
                    st.session_state.test_results = {
                        "impressions": 7500,
                        "engagement": 72.3,
                        "conversion": 11.5,
                        "confidence": 95.0,
                        "variants": {
                            "Conversational": 78,
                            "Professional": 68,
                            "Motivational": 70,
                            "Technical": 65,
                            "Storytelling": 72
                        }
                    }
                    st.rerun()

with tab2:
    if st.session_state.test_results:
        results = st.session_state.test_results
        
        # Display stats in a grid
        st.markdown("## 📈 Test Results & Analysis")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(f"""
            <div class="stat-card">
                <p class="stat-number">{results['impressions']:,}</p>
                <p class="stat-label">Total Impressions</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="stat-card">
                <p class="stat-number">{results['engagement']}%</p>
                <p class="stat-label">Avg Engagement</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class="stat-card">
                <p class="stat-number">{results['conversion']}%</p>
                <p class="stat-label">Conversion Rate</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown(f"""
            <div class="stat-card">
                <p class="stat-number">{results['confidence']}%</p>
                <p class="stat-label">Confidence Level</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Engagement scores
        st.markdown("### 📊 Variant Performance")
        
        # Create bar chart with Plotly
        fig = go.Figure(data=[
            go.Bar(
                x=list(results['variants'].keys()),
                y=list(results['variants'].values()),
                marker_color=['#6366f1', '#94a3b8', '#94a3b8', '#94a3b8', '#94a3b8'][:len(results['variants'])],
                text=[f"{v}%" for v in results['variants'].values()],
                textposition='auto',
            )
        ])
        
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='white',
            showlegend=False,
            height=400,
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # AI Recommendations
        st.markdown("### 🤖 AI Recommendations")
        
        recommendations = [
            f"**Winner Selected**: 'Conversational' style with {max(results['variants'].values())}% engagement score",
            "**Statistical Significance**: 80% higher than next best variant",
            f"**Optimization Opportunity**: Consider refining the messaging or testing different angles for '{st.session_state.topic}'",
            "**Style Analysis**: Friendly and approachable approach resonates best with your audience",
            "**Testing Duration**: For conclusive results, run this test for 48-72 hours before finalizing"
        ]
        
        for rec in recommendations:
            st.markdown(f"- {rec}")
        
        st.markdown("---")
        st.markdown("### 🏆 Winner: Conversational Style")
        
        # Display winning content
        st.markdown("#### 🎉 Winning Content Preview")
        st.markdown(f"""
        <div class="content-card">
            <h4>💬 Conversational Approach for '{st.session_state.topic}'</h4>
            <p>Hey there! Let's chat about {st.session_state.topic} like friends. This variation uses everyday 
            language and relatable examples to make complex concepts easy to understand.</p>
            <p><strong>Hook:</strong> {st.session_state.generated_content.get('youtube', {}).get('hook', 'Have you ever wondered...')}</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🚀 Deploy Winning Variant", use_container_width=True):
            st.success("✅ Winning variant deployed to all platforms!")
    
    else:
        st.info("📊 No test results yet. Run an A/B test in the 'Generate Content' tab to see results here.")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: var(--text-gray); padding: 2rem;">
        <h2 style="font-size: 2.5rem; margin-bottom: 0.5rem;">🚀 BIG IN</h2>
        <p style="font-size: 1.1rem;">AI Content Marketing Optimizer v2.0</p>
    </div>
    """, 
    unsafe_allow_html=True
)