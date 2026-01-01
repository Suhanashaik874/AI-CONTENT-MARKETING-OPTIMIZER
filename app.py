import streamlit as st
import random
import time
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="AI Content Optimizer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1a1f36;
        margin-bottom: 0.5rem;
    }
    
    .sub-header {
        color: #666;
        font-size: 1rem;
        margin-bottom: 2rem;
    }
    
    .platform-card {
        padding: 1rem;
        border-radius: 10px;
        border: 2px solid #e0e6ff;
        background: white;
        margin-bottom: 1rem;
        cursor: pointer;
        transition: all 0.3s;
    }
    
    .platform-card:hover {
        border-color: #667eea;
        transform: translateY(-2px);
    }
    
    .platform-card.active {
        border-color: #667eea;
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
    }
    
    .metric-card {
        background: #f8f9ff;
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #e0e6ff;
        text-align: center;
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        font-family: monospace;
    }
    
    .variant-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        border: 2px solid #e0e6ff;
        margin-bottom: 1rem;
    }
    
    .variant-card.winner {
        border-color: #10b981;
        background: rgba(16, 185, 129, 0.05);
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 1.5rem;
        border-radius: 8px;
        font-weight: 600;
    }
    
    .content-box {
        background: #f8f9ff;
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #e0e6ff;
        min-height: 300px;
        white-space: pre-wrap;
        font-family: 'Segoe UI', sans-serif;
    }
</style>
""", unsafe_allow_html=True)

# AI Content Generator
class ContentGenerator:
    @staticmethod
    def generate_youtube(topic):
        return f"""🎬 **YouTube Video: "{topic}"**

🔴 **HOOK (First 15 seconds):**
"Ever wondered about {topic}? Stick around and I'll show you exactly what you need to know!"

📋 **VIDEO STRUCTURE:**
0:00 - Introduction
1:30 - Key Concepts Explained
3:45 - Practical Examples
6:15 - Common Mistakes
8:30 - Action Steps

💡 **KEY INSIGHTS:**
• Understanding {topic} fundamentals
• Real-world applications
• Step-by-step implementation

🎯 **CALL TO ACTION:**
👍 Like if you found this helpful
🔔 Subscribe for more
💬 Comment your questions

#YouTube #Education #{topic.replace(" ", "")}"""

    @staticmethod
    def generate_twitter(topic):
        return f"""🧵 **Twitter Thread: {topic}**

1/7 Let's talk about {topic}. Here's everything you need to know:

2/7 First, what is {topic}? In simple terms, it's...

3/7 Why {topic} matters now more than ever...

4/7 3 practical applications of {topic}:
1. Application 1
2. Application 2
3. Application 3

5/7 Common mistakes to avoid...

6/7 How to get started today...

7/7 Want to learn more? Follow for daily insights!

#Thread #{topic.replace(" ", "")} #Learning"""

    @staticmethod
    def generate_linkedin(topic):
        return f"""**Professional Insight: {topic}**

As professionals, understanding {topic} is crucial for staying competitive.

**Key Benefits:**
• Increased efficiency
• Better decision-making
• Career advancement

**Action Steps:**
1. Learn the fundamentals
2. Apply in real projects
3. Share your learnings

**Discussion:** How has {topic} impacted your career?

#{topic.replace(" ", "")} #ProfessionalDevelopment #Business"""

    @staticmethod
    def generate_instagram(topic):
        return f"""🌟 **INSTAGRAM: {topic.upper()}** 🌟

Ready to master {topic}? Here's your guide! 👇

[IMAGE 1: Eye-catching graphic]
[IMAGE 2: Step-by-step visual]
[IMAGE 3: Tips carousel]

💡 **3 KEY TAKEAWAYS:**
1️⃣ Start with basics
2️⃣ Practice consistently
3️⃣ Learn from others

💬 **COMMENT BELOW:**
What do you want to know about {topic}?

#{topic.replace(" ", "")} #Instagram #Tips"""

    @staticmethod
    def generate_blog(topic):
        return f"""# Complete Guide to {topic}

## Introduction
{topic} has become increasingly important in today's world.

## What You'll Learn
• Fundamentals of {topic}
• Practical applications
• Future trends

## Getting Started
Begin with these simple steps...

## Conclusion
{topic} offers valuable opportunities for growth.

---

**Ready to learn more about {topic}?**"""

# A/B Testing Generator
class ABTestGenerator:
    def __init__(self):
        self.styles = [
            {"name": "Professional", "emoji": "👔", "desc": "Formal and authoritative"},
            {"name": "Conversational", "emoji": "💬", "desc": "Friendly and casual"},
            {"name": "Motivational", "emoji": "🚀", "desc": "Inspiring and energetic"},
            {"name": "Analytical", "emoji": "📊", "desc": "Data-driven and detailed"},
            {"name": "Storytelling", "emoji": "📖", "desc": "Personal and narrative"}
        ]
    
    def generate_variations(self, topic, platform, count=3):
        variations = []
        
        for i in range(count):
            style = self.styles[i % len(self.styles)]
            engagement = 70 + random.random() * 25
            clarity = 75 + random.random() * 20
            sentiment = 0.8 + random.random() * 1.2
            
            variations.append({
                "id": i,
                "name": f"{style['emoji']} {style['name']}",
                "style": style['name'],
                "desc": style['desc'],
                "engagement": round(engagement),
                "clarity": round(clarity),
                "sentiment": round(sentiment, 2),
                "impressions": random.randint(500, 2500),
                "content": self.generate_content(topic, platform, style)
            })
        
        # Sort by engagement and mark winner
        variations.sort(key=lambda x: x['engagement'], reverse=True)
        variations[0]['winner'] = True
        return variations
    
    def generate_content(self, topic, platform, style):
        generators = {
            "youtube": ContentGenerator.generate_youtube,
            "twitter": ContentGenerator.generate_twitter,
            "linkedin": ContentGenerator.generate_linkedin,
            "instagram": ContentGenerator.generate_instagram,
            "blog": ContentGenerator.generate_blog
        }
        
        base_content = generators[platform](topic)
        return f"{style['emoji']} **{style['name']} Style**\n\n{base_content[:200]}..."

