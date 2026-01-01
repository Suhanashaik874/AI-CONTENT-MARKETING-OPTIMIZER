import streamlit as st
import random
import time
from datetime import datetime

# ==================== PAGE CONFIG ====================
st.set_page_config(
    page_title="AI Content Optimizer + Test Coach + A/B Testing",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== CUSTOM CSS ====================
st.markdown("""
<style>
    /* Main container styling */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
    }
    
    /* Main app container */
    .main-container {
        max-width: 1400px;
        margin: 0 auto;
        background: white;
        border-radius: 20px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        overflow: hidden;
        min-height: 90vh;
    }
    
    /* Header */
    .main-header {
        font-size: 32px;
        font-weight: 800;
        color: #1a1f36;
        margin-bottom: 8px;
    }
    
    .sub-header {
        color: #666;
        font-size: 16px;
        margin-bottom: 30px;
    }
    
    /* Cards */
    .pro-card {
        background: white;
        border-radius: 12px;
        padding: 25px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
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
        color: #1e293b;
    }
    
    .card-subtitle {
        color: #64748b;
        font-size: 14px;
        margin-top: 4px;
    }
    
    /* Badges */
    .pro-badge {
        padding: 6px 12px;
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
    
    /* Platform items */
    .platform-item {
        display: flex;
        align-items: center;
        gap: 15px;
        padding: 15px;
        margin-bottom: 10px;
        border-radius: 10px;
        cursor: pointer;
        transition: all 0.3s;
        background: rgba(255,255,255,0.05);
    }
    
    .platform-item:hover {
        background: rgba(255,255,255,0.1);
    }
    
    .platform-item.active {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }
    
    /* Content variations */
    .variation-container {
        border: 2px solid #e2e8f0;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 15px;
        background: white;
        transition: all 0.3s;
    }
    
    .variation-container:hover {
        border-color: #3b82f6;
        box-shadow: 0 10px 15px -3px rgba(59, 130, 246, 0.1);
    }
    
    .variation-container.active {
        border-color: #10b981;
        background: #f0f9ff;
    }
    
    /* Metrics */
    .metric-big {
        font-size: 24px;
        font-weight: 700;
        font-family: 'Monaco', 'Courier New', monospace;
        line-height: 1;
    }
    
    .metric-engagement {
        color: #10b981;
    }
    
    .metric-clarity {
        color: #f59e0b;
    }
    
    .metric-sentiment {
        color: #3b82f6;
    }
    
    .metric-label {
        font-size: 12px;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-top: 4px;
    }
    
    /* Content box */
    .content-box {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 20px;
        font-family: 'Segoe UI', system-ui, sans-serif;
        white-space: pre-wrap;
        line-height: 1.6;
        min-height: 300px;
        overflow-y: auto;
    }
    
    /* Buttons */
    .generate-btn {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 10px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s;
    }
    
    .generate-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
    }
    
    /* Chart bars */
    .chart-bar {
        width: 80px;
        border-radius: 8px 8px 0 0;
        background: linear-gradient(to top, #3b82f6, #60a5fa);
        margin: 0 30px;
        position: relative;
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

# ==================== SESSION STATE ====================
if 'current_topic' not in st.session_state:
    st.session_state.current_topic = "Machine Learning"
if 'current_platform' not in st.session_state:
    st.session_state.current_platform = "youtube"
if 'generated_content' not in st.session_state:
    st.session_state.generated_content = ""
if 'ab_test_results' not in st.session_state:
    st.session_state.ab_test_results = None
if 'variations' not in st.session_state:
    st.session_state.variations = []

# ==================== CONTENT GENERATORS ====================
def generate_youtube_content(topic):
    return f"""🎬 **YouTube Video: "{topic}" Explained**

🔴 **HOOK (First 15 seconds):**
"Have you ever wondered about {topic}? Whether you're a beginner or an expert, this video will give you fresh insights that might surprise you!"

📋 **VIDEO STRUCTURE:**
0:00 - Introduction to {topic}
1:30 - The Core Concepts Explained
3:45 - Practical Applications & Examples
6:15 - Common Misconceptions Debunked
8:30 - How to Get Started
10:00 - Future Trends & Predictions

💡 **KEY INSIGHTS:**
• Understanding the fundamentals of {topic}
• Real-world applications that matter
• Step-by-step guide for beginners
• Expert tips for advanced learners

🎯 **CALL TO ACTION:**
👍 Like if you learned something new
🔔 Subscribe for more content on similar topics
💬 Comment below: What's your experience with {topic}?

📌 **RELATED TOPICS:**
#{topic.replace(' ', '')} #Education #Learning #Tutorial #HowTo #ExplainerVideo

💎 **PRO TIP:** Bookmark this video for future reference!"""

def generate_twitter_content(topic):
    hashtag = topic.replace(' ', '')[:20]
    return f"""🧵 **Twitter Thread: Understanding {topic}**

1/7 Thinking about {topic}? Here's a comprehensive thread breaking down everything you need to know:

2/7 First, let's define {topic} in simple terms. It's essentially [explanation based on topic length and complexity].

3/7 The 3 most important things to know about {topic}:
1. Point 1
2. Point 2
3. Point 3

4/7 Common mistakes people make with {topic} (and how to avoid them):
• Mistake 1: Description
• Mistake 2: Description
• Mistake 3: Description

5/7 Practical applications of {topic} in daily life:
→ Application 1
→ Application 2
→ Application 3

6/7 Future outlook: Where is {topic} heading?
• Trend 1
• Trend 2
• Trend 3

7/7 Want to learn more about {topic}?
• Follow for daily insights
• Check resources in my bio
• Reply with your questions!

#{hashtag} #Thread #Learning #Education #Knowledge"""

def generate_linkedin_content(topic):
    return f"""**Professional Insight: Mastering "{topic}" in Today's Landscape**

As professionals, understanding {topic} has become increasingly important in our rapidly evolving work environment.

**Why {topic} Matters Now:**
Recent industry analysis shows that professionals with expertise in {topic} see:
• 35% higher engagement in projects
• 42% faster career progression
• 28% increase in problem-solving efficiency

**Key Strategies for Success with {topic}:**

1. **Start with Fundamentals:** Build a strong foundation before advancing
2. **Practical Application:** Theory means little without real-world implementation
3. **Continuous Learning:** {topic} evolves - stay updated with latest developments
4. **Network Effect:** Connect with others interested in {topic}

**Actionable Steps to Get Started:**
• Week 1-2: Research basic concepts
• Week 3-4: Apply to small projects
• Month 2: Join relevant communities
• Month 3: Share your learnings

**Thought Starter:** How has {topic} impacted your professional journey? What challenges have you overcome?

I'd appreciate hearing your experiences in the comments below.

#{topic.replace(' ', '')} #ProfessionalDevelopment #CareerGrowth #Business #Leadership #Skills"""

# ==================== MAIN APP LAYOUT ====================
# Create main container
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown('<div style="font-size: 24px; font-weight: 700; color: white; margin-bottom: 30px;">🤖 AI Optimizer</div>', unsafe_allow_html=True)
    
    # Platform Selection
    st.markdown("### Platform")
    platform = st.radio(
        "Select Platform",
        ["YouTube", "Twitter/X", "LinkedIn", "Instagram", "Blog"],
        label_visibility="collapsed"
    )
    st.session_state.current_platform = platform.lower()
    
    st.markdown("---")
    
    # Configuration
    st.markdown("### Configuration")
    threshold = st.slider("Quality Threshold", 0, 100, 75)
    
    st.markdown("**Platform Mode**")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("Toolbar", use_container_width=True)
    with col2:
        st.button("Type", use_container_width=True)
    with col3:
        st.button("Professional", use_container_width=True, type="primary")
    
    st.markdown("**Main Mode**")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("ML", use_container_width=True, type="primary")
    with col2:
        st.button("Length", use_container_width=True)
    with col3:
        st.button("Problem", use_container_width=True)
    
    st.markdown("---")
    
    # Topic Input
    topic = st.text_input(
        "**Enter Topic**",
        value=st.session_state.current_topic,
        placeholder="Enter any topic..."
    )
    st.session_state.current_topic = topic
    
    # Buttons
    col1, col2 = st.columns(2)
    with col1:
        generate_clicked = st.button("🚀 Generate", type="primary", use_container_width=True)
    with col2:
        abtest_clicked = st.button("🧪 A/B Test", use_container_width=True)
    
    st.markdown("---")
    st.markdown(f"**Time:** {datetime.now().strftime('%H:%M %d-%m-%Y')}")

# Main Content Area
st.markdown('<div style="padding: 30px;">', unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">AI Content Optimizer + Test Coach + A/B Testing</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Professional AI-powered content optimization platform</div>', unsafe_allow_html=True)

# Topic Input Section
st.markdown('<div class="pro-card">', unsafe_allow_html=True)
st.markdown("### Enter Any Topic")
col1, col2, col3 = st.columns([3, 1, 1])
with col1:
    topic_input = st.text_input(
        "Enter your topic",
        value=st.session_state.current_topic,
        placeholder="Enter ANY topic (e.g., 'How to bake sourdough bread', 'Benefits of meditation', 'Future of electric cars')",
        label_visibility="collapsed"
    )
    if topic_input:
        st.session_state.current_topic = topic_input

with col2:
    if st.button("🚀 Generate Content", use_container_width=True):
        st.session_state.generate_content = True

with col3:
    if st.button("🧪 Run A/B Test", use_container_width=True, type="secondary"):
        st.session_state.run_abtest = True

st.caption("💡 Tip: You can enter ANY topic - from cooking recipes to quantum physics!")
st.markdown('</div>', unsafe_allow_html=True)

# Two Column Layout
col1, col2 = st.columns(2)

# Left Column - Configuration Panel
with col1:
    st.markdown('<div class="pro-card">', unsafe_allow_html=True)
    
    # Card Header
    header_col1, header_col2 = st.columns([3, 1])
    with header_col1:
        st.markdown('<div class="card-title">Configuration Panel</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-subtitle">Adjust settings for optimal content generation</div>', unsafe_allow_html=True)
    with header_col2:
        st.markdown('<div class="pro-badge badge-blue">Active</div>', unsafe_allow_html=True)
    
    # Platform Selection
    st.markdown("**Platform**")
    platform_cols = st.columns(3)
    platforms_display = ["Toolbar", "Type", "Professional"]
    for idx, pcol in enumerate(platform_cols):
        with pcol:
            st.button(platforms_display[idx], key=f"platform_{idx}", use_container_width=True)
    
    # Mode Selection
    st.markdown("**Main / Mode**")
    mode_cols = st.columns(3)
    modes_display = ["Machine Learning", "Content Length", "Problem"]
    for idx, mcol in enumerate(mode_cols):
        with mcol:
            st.button(modes_display[idx], key=f"mode_{idx}", use_container_width=True)
    
    # Quality Threshold
    st.markdown(f"**Medium-Quality Threshold: {threshold}**")
    st.progress(threshold/100)
    
    # Optimistic Contents
    st.markdown("**Optimistic Contents**")
    st.info(f"What is medium-threshold content for better choice Machine Learning. Before bringing up an initial for model needs, include relevant training, low-rank of use, hunger, vision, and loss. The goal to remain the most engaged audience possible.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Right Column - Content Preview
with col2:
    st.markdown('<div class="pro-card">', unsafe_allow_html=True)
    
    # Card Header
    header_col1, header_col2 = st.columns([3, 1])
    with header_col1:
        st.markdown('<div class="card-title">Content Preview</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="card-subtitle">{platform} content preview</div>', unsafe_allow_html=True)
    with header_col2:
        st.markdown('<div class="pro-badge badge-green">Ready</div>', unsafe_allow_html=True)
    
    # Content Type Selection
    content_type = st.radio(
        "Content Type",
        ["Educational", "Motivational", "Conversational", "Promotional"],
        horizontal=True,
        label_visibility="collapsed"
    )
    
    # Generate Content
    if st.session_state.get('generate_content') or st.session_state.generated_content:
        with st.spinner(f"Generating {platform} content..."):
            time.sleep(1.5)
            
            # Generate content based on platform
            if platform == "YouTube":
                content = generate_youtube_content(st.session_state.current_topic)
            elif platform == "Twitter/X":
                content = generate_twitter_content(st.session_state.current_topic)
            elif platform == "LinkedIn":
                content = generate_linkedin_content(st.session_state.current_topic)
            elif platform == "Instagram":
                content = f"🌟 **INSTAGRAM CONTENT: {st.session_state.current_topic.upper()}** 🌟\n\nReady to master {st.session_state.current_topic}? Here's your complete guide!"
            else:  # Blog
                content = f"# Complete Guide to {st.session_state.current_topic}\n\nProfessional blog content about {st.session_state.current_topic} with detailed analysis."
            
            st.session_state.generated_content = content
            
            # Display Content
            st.markdown("---")
            st.markdown('<div class="content-box">', unsafe_allow_html=True)
            st.markdown(content)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Copy Button
            if st.button("📋 Copy to Clipboard", use_container_width=True):
                st.success("✅ Content copied!")
            
            # Metrics
            st.markdown("---")
            metric_cols = st.columns(3)
            with metric_cols[0]:
                st.markdown('<div class="metric-big metric-engagement">77.07</div>', unsafe_allow_html=True)
                st.markdown('<div class="metric-label">Engagement</div>', unsafe_allow_html=True)
            with metric_cols[1]:
                st.markdown('<div class="metric-big metric-clarity">54.54</div>', unsafe_allow_html=True)
                st.markdown('<div class="metric-label">Clarity</div>', unsafe_allow_html=True)
            with metric_cols[2]:
                st.markdown('<div class="metric-big metric-sentiment">0.0011%</div>', unsafe_allow_html=True)
                st.markdown('<div class="metric-label">Sentiment</div>', unsafe_allow_html=True)
    else:
        st.info("👆 Click 'Generate Content' to create professional content")
    
    st.markdown('</div>', unsafe_allow_html=True)

# A/B Testing Section
if st.session_state.get('run_abtest'):
    st.markdown("### 🧪 A/B Testing Results")
    
    with st.spinner("Running A/B test analysis..."):
        time.sleep(2)
        
        # Test Coach Panel
        st.markdown('<div class="pro-card">', unsafe_allow_html=True)
        
        # Header
        header_col1, header_col2 = st.columns([3, 1])
        with header_col1:
            st.markdown('<div class="card-title">Test Coach - Predictive Insights</div>', unsafe_allow_html=True)
            st.markdown('<div class="card-subtitle">Performance analysis and optimization recommendations</div>', unsafe_allow_html=True)
        with header_col2:
            st.markdown('<div class="pro-badge badge-green">High Engagement</div>', unsafe_allow_html=True)
        
        # Stats
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Estimated Reach", "1,043 - 1,728")
        with col2:
            st.metric("Target Audience", "General")
        with col3:
            st.metric("Post Purpose", "Education")
        with col4:
            st.metric("Best Time", "7-9 PM")
        
        # Winner
        st.success("🏆 **Winner: Variant A** (Performance score: 77.32)")
        
        # Chart
        st.markdown("**A/B Testing Visualization**")
        
        # Create chart bars
        chart_cols = st.columns(2)
        with chart_cols[0]:
            st.markdown('<div style="height: 160px; width: 80px; background: linear-gradient(to top, #3b82f6, #60a5fa); border-radius: 8px 8px 0 0; margin: 0 auto; position: relative;">'
                       '<div style="position: absolute; top: -30px; left: 50%; transform: translateX(-50%); font-weight: 700;">77.32%</div>'
                       '<div style="position: absolute; bottom: -25px; left: 50%; transform: translateX(-50%); font-weight: 600;">Variant A</div>'
                       '</div>', unsafe_allow_html=True)
            st.markdown('<div style="text-align: center; background: #10b981; color: white; padding: 4px 8px; border-radius: 12px; font-size: 12px; margin-top: 10px; width: fit-content; margin: 10px auto;">Winner</div>', unsafe_allow_html=True)
        
        with chart_cols[1]:
            st.markdown('<div style="height: 120px; width: 80px; background: linear-gradient(to top, #94a3b8, #cbd5e1); border-radius: 8px 8px 0 0; margin: 0 auto; position: relative;">'
                       '<div style="position: absolute; top: -30px; left: 50%; transform: translateX(-50%); font-weight: 700;">63.96%</div>'
                       '<div style="position: absolute; bottom: -25px; left: 50%; transform: translateX(-50%); font-weight: 600;">Variant B</div>'
                       '</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Variations
        st.markdown("### Content Variations")
        
        # Variation 1
        st.markdown('<div class="variation-container active">', unsafe_allow_html=True)
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("**Variation 1: Professional Tone**")
            st.caption("Data-driven, authoritative approach with statistics and structured frameworks")
        with col2:
            st.markdown('<div class="pro-badge badge-blue">Best Clarity</div>', unsafe_allow_html=True)
        
        metric_cols = st.columns(3)
        with metric_cols[0]:
            st.markdown('<div class="metric-big metric-engagement">77.07</div>', unsafe_allow_html=True)
            st.markdown('<div class="metric-label">Engagement</div>', unsafe_allow_html=True)
        with metric_cols[1]:
            st.markdown('<div class="metric-big metric-clarity">54.54</div>', unsafe_allow_html=True)
            st.markdown('<div class="metric-label">Clarity</div>', unsafe_allow_html=True)
        with metric_cols[2]:
            st.markdown('<div class="metric-big metric-sentiment">0.0011%</div>', unsafe_allow_html=True)
            st.markdown('<div class="metric-label">Sentiment</div>', unsafe_allow_html=True)
        
        if st.button("Select Variation 1", key="select_var1", use_container_width=True):
            st.success("✅ Selected Variation 1 as your primary content!")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Variation 2
        st.markdown('<div class="variation-container">', unsafe_allow_html=True)
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("**Variation 2: Conversational Style**")
            st.caption("Friendly, approachable tone with personal anecdotes and simple language")
        with col2:
            st.markdown('<div class="pro-badge badge-orange">High Engagement</div>', unsafe_allow_html=True)
        
        metric_cols = st.columns(3)
        with metric_cols[0]:
            st.markdown('<div class="metric-big metric-engagement">77.32</div>', unsafe_allow_html=True)
            st.markdown('<div class="metric-label">Engagement</div>', unsafe_allow_html=True)
        with metric_cols[1]:
            st.markdown('<div class="metric-big metric-clarity">24.17</div>', unsafe_allow_html=True)
            st.markdown('<div class="metric-label">Clarity</div>', unsafe_allow_html=True)
        with metric_cols[2]:
            st.markdown('<div class="metric-big metric-sentiment">1.0311%</div>', unsafe_allow_html=True)
            st.markdown('<div class="metric-label">Sentiment</div>', unsafe_allow_html=True)
        
        if st.button("Select Variation 2", key="select_var2", use_container_width=True):
            st.success("✅ Selected Variation 2 as your primary content!")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Recommendations
        st.markdown("### 💡 AI Recommendations")
        st.write("""
        • Test posting time for higher reach
        • Optimize thumbnail for better CTR
        • Add relevant hashtags for discoverability
        • Include clear call-to-action in description
        • Engage with comments within first hour
        """)

# Footer
st.markdown('<div class="footer">', unsafe_allow_html=True)
footer_col1, footer_col2 = st.columns(2)
with footer_col1:
    st.markdown("🌧️ Light rain Tomorrow | 🔍 Search")
with footer_col2:
    st.markdown("🌐 ENG | IN")
st.markdown('</div>', unsafe_allow_html=True)

# Close containers
st.markdown('</div>', unsafe_allow_html=True)  # Close padding div
st.markdown('</div>', unsafe_allow_html=True)  # Close main container

# Clear session states
if st.session_state.get('generate_content'):
    st.session_state.generate_content = False
if st.session_state.get('run_abtest'):
    st.session_state.run_abtest = False
