# 🛡️ CyberScope - Automated OSINT Intelligence Platform

[![Live Demo](https://img.shields.io/badge/Live_Demo-cyberscope.vercel.app-00f2fe?style=for-the-badge&logo=vercel&logoColor=000)](https://cyberscope.vercel.app)
[![Vercel Deployment](https://img.shields.io/badge/Vercel-Deployed-success?style=for-the-badge&logo=vercel)](https://cyberscope.vercel.app)
[![Python Version](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Framework](https://img.shields.io/badge/Framework-Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)

An open-source, Flask-based **Open Source Intelligence (OSINT)** platform providing automated investigative capabilities for IP geolocation, telecommunications metadata, and multi-platform username presence analysis.

---

## 🚀 Key Features & Modules

- 🌐 **IP Geolocation & Threat Reconnaissance:** Instant lookup of IP addresses, ISP/organization metadata, timezone, country, and precise latitude/longitude coordinates via `/api/ip`.
- 📱 **Telecommunications Intelligence:** Phone number parsing, carrier verification, format validation (E.164/National), and country origin detection via `/api/phone`.
- 🔍 **Multi-Platform Username Scanner:** Automated cross-platform username presence checking across major social and technical networks (GitHub, Twitter, Reddit, LinkedIn, TikTok, YouTube) via `/api/username`.
- 📚 **OSINT Knowledge Base & Tutorials:** In-depth tutorials and resource guides covering privacy, threat intelligence, and digital footprint analysis.
- 🎨 **Dark Cyberpunk UI:** Modern glassmorphism design with terminal loading overlays and interactive data visualization.

---

## 📡 REST API Reference

### 1. IP Geolocation Lookup
* **Endpoint:** `POST /api/ip`
* **Payload:** `{"ip": "8.8.8.8"}`
* **Response Example:**
  ```json
  {
    "query": "8.8.8.8",
    "status": "success",
    "country": "United States",
    "city": "Ashburn",
    "isp": "Google LLC",
    "lat": 39.03,
    "lon": -77.5
  }
  ```

### 2. Phone Number Intelligence
* **Endpoint:** `POST /api/phone`
* **Payload:** `{"phone": "+14155552671"}`
* **Response Example:**
  ```json
  {
    "valid": true,
    "number": "+14155552671",
    "country_code": 1,
    "location": "California",
    "carrier": "Fixed-line or mobile"
  }
  ```

### 3. Username Presence Scanner
* **Endpoint:** `POST /api/username`
* **Payload:** `{"username": "octocat"}`
* **Response Example:**
  ```json
  {
    "GitHub": "Found",
    "Twitter": "Found",
    "Reddit": "Found",
    "LinkedIn": "Found"
  }
  ```

---

## 📁 Repository Structure

```text
CyberScope/
├── app.py                      # Flask Application Server & API Routes
├── vercel.json                 # Vercel Python Serverless Deployment Config
├── requirements.txt            # Python Dependencies (Flask, requests, phonenumbers)
├── static/
│   ├── style.css               # Dark Neon Cyberpunk UI Styles
│   └── images/                 # SVG & PNG Diagrams and Illustrations
└── templates/
    ├── index.html              # Main OSINT Dashboard & Interactive Tools
    ├── tutorials.html          # OSINT Tutorial Library
    ├── tutorial_detail.html    # Detailed Tutorial Reader
    ├── resources.html          # Intelligence Resource Hub
    ├── documentation.html      # Platform Documentation
    └── 404.html                # Branded Target Not Found Page
```

---

## 🛠️ Local Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AvishkarRanjane/CyberScope.git
   cd CyberScope
   ```

2. **Set up virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run local server:**
   ```bash
   python app.py
   ```
   Access the dashboard at `http://127.0.0.1:5000`.

---

## 🌐 Live Deployment

Access the live platform on Vercel:
👉 **[https://cyberscope.vercel.app](https://cyberscope.vercel.app)**

---

*Open Source Intelligence & Security Reconnaissance Platform.*
