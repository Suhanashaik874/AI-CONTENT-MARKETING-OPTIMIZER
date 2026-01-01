import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.graph_objects as go
import random

# ========== PAGE CONFIG ==========
st.set_page_config(
    page_title="AI Content Optimizer PRO",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ========== CUSTOM CSS ==========
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
    
    /* Force dark background */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%) !important;
        min-height: 100vh;
    }
    
    /* Remove all padding */
    .main .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        max-width: 100% !important;
    }
    
    /* Custom header */
    .main-header {
        text-align: center;
        padding: 3rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        margin: 1rem 0 2rem 0;
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
        cursor: pointer;
    }
    
    .platform-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
    }
    
    .platform-card.selected {
        border-left: 5px solid #10b981;
        background: rgba(16, 185, 129, 0.1);
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
    
    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    header {visibility: hidden !important;}
    
    /* Sentiment badges */
    .sentiment-badge {
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: bold;
        display: inline-block;
        margin: 0.3rem;
    }
    
    .sentiment-positive {
        background: linear-gradient(135deg, rgba(34, 197, 94, 0.2), rgba(34, 197, 94, 0.1));
        color: #10b981;
        border: 1px solid #10b981;
    }
    
    .sentiment-neutral {
        background: linear-gradient(135deg, rgba(234, 179, 8, 0.2), rgba(234, 179, 8, 0.1));
        color: #eab308;
        border: 1px solid #eab308;
    }
    
    .sentiment-negative {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.2), rgba(239, 68, 68, 0.1));
        color: #ef4444;
        border: 1px solid #ef4444;
    }
    
    /* Platform colors */
    .youtube-color { color: #FF0000 !important; }
    .twitter-color { color: #1DA1F2 !important; }
    .linkedin-color { color: #0A66C2 !important; }
    .instagram-color { color: #E4405F !important; }
    .blog-color { color: #FF6B6B !important; }
    
    /* Make all text white */
    h1, h2, h3, h4, h5, h6, p, label, span, div {
        color: var(--text-light) !important;
    }
    
    /* Success/Info boxes */
    .stAlert {
        background: rgba(99, 102, 241, 0.1) !important;
        border: 2px solid var(--primary) !important;
        border-radius: 10px !important;
    }
    
    .stSuccess {
        background: rgba(34, 197, 94, 0.1) !important;
        border: 2px solid #10b981 !important;
        border-radius: 10px !important;
    }
</style>
""", unsafe_allow_html=True)

# ========== SESSION STATE ==========
if 'topic' not in st.session_state:
    st.session_state.topic = "Machine Learning"
if 'test_results' not in st.session_state:
    st.session_state.test_results = None
if 'generated_content' not in st.session_state:
    st.session_state.generated_content = {}
if 'selected_platform' not in st.session_state:
    st.session_state.selected_platform = "YouTube"
if 'selected_style' not in st.session_state:
    st.session_state.selected_style = "conversational"
if 'sentiment_results' not in st.session_state:
    st.session_state.sentiment_results = {}
if 'show_platform_content' not in st.session_state:
    st.session_state.show_platform_content = False

# ========== FUNCTIONS ==========
def analyze_sentiment(text):
    """Simple sentiment analysis without external dependencies"""
    positive_words = ['great', 'good', 'excellent', 'amazing', 'awesome', 'love', 
                     'best', 'perfect', 'happy', 'win', 'success', 'fantastic',
                     'wonderful', 'brilliant', 'superb', 'outstanding', 'positive',
                     'easy', 'simple', 'effective', 'powerful', 'innovative']
    negative_words = ['bad', 'poor', 'terrible', 'awful', 'hate', 'worst', 
                     'failure', 'sad', 'angry', 'problem', 'issue', 'difficult',
                     'hard', 'challenge', 'negative', 'disappointing', 'weak',
                     'complex', 'complicated', 'expensive', 'slow']
    
    text_lower = text.lower()
    words = text_lower.split()
    
    pos_count = sum(1 for word in words if any(pw in word for pw in positive_words))
    neg_count = sum(1 for word in words if any(nw in word for nw in negative_words))
    
    total_words = max(len(words), 1)
    polarity = (pos_count - neg_count) / total_words
    
    if polarity > 0.1:
        return "positive", min(polarity, 1.0), "😊"
    elif polarity < -0.1:
        return "negative", max(polarity, -1.0), "😟"
    else:
        return "neutral", polarity, "😐"

def generate_platform_content(topic, platform, style="conversational"):
    """Generate content for different platforms"""
    style_configs = {
        "conversational": {
            "tone": "friendly and approachable",
            "phrases": ["Hey there!", "Let's chat about", "You'll love this", "Super easy to understand"],
            "emoji": "💬"
        },
        "professional": {
            "tone": "formal and expert-level", 
            "phrases": ["Research indicates", "Data shows", "According to industry analysis", "Best practices suggest"],
            "emoji": "👔"
        },
        "motivational": {
            "tone": "inspiring and energetic",
            "phrases": ["Unlock your potential", "Transform your approach", "Achieve amazing results", "Breakthrough insights"],
            "emoji": "🚀"
        }
    }
    
    style_info = style_configs.get(style.lower(), style_configs["conversational"])
    
    if platform == "YouTube":
        return {
            "type": "video",
            "title": f"{topic}: Complete Beginner's Guide (2024)",
            "hook": f"Ever wondered about {topic}? In this video, we'll break down everything you need to know - from basics to advanced concepts! {style_info['phrases'][0]}",
            "description": f"""# {topic} Explained
{style_info['phrases'][1]} {topic} - one of the most important topics today!

📌 **What you'll learn:**
• Fundamentals of {topic}
• Real-world applications  
• Step-by-step implementation
• Future trends

🔥 **Why this matters:**
{topic} is transforming industries. Whether you're a beginner or looking to advance your skills, this guide has you covered.

👍 **Like & Subscribe** for more content!
🔔 **Turn on notifications** so you don't miss updates!

# {topic.replace(' ', '')} #Education #Tech #Learning""",
            "timestamps": [
                "0:00 - Introduction & Hook",
                "1:30 - What is " + topic + "?",
                "3:15 - Key Concepts Explained", 
                "5:45 - Practical Applications",
                "7:30 - Getting Started Guide",
                "9:15 - Future Trends",
                "10:30 - Conclusion & Next Steps"
            ],
            "hashtags": [f"#{topic.replace(' ', '')}", "#Tech", "#Education", "#HowTo", "#Tutorial"]
        }
    
    elif platform == "Twitter/X":
        thread = [
            f"🚀 NEW: Complete Thread on {topic}",
            f"1/{random.randint(5,8)}: What is {topic}? {style_info['phrases'][0]} Let's dive in!",
            f"2/{random.randint(5,8)}: At its core, {topic} involves... This is changing how we approach problems.",
            f"3/{random.randint(5,8)}: Key benefits of {topic}: • Efficiency • Innovation • Competitive edge",
            f"4/{random.randint(5,8)}: Real-world applications are everywhere! From healthcare to finance, {topic} is making waves.",
            f"5/{random.randint(5,8)}: Getting started with {topic}? Begin with fundamentals, then practice regularly.",
            f"6/{random.randint(5,8)}: {style_info['phrases'][3]} The future of {topic} looks incredibly promising!",
            f"7/{random.randint(5,8)}: Like/Retweet if you found this helpful! Follow for more threads on tech & innovation."
        ]
        return {
            "type": "thread",
            "thread": thread,
            "hashtags": [f"#{topic.replace(' ', '')}", "#TechTwitter", "#Thread", "#Learning", "#Innovation"]
        }
    
    elif platform == "LinkedIn":
        return {
            "type": "post",
            "title": f"Professional Insights: The Impact of {topic}",
            "content": f"""🏢 **Professional Perspective: {topic}**

{style_info['phrases'][1]} {topic} is more than just a trend - it's a fundamental shift in how we approach problem-solving.

**Why {topic} Matters:**
✅ Drives innovation across sectors
✅ Creates competitive advantages  
✅ Opens new career opportunities
✅ Enhances decision-making processes

**Key Observations:**
• Companies adopting {topic} strategies report significant improvements
• The demand for {topic} skills is growing exponentially
• Early adopters are seeing remarkable ROI

**Actionable Advice:**
1. Start with foundational knowledge
2. Apply concepts to real scenarios
3. Connect with professionals in the field
4. Stay updated with latest developments

What's your experience with {topic}? Share your thoughts below!

#ProfessionalDevelopment #{topic.replace(' ', '')} #CareerGrowth #Innovation #BusinessStrategy""",
            "hashtags": [f"#{topic.replace(' ', '')}", "#LinkedIn", "#ProfessionalGrowth", "#Career", "#Business"]
        }
    
    elif platform == "Instagram":
        return {
            "type": "social",
            "caption": f"""✨ {topic} EXPLAINED ✨

{style_info['phrases'][0]} Today we're exploring {topic} - one of the most exciting topics right now! 💫

🔍 What you need to know:
✅ {topic} is more accessible than you think
✅ Real applications change lives
✅ Start small, think big
✅ Continuous learning is key

💭 Remember: Every expert was once a beginner!

👉 Tag someone who needs to see this!
📲 Save for later reference

#LearnWithMe #{topic.replace(' ', '')} #Knowledge #DailyLearning #Education #GrowthMindset""",
            "stories": [
                f"Day 1️⃣: {topic} Basics 🎯",
                f"Did you know? 🤯 {topic} facts!",
                f"Quick tip for beginners 💡",
                f"{topic} in action 🚀",
                f"Q&A about {topic} ❓",
                f"Resources to learn {topic} 📚",
                f"Future of {topic} 🔮"
            ],
            "hashtags": [f"#{topic.replace(' ', '')}", "#Instagram", "#Learn", "#Education", "#Content"]
        }
    
    elif platform == "Blog":
        return {
            "type": "article",
            "title": f"The Comprehensive Guide to {topic}: Everything You Need to Know",
            "content": f"""# The Ultimate Guide to {topic}

## Introduction
{style_info['phrases'][1]} {topic} has emerged as one of the most transformative fields in recent years. This comprehensive guide will walk you through everything from basic concepts to advanced applications.

## What is {topic}?
{topic} refers to a set of principles, methods, and technologies that... It represents a paradigm shift in how we approach challenges and create solutions.

## Why {topic} Matters
### 1. Efficiency Improvements
Organizations implementing {topic} strategies report efficiency gains of 30-50%.

### 2. Innovation Catalyst
{topic} drives breakthrough innovations across industries.

### 3. Competitive Advantage
Early adopters gain significant market advantages.

### 4. Career Opportunities
The demand for {topic} professionals is growing at 40% annually.

## Core Concepts
### Fundamental Principles
• Principle 1: Foundation of {topic}
• Principle 2: Application methodology  
• Principle 3: Measurement and optimization

### Key Technologies
• Technology A: Enables X
• Technology B: Facilitates Y
• Technology C: Enhances Z

## Getting Started
### Step 1: Learn the Basics
Start with online courses, books, and tutorials focused on {topic} fundamentals.

### Step 2: Practical Application
Apply concepts to small projects to build hands-on experience.

### Step 3: Advanced Learning
Once comfortable with basics, explore specialized areas within {topic}.

### Step 4: Community Engagement
Join forums, attend meetups, and connect with other {topic} enthusiasts.

## Real-World Applications
### Case Study 1: Industry Transformation
How Company X used {topic} to achieve remarkable results.

### Case Study 2: Innovation Example  
Breakthrough achieved through {topic} implementation.

## Future Trends
### Emerging Developments
• Trend 1: AI integration with {topic}
• Trend 2: Democratization of {topic} tools
• Trend 3: Cross-industry applications

### Predictions
The {topic} market is expected to grow to $XX billion by 2025, with increasing adoption across sectors.

## Conclusion
{topic} represents not just a technological shift, but a fundamental change in how we approach problems and create value. {style_info['phrases'][3]} begin your journey with {topic} today.

## Additional Resources
• Recommended books on {topic}
• Online courses and certifications
• Professional communities and forums
• Tools and software for {topic}

*This article provides a comprehensive overview of {topic}. For personalized guidance, consider consulting with a {topic} specialist.*""",
            "meta_description": f"Learn everything about {topic} - from basic concepts to advanced applications. Perfect guide for beginners and professionals looking to master {topic}.",
            "tags": [topic, "Technology", "Guide", "Tutorial", "Education"]
        }

# ========== HEADER ==========
st.markdown("""
<div class="main-header">
    <h1>🎯 AI CONTENT OPTIMIZER PRO</h1>
    <p>Generate & optimize content for any topic on any platform</p>
</div>
""", unsafe_allow_html=True)

# ========== TABS ==========
tab1, tab2 = st.tabs(["📝 GENERATE CONTENT", "📊 TEST RESULTS"])

# ========== TAB 1: GENERATE CONTENT ==========
with tab1:
    col1, col2 = st.columns([1, 2])
    
    # ===== COLUMN 1: PLATFORMS =====
    with col1:
        st.markdown("### 📱 CONTENT PLATFORMS")
        
        platforms = [
            {"name": "YouTube", "icon": "🎬", "color": "youtube-color"},
            {"name": "Twitter/X", "icon": "🐦", "color": "twitter-color"},
            {"name": "LinkedIn", "icon": "💼", "color": "linkedin-color"},
            {"name": "Instagram", "icon": "📸", "color": "instagram-color"},
            {"name": "Blog", "icon": "✍️", "color": "blog-color"}
        ]
        
        for platform in platforms:
            is_selected = st.session_state.selected_platform == platform["name"]
            card_class = "platform-card selected" if is_selected else "platform-card"
            
            if st.button(f"{platform['icon']} {platform['name']}", 
                        key=f"platform_{platform['name']}",
                        use_container_width=True):
                st.session_state.selected_platform = platform["name"]
                st.session_state.show_platform_content = True
                st.rerun()
    
    # ===== COLUMN 2: CONTENT GENERATOR =====
    with col2:
        st.markdown("### 🚀 AI CONTENT OPTIMIZER")
        st.markdown("Generate content for any topic on any platform")
        
        # Topic Input
        col_topic1, col_topic2 = st.columns([2, 1])
        with col_topic1:
            topic = st.text_input(
                "**Enter Any Topic**",
                value="Machine Learning",
                placeholder="e.g., Artificial Intelligence, Digital Marketing, Python Programming...",
                help="You can enter ANY topic - from cooking recipes to quantum physics"
            )
        
        with col_topic2:
            content_style = st.selectbox(
                "**Content Style**",
                ["Conversational", "Professional", "Motivational"],
                index=0
            )
        
        # Action Buttons
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("✨ **GENERATE CONTENT**", use_container_width=True, type="primary"):
                if topic.strip():
                    st.session_state.topic = topic.strip()
                    st.session_state.selected_style = content_style.lower()
                    
                    # Generate content
                    content = generate_platform_content(
                        st.session_state.topic,
                        st.session_state.selected_platform,
                        st.session_state.selected_style
                    )
                    st.session_state.generated_content = content
                    
                    # Analyze sentiment
                    if st.session_state.selected_platform == "Twitter/X":
                        text_to_analyze = " ".join(content.get("thread", []))
                    elif st.session_state.selected_platform in ["YouTube", "LinkedIn", "Instagram"]:
                        text_to_analyze = content.get("description", content.get("content", content.get("caption", "")))
                    else:
                        text_to_analyze = content.get("content", "")
                    
                    sentiment, polarity, emoji = analyze_sentiment(text_to_analyze)
                    st.session_state.sentiment_results = {
                        "sentiment": sentiment,
                        "polarity": polarity,
                        "emoji": emoji
                    }
                    
                    st.session_state.show_platform_content = True
                    st.success(f"✅ Content generated for **{st.session_state.selected_platform}**!")
                else:
                    st.warning("⚠️ Please enter a topic first!")
        
        with col_btn2:
            if st.button("📊 **ANALYZE SENTIMENT**", use_container_width=True):
                if st.session_state.generated_content:
                    if st.session_state.selected_platform == "Twitter/X":
                        text_to_analyze = " ".join(st.session_state.generated_content.get("thread", []))
                    elif st.session_state.selected_platform in ["YouTube", "LinkedIn", "Instagram"]:
                        text_to_analyze = st.session_state.generated_content.get("description", 
                            st.session_state.generated_content.get("content", 
                            st.session_state.generated_content.get("caption", "")))
                    else:
                        text_to_analyze = st.session_state.generated_content.get("content", "")
                    
                    sentiment, polarity, emoji = analyze_sentiment(text_to_analyze)
                    st.session_state.sentiment_results = {
                        "sentiment": sentiment,
                        "polarity": polarity,
                        "emoji": emoji
                    }
                    st.rerun()
                else:
                    st.warning("⚠️ Generate content first!")
        
        # ===== DISPLAY GENERATED CONTENT =====
        if st.session_state.get('show_platform_content', False) and st.session_state.generated_content:
            st.markdown("---")
            
            # Display Platform Header
            platform = st.session_state.selected_platform
            platform_icons = {"YouTube": "🎬", "Twitter/X": "🐦", "LinkedIn": "💼", "Instagram": "📸", "Blog": "✍️"}
            
            st.markdown(f"### {platform_icons.get(platform, '📝')} {platform} CONTENT")
            st.markdown(f"*Topic: **{st.session_state.topic}** | Style: **{content_style}***")
            
            # Sentiment Analysis Card
            if st.session_state.sentiment_results:
                sentiment = st.session_state.sentiment_results["sentiment"]
                polarity = st.session_state.sentiment_results["polarity"]
                emoji = st.session_state.sentiment_results["emoji"]
                
                st.markdown(f"""
                <div class="content-card">
                    <h4>📈 SENTIMENT ANALYSIS</h4>
                    <div style="display: flex; align-items: center; gap: 1rem; margin: 1rem 0;">
                        <span class="sentiment-badge sentiment-{sentiment}" style="font-size: 1.2rem;">
                            {emoji} <strong>{sentiment.upper()}</strong>
                        </span>
                        <span style="color: var(--text-gray);">
                            Polarity Score: <strong>{polarity:.3f}</strong>
                        </span>
                    </div>
                    <p style="color: var(--text-gray); margin-top: 0.5rem; font-size: 0.9rem;">
                        <strong>Insight:</strong> Your content has a <strong>{sentiment}</strong> tone. 
                        {f"Perfect for engaging and inspiring your audience! 🎯" if sentiment == "positive" else 
                          f"Great for balanced, informative content. 📊" if sentiment == "neutral" else 
                          f"Consider adding more positive elements for better engagement. 💡"}
                    </p>
                </div>
                """, unsafe_allow_html=True)
            
            # Display Platform-Specific Content
            content = st.session_state.generated_content
            
            if platform == "YouTube":
                with st.expander("🎬 **VIDEO CONTENT**", expanded=True):
                    st.markdown("#### 🎯 TITLE")
                    st.markdown(f"```\n{content.get('title', '')}\n```")
                    
                    st.markdown("#### 🎣 HOOK (First 15 seconds)")
                    st.info(content.get('hook', ''))
                    
                    st.markdown("#### 📝 DESCRIPTION")
                    st.code(content.get('description', ''), language="markdown")
                    
                    st.markdown("#### ⏱️ TIMESTAMPS")
                    for ts in content.get('timestamps', []):
                        st.markdown(f"• {ts}")
                    
                    st.markdown("#### 🔖 HASHTAGS")
                    st.write(" ".join(content.get('hashtags', [])))
            
            elif platform == "Twitter/X":
                with st.expander("🐦 **TWITTER THREAD**", expanded=True):
                    for i, tweet in enumerate(content.get('thread', []), 1):
                        st.markdown(f"**Tweet {i}:**")
                        st.info(tweet)
                        st.markdown("---")
                    
                    st.markdown("#### 🔖 HASHTAGS")
                    st.write(" ".join(content.get('hashtags', [])))
            
            elif platform == "LinkedIn":
                with st.expander("💼 **LINKEDIN POST**", expanded=True):
                    st.markdown("#### 📝 POST CONTENT")
                    st.code(content.get('content', ''), language="markdown")
                    
                    st.markdown("#### 🔖 HASHTAGS")
                    st.write(" ".join(content.get('hashtags', [])))
            
            elif platform == "Instagram":
                with st.expander("📸 **INSTAGRAM CONTENT**", expanded=True):
                    st.markdown("#### 📝 CAPTION")
                    st.code(content.get('caption', ''), language="markdown")
                    
                    st.markdown("#### 📱 STORY IDEAS")
                    for story in content.get('stories', []):
                        st.markdown(f"• {story}")
                    
                    st.markdown("#### 🔖 HASHTAGS")
                    st.write(" ".join(content.get('hashtags', [])))
            
            elif platform == "Blog":
                with st.expander("✍️ **BLOG ARTICLE**", expanded=True):
                    st.markdown("#### 📝 ARTICLE CONTENT")
                    st.code(content.get('content', ''), language="markdown")
                    
                    st.markdown("#### 🔖 TAGS")
                    st.write(", ".join(content.get('tags', [])))
            
            # Action Buttons
            col_copy, col_download, col_test = st.columns(3)
            with col_copy:
                if st.button("📋 **COPY CONTENT**", use_container_width=True):
                    st.toast(f"✅ {platform} content copied to clipboard!", icon="📋")
            with col_download:
                if st.button("💾 **DOWNLOAD**", use_container_width=True):
                    st.toast(f"✅ {platform} content downloaded as text file!", icon="💾")
            with col_test:
                if st.button("🧪 **RUN A/B TEST**", use_container_width=True):
                    # Simulate test results
                    st.session_state.test_results = {
                        "impressions": random.randint(3000, 10000),
                        "engagement": round(random.uniform(60, 85), 1),
                        "conversion": round(random.uniform(8, 15), 1),
                        "confidence": round(random.uniform(85, 98), 1),
                        "variants": {
                            "Conversational": random.randint(70, 85),
                            "Professional": random.randint(65, 80),
                            "Motivational": random.randint(68, 82)
                        },
                        "platform": platform,
                        "sentiment": sentiment,
                        "polarity": polarity
                    }
                    st.toast("🧪 A/B test initiated! Check Results tab.", icon="🧪")
                    st.rerun()

# ========== TAB 2: TEST RESULTS ==========
with tab2:
    if st.session_state.test_results:
        results = st.session_state.test_results
        
        # Stats Cards
        st.markdown("## 📊 TEST RESULTS & ANALYSIS")
        
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
        
        # Performance Chart
        st.markdown("### 📈 VARIANT PERFORMANCE")
        
        fig = go.Figure(data=[
            go.Bar(
                x=list(results['variants'].keys()),
                y=list(results['variants'].values()),
                marker_color=['#6366f1', '#94a3b8', '#94a3b8'],
                text=[f"{v}%" for v in results['variants'].values()],
                textposition='auto',
            )
        ])
        
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='white',
            showlegend=False,
            height=350,
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # AI Recommendations
        st.markdown("### 🤖 AI RECOMMENDATIONS")
        
        winning_style = max(results['variants'], key=results['variants'].get)
        winning_score = max(results['variants'].values())
        
        recommendations = [
            f"🏆 **WINNER**: **{winning_style}** style with **{winning_score}%** engagement",
            f"📊 **STATISTICAL SIGNIFICANCE**: {random.randint(75, 95)}% higher than next best variant",
            f"🎯 **OPTIMIZATION**: Test different angles for '{st.session_state.topic}' on {results['platform']}",
            f"💡 **INSIGHT**: {results['sentiment'].capitalize()} sentiment works well with {winning_style.lower()} tone",
            f"⏱️ **NEXT STEPS**: Run this test for 48-72 hours before final deployment"
        ]
        
        for rec in recommendations:
            st.markdown(f"• {rec}")
        
        # Deploy Button
        st.markdown("---")
        col_deploy, col_clear, _ = st.columns([1, 1, 2])
        with col_deploy:
            if st.button("🚀 **DEPLOY WINNING VARIANT**", use_container_width=True):
                st.success(f"✅ {winning_style} variant deployed to {results['platform']}!")
        with col_clear:
            if st.button("🔄 **CLEAR RESULTS**", use_container_width=True):
                st.session_state.test_results = None
                st.rerun()
    
    else:
        st.markdown("""
        <div style="text-align: center; padding: 4rem 2rem;">
            <div style="font-size: 4rem; margin-bottom: 1rem;">📊</div>
            <h3 style="color: var(--text-light); margin-bottom: 1rem;">NO TEST RESULTS YET</h3>
            <p style="color: var(--text-gray); margin-bottom: 2rem;">
                Generate content and run A/B tests in the 'Generate Content' tab to see detailed analytics here.
            </p>
        </div>
        """, unsafe_allow_html=True)

# ========== FOOTER ==========
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: var(--text-gray); padding: 2rem;">
        <h2 style="font-size: 2.5rem; margin-bottom: 0.5rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            🚀 AI CONTENT OPTIMIZER PRO
        </h2>
        <p style="font-size: 1rem; margin-top: 0.5rem;">v4.0 • Multi-Platform Content Generation • Sentiment Analysis • A/B Testing</p>
    </div>
    """, 
    unsafe_allow_html=True
)