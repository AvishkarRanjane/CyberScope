from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

IP_API = "http://ip-api.com/json/"
PHONE_API_KEY = os.getenv("PHONE_API_KEY")

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

# IP Analysis API Endpoint
@app.route("/analyze-ip", methods=["POST"])
def analyze_ip():
    try:
        ip = request.form.get("ip_address", "").strip()
        
        if not ip:
            return jsonify({"error": "IP address not provided"}), 400
        
        response = requests.get(IP_API + ip, timeout=10)
        ip_data = response.json()
        
        if not ip_data.get("status") == "success":
            return jsonify({"error": "Invalid IP address or API error"}), 400
        
        # Format response like GhostTR.py
        result = {
            "IP_Address": ip,
            "Country": ip_data.get("country", "N/A"),
            "Country_Code": ip_data.get("countryCode", "N/A"),
            "Region": ip_data.get("region", "N/A"),
            "Region_Name": ip_data.get("regionName", "N/A"),
            "City": ip_data.get("city", "N/A"),
            "Postal": ip_data.get("postal", "N/A"),
            "Latitude": ip_data.get("lat", "N/A"),
            "Longitude": ip_data.get("lon", "N/A"),
            "Timezone": ip_data.get("timezone", "N/A"),
            "ISP": ip_data.get("isp", "N/A"),
            "Organization": ip_data.get("org", "N/A"),
            "AS": ip_data.get("as", "N/A"),
        }
        
        if ip_data.get("lat") and ip_data.get("lon"):
            result["Maps"] = f"https://www.google.com/maps/@{ip_data.get('lat')},{ip_data.get('lon')},8z"
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Phone Analysis API Endpoint
@app.route("/analyze-phone", methods=["POST"])
def analyze_phone():
    try:
        phone = request.form.get("phone_number", "").strip()
        
        if not phone:
            return jsonify({"error": "Phone number not provided"}), 400
        
        # Using phonenumbers library for phone analysis
        try:
            import phonenumbers
            from phonenumbers import carrier, geocoder, timezone
            
            parsed_number = phonenumbers.parse(phone, None)
            
            region_code = phonenumbers.region_code_for_number(parsed_number)
            carrier_name = carrier.name_for_number(parsed_number, "en")
            location = geocoder.description_for_number(parsed_number, "en")
            tz = timezone.time_zones_for_number(parsed_number)
            
            result = {
                "Phone_Number": phone,
                "Country": location or "N/A",
                "Region_Code": region_code or "N/A",
                "Operator": carrier_name or "N/A",
                "Timezone": tz[0] if tz else "N/A",
                "Valid": "Yes" if phonenumbers.is_valid_number(parsed_number) else "No"
            }
            
            return jsonify(result)
        
        except ImportError:
            # Fallback to API if phonenumbers not installed
            url = f"http://apilayer.net/api/validate?access_key={PHONE_API_KEY}&number={phone}"
            response = requests.get(url, timeout=10)
            phone_data = response.json()
            
            result = {
                "Phone_Number": phone,
                "Valid": "Yes" if phone_data.get("valid") else "No",
                "Country": phone_data.get("country_name", "N/A"),
                "Carrier": phone_data.get("carrier", "N/A"),
                "Line_Type": phone_data.get("line_type", "N/A"),
                "Country_Code": phone_data.get("country_code", "N/A"),
            }
            
            return jsonify(result)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Username Analysis API Endpoint
