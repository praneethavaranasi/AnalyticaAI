import streamlit as st

# Configure page config only once at the entrypoint
st.set_page_config(
    page_title="AnalyticaAI",
    page_icon="📊",
    layout="wide"
)

# Custom CSS to replace the sidebar collapse/expand icons with Lucide PanelLeftOpen and PanelLeftClose
# and to style the landing page layout and aesthetics
custom_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

/* Hide the original Streamlit SVG/material icons, child elements, and pseudo-elements for collapse/expand */
[data-testid="stSidebarCollapseButton"] svg,    
[data-testid="stSidebarCollapseButton"] span,
[data-testid="stSidebarCollapseButton"] div,
[data-testid="stSidebarCollapseButton"]::before,
[data-testid="stSidebarCollapseButton"]::after,
[data-testid="collapsedControl"] svg,
[data-testid="collapsedControl"] span,
[data-testid="collapsedControl"] div,
[data-testid="collapsedControl"]::before,
[data-testid="collapsedControl"]::after {
    display: none !important;
    content: "" !important;
}

/* Style the Collapse button (inside the open sidebar) with PanelLeftClose */
[data-testid="stSidebar"] [data-testid="stSidebarCollapseButton"],
[data-testid="stSidebar"] [data-testid="stSidebarCollapseButton"] button,
[data-testid="stSidebar"] button[data-testid="stSidebarCollapseButton"] {
    background-image: url('data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2224%22%20height%3D%2224%22%20viewBox%3D%220%200%2024%2024%22%20fill%3D%22none%22%20stroke%3D%22%231F2937%22%20stroke-width%3D%222%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%3E%3Crect%20width%3D%2218%22%20height%3D%2218%22%20x%3D%223%22%20y%3D%223%22%20rx%3D%222%22%20ry%3D%222%22%2F%3E%3Cpath%20d%3D%22M9%203v18%22%2F%3E%3Cpath%20d%3D%22m14%2015-3-3%203-3%22%2F%3E%3C%2Fsvg%3E') !important;
    background-repeat: no-repeat !important;
    background-position: center !important;
    background-size: 20px !important;
    background-color: transparent !important;
    border: none !important;
}

/* Style the Expand button (outside the collapsed sidebar) with PanelLeftOpen */
[data-testid="collapsedControl"],
[data-testid="collapsedControl"] button,
button[data-testid="collapsedControl"],
[data-testid="stSidebarCollapseButton"]:not([data-testid="stSidebar"] *),
[data-testid="stSidebarCollapseButton"]:not([data-testid="stSidebar"] *) button,
button[data-testid="stSidebarCollapseButton"]:not([data-testid="stSidebar"] *) {
    background-image: url('data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2224%22%20height%3D%2224%22%20viewBox%3D%220%200%2024%2024%22%20fill%3D%22none%22%20stroke%3D%22%231F2937%22%20stroke-width%3D%222%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%3E%3Crect%20width%3D%2218%22%20height%3D%2218%22%20x%3D%223%22%20y%3D%223%22%20rx%3D%222%22%20ry%3D%222%22%2F%3E%3Cpath%20d%3D%22M9%203v18%22%2F%3E%3Cpath%20d%3D%22m14%209%203%203-3%203%22%2F%3E%3C%2Fsvg%3E') !important;
    background-repeat: no-repeat !important;
    background-position: center !important;
    background-size: 20px !important;
    background-color: transparent !important;
    border: none !important;
}

/* Landing Page Styles */
.landing-page {
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #0F172A;
    background-color: #FFFFFF;
    line-height: 1.5;
    margin-top: -3rem; /* Compensate for Streamlit top padding */
}

/* Hero Section */
.hero-sec {
    max-width: 1200px;
    margin: 0 auto;
    padding: 5rem 1.5rem;
    display: grid;
    grid-template-columns: 1.2fr 1fr;
    gap: 4rem;
    align-items: center;
}

@media (max-width: 900px) {
    .hero-sec {
        grid-template-columns: 1fr;
        text-align: center;
        gap: 3rem;
        padding: 3rem 1.5rem;
    }
}

.hero-content {
    display: flex;
    flex-direction: column;
}

.logo-container {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 2rem;
}

@media (max-width: 900px) {
    .logo-container {
        justify-content: center;
    }
}

