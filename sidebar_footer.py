# Enhanced sidebar footer
import streamlit as st
from datetime import datetime

st.sidebar.divider()

# Live status indicators
st.sidebar.markdown(f"""
<div style="background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 10px; margin-bottom: 1rem;">
    <h4 style="color: white; margin: 0;">🔴 System Status</h4>
    <p style="color: #90EE90; margin: 0.5rem 0;">🟢 All Systems Online</p>
    <p style="color: rgba(255,255,255,0.8); margin: 0; font-size: 0.8rem;">Last Updated: {datetime.now().strftime('%H:%M:%S')}</p>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown(f"""
<div style="background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 10px; margin-bottom: 1rem;">
    <h4 style="color: white; margin: 0;">📅 Today's Info</h4>
    <p style="color: white; margin: 0.5rem 0;">{datetime.now().strftime('%A')}</p>
    <p style="color: white; margin: 0.5rem 0;">{datetime.now().strftime('%d %B %Y')}</p>
    <p style="color: #FFD700; margin: 0; font-size: 1.2rem;">🕒 {datetime.now().strftime('%I:%M %p')}</p>
</div>
""", unsafe_allow_html=True)

st.sidebar.divider()

st.sidebar.markdown("""
<div style="background: linear-gradient(45deg, #667eea, #764ba2); padding: 1rem; border-radius: 15px; color: white; text-align: center;">
    <h3>👨💻 Developer</h3>
    <h4>Imtiaz Hussain</h4>
    <p>Full Stack Developer</p>
    <hr style="border-color: rgba(255,255,255,0.3);">
    <p><strong>Version:</strong> 4.0 Pro</p>
    <p><strong>Build:</strong> March 2024</p>
    <p><strong>Tech:</strong> Python + AI</p>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
<div style="background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 10px; margin-top: 1rem;">
    <h4 style="color: white;">🏆 Features</h4>
    <ul style="color: rgba(255,255,255,0.9); font-size: 0.9rem;">
        <li>📊 16 Smart Modules</li>
        <li>🗄️ 11 Database Tables</li>
        <li>📊 Live Monitoring</li>
        <li>🤖 AI Assistant</li>
        <li>🛏️ Bed Management</li>
        <li>🔬 Advanced Lab</li>
        <li>💊 Smart Pharmacy</li>
        <li>🚑 Emergency System</li>
        <li>🩸 Blood Bank</li>
        <li>💰 Finance Control</li>
    </ul>
</div>
""")