@app.route("/analyze-username", methods=["POST"])
def analyze_username():
    try:
        username = request.form.get("username", "").strip()
        
        if not username:
            return jsonify({"error": "Username not provided"}), 400
        
        platforms = {
            "Instagram": f"https://www.instagram.com/{username}",
            "GitHub": f"https://github.com/{username}",
            "Twitter": f"https://twitter.com/{username}",
            "Reddit": f"https://www.reddit.com/user/{username}",
            "Facebook": f"https://www.facebook.com/{username}",
            "LinkedIn": f"https://www.linkedin.com/in/{username}",
            "TikTok": f"https://www.tiktok.com/@{username}",
            "YouTube": f"https://www.youtube.com/@{username}"
        }
        
        result = {}
        
        for platform, url in platforms.items():
            try:
                r = requests.head(url, timeout=5, allow_redirects=True)
                status = "Found" if r.status_code == 200 else "Not Found"
                result[platform] = status
            except:
                result[platform] = "Error"
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/resources")
def resources():
    return render_template("resources.html")

# Resource metadata for internal pages
resource_meta = {
    'osint-fundamentals': {'title':'OSINT Fundamentals','description':'Learn the basics of Open Source Intelligence gathering.','image':'images/resource-1.svg'},
    'network-intelligence': {'title':'Network Intelligence','description':'IP addresses, DNS, and network reconnaissance techniques.','image':'images/resource-2.svg'},
    'social-media-osint': {'title':'Social Media OSINT','description':'Social media analysis and username verification.','image':'images/resource-1.svg'},
    'privacy-and-ethics': {'title':'Privacy & Ethics','description':'Guidelines for responsible OSINT practices.','image':'images/resource-2.svg'},
    'ip-databases': {'title':'IP Databases','description':'Curated list of IP geolocation and WHOIS databases.','image':'images/resource-2.svg'},
    'public-data-sources': {'title':'Public Data Sources','description':'Comprehensive list of legitimate public data sources.','image':'images/resource-1.svg'},
    'api-reference': {'title':'API Reference','description':'Integration guides and technical docs.','image':'images/resource-2.svg'},
    'best-practices': {'title':'Best Practices','description':'Industry standards and recommended methodologies.','image':'images/resource-1.svg'},
    'academic-papers': {'title':'Academic Papers','description':'Peer-reviewed research on OSINT methodologies.','image':'images/resource-1.svg'},
    'case-studies': {'title':'Case Studies','description':'Real-world OSINT investigations and analyses.','image':'images/resource-2.svg'},
    'whitepapers': {'title':'Whitepapers','description':'In-depth technical documents on OSINT topics.','image':'images/resource-1.svg'},
    'industry-news': {'title':'Industry News','description':'Latest updates on cybersecurity and OSINT.','image':'images/resource-2.svg'},
    'discussion-forums': {'title':'Discussion Forums','description':'Community forums to discuss OSINT techniques.','image':'images/resource-1.svg'},
    'webinars': {'title':'Webinars','description':'Live training sessions and expert talks.','image':'images/resource-2.svg'},
    'github-repositories': {'title':'GitHub Repositories','description':'Open-source tools and scripts for OSINT.', 'image':'images/resource-1.svg'},
    'certifications': {'title':'Certifications','description':'OSINT-related professional certification info.','image':'images/resource-2.svg'}
}


@app.route('/resources/<slug>')
def resource_detail(slug):
    meta = resource_meta.get(slug)
    if not meta:
        return render_template('404.html'), 404
    return render_template('resource_detail.html', title=meta['title'], description=meta['description'], image=meta['image'])

