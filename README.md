# 🕌 Adzan & Weather Extension

A lightweight Chrome/Firefox browser extension that provides real-time prayer times and current weather updates. 

This project was built to demonstrate the **Backend-For-Frontend (BFF)** architecture, where a custom Python server acts as a middleman (API Gateway) to fetch, clean, and format data from external APIs before sending it to the browser extension.

## ✨ Features
*   **Real-time Prayer Times:** Fetches accurate Adzan schedules based on the user's city.
*   **Live Weather Updates:** Displays current temperature and weather conditions.
*   **Resilient Backend:** Built-in error handling (fallback to "N/A" if the weather API is down without crashing the prayer times).
*   **Modern UI:** Clean, minimalist popup interface using pure HTML/CSS.

## 🛠️ Tech Stack
**Backend (API Gateway):**
*   Python 3.x
*   [FastAPI](https://fastapi.tiangolo.com/) - Web framework
*   Uvicorn - ASGI server
*   Requests - HTTP library
*   External APIs: [Aladhan API](https://aladhan.com/prayer-times-api) (Prayer times) & [wttr.in](https://github.com/chubin/wttr.in) (Weather)

**Frontend (Browser Extension):**
*   HTML, CSS, Vanilla JavaScript
*   Chrome Extension Manifest V3

## 📂 Project Structure
```text
adzan-extension/
├── backend/
│   ├── main.py              # FastAPI server & API logic
│   └── requirements.txt     # Python dependencies
└── extension/
    ├── manifest.json        # Extension configuration
    └── popup/
        ├── popup.html       # UI Layout
        └── popup.js         # Frontend logic & API calling

```

## 🚀 How to Run Locally

### 1. Start the Python Backend

Navigate to the backend directory and install the required Python libraries:

```bash
cd backend
pip install fastapi uvicorn requests

```

Start the local server:

```bash
uvicorn main:app --reload

```

*The server will start running at `http://localhost:8000`.*

### 2. Install the Extension in Chrome

1. Open Google Chrome and go to `chrome://extensions/`.
2. Turn on **Developer mode** in the top right corner.
3. Click the **Load unpacked** button in the top left.
4. Select the `extension` folder from this repository.
5. The extension is now installed! Pin it to your toolbar and click the icon to test it.

## 📡 API Reference (Local)

The Python backend exposes a single optimized endpoint for the frontend.

**`GET /api/info?kota={city_name}`**

**Response Example:**

```json
{
  "lokasi": "Serang",
  "cuaca": {
    "suhu_celcius": "28",
    "kondisi": "Partly cloudy"
  },
  "jadwal_sholat": {
    "Subuh": "04:30",
    "Dzuhur": "11:55",
    "Ashar": "15:15",
    "Maghrib": "18:00",
    "Isya": "19:12"
  }
}

```

## 📝 Learning Notes

This project focuses on separating concerns:

* The **Frontend (JS)** is completely "dumb". It only knows how to ask the Python server for data and display it.
* The **Backend (Python)** does the heavy lifting: communicating with 3rd-party services, handling timeouts, managing CORS, and formatting complex nested JSON into a flat, predictable structure for the extension.

```

```
