import streamlit as st
import random
import time

st.set_page_config(
    page_title="Smart Home Automation Dashboard",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 Smart Home Automation Dashboard")
st.markdown("### Arduino-Based Home Automation & Security Monitoring System")

# Sidebar
st.sidebar.header("Control Panel")

light = st.sidebar.toggle("💡 Living Room Light")
fan = st.sidebar.toggle("🌀 Fan")
security = st.sidebar.toggle("🔒 Security System", value=True)

# Simulated Sensor Values
ldr_value = random.randint(100, 1000)
motion_detected = random.choice([True, False])

# Appliance Status
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("💡 Light Status", "ON" if light else "OFF")

with col2:
    st.metric("🌀 Fan Status", "ON" if fan else "OFF")

with col3:
    st.metric("🔒 Security", "ACTIVE" if security else "DISABLED")

st.divider()

# Sensors
st.subheader("📡 Sensor Monitoring")

col4, col5 = st.columns(2)

with col4:
    st.metric("☀️ LDR Value", f"{ldr_value}")

with col5:
    if motion_detected and security:
        st.error("🚨 Motion Detected!")
        buzzer = "ON"
    else:
        st.success("✅ No Motion Detected")
        buzzer = "OFF"

st.divider()

# LCD Simulation
st.subheader("📺 LCD Display Simulation")

if motion_detected and security:
    lcd_text = """
    Motion Detected
    Security Alert
    """
else:
    lcd_text = """
    System Normal
    Monitoring...
    """

st.code(lcd_text)

# Buzzer Status
st.subheader("🔊 Buzzer Status")

if buzzer == "ON":
    st.error("BUZZER ACTIVE")
else:
    st.success("BUZZER OFF")

st.divider()

# Home Status
st.subheader("🏠 Home Summary")

st.write(f"💡 Light: {'ON' if light else 'OFF'}")
st.write(f"🌀 Fan: {'ON' if fan else 'OFF'}")
st.write(f"🔒 Security: {'ACTIVE' if security else 'DISABLED'}")
st.write(f"🔊 Buzzer: {buzzer}")

st.success("Smart Home System Running Successfully")