@app.route("/documentation")
def documentation():
    return render_template("documentation.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

# Blog metadata for internal pages
blog_meta = {
    'ip-geolocation-guide': {'title':'The Complete Guide to IP Geolocation in OSINT','description':'Comprehensive guide to IP geolocation techniques.','image':'images/blog-1.svg'},
    'advanced-username-investigations': {'title':'Advanced Username Investigations: Tips & Tricks','description':'Professional techniques for username investigations.','image':'images/blog-1.svg'},
    'protecting-digital-footprint': {'title':'Protecting Your Digital Footprint Online','description':'How to minimize your digital footprint.','image':'images/blog-1.svg'},
    'essential-osint-tools': {'title':'Essential OSINT Tools Every Security Professional Needs','description':'Curated list of tools and reviews.','image':'images/blog-1.svg'},
    'osint-laws-ethics': {'title':'OSINT Laws and Ethics: What You Need to Know','description':'Legal and ethical considerations for OSINT practitioners.','image':'images/blog-1.svg'},
    'phone-number-intelligence': {'title':'Phone Number Intelligence: Database Insights','description':'Phone database structures and interpretation.','image':'images/blog-1.svg'},
    'building-osint-framework': {'title':'Building Your Own OSINT Framework','description':'Organize tools and workflows for efficient research.','image':'images/blog-1.svg'}
}


@app.route('/blog/<slug>')
def blog_detail(slug):
    meta = blog_meta.get(slug)
    if not meta:
        return render_template('404.html'), 404
    return render_template('blog_detail.html', meta=meta)

@app.route("/tutorials")
def tutorials():
    return render_template("tutorials.html")

# Tutorial and content metadata for internal pages
tutorial_meta = {
    'introduction-to-cyberscope': {
        'title': 'Introduction to CyberScope',
        'description': 'Overview of the CyberScope interface and main features.',
        'image': 'images/tutorials-1.svg'
    },
    'account-setup-and-configuration': {
        'title': 'Account Setup and Configuration',
        'description': 'How to set up and configure your CyberScope account.',
        'image': 'images/tutorials-2.svg'
    },
    'understanding-osint-basics': {
        'title': 'Understanding OSINT Basics',
        'description': 'Fundamental concepts and ethical considerations of OSINT.',
        'image': 'images/tutorials-3.svg'
    },
    'ip-geolocation-lookup': {
        'title': 'IP Geolocation Lookup',
        'description': 'How to perform IP geolocation lookups and interpret results.',
        'image': 'images/tutorials-4.svg'
    },
    'advanced-ip-analysis': {
        'title': 'Advanced IP Analysis',
        'description': 'Deep dive into advanced IP analysis techniques.',
        'image': 'images/tutorials-5.svg'
    },
    'bulk-ip-analysis': {
        'title': 'Bulk IP Analysis and Automation',
        'description': 'Methods for processing and automating IP intelligence collection.',
        'image': 'images/tutorials-6.svg'
    },
    'phone-number-lookup': {
        'title': 'Phone Number Lookup Guide',
        'description': 'Lookup phone number carrier and location metadata.',
        'image': 'images/tutorials-6.svg'
    },
    'phone-number-verification': {
        'title': 'Phone Number Verification Techniques',
        'description': 'Techniques to verify and validate phone numbers.',
        'image': 'images/tutorials-7.svg'
    },
    'telecommunications-osint': {
        'title': 'Telecommunications OSINT Deep Dive',
        'description': 'Understanding telecom infrastructure for OSINT research.',
        'image': 'images/tutorials-8.svg'
    },
    'username-scanner-basics': {
        'title': 'Username Scanner Basic Usage',
        'description': 'How to scan usernames across platforms efficiently.',
        'image': 'images/tutorials-9.svg'
    },
    'account-linking-analysis': {
        'title': 'Account Linking and Connection Analysis',
        'description': 'Methods for linking accounts and network analysis.',
        'image': 'images/tutorials-10.svg'
    },
    'social-media-profile-analysis': {
        'title': 'Social Media Profile Analysis',
        'description': 'Analyzing social profiles to extract OSINT.',
        'image': 'images/tutorials-11.svg'
    }
}


@app.route('/tutorials/<slug>')
def tutorial_detail(slug):
    meta = tutorial_meta.get(slug)
    if not meta:
        return render_template('404.html'), 404
    return render_template('tutorial_detail.html', meta=meta)

@app.route("/api-docs")
def api_docs():
    return render_template("api-docs.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

@app.route("/terms")
def terms():
    return render_template("terms.html")

@app.route("/disclaimer")
def disclaimer():
    return render_template("disclaimer.html")


if __name__ == "__main__":
    app.run(debug=True)
