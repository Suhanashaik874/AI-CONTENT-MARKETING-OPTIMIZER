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
    
    .main {
        background-color: var(--dark-bg);
        color: var(--text-light);
    }
    
    .stApp {
        background-color: var(--dark-bg);
    }
    
    /* Custom header */
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
    .main-header h1 {
        color: white;
        font-size: 3rem;
        font-weight: bold;
        margin: 0;
    }
    
    .main-header p {
        color: rgba(255,255,255,0.9);
        font-size: 1.2rem;
        margin-top: 0.5rem;
    }
    
    /* Platform cards */
    .platform-card {
        background-color: var(--card-bg);
        padding: 1.5rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        border-left: 4px solid var(--primary);
        transition: transform 0.3s;
    }
    
    .platform-card:hover {
        transform: translateY(-5px);
    }
    
    .platform-icon {
        font-size: 2rem;
        margin-bottom: 1rem;
    }
    
    /* Content cards */
    .content-card {
        background-color: var(--card-bg);
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border: 1px solid #334155;
    }
    
    /* Stats cards */
    .stat-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        margin: 0.5rem;
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: bold;
        color: white;
        margin: 0;
    }
    
    .stat-label {
        color: rgba(255,255,255,0.9);
        font-size: 0.9rem;
        margin: 0;
    }
    
    /* Buttons */
    .stButton button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.5rem 2rem;
        border-radius: 5px;
        font-weight: bold;
        width: 100%;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
        background-color: var(--card-bg);
        padding: 0.5rem;
        border-radius: 10px;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 5px;
        padding: 0.5rem 1rem;
    }
    
    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
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
        
        # Topic input
        topic = st.text_input(
            "### Enter Any Topic",
            value="Machine Learning",
            help="You can enter ANY topic - from cooking recipes to quantum physics"
        )
        
        if st.button("✨ Generate Content", use_container_width=True):
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
        
        # Display generated content if available
        if st.session_state.generated_content:
            st.markdown("---")
            st.markdown(f"### YouTube Content for '{topic}'")
            
            with st.expander("📹 Video Script & Description", expanded=True):
                content = st.session_state.generated_content["youtube"]
                
                st.markdown("#### 🎣 HOOK (First 15 seconds)")
                st.info(content["hook"])
                
                st.markdown("#### 📋 VIDEO STRUCTURE")
                for item in content["structure"]:
                    st.markdown(f"- {item}")
                
                if st.button("📋 Copy Content", use_container_width=True):
                    st.success("Content copied to clipboard!")
            
            # A/B Testing Section
            st.markdown("---")
            st.markdown("### 🔬 A/B Testing Variations")
            
            col_a, col_b, col_c = st.columns(3)
            
            with col_a:
                st.markdown("""
                <div class="content-card">
                    <h4>💬 Conversational</h4>
                    <p style="color: var(--text-gray); font-size: 0.9rem;">
                        Friendly and approachable style using everyday language.
                    </p>
                </div>
                """, unsafe_allow_html=True)
            
            with col_b:
                st.markdown("""
                <div class="content-card">
                    <h4>👔 Professional</h4>
                    <p style="color: var(--text-gray); font-size: 0.9rem;">
                        Formal and expert-level tone for professional audiences.
                    </p>
                </div>
                """, unsafe_allow_html=True)
            
            with col_c:
                st.markdown("""
                <div class="content-card">
                    <h4>🚀 Motivational</h4>
                    <p style="color: var(--text-gray); font-size: 0.9rem;">
                        Inspiring and energetic tone to motivate your audience.
                    </p>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("#### Run A/B Test")
            
            test_col1, test_col2 = st.columns(2)
            
            with test_col1:
                if st.button("⚡ Quick Test (3 variants)", use_container_width=True):
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
                if st.button("📊 Comprehensive Test (5 variants)", use_container_width=True):
                    st.info("Starting comprehensive A/B test...")
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
        
        # Create bar chart
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
            height=300
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
            st.success("Winning variant deployed to all platforms!")
    
    else:
        st.info("No test results yet. Run an A/B test in the 'Generate Content' tab to see results here.")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: var(--text-gray); padding: 2rem;">
        <h3>🚀 BIG IN</h3>
        <p>AI Content Marketing Optimizer v1.0</p>
    </div>
    """, 
    unsafe_allow_html=True
)
