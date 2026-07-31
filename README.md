# CyberScope OSINT Dashboard

**Advanced Public Data Analysis for Cybersecurity Research**

Live Demo: [https://cyberscope-osint-app.vercel.app](https://cyberscope-osint-app.vercel.app)

## Features
- **IP Intelligence Lookup**: Pinpoint geographical location and ISP details of internet addresses.
- **Phone Metadata Lookup**: Retrieve carrier information and number classification.
- **Username OSINT Scanner**: Search for usernames across multiple social media platforms simultaneously.
- **Dark Terminal Theme**: OSINT-focused UI featuring terminal scanline effects, matte black, and terminal green.

## Tech Stack
- **Backend**: Python, Flask, Flask-Limiter
- **Frontend**: HTML5, CSS3 (Custom Terminal Theme), JavaScript
- **APIs**: ip-api.com, phonenumbers (Python library)

## Setup Instructions
1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment
4. Install dependencies: `pip install -r requirements.txt`
5. Create a `.env` file with `SECRET_KEY=your_secret_key` and `PHONE_API_KEY=your_apilayer_key` (optional)
6. Run the application: `python app.py`

## Security Disclaimer
**For Educational Use Only**: This tool is designed for legitimate cybersecurity research and education. Users are responsible for ensuring their usage complies with local laws and regulations. Unauthorized access to computer systems is illegal.

## License
MIT License
