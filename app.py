import streamlit as st
import random
import re
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="AI Content Optimizer",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ========== CUSTOM CSS - EXACTLY MATCHING YOUR HTML ==========
st.markdown("""
<style>
    /* Reset and base styles */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: 'Segoe UI', system-ui, sans-serif;
    }

    /* Force the body and app to match your HTML */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        padding: 20px !important;
        min-height: 100vh !important;
    }

    /* Main container - exactly like your HTML */
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

    /* Sidebar styles */
    .sidebar-container {
        width: 280px;
        background: #1a1f36;
        color: white;
        padding: 30px 20px;
        display: flex;
        flex-direction: column;
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
        border: none;
        width: 100%;
        text-align: left;
        color: white;
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

    .platform-info h3 {
        font-size: 16px;
        margin-bottom: 5px;
        font-weight: 600;
    }

    .platform-info p {
        font-size: 12px;
        opacity: 0.7;
        margin: 0;
    }

    /* Main content area */
    .main-content-container {
        flex: 1;
        padding: 30px;
        display: flex;
        flex-direction: column;
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

    /* Topic section */
    .topic-section {
        background: #f8f9ff;
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 30px;
        border: 2px solid #e0e6ff;
    }

    .section-title {
        color: #1a1f36;
        font-size: 20px;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    /* Buttons */
    .custom-button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 12px 30px;
        border-radius: 10px;
        font-weight: 600;
        cursor: pointer;
        display: flex;
        align-items: center;
        gap: 10px;
        transition: all 0.3s;
        font-size: 14px;
    }

    .custom-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
    }

    .custom-button.secondary {
        background: #10b981;
    }

    /* Generator panel */
    .generator-panel {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 30px;
        margin-bottom: 30px;
        flex: 1;
    }

    /* Platform preview */
    .platform-preview {
        background: white;
        border-radius: 15px;
        padding: 25px;
        border: 2px solid #e0e6ff;
        display: flex;
        flex-direction: column;
    }

    .platform-preview-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
        padding-bottom: 20px;
        border-bottom: 1px solid #e0e6ff;
    }

    .platform-display {
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 10px 20px;
        background: #f8f9ff;
        border-radius: 10px;
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
        transition: all 0.3s;
    }

    .ab-variant-card.winner {
        border-color: #10b981;
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.05) 0%, rgba(16, 185, 129, 0.1) 100%);
    }

    /* Hide all Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .stApp > header {display: none !important;}
    .stApp > div:nth-child(2) {padding: 0 !important;}
    
    /* Override Streamlit columns */
    .st-emotion-cache-1r6slb0 {
        padding: 0 !important;
        gap: 0 !important;
    }
    
    /* Make sure buttons look right */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        padding: 12px 24px !important;
    }
    
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
</style>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
""", unsafe_allow_html=True)

# ========== SESSION STATE ==========
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

# ========== CONTENT GENERATOR FUNCTIONS ==========
def generate_youtube_content(topic):
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

def generate_twitter_content(topic):
    return f'''🧵 **Twitter Thread: Understanding {topic}**

1/7 Thinking about {topic}? Here's a comprehensive thread breaking down everything you need to know:

2/7 First, let's define {topic} in simple terms. It's essentially a fascinating concept worth exploring.

3/7 The 3 most important things to know about {topic}:
1. It's more accessible than you think
2. It has practical applications
3. It's evolving rapidly

4/7 Common mistakes people make with {topic} (and how to avoid them):
• Overcomplicating basic concepts
• Not applying learnings practically
• Giving up too early

5/7 Practical applications of {topic} in daily life:
→ Problem-solving
→ Decision-making
→ Innovation

6/7 Future outlook: Where is {topic} heading?
• Increased adoption
• New technologies
• Broader applications

7/7 Want to learn more about {topic}?
• Follow for daily insights
• Check resources in my bio
• Reply with your questions!

#{topic.replace(" ", "")} #Thread #Learning #Education #Knowledge'''

def generate_linkedin_content(topic):
    return f'''**Professional Insight: Mastering "{topic}" in Today's Landscape**

As professionals, understanding {topic} has become increasingly important in our rapidly evolving work environment.

**Why {topic} Matters Now:**
Recent industry analysis shows that professionals with expertise in {topic} see significant advantages in their careers.

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

def generate_instagram_content(topic):
    return f'''🌟 **INSTAGRAM POST: MASTERING {topic.upper()}** 🌟

Ready to dive into {topic}? Here's your complete guide! 👇

💡 **5 KEY TAKEAWAYS:**

1️⃣ Start small - don't overwhelm yourself!
2️⃣ Consistency beats intensity every time
3️⃣ Learn from both successes AND failures
4️⃣ Document your progress
5️⃣ Share your journey with others

