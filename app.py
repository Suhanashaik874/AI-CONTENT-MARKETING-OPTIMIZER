import streamlit as st
import pandas as pd
import numpy as np
import random
from datetime import datetime
import time
import re
from typing import Dict, List, Any

# Page configuration
st.set_page_config(
    page_title="AI Content Optimizer",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS to match your HTML exactly
st.markdown("""
<style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: 'Segoe UI', system-ui, sans-serif;
    }

    body {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: #333;
        min-height: 100vh;
        padding: 20px;
    }

    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        min-height: 100vh;
    }

    .main-container {
        max-width: 1400px;
        margin: 0 auto;
        background: white;
        border-radius: 20px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        overflow: hidden;
        display: flex;
        min-height: 90vh;
    }

    /* Sidebar */
    .sidebar {
        width: 280px;
        background: #1a1f36;
        color: white;
        padding: 30px 20px;
    }

    .logo {
        display: flex;
        align-items: center;
        gap: 15px;
        margin-bottom: 40px;
        padding-bottom: 20px;
        border-bottom: 1px solid rgba(255,255,255,0.1);
    }

    .logo-icon {
        width: 40px;
        height: 40px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 20px;
    }

    .logo-text {
        font-size: 24px;
        font-weight: 700;
    }

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

    .platform-icon {
        width: 40px;
        height: 40px;
        background: rgba(255,255,255,0.1);
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 20px;
    }

    /* Main Content */
    .main-content {
        flex: 1;
        padding: 30px;
    }

    /* Header */
    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 30px;
    }

    .header-left h1 {
        font-size: 28px;
        color: #1a1f36;
        margin-bottom: 5px;
    }

    .header-left p {
        color: #666;
        font-size: 14px;
    }

    /* Topic Section */
    .topic-section {
        background: #f8f9ff;
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 30px;
        border: 2px solid #e0e6ff;
    }

    /* Generator Panel */
    .generator-panel {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 30px;
        margin-bottom: 30px;
    }

    /* Platform Preview */
    .platform-preview {
        background: white;
        border-radius: 15px;
        padding: 25px;
        border: 2px solid #e0e6ff;
    }

    .content-preview {
        flex: 1;
        background: #f8f9ff;
        border-radius: 10px;
        padding: 20px;
        font-size: 15px;
        line-height: 1.6;
        white-space: pre-wrap;
        margin-bottom: 20px;
        border: 1px solid #e0e6ff;
        min-height: 300px;
        max-height: 400px;
        overflow-y: auto;
    }

    /* A/B Testing */
    .ab-testing-section {
        background: white;
        border-radius: 15px;
        padding: 25px;
        border: 2px solid #e0e6ff;
    }

    .ab-variant-card {
        background: white;
        border-radius: 10px;
        padding: 20px;
        border: 2px solid #e0e6ff;
        margin-bottom: 15px;
    }

    .ab-variant-card.winner {
        border-color: #10b981;
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.05) 0%, rgba(16, 185, 129, 0.1) 100%);
    }

    /* Results */
    .ab-results-panel {
        background: white;
        border-radius: 15px;
        padding: 25px;
        margin-top: 20px;
        border: 2px solid #e0e6ff;
    }

    .results-stats {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 15px;
        margin: 20px 0;
    }

    .result-stat {
        text-align: center;
        padding: 15px;
        background: #f8f9ff;
        border-radius: 10px;
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        transition: all 0.3s !important;
    }

    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3) !important;
    }

    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom scrollbar */
    .content-preview::-webkit-scrollbar {
        width: 8px;
    }
    
    .content-preview::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 4px;
    }
    
    .content-preview::-webkit-scrollbar-thumb {
        background: #667eea;
        border-radius: 4px;
    }
    
    /* Ensure proper spacing */
    .main .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }
    
    /* Make text white in dark areas */
    .sidebar h3, .sidebar p, .platform-info h3 {
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'current_platform' not in st.session_state:
    st.session_state.current_platform = 'youtube'
if 'current_topic' not in st.session_state:
    st.session_state.current_topic = 'Machine Learning'
if 'current_test_type' not in st.session_state:
    st.session_state.current_test_type = 'quick'
if 'generated_content' not in st.session_state:
    st.session_state.generated_content = ''
if 'show_results' not in st.session_state:
    st.session_state.show_results = False
if 'variations' not in st.session_state:
    st.session_state.variations = []
if 'test_results' not in st.session_state:
    st.session_state.test_results = {}

# Content Generator Functions (FIXED VERSION - Python syntax)
def create_hashtag(topic: str) -> str:
    """Create hashtag from topic - FIXED Python version"""
    # Remove non-alphanumeric characters using Python regex
    cleaned = re.sub(r'[^\w\s]', '', topic)
    # Remove spaces
    no_spaces = re.sub(r'\s+', '', cleaned)
    # Take first 20 characters
    return no_spaces[:20]

def generate_youtube_content(topic: str) -> str:
    """Generate YouTube content for any topic"""
    return f'''🎬 **YouTube Video: "{topic}" Explained**

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
#{topic.replace(" ", "")} #Education #Learning #Tutorial #HowTo #ExplainerVideo

💎 **PRO TIP:** Bookmark this video for future reference!'''

def generate_twitter_content(topic: str) -> str:
    """Generate Twitter content for any topic"""
    hashtag = topic.replace(" ", "")
    return f'''🧵 **Twitter Thread: Understanding {topic}**

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

#{hashtag} #Thread #Learning #Education #Knowledge'''

def generate_linkedin_content(topic: str) -> str:
    """Generate LinkedIn content for any topic"""
    return f'''**Professional Insight: Mastering "{topic}" in Today's Landscape**

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

#{topic.replace(" ", "")} #ProfessionalDevelopment #CareerGrowth #Business #Leadership #Skills'''

def generate_instagram_content(topic: str) -> str:
    """Generate Instagram content for any topic"""
    return f'''🌟 **INSTAGRAM POST: MASTERING {topic.upper()}** 🌟

Ready to dive into {topic}? Here's your complete guide! 👇

[IMAGE 1: Eye-catching graphic about {topic}]
[IMAGE 2: Step-by-step process visual]
[IMAGE 3: Before/After comparison]
[IMAGE 4: Quick tips carousel]

💡 **5 KEY TAKEAWAYS:**

1️⃣ Start small - don't overwhelm yourself!
2️⃣ Consistency beats intensity every time
3️⃣ Learn from both successes AND failures
4️⃣ Document your progress
5️⃣ Share your journey with others

✨ **PRO TIP:** The best time to start was yesterday. The second best time is NOW!

🔔 **TURN ON POST NOTIFICATIONS** for daily tips!

[STORY IDEAS]
→ "Myth vs Fact about {topic}"
→ "Quick tutorial: Getting started"
→ "Common mistakes to avoid"
→ "Poll: What's your biggest challenge?"

📌 **SAVE THIS POST** for when you need it!

💬 **COMMENT BELOW:**
What's one thing you want to learn about {topic}?

#{topic.replace(" ", "")} #Instagram #HowTo #Guide #Tips #Learn #Education'''

def generate_blog_content(topic: str) -> str:
    """Generate Blog content for any topic"""
    return f'''# The Complete Guide to {topic}: Everything You Need to Know

## Executive Summary
This comprehensive guide explores {topic} from multiple angles, providing both beginners and experienced individuals with valuable insights and actionable strategies.

## Introduction
In today's fast-paced world, {topic} has emerged as a critical area of interest. Whether you're just starting out or looking to deepen your understanding, this guide will provide the foundation you need.

## Understanding {topic}

### What is {topic}?
At its core, {topic} represents [adaptive explanation based on topic]. It's more than just a concept - it's a framework for understanding [related area].

### Historical Context
• Origins and early development
• Key milestones and breakthroughs
• Current state and future potential

## Why {topic} Matters

### Personal Benefits
• Enhanced understanding of [related concepts]
• Improved decision-making capabilities
• Increased confidence in [related areas]

### Professional Applications
• Workplace efficiency improvements
• Career advancement opportunities
• Industry-specific advantages

## Getting Started with {topic}

### Step 1: Foundation Building
Begin with basic concepts and terminology.

### Step 2: Practical Application
Apply what you learn in real-world scenarios.

### Step 3: Advanced Techniques
Once comfortable, explore more complex applications.

## Common Challenges & Solutions

### Challenge 1: Overcoming Initial Complexity
**Solution:** Break it down into smaller, manageable parts.

### Challenge 2: Staying Motivated
**Solution:** Set clear goals and track progress.

### Challenge 3: Finding Quality Resources
**Solution:** Curate a list of trusted sources.

## Future Outlook
The future of {topic} looks promising, with several key developments on the horizon. Experts predict significant evolution in how we approach and apply these concepts.

## Conclusion
{topic} offers valuable insights and practical applications for anyone willing to invest the time to learn. By following the guidance in this article, you'll be well on your way to mastering this important area.

---

**Ready to dive deeper into {topic}?** Share your thoughts and questions in the comments below!'''

def generate_content(topic: str, platform: str) -> str:
    """Generate content for any topic on any platform"""
    generators = {
        'youtube': generate_youtube_content,
        'twitter': generate_twitter_content,
        'linkedin': generate_linkedin_content,
        'instagram': generate_instagram_content,
        'blog': generate_blog_content
    }
    
    generator = generators.get(platform, generate_youtube_content)
    return generator(topic)

def generate_ab_variations(topic: str, platform: str, test_type: str = 'quick') -> List[Dict]:
    """Generate A/B test variations"""
    variant_count = 3 if test_type == 'quick' else 5
    
    styles = [
        {'name': 'Professional', 'emoji': '👔', 'tone': 'formal', 'description': 'Data-driven and authoritative', 'color': '#3b82f6'},
        {'name': 'Conversational', 'emoji': '💬', 'tone': 'casual', 'description': 'Friendly and approachable', 'color': '#10b981'},
        {'name': 'Motivational', 'emoji': '🚀', 'tone': 'inspiring', 'description': 'Energetic and encouraging', 'color': '#f59e0b'},
        {'name': 'Analytical', 'emoji': '📊', 'tone': 'detailed', 'description': 'In-depth and technical', 'color': '#8b5cf6'},
        {'name': 'Storytelling', 'emoji': '📖', 'tone': 'narrative', 'description': 'Personal and engaging', 'color': '#ec4899'}
    ]
    
    variations = []
    for i in range(min(variant_count, len(styles))):
        style = styles[i]
        
        # Generate dynamic metrics
        if style['tone'] == 'conversational':
            base_engagement = 75
        elif style['tone'] == 'motivational':
            base_engagement = 80
        elif style['tone'] == 'storytelling':
            base_engagement = 78
        else:
            base_engagement = 70
            
        engagement = base_engagement + (random.random() * 15 - 5)
        clarity = 70 + random.random() * 25
        sentiment = style['tone'] == 'motivational' and 1.2 + random.random() * 0.8 or 0.8 + random.random() * 0.6
        impressions = random.randint(500, 2500)
        
        # Get platform name
        platform_names = {
            'youtube': 'YouTube',
            'twitter': 'Twitter/X',
            'linkedin': 'LinkedIn',
            'instagram': 'Instagram',
            'blog': 'Blog'
        }
        
        # Generate variant content
        base_content = generate_content(topic, platform)
        style_modifiers = {
            'Professional': f"**{style['name']} Approach:** This variation presents {topic} with precision and authority, backed by data and expert insights. Perfect for audiences seeking credible, well-researched information.\n\n",
            'Conversational': f"**{style['name']} Approach:** Hey there! Let's chat about {topic} like friends. This variation uses everyday language and relatable examples to make complex concepts easy to understand.\n\n",
            'Motivational': f"**{style['name']} Approach:** Ready to transform your understanding of {topic}? This inspiring variation will energize and motivate you to take action today!\n\n",
            'Analytical': f"**{style['name']} Approach:** Detailed analysis of {topic} reveals key patterns and insights. This variation breaks down complex information into understandable components with clear explanations.\n\n",
            'Storytelling': f"**{style['name']} Approach:** Let me share a story about {topic} that changed my perspective. This personal, narrative approach creates emotional connection and memorable learning.\n\n"
        }
        
        modifier = style_modifiers.get(style['name'], style_modifiers['Professional'])
        content = modifier + base_content[:300] + '...'
        
        variations.append({
            'id': f'variant-{i+1}',
            'name': f"{style['emoji']} {style['name']}",
            'style': style['name'],
            'description': style['description'],
            'platform': platform_names.get(platform, platform),
            'engagement': round(engagement),
            'clarity': round(clarity),
            'sentiment': round(sentiment, 2),
            'impressions': impressions,
            'content': content,
            'conversion': round(3 + random.random() * 7, 1),
            'color': style['color'],
            'emoji': style['emoji']
        })
    
    # Sort by engagement and mark winner
    variations.sort(key=lambda x: x['engagement'], reverse=True)
    variations[0]['is_winner'] = True
    variations[0]['badge'] = 'winner'
    
    for v in variations[1:]:
        v['is_winner'] = False
        v['badge'] = 'contender'
    
    return variations

def generate_test_results(variations: List[Dict]) -> Dict:
    """Generate test results from variations"""
    total_impressions = sum(v['impressions'] for v in variations)
    avg_engagement = sum(v['engagement'] for v in variations) / len(variations)
    winner = variations[0]
    second_best = variations[1] if len(variations) > 1 else winner
    confidence = min(99, 75 + ((winner['engagement'] - second_best['engagement']) * 2))
    
    return {
        'total_impressions': f"{total_impressions:,}",
        'avg_engagement': f"{avg_engagement:.1f}%",
        'conversion_rate': f"{winner['conversion']}%",
        'confidence_level': f"{confidence:.1f}%",
        'winner': winner,
        'variations': variations
    }

def generate_recommendations(winner: Dict, variations: List[Dict], topic: str) -> List[str]:
    """Generate AI recommendations"""
    recommendations = []
    
    second_best_engagement = variations[1]['engagement'] if len(variations) > 1 else winner['engagement']
    difference = winner['engagement'] - second_best_engagement
    
    recommendations.append(f"🎯 **Winner Selected:** \"{winner['style']}\" style with {winner['engagement']}% engagement score")
    recommendations.append(f"📊 **Statistical Significance:** {difference:.1f}% higher than next best variant")
    
    if winner['engagement'] > 85:
        recommendations.append(f"🌟 **Excellent Performance:** This variant is performing exceptionally well. Consider using it as your primary content strategy.")
    elif winner['engagement'] > 75:
        recommendations.append(f"👍 **Good Performance:** Solid results. This variant shows strong potential for your \"{topic}\" content.")
    else:
        recommendations.append(f"💡 **Optimization Opportunity:** Consider refining the messaging or testing different angles for \"{topic}\".")
    
    recommendations.append(f"🎨 **Style Analysis:** {winner['description']} approach resonates best with your audience for \"{topic}\" content.")
    recommendations.append(f"⏰ **Testing Duration:** For conclusive results, run this test for 48-72 hours before finalizing.")
    
    return recommendations

# Main App Layout
def main():
    # Add Font Awesome
    st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    """, unsafe_allow_html=True)
    
    # Create container for the main app
    main_container = st.container()
    
    with main_container:
        # Create two columns for sidebar and main content
        col1, col2 = st.columns([280, 1120])
        
        with col1:
            # Sidebar Logo
            st.markdown("""
            <div class="sidebar">
                <div class="logo">
                    <div class="logo-icon">
                        <i class="fas fa-robot"></i>
                    </div>
                    <div class="logo-text">AI Optimizer</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Platform Selection
            platforms = [
                {'id': 'youtube', 'name': 'YouTube', 'icon': 'fab fa-youtube', 'desc': 'Video scripts & descriptions'},
                {'id': 'twitter', 'name': 'Twitter/X', 'icon': 'fab fa-twitter', 'desc': 'Tweets & threads'},
                {'id': 'linkedin', 'name': 'LinkedIn', 'icon': 'fab fa-linkedin', 'desc': 'Professional posts'},
                {'id': 'instagram', 'name': 'Instagram', 'icon': 'fab fa-instagram', 'desc': 'Captions & stories'},
                {'id': 'blog', 'name': 'Blog', 'icon': 'fas fa-blog', 'desc': 'Articles & long-form'}
            ]
            
            for platform in platforms:
                is_active = st.session_state.current_platform == platform['id']
                active_class = 'active' if is_active else ''
                
                if st.button(
                    f"{platform['name']}",
                    key=f"platform_{platform['id']}",
                    help=platform['desc'],
                    use_container_width=True
                ):
                    st.session_state.current_platform = platform['id']
                    st.rerun()
        
        with col2:
            # Header
            col_header1, col_header2 = st.columns([3, 1])
            
            with col_header1:
                platform_names = {
                    'youtube': 'YouTube',
                    'twitter': 'Twitter/X', 
                    'linkedin': 'LinkedIn',
                    'instagram': 'Instagram',
                    'blog': 'Blog'
                }
                current_platform_name = platform_names.get(st.session_state.current_platform, 'AI Content Optimizer')
                
                st.markdown(f"""
                <div class="header">
                    <div class="header-left">
                        <h1>{current_platform_name} Content Generator</h1>
                        <p>Generate content for any topic on any platform</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            with col_header2:
                current_time = datetime.now().strftime("%H:%M %d-%m-%Y")
                st.markdown(f"""
                <div style="text-align: right; color: #666; font-size: 14px; margin-top: 10px;">
                    <i class="far fa-clock"></i> {current_time}
                </div>
                """, unsafe_allow_html=True)
            
            # Topic Input Section
            st.markdown("""
            <div class="topic-section">
                <h2 class="section-title">
                    <i class="fas fa-edit"></i> Enter Any Topic
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            col_topic1, col_topic2, col_topic3 = st.columns([3, 1, 1])
            
            with col_topic1:
                topic = st.text_input(
                    " ",
                    value=st.session_state.current_topic,
                    placeholder="Enter ANY topic (e.g., 'How to bake sourdough bread', 'Benefits of meditation', 'Future of electric cars')",
                    label_visibility="collapsed",
                    key="topic_input"
                )
            
            with col_topic2:
                if st.button("✨ Generate Content", use_container_width=True, type="primary"):
                    if topic.strip():
                        st.session_state.current_topic = topic.strip()
                        st.session_state.generated_content = generate_content(
                            st.session_state.current_topic,
                            st.session_state.current_platform
                        )
                        st.rerun()
                    else:
                        st.warning("Please enter a topic!")
            
            with col_topic3:
                if st.button("🧪 Run A/B Test", use_container_width=True, type="secondary"):
                    if topic.strip():
                        st.session_state.current_topic = topic.strip()
                        
                        # Generate content if not already generated
                        if not st.session_state.generated_content:
                            st.session_state.generated_content = generate_content(
                                st.session_state.current_topic,
                                st.session_state.current_platform
                            )
                        
                        # Generate variations
                        st.session_state.variations = generate_ab_variations(
                            st.session_state.current_topic,
                            st.session_state.current_platform,
                            st.session_state.current_test_type
                        )
                        
                        # Generate test results
                        st.session_state.test_results = generate_test_results(st.session_state.variations)
                        st.session_state.show_results = True
                        st.rerun()
                    else:
                        st.warning("Please enter a topic!")
            
            st.markdown("""
            <p style="margin-top: 10px; color: #666; font-size: 14px;">
                <i class="fas fa-lightbulb"></i> Tip: You can enter ANY topic - from cooking recipes to quantum physics!
            </p>
            """, unsafe_allow_html=True)
            
            # Generator Panel
            st.markdown('<div class="generator-panel">', unsafe_allow_html=True)
            
            # Left Column: Platform Content Preview
            col_preview, col_ab = st.columns(2)
            
            with col_preview:
                st.markdown("""
                <div class="platform-preview">
                    <div class="platform-preview-header">
                        <div class="platform-display">
                            <i class="fab fa-youtube"></i>
                            <div>
                                <h3>YouTube Content</h3>
                                <p>Video script & description</p>
                            </div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Display content preview
                if st.session_state.generated_content:
                    st.markdown(f'<div class="content-preview">{st.session_state.generated_content}</div>', unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div class="content-preview">
                        Enter any topic above and click "Generate Content" to see platform-specific content here.
                    </div>
                    """, unsafe_allow_html=True)
                
                # Copy button
                if st.button("📋 Copy Content", use_container_width=True):
                    if st.session_state.generated_content:
                        st.toast("Content copied to clipboard! ✅", icon="📋")
                    else:
                        st.warning("Generate content first!")
            
            # Right Column: A/B Testing
            with col_ab:
                st.markdown("""
                <div class="ab-testing-section">
                    <div class="ab-testing-header">
                        <h2 class="section-title">
                            <i class="fas fa-vial"></i> A/B Testing Variations
                        </h2>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Test type selection
                col_test1, col_test2 = st.columns(2)
                with col_test1:
                    if st.button("Quick Test (3 variants)", 
                                key="quick_test",
                                use_container_width=True,
                                type="primary" if st.session_state.current_test_type == 'quick' else "secondary"):
                        st.session_state.current_test_type = 'quick'
                        st.rerun()
                
                with col_test2:
                    if st.button("Comprehensive (5 variants)",
                                key="comprehensive_test",
                                use_container_width=True,
                                type="primary" if st.session_state.current_test_type == 'comprehensive' else "secondary"):
                        st.session_state.current_test_type = 'comprehensive'
                        st.rerun()
                
                # Display variations
                if st.session_state.variations:
                    for i, variant in enumerate(st.session_state.variations):
                        winner_class = 'winner' if variant['is_winner'] else ''
                        
                        st.markdown(f"""
                        <div class="ab-variant-card {winner_class}">
                            <div class="ab-variant-header">
                                <div>
                                    <div class="variant-title">{variant['name']} - {variant['description']}</div>
                                    <div class="variant-platform">
                                        <i class="fab fa-{st.session_state.current_platform}"></i>
                                        For: "{st.session_state.current_topic}"
                                    </div>
                                </div>
                                <div class="variant-badge" style="background: {'#10b981' if variant['badge'] == 'winner' else '#f59e0b'}; color: white; padding: 5px 12px; border-radius: 20px; font-size: 12px; font-weight: 500;">
                                    {'🏆 Winner' if variant['badge'] == 'winner' else '🥈 Contender'}
                                </div>
                            </div>
                            
                            <div class="variant-content" style="color: #666; font-size: 14px; line-height: 1.5; margin-bottom: 20px;">
                                {variant['content']}
                            </div>
                            
                            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin: 15px 0;">
                                <div style="text-align: center; padding: 10px; background: #f8f9ff; border-radius: 8px;">
                                    <div style="font-size: 18px; font-weight: 700; margin-bottom: 5px;">{variant['engagement']}%</div>
                                    <div style="font-size: 11px; color: #666;">Engagement</div>
                                </div>
                                <div style="text-align: center; padding: 10px; background: #f8f9ff; border-radius: 8px;">
                                    <div style="font-size: 18px; font-weight: 700; margin-bottom: 5px;">{variant['clarity']}%</div>
                                    <div style="font-size: 11px; color: #666;">Clarity</div>
                                </div>
                                <div style="text-align: center; padding: 10px; background: #f8f9ff; border-radius: 8px;">
                                    <div style="font-size: 18px; font-weight: 700; margin-bottom: 5px;">{variant['sentiment']}%</div>
                                    <div style="font-size: 11px; color: #666;">Sentiment</div>
                                </div>
                            </div>
                            
                            <div style="display: flex; gap: 10px; margin-top: 15px;">
                                <button style="flex: 1; padding: 8px; background: #667eea; color: white; border: none; border-radius: 6px; cursor: pointer; font-size: 12px;" onclick="alert('Variant selected!')">
                                    <i class="fas fa-check"></i> Use This
                                </button>
                                <button style="flex: 1; padding: 8px; background: white; border: 1px solid #e0e6ff; border-radius: 6px; cursor: pointer; font-size: 12px;" onclick="alert('Preview variant')">
                                    <i class="fas fa-eye"></i> Preview
                                </button>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div style="text-align: center; padding: 40px; color: #666;">
                        <i class="fas fa-vial" style="font-size: 48px; margin-bottom: 20px; opacity: 0.3;"></i>
                        <p>Click "Run A/B Test" to generate variations for your topic</p>
                    </div>
                    """, unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)  # Close generator-panel
            
            # A/B Test Results Panel
            if st.session_state.show_results and st.session_state.test_results:
                st.markdown('<div class="ab-results-panel">', unsafe_allow_html=True)
                
                # Results Header
                col_results1, col_results2 = st.columns([3, 1])
                with col_results1:
                    st.markdown("""
                    <h2 class="section-title">
                        <i class="fas fa-chart-bar"></i> Test Results & Analysis
                    </h2>
                    """, unsafe_allow_html=True)
                
                with col_results2:
                    winner = st.session_state.test_results['winner']
                    st.markdown(f"""
                    <div style="background: #10b981; color: white; padding: 8px 16px; border-radius: 20px; font-weight: 600; text-align: center;">
                        Winner: {winner['style']} Style
                    </div>
                    """, unsafe_allow_html=True)
                
                # Stats Grid
                results = st.session_state.test_results
                col_stats1, col_stats2, col_stats3, col_stats4 = st.columns(4)
                
                with col_stats1:
                    st.markdown(f"""
                    <div class="result-stat">
                        <div class="result-stat-value">{results['total_impressions']}</div>
                        <div class="result-stat-label">Total Impressions</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col_stats2:
                    st.markdown(f"""
                    <div class="result-stat">
                        <div class="result-stat-value">{results['avg_engagement']}</div>
                        <div class="result-stat-label">Avg Engagement</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col_stats3:
                    st.markdown(f"""
                    <div class="result-stat">
                        <div class="result-stat-value">{results['conversion_rate']}</div>
                        <div class="result-stat-label">Conversion Rate</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col_stats4:
                    st.markdown(f"""
                    <div class="result-stat">
                        <div class="result-stat-value">{results['confidence_level']}</div>
                        <div class="result-stat-label">Confidence Level</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Performance Chart
                st.markdown("""
                <h3 style="color: #1a1f36; margin: 30px 0 20px 0;">📊 Variant Performance</h3>
                """, unsafe_allow_html=True)
                
                # Create chart using columns
                chart_cols = st.columns(len(st.session_state.variations))
                for idx, (col, variant) in enumerate(zip(chart_cols, st.session_state.variations)):
                    bar_height = min(100, variant['engagement'] + 20)
                    with col:
                        st.markdown(f"""
                        <div style="text-align: center;">
                            <div style="height: {bar_height}px; width: 60px; margin: 0 auto; background: linear-gradient(to top, {variant['color']}, {variant['color']}99); border-radius: 8px 8px 0 0; position: relative;">
                                <div style="position: absolute; top: -30px; left: 50%; transform: translateX(-50%); font-weight: 700; color: #1a1f36;">
                                    {variant['engagement']}%
                                </div>
                            </div>
                            <div style="margin-top: 10px; font-weight: 600; color: #1a1f36;">{variant['style']}</div>
                        </div>
                        """, unsafe_allow_html=True)
                
                # AI Recommendations
                st.markdown("""
                <h3 style="color: #1a1f36; margin: 40px 0 20px 0;">
                    <i class="fas fa-lightbulb"></i> AI Recommendations
                </h3>
                """, unsafe_allow_html=True)
                
                recommendations = generate_recommendations(
                    results['winner'],
                    results['variations'],
                    st.session_state.current_topic
                )
                
                for rec in recommendations:
                    st.markdown(f"""
                    <div style="margin-bottom: 10px; padding-left: 20px; position: relative;">
                        <span style="position: absolute; left: 0;">•</span> {rec}
                    </div>
                    """, unsafe_allow_html=True)
                
                st.markdown('</div>', unsafe_allow_html=True)  # Close ab-results-panel
            
            # Footer
            st.markdown("""
            <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 30px; padding-top: 20px; border-top: 1px solid #e0e6ff; color: #666; font-size: 14px;">
                <div>
                    <div><i class="fas fa-cloud-rain"></i> Light rain Tomorrow</div>
                    <div><i class="fas fa-search"></i> Search</div>
                </div>
                <div>
                    <span><i class="fas fa-globe"></i> ENG</span>
                    <span style="margin-left: 10px;">IN</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()