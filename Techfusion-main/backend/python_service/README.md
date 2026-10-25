# TinyFish Python Service for AapdaRakshak

This Python service integrates TinyFish for web scraping and automation tasks to support disaster management operations.

## Installation

1. Install Python 3.8 or higher
2. Install dependencies:
```bash
cd backend/python_service
pip install -r requirements.txt
```

## Running the Service

```bash
cd backend/python_service
python tinyfish_service.py
```

The service will run on `http://localhost:5001`

## API Endpoints

### 1. Scrape Disaster News
**POST** `/api/scrape-disaster-news`

Extract disaster-related news from any news website.

**Request Body:**
```json
{
  "url": "https://news-site.com/disasters",
  "goal": "Extract disaster news headlines and summaries"
}
```

### 2. Scrape Emergency Contacts
**POST** `/api/scrape-emergency-contacts`

Extract emergency contact information from government websites.

**Request Body:**
```json
{
  "url": "https://government-site.gov/emergency"
}
```

### 3. Monitor Disaster Alerts
**POST** `/api/monitor-disaster-alerts`

Monitor and extract disaster alerts from official sources.

**Request Body:**
```json
{
  "url": "https://weather.gov/alerts"
}
```

### 4. Extract Relief Resources
**POST** `/api/extract-relief-resources`

Extract information about relief resources, shelters, and distribution points.

**Request Body:**
```json
{
  "url": "https://relief-organization.org/resources"
}
```

## Integration with Node.js Backend

The Node.js backend can call these endpoints using axios:

```javascript
const axios = require('axios');

async function scrapeDisasterNews(url) {
  const response = await axios.post('http://localhost:5001/api/scrape-disaster-news', {
    url: url,
    goal: 'Extract disaster news and alerts'
  });
  return response.data;
}
```

## Use Cases for AapdaRakshak

- **Real-time News Monitoring**: Automatically scrape disaster news from multiple sources
- **Emergency Contact Updates**: Keep emergency contact databases updated from government sites
- **Alert Aggregation**: Collect alerts from weather services, disaster management authorities
- **Resource Tracking**: Monitor relief resource availability from NGO websites
- **Social Media Monitoring**: Track disaster-related discussions and requests for help

## Security Notes

- Rate limit requests to avoid overwhelming target websites
- Validate and sanitize URLs before scraping
- Implement authentication for production use
- Cache results to reduce redundant scraping
