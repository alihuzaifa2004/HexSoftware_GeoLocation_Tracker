import streamlit as st
import requests
import pandas as pd
import pydeck as pdk

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="GeoLocation Tracker ",
    page_icon="🌍",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS (Optimized for Google Maps Aesthetic)
# ---------------------------------------------------
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0f172a;
    }

    .main-title {
        font-size: 48px;
        font-weight: bold;
        color: #38bdf8;
        text-align: center;
        margin-bottom: 10px;
    }

    .subtitle {
        font-size: 18px;
        color: #cbd5e1;
        text-align: center;
        margin-bottom: 30px;
    }

    .info-box {
        background: #111827;
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #334155;
        margin-bottom: 20px;
    }

    .info-title {
        color: #38bdf8;
        font-size: 22px;
        font-weight: bold;
        margin-bottom: 10px;
    }

    .info-text {
        color: white;
        font-size: 18px;
        line-height: 1.8;
    }

    /* Google Maps Floating Info-Bar Overlay Style */
    .gmaps-overlay {
        background-color: rgba(255, 255, 255, 0.95);
        border-radius: 8px;
        padding: 15px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.15);
        color: #1e293b;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        border-left: 5px solid #1a73e8; /* Google Maps Signature Blue */
        margin-bottom: 15px;
    }
    .gmaps-overlay b {
        color: #1a73e8;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------
st.markdown('<div class="main-title">🌍 GeoLocation Tracker</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Track IP-based Geolocation with Interactive Maps</div>', unsafe_allow_html=True)

# ---------------------------------------------------
# FAIL-SAFE MULTI-API LOCATION FETCHER
# ---------------------------------------------------
def get_location_data():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    
    # --- Try Endpoint 1: ipapi.co ---
    try:
        response = requests.get("https://ipapi.co/json/", headers=headers, timeout=4)
        if response.status_code == 200:
            res_json = response.json()
            if "error" not in res_json:
                return {
                    "ip": res_json.get("ip"),
                    "city": res_json.get("city"),
                    "region": res_json.get("region"),
                    "country_name": res_json.get("country_name"),
                    "latitude": res_json.get("latitude"),
                    "longitude": res_json.get("longitude"),
                    "timezone": res_json.get("timezone"),
                    "org": res_json.get("org")
                }
    except Exception as e:
        st.sidebar.warning(f"Primary API (ipapi.co) bypassed: {e}")

    # --- Try Endpoint 2: ip-api.com (Failover) ---
    try:
        response = requests.get("http://ip-api.com/json/", headers=headers, timeout=4)
        if response.status_code == 200:
            res_json = response.json()
            if res_json.get("status") == "success":
                return {
                    "ip": res_json.get("query"),
                    "city": res_json.get("city"),
                    "region": res_json.get("regionName"),
                    "country_name": res_json.get("country"),
                    "latitude": res_json.get("lat"),
                    "longitude": res_json.get("lon"),
                    "timezone": res_json.get("timezone"),
                    "org": res_json.get("isp")
                }
    except Exception as e:
        st.sidebar.warning(f"Backup API (ip-api.com) bypassed: {e}")

    # --- Try Endpoint 3: ipinfo.io (Second Failover) ---
    try:
        response = requests.get("https://ipinfo.io/json", headers=headers, timeout=4)
        if response.status_code == 200:
            res_json = response.json()
            loc = res_json.get("loc", "0,0").split(",")
            return {
                "ip": res_json.get("ip"),
                "city": res_json.get("city"),
                "region": res_json.get("region"),
                "country_name": res_json.get("country"),
                "latitude": float(loc[0]),
                "longitude": float(loc[1]),
                "timezone": res_json.get("timezone"),
                "org": res_json.get("org")
            }
    except Exception as e:
        st.sidebar.warning(f"Final Fallback (ipinfo.io) failed: {e}")
        
    return None

# ---------------------------------------------------
# FETCH DATA
# ---------------------------------------------------
with st.spinner("Fetching geolocation parameters..."):
    data = get_location_data()

# ---------------------------------------------------
# DISPLAY DATA
# ---------------------------------------------------
if data:
    ip = data.get("ip", "N/A")
    city = data.get("city", "N/A")
    region = data.get("region", "N/A")
    country = data.get("country_name", "N/A")
    latitude = data.get("latitude", 0.0)
    longitude = data.get("longitude", 0.0)
    timezone = data.get("timezone", "N/A")
    org = data.get("org", "N/A")

    # Safeguard coordinates processing
    try:
        latitude = float(latitude) if latitude is not None else 0.0
        longitude = float(longitude) if longitude is not None else 0.0
    except ValueError:
        latitude, longitude = 0.0, 0.0

    # ---------------------------------------------------
    # INFO SECTION
    # ---------------------------------------------------
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            f"""
            <div class="info-box">
                <div class="info-title">📌 IP Information</div>
                <div class="info-text">
                🌐 IP Address: <b>{ip}</b><br>
                🏙️ City: <b>{city}</b><br>
                🌍 Region: <b>{region}</b><br>
                🏳️ Country: <b>{country}</b>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="info-box">
                <div class="info-title">🛰️ Coordinates</div>
                <div class="info-text">
                📍 Latitude: <b>{latitude}</b><br>
                📍 Longitude: <b>{longitude}</b><br>
                ⏰ Timezone: <b>{timezone}</b><br>
                🏢 ISP: <b>{org}</b>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # ---------------------------------------------------
    # MAP DATAFRAME CONFIGURATION
    # ---------------------------------------------------
    map_data = pd.DataFrame({
        'lat': [latitude],
        'lon': [longitude],
        'city': [city],
        'ip': [ip]
    })

    # ---------------------------------------------------
    # GOOGLE MAPS FLOATING CONTROL CARD OVERLAY
    # ---------------------------------------------------
    st.markdown(
        f"""
        <div class="gmaps-overlay">
            📍 <b>Google Maps View Engine:</b> Tracked target matched near <u>{city}, {region}</u>. <br/>
            🔍 Zoom in to view street-level infrastructure, parks, transit locations, and buildings.
        </div>
        """,
        unsafe_allow_html=True
    )

    # ---------------------------------------------------
    # GOOGLE MAPS STYLE ENGINE
    # ---------------------------------------------------
    st.pydeck_chart(
        pdk.Deck(
            # Using Mapbox Streets style layer to duplicate Google Maps' exact colors
            map_style='mapbox://styles/mapbox/streets-v12',
            initial_view_state=pdk.ViewState(
                latitude=latitude,
                longitude=longitude,
                zoom=14,         # High-resolution close-up view to focus on street layouts
                pitch=0,         # Flat birds-eye view identical to standard default Google Maps
                bearing=0,
            ),
            # Google Maps Red Marker Style Tooltip Hover window
            tooltip={
                "html": "<div style='font-family: Arial; padding: 5px; color: white;'>"
                        "<b>📌 Google Maps Location Mark</b><br/>"
                        "<b>City:</b> {city}<br/>"
                        "<b>IP Address:</b> {ip}</div>",
                "style": {
                    "backgroundColor": "#ea4335", # Google Maps Signature Red Location Marker Pin color
                    "borderRadius": "4px",
                    "border": "1px solid #c5221f"
                }
            },
            layers=[
                # Layer 1: Google Maps Blue Pin Core Indicator Node
                pdk.Layer(
                    'ScatterplotLayer',
                    data=map_data,
                    get_position='[lon, lat]',
                    get_color='[26, 115, 232, 230]', # Google Map Pointer Blue Core Glow
                    get_radius=120,
                    pickable=True
                ),
                # Layer 2: Soft White Outer Ring (Emulating GPS location pulsing bubble)
                pdk.Layer(
                    'ScatterplotLayer',
                    data=map_data,
                    get_position='[lon, lat]',
                    get_color='[26, 115, 232, 45]', # Translucent perimeter beacon radius
                    get_radius=350,
                    pickable=False
                )
            ],
        )
    )
    st.success("✅ Location Successfully Rendered on Google Maps Engine Grid.")
else:
    st.error("❌ Failed to Fetch Geolocation Data from all provider streams. Verify internet connection.")

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------
st.markdown("---")
st.markdown("<center>🚀 Developed By Ali Huzaifa for HexSoftwares Internship Program</center>", unsafe_allow_html=True)