.logo-icon-box {
    width: 3.5rem;
    height: 3.5rem;
    background: linear-gradient(135deg, #6366F1 0%, #A855F7 50%, #EC4899 100%);
    border-radius: 1rem;
    box-shadow: 0 10px 15px -3px rgba(99, 102, 241, 0.3);
    display: flex;
    align-items: flex-end;
    justify-content: center;
    gap: 4px;
    padding-bottom: 12px;
}

.logo-icon-bar {
    width: 6px;
    border-radius: 2px;
    background: rgba(255, 255, 255, 0.9);
}
.bar1 { height: 16px; opacity: 0.8; }
.bar2 { height: 28px; }
.bar3 { height: 20px; opacity: 0.7; }
.bar4 { height: 32px; }

.logo-title {
    font-size: 2.5rem;
    font-weight: 900;
    letter-spacing: -0.05em;
    color: #0F172A;
}

.hero-main-title {
    font-size: 3.5rem;
    font-weight: 800;
    letter-spacing: -0.03em;
    line-height: 1.1;
    margin-bottom: 1.5rem;
}

@media (max-width: 600px) {
    .hero-main-title {
        font-size: 2.5rem;
    }
}

.gradient-text-indigo-purple {
    background: linear-gradient(to right, #4F46E5, #9333EA);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-desc {
    font-size: 1.25rem;
    color: #475569;
    margin-bottom: 2.5rem;
    max-width: 36rem;
    line-height: 1.625;
}

@media (max-width: 900px) {
    .hero-desc {
        margin-left: auto;
        margin-right: auto;
    }
}

.hero-buttons-row {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
}

@media (max-width: 900px) {
    .hero-buttons-row {
        justify-content: center;
    }
}

.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 1rem 2rem;
    font-weight: 600;
    border-radius: 0.75rem;
    transition: all 0.2s ease-in-out;
    text-decoration: none;
    cursor: pointer;
}

.btn-primary {
    background-color: #0F172A;
    color: #FFFFFF !important;
    box-shadow: 0 10px 15px -3px rgba(15, 23, 42, 0.1);
}
.btn-primary:hover {
    background-color: #1E293B;
    transform: translateY(-2px);
}

.btn-secondary {
    background-color: #FFFFFF;
    color: #0F172A !important;
    border: 2px solid #E2E8F0;
}
.btn-secondary:hover {
    border-color: #CBD5E1;
    transform: translateY(-2px);
}

/* Hero Right: Mock Dashboard Card */
.hero-visual {
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
}

.mock-dashboard {
    background-color: #FFFFFF;
    border: 1px solid #F1F5F9;
    border-radius: 1.5rem;
    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.08);
    padding: 1.5rem;
    width: 100%;
    max-width: 420px;
    transition: transform 0.3s ease;
    animation: floatAnimation 4s ease-in-out infinite;
}

@keyframes floatAnimation {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
    100% { transform: translateY(0px); }
}

.mock-chart-box {
    height: 16rem;
    background-color: #F8FAFC;
    border: 1px solid #F1F5F9;
    border-radius: 1rem;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    overflow: hidden;
}