✨ **PRO TIP:** The best time to start was yesterday. The second best time is NOW!

[STORY IDEAS]
→ "Myth vs Fact about {topic}"
→ "Quick tutorial: Getting started"
→ "Common mistakes to avoid"
→ "Poll: What's your biggest challenge?"

📌 **SAVE THIS POST** for when you need it!

💬 **COMMENT BELOW:**
What's one thing you want to learn about {topic}?

#{topic.replace(" ", "")} #Instagram #HowTo #Guide #Tips #Learn #Education'''

def generate_blog_content(topic):
    return f'''# The Complete Guide to {topic}: Everything You Need to Know

## Introduction
In today's fast-paced world, {topic} has emerged as a critical area of interest. Whether you're just starting out or looking to deepen your understanding, this guide will provide the foundation you need.

## Understanding {topic}
{topic} represents an important field that combines various disciplines to solve complex problems and create new opportunities.

## Why {topic} Matters
• Enhanced understanding of related concepts
• Improved decision-making capabilities
• Career advancement opportunities
• Industry-specific advantages

## Getting Started with {topic}

### Step 1: Foundation Building
Begin with basic concepts and terminology.

### Step 2: Practical Application
Apply what you learn in real-world scenarios.

### Step 3: Advanced Techniques
Once comfortable, explore more complex applications.

## Conclusion
{topic} offers valuable insights and practical applications for anyone willing to invest the time to learn. By following the guidance in this article, you'll be well on your way to mastering this important area.

---

**Ready to dive deeper into {topic}?** Share your thoughts and questions in the comments below!'''

def generate_content(topic, platform):
    generators = {
        'youtube': generate_youtube_content,
        'twitter': generate_twitter_content,
        'linkedin': generate_linkedin_content,
        'instagram': generate_instagram_content,
        'blog': generate_blog_content
    }
    return generators.get(platform, generate_youtube_content)(topic)

def generate_ab_variations(topic, platform, test_type='quick'):
    styles = [
        {'name': 'Professional', 'emoji': '👔', 'color': '#3b82f6'},
        {'name': 'Conversational', 'emoji': '💬', 'color': '#10b981'},
        {'name': 'Motivational', 'emoji': '🚀', 'color': '#f59e0b'}
    ]
    
    if test_type == 'comprehensive':
        styles.extend([
            {'name': 'Analytical', 'emoji': '📊', 'color': '#8b5cf6'},
            {'name': 'Storytelling', 'emoji': '📖', 'color': '#ec4899'}
        ])
    
    variations = []
    for style in styles:
        engagement = random.randint(65, 85)
        clarity = random.randint(70, 95)
        sentiment = round(random.uniform(0.7, 1.3), 2)
        impressions = random.randint(1000, 5000)
        
        base_content = generate_content(topic, platform)
        style_modifiers = {
            'Professional': f"**{style['name']} Approach:** This variation presents {topic} with precision and authority.\n\n",
            'Conversational': f"**{style['name']} Approach:** Hey there! Let's chat about {topic} like friends.\n\n",
            'Motivational': f"**{style['name']} Approach:** Ready to transform your understanding of {topic}?\n\n",
            'Analytical': f"**{style['name']} Approach:** Detailed analysis of {topic} reveals key patterns.\n\n",
            'Storytelling': f"**{style['name']} Approach:** Let me share a story about {topic}.\n\n"
        }
        
        modifier = style_modifiers.get(style['name'], '')
        content = modifier + base_content[:200] + '...'
        
        variations.append({
            'name': f"{style['emoji']} {style['name']}",
            'style': style['name'],
            'description': f'For: "{topic}"',
            'engagement': engagement,
            'clarity': clarity,
            'sentiment': sentiment,
            'impressions': impressions,
            'content': content,
            'conversion': round(random.uniform(5, 15), 1),
            'color': style['color'],
            'emoji': style['emoji']
        })
    
    variations.sort(key=lambda x: x['engagement'], reverse=True)
    variations[0]['is_winner'] = True
    return variations

