# 🌍 GeoLocation Tracker Pro (Google Maps Edition)

An enterprise-grade, fail-safe IP Geolocation Tracking System engineered using Python, Streamlit, and PyDeck vector visualization technology. This application dynamically detects the client’s public network address, resolves geospatial telemetry through a resilient multi-provider API architecture, and renders the live coordinate stream onto an interactive Google Maps–styled spatial interface.

Developed specifically for the **Hex Softwares Internship Program**.

---

# ✨ Premium Features

## 🗺️ Google Maps–Style Rendering

Powered by **Mapbox Streets v12** vector engines to simulate a premium Google Maps experience with:

* realistic terrain visualization
* highway and road topology
* public landmarks & parks
* modern vector-based rendering
* smooth zoom & pitch interactions

---

## 🛡️ Multi-Provider API Failover Pipeline

This project integrates an intelligent fallback architecture to maintain uninterrupted geolocation tracking.

### Supported Providers

| Priority | Provider     | Purpose                      |
| -------- | ------------ | ---------------------------- |
| 1️⃣      | `ipapi.co`   | Primary Geolocation Resolver |
| 2️⃣      | `ip-api.com` | Backup Failover Endpoint     |
| 3️⃣      | `ipinfo.io`  | Emergency Recovery Provider  |

If one provider becomes:

* rate-limited
* blocked
* offline
* timeout restricted

…the system automatically reroutes requests to the next available endpoint seamlessly.

---

# 📍 Precision GPS Bubble System

Unlike traditional flat markers, this tracker introduces a modern:

## 🔴 Multi-Layer Tracking Bubble

Featuring:

* central high-visibility GPS node
* translucent radar pulse perimeter
* scalable radius simulation
* animated focus-style positioning

This creates a realistic live-tracking dashboard experience.

---

# 🔍 Interactive Spatial Information Overlay

The platform dynamically displays:

* 🌐 Public IP Address
* 🏙️ City & Region
* 🌍 Country
* 🛰️ Latitude / Longitude
* ⏰ Timezone
* 🏢 ISP / Network Provider

All rendered using modern micro-CSS UI structures optimized for readability and responsiveness.

---

# 🏷️ Brand-Matched Tooltip Rendering

Interactive hover tooltips are styled using:

* Google-inspired design palettes
* branded accent colors (`#ea4335`)
* soft shadow elevation
* HTML-enhanced UI overlays

---

# 🧠 Technical Architecture

## ⚡ Request Flow Pipeline

```text
          ┌─────────────────────┐
          │   User Connects     │
          └──────────┬──────────┘
                     │
                     ▼
      ┌─────────────────────────────┐
      │ Query Primary API: ipapi.co │
      └──────────┬──────────────────┘
                 │
        Success  │  Failure / Timeout
                 ▼
      ┌─────────────────────────────┐
      │ Parse Coordinates & Render  │
      └─────────────────────────────┘
                 │
                 ▼
        [ Live Map Visualization ]

────────────────────────────────────────

If Primary API Fails:

                 ▼
      ┌─────────────────────────────┐
      │ Fallback API: ip-api.com    │
      └──────────┬──────────────────┘
                 │
        Success  │  Failure
                 ▼
      ┌─────────────────────────────┐
      │ Render Backup Coordinates   │
      └─────────────────────────────┘

────────────────────────────────────────

If Backup API Fails:

                 ▼
      ┌─────────────────────────────┐
      │ Emergency API: ipinfo.io    │
      └──────────┬──────────────────┘
                 │
        Success  │  Failure
                 ▼
      ┌─────────────────────────────┐
      │ Trigger Error UI State      │
      └─────────────────────────────┘
```

---

# ⚙️ Technology Stack

| Technology | Purpose             |
| ---------- | ------------------- |
| Python     | Backend Logic       |
| Streamlit  | Web Interface       |
| Requests   | API Communication   |
| PyDeck     | Interactive Mapping |
| Pandas     | Data Handling       |
| CSS3       | UI Styling          |

---

# 📦 Installation

Install all required dependencies:

```bash
pip install streamlit requests pandas pydeck
```

---

# ▶️ Run Application

```bash
streamlit run app.py
```

---

# 📂 Recommended Project Structure

```text
HexSoftwares_Geolocation_Tracker/
│
├── app.py
├── requirements.txt
├── README.md
└── assets/
```

---

# 🚀 Enterprise-Level Features

✅ Real-Time IP Tracking
✅ Dynamic API Failover Protection
✅ Interactive GPS Mapping
✅ Google Maps–Style Rendering
✅ Responsive Dashboard UI
✅ Production-Oriented Architecture
✅ Internship Submission Ready

---

# 📌 Suggested Repository Name

```text
HexSoftwares_Geolocation_Tracker
```

---

# 📢 LinkedIn Caption

🚀 Excited to complete **Task 1 — GeoLocation Tracker** as part of my Python Programming Internship at Hex Softwares.

I developed an enterprise-grade IP Geolocation Tracking System using Python and Streamlit featuring:

✅ Interactive Google Maps–style rendering
✅ Multi-provider API failover architecture
✅ Real-time IP telemetry tracking
✅ Dynamic coordinate visualization
✅ Modern responsive dashboard UI

### Tech Stack

Python • Streamlit • PyDeck • Requests • Pandas

#Python #Streamlit #Geolocation #Maps #OpenSource #HexSoftwares #Internship #PythonDeveloper

---

# 👨‍💻 Developer

Developed By Ali Huzaifa using Python & Streamlit.