.mock-chart-overlay {
    position: absolute;
    inset: 0;
    opacity: 0.15;
    background: radial-gradient(circle at 50% 50%, #4F46E5, transparent);
}

.mock-chart-svg {
    width: 6rem;
    height: 6rem;
    color: #6366F1;
    position: relative;
    z-index: 10;
}

.mock-meta {
    margin-top: 1.5rem;
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
}

.mock-line-long {
    height: 1rem;
    background-color: #F1F5F9;
    border-radius: 9999px;
    width: 75%;
}

.mock-line-short {
    height: 1rem;
    background-color: #F1F5F9;
    border-radius: 9999px;
    width: 50%;
}

.mock-pills-row {
    display: flex;
    gap: 0.5rem;
    margin-top: 0.5rem;
}

.mock-pill-style {
    font-size: 0.875rem;
    font-weight: 500;
    padding: 0.5rem 1rem;
    border-radius: 0.5rem;
}

.pill-indigo {
    background-color: #EEF2F6;
    color: #4F46E5;
}

.pill-purple {
    background-color: #F3E8FF;
    color: #9333EA;
}

/* Features Section */
.features-sec {
    background-color: #F8FAFC;
    padding: 6rem 1.5rem;
}

.features-sec-header {
    text-align: center;
    max-width: 48rem;
    margin: 0 auto 4rem auto;
}

.features-sec-header h2 {
    font-size: 2.25rem;
    font-weight: 800;
    color: #0F172A;
    margin-bottom: 1rem;
}

.features-sec-header p {
    font-size: 1.125rem;
    color: #475569;
}

.features-grid-layout {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    max-width: 1200px;
    margin: 0 auto;
}

.feature-card-item {
    background-color: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 1.25rem;
    padding: 2rem;
    transition: all 0.3s ease;
}

.feature-card-item:hover {
    border-color: #C7D2FE;
    box-shadow: 0 20px 25px -5px rgba(99, 102, 241, 0.05), 0 10px 10px -5px rgba(99, 102, 241, 0.03);
    transform: translateY(-4px);
}

.feature-icon-wrapper {
    width: 3rem;
    height: 3rem;
    border-radius: 0.75rem;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #FFFFFF;
    margin-bottom: 1.5rem;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

.color-blue { background-color: #3B82F6; }
.color-indigo { background-color: #6366F1; }
.color-amber { background-color: #F59E0B; }
.color-emerald { background-color: #10B981; }
.color-rose { background-color: #F43F5E; }
.color-violet { background-color: #8B5CF6; }

.feature-card-item h3 {
    font-size: 1.25rem;
    font-weight: 700;
    color: #0F172A;
    margin-bottom: 0.75rem;
}

.feature-card-item p {
    color: #475569;
    line-height: 1.625;
}

/* Testimonials Section */
.testimonials-sec {
    padding: 6rem 1.5rem;
    max-width: 1200px;
    margin: 0 auto;
}

.testimonials-sec-header {
    text-align: center;
    margin-bottom: 4rem;
}

.testimonials-sec-header h2 {
    font-size: 2.25rem;
    font-weight: 800;
    color: #0F172A;
}

.testimonials-grid-layout {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
}

.testimonial-card-item {
    background-color: #FFFFFF;
    border: 1px solid #F1F5F9;
    border-radius: 1.25rem;
    padding: 2rem;
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.02), 0 4px 6px -2px rgba(0, 0, 0, 0.01);
    display: flex;
    flex-direction: column;
}

.stars-rating {
    color: #FBBF24;
    margin-bottom: 1.5rem;
    font-size: 1.25rem;
}

.testimonial-quote {
    font-size: 1rem;
    font-style: italic;
    color: #334155;
    margin-bottom: 2rem;
    flex: 1;
    line-height: 1.625;
}

.author-block {
    display: flex;
    align-items: center;
    gap: 1rem;
}

.author-avatar {
    width: 3rem;
    height: 3rem;
    border-radius: 9999px;
    background-color: #0F172A;
    color: #FFFFFF;
    font-weight: 700;
    display: flex;
    align-items: center;
    justify-content: center;
}

.author-info h4 {
    font-size: 1rem;
    font-weight: 700;
    color: #0F172A;
    margin: 0;
}

.author-info p {
    font-size: 0.875rem;
    color: #64748B;
    margin: 0;
}

/* FAQ Section */
.faq-sec {
    background-color: #F8FAFC;
    padding: 6rem 1.5rem;
}

.faq-sec-content {
    max-width: 48rem;
    margin: 0 auto;
}

.faq-sec-header {
    text-align: center;
    margin-bottom: 4rem;
}

.faq-sec-header h2 {
    font-size: 2.25rem;
    font-weight: 800;
    color: #0F172A;
    margin-bottom: 1rem;
}

.faq-sec-header p {
    font-size: 1.125rem;
    color: #475569;
}

.faq-accordion-box {
    background-color: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 1.5rem;
    padding: 2rem;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
}

details.faq-item {
    border-bottom: 1px solid #E2E8F0;
    padding: 1.5rem 0;
}

details.faq-item:last-child {
    border-bottom: none;
}

details.faq-item summary {
    font-size: 1.125rem;
    font-weight: 700;
    color: #1E293B;
    list-style: none;
    cursor: pointer;
    display: flex;
    justify-content: space-between;
    align-items: center;
    outline: none;
}

details.faq-item summary::-webkit-details-marker {
    display: none;
}

details.faq-item summary::after {
    content: "▼";
    font-size: 0.75rem;
    color: #94A3B8;
    transition: transform 0.2s ease;
}

details.faq-item[open] summary::after {
    transform: rotate(180deg);
}

details.faq-item p {
    margin-top: 1rem;
    color: #475569;
    line-height: 1.625;
}

/* CTA Section */
.cta-sec {
    background: linear-gradient(135deg, #4F46E5 0%, #4338CA 100%);
    color: #FFFFFF;
    text-align: center;
    padding: 6rem 1.5rem;
}

.cta-sec-content {
    max-width: 56rem;
    margin: 0 auto;
}

.cta-sec-content h2 {
    font-size: 2.75rem;
    font-weight: 800;
    letter-spacing: -0.02em;
    margin-bottom: 1.5rem;
}

.cta-sec-content p {
    font-size: 1.25rem;
    color: #E0E7FF;
    margin-bottom: 2.5rem;
}

.cta-banner-tip {
    background-color: rgba(231, 243, 255, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 1rem;
    padding: 1rem 2rem;
    display: inline-block;
    backdrop-filter: blur(4px);
    margin-bottom: 3rem;
    font-weight: 500;
}

.btn-cta-link {
    background-color: #FFFFFF;
    color: #4F46E5 !important;
    font-size: 1.125rem;
    font-weight: 700;
    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
}

.btn-cta-link:hover {
    background-color: #F8FAFC;
    transform: translateY(-2px);
}
</style>
"""

# Inject the custom styling on every page rerun
st.markdown(custom_css, unsafe_allow_html=True)

# Define home page content
def show_home():
    # Keep HTML strings entirely left-aligned (no leading indentation) 
    # to prevent Streamlit's Markdown parser from treating HTML as a code block.
    landing_page_html = """
<div class="landing-page">
<!-- Hero Section -->
<section class="hero-sec">
<div class="hero-content">
<div class="logo-container">
<div class="logo-icon-box">
<div class="logo-icon-bar bar1"></div>
<div class="logo-icon-bar bar2"></div>
<div class="logo-icon-bar bar3"></div>
<div class="logo-icon-bar bar4"></div>
</div>
<span class="logo-title">AnalyticaAI</span>
</div>
<h2 class="hero-main-title">Turn your data into <span class="gradient-text-indigo-purple">intelligence</span></h2>
<p class="hero-desc">The all-in-one platform for automated data cleaning, exploratory analysis, and AI-driven insights. Built for modern teams.</p>
<div class="hero-buttons-row">
<a href="/Upload" target="_self" class="btn btn-primary">Get Started Free &rarr;</a>
<a href="https://github.com/praneethavaranasi/AnalyticaAI" class="btn btn-secondary">View Documentation</a>
</div>
</div>
<div class="hero-visual">
<div class="mock-dashboard">
<div class="mock-chart-box">
<div class="mock-chart-overlay"></div>
<svg class="mock-chart-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<line x1="18" y1="20" x2="18" y2="10"></line>
<line x1="12" y1="20" x2="12" y2="4"></line>
<line x1="6" y1="20" x2="6" y2="14"></line>
</svg>
</div>
<div class="mock-meta">
<div class="mock-line-long"></div>
<div class="mock-line-short"></div>
<div class="mock-pills-row">
<span class="mock-pill-style pill-indigo">Active</span>
<span class="mock-pill-style pill-purple">98% Accuracy</span>
</div>
</div>
</div>
</div>
</section>

<!-- Features Grid -->
<section class="features-sec">
<div class="features-sec-header">
<h2>Everything you need to master your data</h2>
<p>Powerful tools designed to simplify complex workflows and accelerate decision making.</p>
</div>
<div class="features-grid-layout">
<div class="feature-card-item">
<div class="feature-icon-wrapper color-blue">
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg>
</div>
<h3>Advanced Analytics</h3>
<p>Transform raw data into actionable insights with our powerful processing engine.</p>
</div>
<div class="feature-card-item">
<div class="feature-icon-wrapper color-indigo">
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
</div>
<h3>Secure by Design</h3>
<p>Enterprise-grade security ensuring your sensitive data stays private and protected.</p>
</div>
<div class="feature-card-item">
<div class="feature-icon-wrapper color-amber">
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>
</div>
<h3>Real-time Processing</h3>
<p>Experience lightning-fast data cleaning and analysis as your files upload.</p>
</div>
<div class="feature-card-item">
<div class="feature-icon-wrapper color-emerald">
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
</div>
<h3>Global Scale</h3>
<p>Distributed architecture built to handle massive datasets from anywhere in the world.</p>
</div>
<div class="feature-card-item">
<div class="feature-icon-wrapper color-rose">
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5" rx="9" ry="3"></ellipse><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"></path><path d="M3 12c0 1.66 4 3 9 3s9-1.34 9-3"></path></svg>
</div>
<h3>Data Integration</h3>
<p>Seamlessly connect with your existing databases and cloud storage solutions.</p>
</div>
<div class="feature-card-item">
<div class="feature-icon-wrapper color-violet">
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="4" width="16" height="16" rx="2" ry="2"></rect><rect x="9" y="9" width="6" height="6"></rect><line x1="9" y1="1" x2="9" y2="4"></line><line x1="15" y1="1" x2="15" y2="4"></line><line x1="9" y1="20" x2="9" y2="23"></line><line x1="15" y1="20" x2="15" y2="23"></line><line x1="20" y1="9" x2="23" y2="9"></line><line x1="20" y1="15" x2="23" y2="15"></line><line x1="1" y1="9" x2="4" y2="9"></line><line x1="1" y1="15" x2="4" y2="15"></line></svg>
</div>
<h3>AI-Powered Insights</h3>
<p>Leverage cutting-edge machine learning to uncover hidden patterns in your data.</p>
</div>
</div>
</section>

<!-- Testimonials Section -->
<section class="testimonials-sec">
<div class="testimonials-sec-header">
<h2>Trusted by data experts everywhere</h2>
</div>
<div class="testimonials-grid-layout">
<div class="testimonial-card-item">
<div class="stars-rating">★★★★★</div>
<p class="testimonial-quote">"AnalyticaAI has completely transformed how our team handles exploratory data analysis. The speed is unmatched."</p>
<div class="author-block">
<div class="author-avatar">SC</div>
<div class="author-info">
<h4>Sarah Chen</h4>
<p>Data Scientist at TechFlow</p>
</div>
</div>
</div>
<div class="testimonial-card-item">
<div class="stars-rating">★★★★★</div>
<p class="testimonial-quote">"The automatic data cleaning feature saved us hundreds of hours. It's intuitively designed and incredibly robust."</p>
<div class="author-block">
<div class="author-avatar">MT</div>
<div class="author-info">
<h4>Marcus Thorne</h4>
<p>CTO, DataBridge</p>
</div>
</div>
</div>
<div class="testimonial-card-item">
<div class="stars-rating">★★★★★</div>
<p class="testimonial-quote">"Finally, a data platform that is both powerful enough for experts and simple enough for everyone else."</p>
<div class="author-block">
<div class="author-avatar">ER</div>
<div class="author-info">
<h4>Elena Rodriguez</h4>
<p>Product Manager, Insightly</p>
</div>
</div>
</div>
</div>
</section>

<!-- FAQ Section -->
<section class="faq-sec">
<div class="faq-sec-content">
<div class="faq-sec-header">
<h2>Frequently Asked Questions</h2>
<p>Quick answers to common questions about AnalyticaAI.</p>
</div>
<div class="faq-accordion-box">
<details class="faq-item">
<summary>How secure is my data?</summary>
<p>We use industry-standard encryption and secure cloud protocols to ensure your data is always protected and private.</p>
</details>
<details class="faq-item">
<summary>What file formats do you support?</summary>
<p>Currently we support CSV, Excel (XLSX), and JSON formats. We are constantly adding support for more types.</p>
</details>
<details class="faq-item">
<summary>Is there a limit on file size?</summary>
<p>Standard accounts can upload up to 500MB per file. Enterprise plans offer unlimited capacity.</p>
</details>
</div>
</div>
</section>

<!-- CTA Section -->
<section class="cta-sec">
<div class="cta-sec-content">
<h2>Ready to see the magic in your data?</h2>
<p>Join thousands of teams using AnalyticaAI to drive growth and efficiency.</p>
<div class="cta-banner-tip">
Pro tip: Use the left sidebar to explore our powerful analytical modules.
</div>
<div>
<a href="/Upload" target="_self" class="btn btn-cta-link">Create Your Account</a>
</div>
</div>
</section>
</div>
"""
    st.markdown(landing_page_html, unsafe_allow_html=True)

# Set up page navigation with titles and icons
pages = [
    st.Page(show_home, title="App", icon=":material/home:", default=True),
    st.Page("pages/01_Upload.py", title="Upload", icon=":material/upload:"),
    st.Page("pages/02_Dashboard.py", title="Dashboard", icon=":material/dashboard:"),
    st.Page("pages/03_Visualizations.py", title="Visualizations", icon=":material/bar_chart:"),
    st.Page("pages/04_Insights.py", title="Insights", icon=":material/lightbulb:"),
    st.Page("pages/05_Reports.py", title="Reports", icon=":material/description:"),
    st.Page("pages/06_AI_Assistant.py", title="AI Assistant", icon=":material/smart_toy:"),
    st.Page("pages/07_Anomaly_Detection.py", title="Anomaly Detection", icon=":material/warning:"),
]

# Run navigation
pg = st.navigation(pages)
pg.run()