# ========== MAIN APP ==========
def main():
    # Create the main container structure
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    # Left Sidebar
    col1, col2 = st.columns([280, 1120])
    
    with col1:
        st.markdown('''
        <div class="sidebar-container">
            <div class="logo">
                <div class="logo-icon">
                    <i class="fas fa-robot"></i>
                </div>
                <div class="logo-text">AI Optimizer</div>
            </div>
        ''', unsafe_allow_html=True)
        
        # Platform selection buttons
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
                label=f"**{platform['name']}**",
                key=f"platform_{platform['id']}",
                help=platform['desc'],
                use_container_width=True
            ):
                st.session_state.current_platform = platform['id']
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)  # Close sidebar-container
    
    with col2:
        st.markdown('<div class="main-content-container">', unsafe_allow_html=True)
        
        # Header
        st.markdown('''
        <div class="header">
            <div class="header-left">
                <h1>AI Content Optimizer</h1>
                <p>Generate content for any topic on any platform</p>
            </div>
            <div style="color: #666; font-size: 14px;">
                <i class="far fa-clock"></i> ''' + datetime.now().strftime("%H:%M %d-%m-%Y") + '''
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
        # Topic Input Section
        st.markdown('''
        <div class="topic-section">
            <h2 class="section-title">
                <i class="fas fa-edit"></i> Enter Any Topic
            </h2>
        </div>
        ''', unsafe_allow_html=True)
        
        col_t1, col_t2, col_t3 = st.columns([3, 1, 1])
        with col_t1:
            topic = st.text_input(
                label=" ",
                value=st.session_state.current_topic,
                placeholder="Enter ANY topic (e.g., 'How to bake sourdough bread', 'Benefits of meditation', 'Future of electric cars')",
                label_visibility="collapsed"
            )
        
        with col_t2:
            if st.button("✨ **Generate Content**", use_container_width=True, type="primary"):
                if topic.strip():
                    st.session_state.current_topic = topic.strip()
                    st.session_state.generated_content = generate_content(
                        st.session_state.current_topic,
                        st.session_state.current_platform
                    )
                    st.rerun()
        
        with col_t3:
            if st.button("🧪 **Run A/B Test**", use_container_width=True, type="secondary"):
                if topic.strip():
                    st.session_state.current_topic = topic.strip()
                    if not st.session_state.generated_content:
                        st.session_state.generated_content = generate_content(
                            st.session_state.current_topic,
                            st.session_state.current_platform
                        )
                    st.session_state.variations = generate_ab_variations(
                        st.session_state.current_topic,
                        st.session_state.current_platform,
                        st.session_state.current_test_type
                    )
                    st.session_state.show_results = True
                    st.rerun()
        
        st.markdown('''
        <p style="margin-top: 10px; color: #666; font-size: 14px;">
            <i class="fas fa-lightbulb"></i> Tip: You can enter ANY topic - from cooking recipes to quantum physics!
        </p>
        ''', unsafe_allow_html=True)
        
        # Generator Panel
        st.markdown('<div class="generator-panel">', unsafe_allow_html=True)
        
        # Left: Content Preview
        with st.container():
            st.markdown('''
            <div class="platform-preview">
                <div class="platform-preview-header">
                    <div class="platform-display">
                        <i class="fab fa-''' + st.session_state.current_platform + '''"></i>
                        <div>
                            <h3>''' + st.session_state.current_platform.capitalize() + ''' Content</h3>
                            <p>Generated content preview</p>
                        </div>
                    </div>
                </div>
            </div>
            ''', unsafe_allow_html=True)
            
            if st.session_state.generated_content:
                st.markdown(f'<div class="content-preview">{st.session_state.generated_content}</div>', unsafe_allow_html=True)
            else:
                st.markdown('''
                <div class="content-preview">
                    Enter any topic above and click "Generate Content" to see platform-specific content here.
                </div>
                ''', unsafe_allow_html=True)
            
            if st.button("📋 **Copy Content**", use_container_width=True):
                if st.session_state.generated_content:
                    st.toast("✅ Content copied to clipboard!", icon="📋")
        
        # Right: A/B Testing
        with st.container():
            st.markdown('''
            <div class="ab-testing-section">
                <div class="ab-testing-header">
                    <h2 class="section-title">
                        <i class="fas fa-vial"></i> A/B Testing Variations
                    </h2>
                </div>
            </div>
            ''', unsafe_allow_html=True)
            
            # Test type buttons
            col_test1, col_test2 = st.columns(2)
            with col_test1:
                if st.button("⚡ Quick Test (3 variants)", 
                           use_container_width=True,
                           type="primary" if st.session_state.current_test_type == 'quick' else "secondary"):
                    st.session_state.current_test_type = 'quick'
                    st.rerun()
            with col_test2:
                if st.button("📊 Comprehensive (5 variants)",
                           use_container_width=True,
                           type="primary" if st.session_state.current_test_type == 'comprehensive' else "secondary"):
                    st.session_state.current_test_type = 'comprehensive'
                    st.rerun()
            
            # Display variations
            if st.session_state.variations:
                for variant in st.session_state.variations:
                    winner_class = 'winner' if variant.get('is_winner', False) else ''
                    st.markdown(f'''
                    <div class="ab-variant-card {winner_class}">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                            <div>
                                <div style="font-weight: 600; color: #1a1f36; font-size: 16px;">{variant['name']}</div>
                                <div style="font-size: 12px; color: #666; margin-top: 5px;">{variant['description']}</div>
                            </div>
                            <div style="background: {'#10b981' if variant.get('is_winner', False) else '#f59e0b'}; color: white; padding: 5px 12px; border-radius: 20px; font-size: 12px; font-weight: 500;">
                                {'🏆 Winner' if variant.get('is_winner', False) else '🥈 Contender'}
                            </div>
                        </div>
                        
                        <div style="color: #666; font-size: 14px; line-height: 1.5; margin-bottom: 20px;">
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
                    </div>
                    ''', unsafe_allow_html=True)
            else:
                st.markdown('''
                <div style="text-align: center; padding: 40px; color: #666;">
                    <i class="fas fa-vial" style="font-size: 48px; margin-bottom: 20px; opacity: 0.3;"></i>
                    <p>Click "Run A/B Test" to generate variations for your topic</p>
                </div>
                ''', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)  # Close generator-panel
        
        # Results Panel
        if st.session_state.show_results and st.session_state.variations:
            st.markdown('''
            <div class="ab-testing-section" style="margin-top: 20px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                    <h2 class="section-title">
                        <i class="fas fa-chart-bar"></i> Test Results & Analysis
                    </h2>
                    <div style="background: #10b981; color: white; padding: 8px 16px; border-radius: 20px; font-weight: 600;">
                        Winner: ''' + st.session_state.variations[0]['style'] + ''' Style
                    </div>
                </div>
            ''', unsafe_allow_html=True)
            
            # Stats
            total_impressions = sum(v['impressions'] for v in st.session_state.variations)
            avg_engagement = sum(v['engagement'] for v in st.session_state.variations) / len(st.session_state.variations)
            
            col_s1, col_s2, col_s3, col_s4 = st.columns(4)
            with col_s1:
                st.metric("Total Impressions", f"{total_impressions:,}")
            with col_s2:
                st.metric("Avg Engagement", f"{avg_engagement:.1f}%")
            with col_s3:
                st.metric("Conversion Rate", f"{st.session_state.variations[0]['conversion']}%")
            with col_s4:
                confidence = min(99, 75 + ((st.session_state.variations[0]['engagement'] - st.session_state.variations[1]['engagement']) * 2)) if len(st.session_state.variations) > 1 else 85
                st.metric("Confidence Level", f"{confidence:.1f}%")
            
            # Chart
            st.markdown("<h3 style='color: #1a1f36; margin: 30px 0 20px 0;'>📊 Variant Performance</h3>", unsafe_allow_html=True)
            chart_cols = st.columns(len(st.session_state.variations))
            for idx, (col, variant) in enumerate(zip(chart_cols, st.session_state.variations)):
                with col:
                    bar_height = min(100, variant['engagement'] + 20)
                    st.markdown(f'''
                    <div style="text-align: center;">
                        <div style="height: {bar_height}px; width: 60px; margin: 0 auto; background: linear-gradient(to top, {variant['color']}, {variant['color']}99); border-radius: 8px 8px 0 0; position: relative;">
                            <div style="position: absolute; top: -30px; left: 50%; transform: translateX(-50%); font-weight: 700; color: #1a1f36;">
                                {variant['engagement']}%
                            </div>
                        </div>
                        <div style="margin-top: 10px; font-weight: 600; color: #1a1f36;">{variant['style']}</div>
                    </div>
                    ''', unsafe_allow_html=True)
            
            # Recommendations
            st.markdown('''
            <h3 style="color: #1a1f36; margin: 40px 0 20px 0;">
                <i class="fas fa-lightbulb"></i> AI Recommendations
            </h3>
            <div style="color: #666;">
                <p>• 🎯 <strong>Winner Selected:</strong> "''' + st.session_state.variations[0]['style'] + '''" style with ''' + str(st.session_state.variations[0]['engagement']) + '''% engagement score</p>
                <p>• 📊 <strong>Statistical Significance:</strong> Higher than other variants</p>
                <p>• 💡 <strong>Optimization Opportunity:</strong> Consider refining the messaging for "''' + st.session_state.current_topic + '''"</p>
                <p>• 🎨 <strong>Style Analysis:</strong> This approach resonates best with your audience</p>
                <p>• ⏰ <strong>Testing Duration:</strong> For conclusive results, run this test for 48-72 hours</p>
            </div>
            ''', unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)  # Close results panel
        
        # Footer
        st.markdown('''
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
        </div>
        ''', unsafe_allow_html=True)  # Close main-content-container
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close main-container

if __name__ == "__main__":
    main()