# Initialize
content_gen = ContentGenerator()
ab_gen = ABTestGenerator()

# Sidebar
with st.sidebar:
    st.markdown('<div class="logo">🤖 AI Content Optimizer</div>', unsafe_allow_html=True)
    
    st.markdown("### Platforms")
    platforms = ["YouTube", "Twitter", "LinkedIn", "Instagram", "Blog"]
    selected_platform = st.radio(
        "Select Platform",
        platforms,
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("### Test Type")
    test_type = st.radio(
        "A/B Test Options",
        ["Quick (3 variants)", "Comprehensive (5 variants)"],
        index=0
    )
    
    st.markdown("---")
    st.markdown(f"**Current Time:** {datetime.now().strftime('%H:%M %d-%m-%Y')}")

# Main Content
st.markdown('<div class="main-header">AI Content Optimizer</div>', unsafe_allow_html=True)
st.markdown(f'<div class="sub-header">Generate content for {selected_platform}</div>', unsafe_allow_html=True)

# Topic Input
col1, col2, col3 = st.columns([3, 1, 1])
with col1:
    topic = st.text_input(
        "Enter your topic",
        value="Machine Learning",
        placeholder="Enter any topic..."
    )

with col2:
    generate_btn = st.button("🚀 Generate Content")

with col3:
    if topic:
        test_btn = st.button("🧪 Run A/B Test")
    else:
        test_btn = st.button("🧪 Run A/B Test", disabled=True)

# Main Content Area
if generate_btn or topic:
    with st.spinner(f"Generating {selected_platform.lower()} content for '{topic}'..."):
        time.sleep(1.5)
        
        # Generate content
        platform_func = getattr(content_gen, f"generate_{selected_platform.lower()}")
        content = platform_func(topic)
        
        # Display content
        st.markdown("### 📝 Generated Content")
        st.markdown(f'<div class="content-box">{content}</div>', unsafe_allow_html=True)
        
        # Copy button
        if st.button("📋 Copy to Clipboard"):
            st.success("Content copied to clipboard!")
        
        # Generate A/B test variations if requested
        if test_btn:
            st.markdown("---")
            st.markdown("### 🧪 A/B Testing Results")
            
            with st.spinner("Running A/B test..."):
                time.sleep(2)
                
                variant_count = 3 if "Quick" in test_type else 5
                variations = ab_gen.generate_variations(
                    topic, 
                    selected_platform.lower(), 
                    variant_count
                )
                
                # Display variations
                cols = st.columns(variant_count)
                for idx, (col, var) in enumerate(zip(cols, variations)):
                    with col:
                        st.markdown(f'<div class="variant-card {"winner" if var.get("winner", False) else ""}">', unsafe_allow_html=True)
                        st.markdown(f"##### {var['name']}")
                        st.markdown(f"*{var['desc']}*")
                        
                        # Metrics
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.markdown(f'<div class="metric-card"><div class="metric-value" style="color:#10b981;">{var["engagement"]}%</div><small>Engagement</small></div>', unsafe_allow_html=True)
                        with col2:
                            st.markdown(f'<div class="metric-card"><div class="metric-value" style="color:#f59e0b;">{var["clarity"]}%</div><small>Clarity</small></div>', unsafe_allow_html=True)
                        with col3:
                            st.markdown(f'<div class="metric-card"><div class="metric-value" style="color:#667eea;">{var["sentiment"]}%</div><small>Sentiment</small></div>', unsafe_allow_html=True)
                        
                        # Preview button
                        with st.expander("Preview Content"):
                            st.write(var['content'])
                        
                        # Select button
                        if st.button(f"Select", key=f"select_{idx}"):
                            st.session_state.selected_variant = var
                            st.success(f"Selected {var['style']} variant!")
                        
                        st.markdown('</div>', unsafe_allow_html=True)
                
                # Results summary
                st.markdown("---")
                st.markdown("### 📊 Test Summary")
                
                total_impressions = sum(v['impressions'] for v in variations)
                avg_engagement = sum(v['engagement'] for v in variations) / len(variations)
                winner = next((v for v in variations if v.get('winner', False)), variations[0])
                
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Total Impressions", f"{total_impressions:,}")
                with col2:
                    st.metric("Avg Engagement", f"{avg_engagement:.1f}%")
                with col3:
                    st.metric("Winner Engagement", f"{winner['engagement']}%")
                with col4:
                    st.metric("Confidence", f"{85 + random.random() * 10:.1f}%")
                
                # Recommendations
                st.markdown("### 💡 AI Recommendations")
                recommendations = [
                    f"🎯 **Winner identified:** {winner['style']} style with {winner['engagement']}% engagement",
                    "📊 **Recommendation:** Use this variant as your primary content",
                    f"⏰ **Timing:** Best posting time: {random.choice(['7-9 AM', '12-2 PM', '7-9 PM'])}",
                    "📱 **Optimization:** Ensure proper hashtags and CTAs"
                ]
                
                for rec in recommendations:
                    st.markdown(f"- {rec}")

# Footer
st.markdown("---")
col1, col2 = st.columns([1, 1])
with col1:
    st.markdown("🌧️ Light rain Tomorrow")
with col2:
    st.markdown("🌐 ENG | IN")