from flask import Flask, request, jsonify
from flask_cors import CORS
from tinyfish import TinyFish
import json

app = Flask(__name__)
CORS(app)

client = TinyFish()

@app.route('/api/scrape-disaster-news', methods=['POST'])
def scrape_disaster_news():
    """
    Scrape disaster-related news from a given URL
    Expected payload: { "url": "https://example.com", "goal": "Extract disaster news..." }
    """
    try:
        data = request.json
        url = data.get('url')
        goal = data.get('goal', 'Extract disaster-related news and alerts')
        
        if not url:
            return jsonify({'error': 'URL is required'}), 400
        
        results = []
        with client.agent.stream(url=url, goal=goal) as stream:
            for event in stream:
                results.append(str(event))
        
        return jsonify({
            'success': True,
            'data': results,
            'url': url
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/scrape-emergency-contacts', methods=['POST'])
def scrape_emergency_contacts():
    """
    Scrape emergency contact information from government websites
    Expected payload: { "url": "https://government-site.gov" }
    """
    try:
        data = request.json
        url = data.get('url')
        
        if not url:
            return jsonify({'error': 'URL is required'}), 400
        
        goal = "Extract emergency contact information including phone numbers, email addresses, and helpline services. Return as JSON array with keys: service_name, phone, email, location."
        
        results = []
        with client.agent.stream(url=url, goal=goal) as stream:
            for event in stream:
                results.append(str(event))
        
        return jsonify({
            'success': True,
            'data': results,
            'url': url
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/monitor-disaster-alerts', methods=['POST'])
def monitor_disaster_alerts():
    """
    Monitor disaster alerts from official sources
    Expected payload: { "url": "https://weather.gov/alerts" }
    """
    try:
        data = request.json
        url = data.get('url')
        
        if not url:
            return jsonify({'error': 'URL is required'}), 400
        
        goal = "Extract current disaster alerts including type, severity, location, and timestamp. Return as JSON array with keys: alert_type, severity, location, timestamp, description."
        
        results = []
        with client.agent.stream(url=url, goal=goal) as stream:
            for event in stream:
                results.append(str(event))
        
        return jsonify({
            'success': True,
            'data': results,
            'url': url
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/extract-relief-resources', methods=['POST'])
def extract_relief_resources():
    """
    Extract relief resources and shelter information
    Expected payload: { "url": "https://relief-organization.org" }
    """
    try:
        data = request.json
        url = data.get('url')
        
        if not url:
            return jsonify({'error': 'URL is required'}), 400
        
        goal = "Extract relief resource information including shelter locations, food distribution points, medical centers. Return as JSON array with keys: resource_type, location, capacity, contact, status."
        
        results = []
        with client.agent.stream(url=url, goal=goal) as stream:
            for event in stream:
                results.append(str(event))
        
        return jsonify({
            'success': True,
            'data': results,
            'url': url
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy', 'service': 'TinyFish Python Service'})

if __name__ == '__main__':
    app.run(port=5001, debug=True)
