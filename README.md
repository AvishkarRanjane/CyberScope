# CyberScope

CyberScope is a Flask-based OSINT-style website for cybersecurity research, analysis, and documentation. It includes interactive IP, phone number, and username analysis endpoints plus resource, blog, tutorial, and documentation pages.

## Features

- IP address analysis via `ip-api.com`
- Phone number metadata lookup using `phonenumbers` or fallback API support via `PHONE_API_KEY`
- Username availability checks across popular social platforms
- Static website pages for resources, tutorials, blog posts, documentation, and legal pages
- Template-driven Flask app with HTML templates in `templates/`

## Project Structure

- `app.py` - Flask application entrypoint
- `requirements.txt` - Python dependencies
- `templates/` - HTML templates for pages and detail views
- `static/` - CSS and image assets

## Requirements

- Python 3.9+ (recommended)
- Flask
- requests
- python-dotenv
- phonenumbers (optional)

## Setup

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/CyberScope.git
cd CyberScope
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. (Optional) Create a `.env` file to add a phone validation API key:

```text
PHONE_API_KEY=your_api_layer_access_key
```

## Run

Start the Flask app:

```bash
python app.py
```

By default, the app runs on `http://127.0.0.1:5000`.

## Usage

- Visit `/` for the homepage
- Use `/resources`, `/blog`, `/tutorials`, `/documentation` for content pages
- Submit forms to `/analyze-ip`, `/analyze-phone`, and `/analyze-username` for JSON analysis results

## Notes

- The phone analysis endpoint prefers the `phonenumbers` library. If not installed, it uses the external API configured by `PHONE_API_KEY`.
- The app currently runs with `debug=True` for development. Change this for production.
