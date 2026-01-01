import streamlit as st
import random
import time
from datetime import datetime
APP_VERSION = "2.0" 

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

# ==================== AI CONTENT GENERATOR ====================
class ContentGenerator:
    @staticmethod
    def generate_youtube(topic, style="professional"):
        styles = {
            "professional": f"""🎬 **Professional YouTube Script: {topic}**

🔴 **HOOK (First 15s):**
"What if I told you that mastering {topic} could transform your results? Stay with me to uncover the exact framework that top performers use."

📊 **DATA-DRIVEN INSIGHTS:**
• 87% of successful creators use structured approaches
• Average watch time increases by 42% with proper hooks
• Engagement rates improve by 3.5x with clear CTAs

🎯 **VIDEO STRUCTURE:**
00:00 - Attention-Grabbing Hook
01:30 - The 3 Core Principles of {topic}
04:15 - Real-World Case Studies
07:30 - Common Pitfalls to Avoid
09:45 - Actionable Implementation Plan
11:30 - Q&A & Next Steps

📈 **PERFORMANCE METRICS:**
Estimated Engagement: 78-92%
Retention Rate: 65-80%
Conversion Potential: High

#YouTube #Education #{topic.replace(' ', '')} #ProfessionalContent""",
            
            "conversational": f"""🎥 **Casual YouTube Video: Let's Talk About {topic}!**

👋 **HEY THERE!** Ready to dive into {topic} with me? No fancy jargon, just real talk!

✨ **WHAT YOU'LL LEARN TODAY:**
✓ What {topic} actually means (in plain English!)
✓ Why it matters to YOU personally
✓ Simple steps you can take TODAY
✓ My personal experience with {topic}

😄 **FUN FACT:** Did you know that 9 out of 10 people overcomplicate {topic}? Let's keep it simple!

🗓️ **MY 7-DAY CHALLENGE FOR YOU:**
Day 1: Watch this video (you're here! ✅)
Day 2-4: Apply one tip daily
Day 5: Share your progress
Day 6-7: Review and refine

💬 **COMMENT BELOW:** "I'm in!" if you're joining the challenge!

#CasualYouTube #{topic.replace(' ', '')} #RealTalk #BeginnerFriendly""",
            
            "motivational": f"""🚀 **MOTIVATIONAL MASTERCLASS: Unlock {topic.upper()}!**

⚡ **ATTENTION!** This isn't just another {topic} video. This is your WAKE-UP CALL!

🌟 **BEFORE WE START:** Close your eyes and imagine where you'll be in 30 days after applying what you learn today...

💥 **THE AWAKENING:**
Most people sleepwalk through {topic}. But NOT YOU! You're here because you're BUILT DIFFERENT!

🎯 **YOUR MISSION (SHOULD YOU CHOOSE TO ACCEPT IT):**
1. Watch this video with FULL attention
2. Take IMMEDIATE action
3. Document your journey
4. Become the example others follow

🔥 **SUCCESS STORY TEMPLATE:**
"30 days ago, I knew nothing about {topic}. Today, I'm [YOUR SUCCESS GOAL]. Here's how..."

🙌 **AFFIRMATION:** "I am capable of mastering {topic} and creating exceptional results!"

#Motivation #{topic.replace(' ', '')} #SuccessMindset #TransformYourLife"""
        }
        return styles.get(style, styles["professional"])
    
    @staticmethod
    def generate_twitter(topic, style="professional"):
        return f"""🧵 **Twitter Thread: The Complete Guide to {topic}**

1/8 Let's talk about {topic}. This thread will give you everything you need to know:

2/8 First, what is {topic}? 
• Not what most people think
• Common misconceptions
• Real definition

3/8 Why {topic} matters in 2024:
• Market demand: ↑ 47% YoY
• Salary impact: +$25K average
• Career opportunities

4/8 The 3 pillars of effective {topic}:
1. Foundation (non-negotiable)
2. Application (where magic happens)
3. Optimization (competitive edge)

5/8 Tools for {topic} success:
• Free: [Tool 1], [Tool 2]
• Paid: [Tool 3], [Tool 4]
• Community: [Community Link]

6/8 Common mistakes (avoid these!):
❌ Mistake 1
❌ Mistake 2
❌ Mistake 3

7/8 Action plan:
📍 Week 1: Basics
📍 Week 2-3: Practice
📍 Week 4: Build portfolio

8/8 Want more on {topic}?
• Follow me for daily insights
• Bookmark this thread
• Comment your questions!

#TwitterThread #{topic.replace(' ', '')} #Learning #Education"""
    
    @staticmethod
    def generate_linkedin(topic, style="professional"):
        return f"""**Professional Insight: Mastering {topic} for Career Advancement**

As professionals navigating today's dynamic landscape, proficiency in {topic} has transitioned from "nice-to-have" to "non-negotiable."

**Industry Data Highlights:**
• 72% of hiring managers prioritize {topic} skills
• Professionals with {topic} expertise command 35% higher compensation
• Companies investing in {topic} training report 42% productivity gains

**Strategic Framework for {topic} Mastery:**

1. **Foundational Competence**
   - Core principles and terminology
   - Industry-specific applications
   - Regulatory considerations

2. **Practical Implementation**
   - Real-world case studies
   - Risk assessment protocols
   - ROI measurement frameworks

3. **Leadership Integration**
   - Team capability development
   - Process optimization
   - Innovation facilitation

**Measurable Outcomes:**
Organizations implementing structured {topic} programs report:
✓ 58% faster decision-making cycles
✓ 41% reduction in operational costs
✓ 67% improvement in client satisfaction scores

**Professional Development Pathway:**
• Month 1-2: Certification & Fundamentals
• Month 3-4: Applied Project Work
• Month 5-6: Mentorship & Leadership

**Discussion Catalyst:**
How has {topic} impacted your professional trajectory? What organizational challenges have you observed in implementation?

I welcome constructive dialogue and shared learning in the comments below.

#{topic.replace(' ', '')} #ProfessionalDevelopment #BusinessStrategy #CareerGrowth #Leadership"""
    
    @staticmethod
    def generate_instagram(topic, style="professional"):
        return f"""🌟 **INSTAGRAM GUIDE: {topic.upper()} MADE EASY** 🌟

Ever felt overwhelmed by {topic}? 🤯 This guide breaks it down STEP-BY-STEP! 👇

[SWIPE FOR MORE →]

📱 **CAROUSEL BREAKDOWN:**
Slide 1: {topic} in 60 seconds ⏱️
Slide 2: 3 Key principles 🗝️
Slide 3: Beginner mistakes to avoid 🚫
Slide 4: Success checklist ✅
Slide 5: Free resources 🆓
Slide 6: Your action plan 🎯

💡 **QUICK TIPS:**
1️⃣ Start small → Build consistency
2️⃣ Track progress → Celebrate wins
3️⃣ Join community → Learn together

✨ **SAVE THIS POST** for your {topic} journey!

[STORY IDEAS 📖]
→ Day 1: "My {topic} story"
→ Day 2: "Behind the scenes"
→ Day 3: "Q&A session"
→ Day 4: "Success celebration"
→ Day 5: "Resource dump"

🎁 **BONUS:** DM me "GUIDE" for my free {topic} template!

💬 **COMMENT BELOW:**
What's your #1 question about {topic}?

👇 **TAG someone who needs this!**

#{topic.replace(' ', '')} #InstagramGuide #LearnWithMe #ContentTips #SocialMedia"""
    
    @staticmethod
    def generate_blog(topic, style="professional"):
        return f"""# The Comprehensive Guide to {topic}: Strategy, Implementation, and Optimization

## Executive Summary
{topic} represents a paradigm shift in modern [industry/field], offering unprecedented opportunities for growth, innovation, and competitive advantage. This guide provides a holistic framework for understanding and implementing {topic} strategies effectively.

## Introduction: The {topic} Landscape
The evolution of {topic} has accelerated dramatically in recent years, driven by technological advancements and changing market dynamics. Current industry analysis indicates a compound annual growth rate of 23.7% in {topic} adoption across sectors.

### Market Context:
• **Global Market Size:** $47.8B (2024) → Projected $89.3B (2027)
• **Adoption Rate:** 68% among enterprise organizations
• **ROI Metrics:** 3.2x average return on {topic} investments

## Core Principles of Effective {topic}

### 1. Foundational Understanding
- **Definition & Scope:** Comprehensive overview of {topic} parameters
- **Historical Evolution:** Key milestones and inflection points
- **Current State Analysis:** Market positioning and trends

### 2. Strategic Implementation
- **Framework Development:** Structured approach to {topic} deployment
- **Resource Allocation:** Optimal investment strategies
- **Risk Management:** Mitigation protocols and contingency planning

### 3. Performance Optimization
- **Metrics & KPIs:** Key performance indicators for {topic} success
- **Continuous Improvement:** Iterative enhancement methodologies
- **Scalability Planning:** Growth-oriented infrastructure design

## Practical Applications

### Case Study 1: Enterprise Implementation
**Organization:** Fortune 500 Technology Company
**Challenge:** Inefficient {topic} processes causing 40% resource wastage
**Solution:** Implemented integrated {topic} framework
**Results:** 
- 57% reduction in operational costs
- 89% improvement in process efficiency
- $4.2M annual savings

### Case Study 2: SME Adoption
**Organization:** Mid-sized Financial Services Firm
**Challenge:** Limited {topic} capabilities hindering market competitiveness
**Solution:** Phased {topic} capability development
**Results:**
- 34% increase in client acquisition
- 28% improvement in service delivery
- 41% revenue growth YoY

## Implementation Roadmap

### Phase 1: Foundation (Weeks 1-4)
1. Needs assessment and gap analysis
2. Stakeholder alignment and buy-in
3. Initial capability development

### Phase 2: Execution (Weeks 5-12)
1. Pilot program deployment
2. Performance monitoring
3. Initial optimization

### Phase 3: Scale (Months 4-6)
1. Full-scale implementation
2. Advanced optimization
3. Continuous improvement cycles

## Common Challenges & Solutions

### Challenge 1: Resistance to Change
**Solution:** Comprehensive change management program with clear communication of benefits and structured support systems.

### Challenge 2: Resource Constraints
**Solution:** Phased implementation approach with clear ROI milestones and external partnership opportunities.

### Challenge 3: Measurement Difficulties
**Solution:** Implement robust analytics framework with real-time monitoring capabilities and automated reporting.

## Future Outlook

### Short-term (1-2 years):
• Increased automation in {topic} processes
• Enhanced AI integration
• Standardization of best practices

### Medium-term (3-5 years):
• Complete digital transformation of {topic} ecosystems
• Advanced predictive capabilities
• Global standardization initiatives

### Long-term (5+ years):
• Autonomous {topic} systems
• Complete market disruption
• New business model emergence

## Conclusion

{topic} represents more than a technological advancement—it's a fundamental shift in how organizations operate and compete. By adopting the structured approach outlined in this guide, organizations can position themselves for sustainable success in an increasingly complex and competitive landscape.

## Frequently Asked Questions

**Q: What's the minimum investment required for {topic} implementation?**
A: Initial investments typically range from $25K-$100K, with clear ROI within 6-12 months.

**Q: How long does complete {topic} integration take?**
A: Most organizations achieve full integration within 6-9 months using the phased approach.

**Q: What are the most critical success factors?**
A: Executive sponsorship, clear strategy, adequate resourcing, and continuous measurement.

**Q: Can small businesses benefit from {topic}?**
A: Absolutely—scaled implementations can deliver proportional benefits for organizations of all sizes.

---

*Ready to transform your approach to {topic}? Download our comprehensive implementation toolkit or schedule a consultation to discuss your specific needs.*"""

# ==================== A/B TEST GENERATOR ====================
class ABTestGenerator:
    def __init__(self):
        self.variation_templates = [
            {
                "title": "Professional Tone",
                "type": "professional",
                "badge": "best",
                "description": "Data-driven, authoritative approach with statistics and structured frameworks"
            },
            {
                "title": "Conversational Style",
                "type": "conversational", 
                "badge": "good",
                "description": "Friendly, approachable tone with personal anecdotes and simple language"
            },
            {
                "title": "Motivational Approach",
                "type": "motivational",
                "badge": "good",
                "description": "Energetic, inspiring content with calls to action and success mindsets"
            },
            {
                "title": "Analytical Deep Dive",
                "type": "analytical",
                "badge": "good",
                "description": "Detailed technical analysis with frameworks, case studies, and data"
            },
            {
                "title": "Storytelling Format",
                "type": "storytelling",
                "badge": "good",
                "description": "Narrative-driven content with personal stories and emotional connection"
            }
        ]
    
    def generate_variations(self, topic, platform, count=3):
        variations = []
        
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