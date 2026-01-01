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
    /* Main container */
    .main-container {
        background: #f5f7fa;
    }
    
    /* Header */
    .main-header {
        font-size: 32px;
        font-weight: 800;
        color: #1a2332;
        margin-bottom: 8px;
    }
    
    .sub-header {
        color: #666;
        font-size: 16px;
        margin-bottom: 30px;
    }
    
    /* Cards */
    .card {
        background: white;
        border-radius: 12px;
        padding: 25px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
        border: 1px solid #e2e8f0;
        margin-bottom: 20px;
    }
    
    .card-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
        padding-bottom: 15px;
        border-bottom: 1px solid #e2e8f0;
    }
    
    .card-title {
        font-size: 20px;
        font-weight: 700;
        color: #1a2332;
    }
    
    .card-subtitle {
        color: #666;
        font-size: 14px;
        margin-top: 5px;
    }
    
    /* Badges */
    .badge {
        padding: 6px 16px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
    }
    
    .badge-blue {
        background: #dbeafe;
        color: #1d4ed8;
    }
    
    .badge-green {
        background: #d1fae5;
        color: #065f46;
    }
    
    .badge-orange {
        background: #fef3c7;
        color: #92400e;
    }
    
    /* Platform buttons */
    .platform-btn {
        padding: 12px;
        border: 2px solid #e0e6ff;
        border-radius: 8px;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s;
        font-weight: 500;
        background: white;
    }
    
    .platform-btn:hover {
        border-color: #667eea;
    }
    
    .platform-btn.active {
        background: #667eea;
        color: white;
        border-color: #667eea;
    }
    
    /* Content variations */
    .variation-card {
        border: 2px solid #e0e6ff;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 15px;
        cursor: pointer;
        transition: all 0.3s;
        background: white;
    }
    
    .variation-card:hover {
        border-color: #667eea;
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.1);
    }
    
    .variation-card.active {
        border-color: #667eea;
        background: #f0f9ff;
    }
    
    /* Metrics */
    .metric-value {
        font-size: 24px;
        font-weight: 700;
        font-family: 'Monaco', 'Courier New', monospace;
        line-height: 1;
    }
    
    .engagement {
        color: #10b981;
    }
    
    .clarity {
        color: #f59e0b;
    }
    
    .sentiment {
        color: #667eea;
    }
    
    .metric-label {
        font-size: 12px;
        color: #666;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* Slider */
    .stSlider > div > div > div {
        background: linear-gradient(to right, #667eea, #764ba2);
    }
    
    /* Footer */
    .footer {
        margin-top: 40px;
        padding-top: 20px;
        border-top: 1px solid #e2e8f0;
        color: #666;
        font-size: 14px;
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
        
        for i in range(min(count, 5)):
            template = self.variation_templates[i]
            
            # Generate dynamic metrics
            base_engagement = 75 if template["type"] == "conversational" else 70
            engagement = base_engagement + random.randint(5, 20)
            clarity = 80 + random.randint(5, 15)
            sentiment = 0.8 + random.random() * 1.2
            
            variations.append({
                "id": i,
                "title": template["title"],
                "type": template["type"],
                "badge": template["badge"],
                "description": template["description"],
                "engagement": engagement,
                "clarity": clarity,
                "sentiment": round(sentiment, 2),
                "impressions": random.randint(800, 2500),
                "conversion": round(3 + random.random() * 6, 1)
            })
        
        # Sort and mark winner
        variations.sort(key=lambda x: x["engagement"], reverse=True)
        variations[0]["is_winner"] = True
        return variations

# ==================== SESSION STATE ====================
if 'current_topic' not in st.session_state:
    st.session_state.current_topic = "Machine Learning"
if 'current_platform' not in st.session_state:
    st.session_state.current_platform = "youtube"
if 'current_variations' not in st.session_state:
    st.session_state.current_variations = []
if 'quality_threshold' not in st.session_state:
    st.session_state.quality_threshold = 75
if 'content_type' not in st.session_state:
    st.session_state.content_type = "educational"

# ==================== INITIALIZE ====================
content_gen = ContentGenerator()
ab_gen = ABTestGenerator()

# ==================== SIDEBAR ====================
with st.sidebar:
    st.markdown('<div style="font-size: 24px; font-weight: 700; color: #667eea; margin-bottom: 30px;">🤖 AI Optimizer</div>', unsafe_allow_html=True)
    
    st.markdown("### Platform")
    platforms = ["YouTube", "Twitter", "LinkedIn", "Instagram", "Blog"]
    selected_platform = st.radio(
        "Select Platform",
        platforms,
        index=0,
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    st.markdown("### Main / Mode")
    modes = ["Machine Learning", "Content Length", "Problem Analysis"]
    selected_mode = st.radio(
        "Select Mode",
        modes,
        index=0,
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    st.markdown("### Medium-Quality Threshold")
    quality_threshold = st.slider(
        "Adjust quality threshold",
        0, 100, 75,
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    # Time display
    current_time = datetime.now().strftime("%H:%M %d-%m-%Y")
    st.markdown(f"**Current Time:** {current_time}")

# ==================== MAIN CONTENT ====================
# Header
st.markdown('<div class="main-header">AI Content Optimizer + Test Coach + A/B Testing</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Professional AI-powered content optimization platform</div>', unsafe_allow_html=True)

# Topic Input
col1, col2, col3 = st.columns([3, 1, 1])
with col1:
    topic_input = st.text_input(
        "Enter your topic",
        value=st.session_state.current_topic,
        placeholder="Enter any topic (e.g., Digital Marketing, Climate Change, Python Programming)...",
        key="topic_input"
    )

with col2:
    generate_btn = st.button("🚀 Generate Content", use_container_width=True)

with col3:
    run_test_btn = st.button("🧪 Run A/B Test", use_container_width=True, type="secondary")

# Update session state
if topic_input:
    st.session_state.current_topic = topic_input

# Configuration Panel
col1, col2 = st.columns(2)

with col1:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        
        # Card header
        header_col1, header_col2 = st.columns([3, 1])
        with header_col1:
            st.markdown('<div class="card-title">Configuration Panel</div>', unsafe_allow_html=True)
            st.markdown('<div class="card-subtitle">Adjust settings for optimal content generation</div>', unsafe_allow_html=True)
        with header_col2:
            st.markdown('<div class="badge badge-blue">Active</div>', unsafe_allow_html=True)
        
        # Platform selection
        st.markdown("**Platform**")
        platform_cols = st.columns(3)
        platforms_display = ["Toolbar", "Type", "Professional"]
        for idx, p_col in enumerate(platform_cols):
            with p_col:
                if st.button(platforms_display[idx], key=f"platform_{idx}", use_container_width=True):
                    pass
        
        # Mode selection
        st.markdown("**Main / Mode**")
        mode_cols = st.columns(3)
        modes_display = ["Machine Learning", "Content Length", "Problem"]
        for idx, m_col in enumerate(mode_cols):
            with m_col:
                if st.button(modes_display[idx], key=f"mode_{idx}", use_container_width=True):
                    pass
        
        # Quality threshold
        st.markdown(f"**Medium-Quality Threshold: {quality_threshold}**")
        st.slider("", 0, 100, quality_threshold, key="quality_slider", label_visibility="collapsed")
        
        # Optimistic contents
        st.markdown("**Optimistic Contents**")
        st.info(f"What is medium-threshold content for better choice {selected_mode}. Before bringing up an initial for model needs, include relevant training, low-rank of use, hunger, vision, and loss. The goal to remain the most engaged audience possible.")
        
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        
        # Card header
        header_col1, header_col2 = st.columns([3, 1])
        with header_col1:
            st.markdown('<div class="card-title">Content Preview</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="card-subtitle">{selected_platform} content preview</div>', unsafe_allow_html=True)
        with header_col2:
            st.markdown('<div class="badge badge-green">Generated</div>', unsafe_allow_html=True)
        
        # Content type selection
        content_types = ["Educational", "Motivational", "Conversational", "Promotional"]
        selected_content_type = st.radio(
            "Content Type",
            content_types,
            horizontal=True,
            label_visibility="collapsed"
        )
        
        # Generate content on button click
        if generate_btn or run_test_btn:
            with st.spinner(f"Generating {selected_platform.lower()} content..."):
                time.sleep(1.5)
                
                # Get the generator method
                platform_method = getattr(content_gen, f"generate_{selected_platform.lower()}")
                content = platform_method(st.session_state.current_topic, selected_content_type.lower())
                
                # Display content
                st.markdown("---")
                st.text_area(
                    "Generated Content",
                    value=content,
                    height=300,
                    disabled=True,
                    label_visibility="collapsed"
                )
                
                # Copy button
                if st.button("📋 Copy Content", use_container_width=True):
                    st.success("Content copied to clipboard!")
                
                # Metrics
                st.markdown("---")
                metric_cols = st.columns(3)
                with metric_cols[0]:
                    st.markdown('<div class="metric-value engagement">77.07</div>', unsafe_allow_html=True)
                    st.markdown('<div class="metric-label">Engagement</div>', unsafe_allow_html=True)
                with metric_cols[1]:
                    st.markdown('<div class="metric-value clarity">54.54</div>', unsafe_allow_html=True)
                    st.markdown('<div class="metric-label">Clarity</div>', unsafe_allow_html=True)
                with metric_cols[2]:
                    st.markdown('<div class="metric-value sentiment">0.0011%</div>', unsafe_allow_html=True)
                    st.markdown('<div class="metric-label">Sentiment</div>', unsafe_allow_html=True)
        else:
            st.info("Click 'Generate Content' to see preview here")
        
        st.markdown('</div>', unsafe_allow_html=True)

# A/B Testing Section
if run_test_btn:
    with st.spinner("Running A/B test analysis..."):
        time.sleep(2)
        
        # Generate variations
        variations = ab_gen.generate_variations(
            st.session_state.current_topic,
            selected_platform.lower(),
            3
        )
        st.session_state.current_variations = variations
        
        # Test Coach Results
        st.markdown("---")
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            
            # Header
            header_col1, header_col2 = st.columns([3, 1])
            with header_col1:
                st.markdown('<div class="card-title">Test Coach - Predictive Insights</div>', unsafe_allow_html=True)
                st.markdown('<div class="card-subtitle">Performance analysis and optimization recommendations</div>', unsafe_allow_html=True)
            with header_col2:
                st.markdown('<div class="badge badge-green">High Engagement</div>', unsafe_allow_html=True)
            
            # Stats grid
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                total_impressions = sum(v["impressions"] for v in variations)
                st.metric("Estimated Reach", f"{total_impressions:,} users")
            with col2:
                avg_engagement = sum(v["engagement"] for v in variations) / len(variations)
                st.metric("Avg Engagement", f"{avg_engagement:.1f}%")
            with col3:
                st.metric("Target Audience", "General")
            with col4:
                st.metric("Post Purpose", "Education")
            
            # Winner badge
            winner = next(v for v in variations if v.get("is_winner", False))
            st.success(f"🏆 **Winner: {winner['title']}** with {winner['engagement']}% engagement")
            
            # A/B Testing Visualization
            st.markdown("### A/B Testing Result")
            
            # Create bar chart
            chart_data = {
                "Variants": [v["title"] for v in variations],
                "Engagement": [v["engagement"] for v in variations],
                "Color": ["#3b82f6" if v.get("is_winner", False) else "#94a3b8" for v in variations]
            }
            
            # Display bars
            bar_cols = st.columns(len(variations))
            for idx, (v_col, variation) in enumerate(zip(bar_cols, variations)):
                with v_col:
                    # Bar
                    bar_height = variation["engagement"]
                    st.markdown(f'<div style="height:{bar_height}px; background:{chart_data["Color"][idx]}; border-radius: 6px 6px 0 0; width: 80%; margin: 0 auto;"></div>', unsafe_allow_html=True)
                    
                    # Label
                    st.markdown(f'<div style="text-align: center; margin-top: 10px; font-weight: 600;">{variation["title"]}</div>', unsafe_allow_html=True)
                    
                    # Value
                    st.markdown(f'<div style="text-align: center; font-size: 20px; font-weight: 700;">{variation["engagement"]}%</div>', unsafe_allow_html=True)
                    
                    # Winner badge
                    if variation.get("is_winner", False):
                        st.markdown('<div style="text-align: center; background: #10b981; color: white; padding: 4px 8px; border-radius: 12px; font-size: 12px; margin-top: 5px;">Winner</div>', unsafe_allow_html=True)
            
            # Variations display
            st.markdown("### Content Variations")
            for variation in variations:
                with st.container():
                    st.markdown(f'<div class="variation-card {"active" if variation.get("is_winner", False) else ""}">', unsafe_allow_html=True)
                    
                    # Variation header
                    var_col1, var_col2 = st.columns([3, 1])
                    with var_col1:
                        st.markdown(f"**{variation['title']}**")
                        st.caption(variation["description"])
                    with var_col2:
                        badge_class = "badge-blue" if variation.get("is_winner", False) else "badge-orange"
                        badge_text = "Best Clarity" if variation.get("is_winner", False) else "High Engagement"
                        st.markdown(f'<div class="badge {badge_class}">{badge_text}</div>', unsafe_allow_html=True)
                    
                    # Metrics
                    metric_cols = st.columns(3)
                    with metric_cols[0]:
                        st.markdown(f'<div class="metric-value engagement">{variation["engagement"]}</div>', unsafe_allow_html=True)
                        st.markdown('<div class="metric-label">Engagement</div>', unsafe_allow_html=True)
                    with metric_cols[1]:
                        st.markdown(f'<div class="metric-value clarity">{variation["clarity"]}</div>', unsafe_allow_html=True)
                        st.markdown('<div class="metric-label">Clarity</div>', unsafe_allow_html=True)
                    with metric_cols[2]:
                        st.markdown(f'<div class="metric-value sentiment">{variation["sentiment"]}%</div>', unsafe_allow_html=True)
                        st.markdown('<div class="metric-label">Sentiment</div>', unsafe_allow_html=True)
                    
                    # Select button
                    if st.button(f"Select {variation['title']}", key=f"select_{variation['id']}", use_container_width=True):
                        st.success(f"Selected {variation['title']} as your primary content!")
                    
                    st.markdown('</div>', unsafe_allow_html=True)
            
            # Recommendations
            st.markdown("### 💡 Recommendations")
            recommendations = [
                "Test posting time for higher reach",
                "Optimize thumbnail/images for better CTR",
                "Include relevant hashtags for discoverability",
                "Add clear call-to-action in description",
                "Engage with comments within first hour"
            ]
            
            for rec in recommendations:
                st.markdown(f"• {rec}")
            
            st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">', unsafe_allow_html=True)
footer_col1, footer_col2 = st.columns(2)
with footer_col1:
    st.markdown("🌧️ Light rain Tomorrow | 🔍 Search")
with footer_col2:
    st.markdown("🌐 ENG | IN")
st.markdown('</div>', unsafe_allow_html=True)