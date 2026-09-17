from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/info")
def get_info(kota: str = "Serang"):
    # 1. Ambil data Adzan (API Aladhan biasanya stabil)
    try:
        url_adzan = f"https://api.aladhan.com/v1/timingsByCity?city={kota}&country=Indonesia"
        res_adzan = requests.get(url_adzan, timeout=10).json()
        jadwal = res_adzan["data"]["timings"]
    except Exception as e:
        return {"error": f"API Adzan lagi bermasalah: {str(e)}"}
        
    # 2. Ambil data Cuaca (API wttr.in kadang suka down)
    cuaca_info = {"suhu_celcius": "N/A", "kondisi": "Gagal ambil cuaca"}
    try:
        url_cuaca = f"https://wttr.in/{kota}?format=j1"
        res_cuaca = requests.get(url_cuaca, timeout=5).json()
        cuaca_info["suhu_celcius"] = res_cuaca["current_condition"][0]["temp_C"]
        cuaca_info["kondisi"] = res_cuaca["current_condition"][0]["weatherDesc"][0]["value"]
    except Exception:
        # Kalau error, biarin aja (pass). Nanti return tulisan "N/A" di atas
        pass 

    # 3. Gabungin dan return
    return {
        "lokasi": kota,
        "cuaca": cuaca_info,
        "jadwal_sholat": {
            "Subuh": jadwal["Fajr"],
            "Dzuhur": jadwal["Dhuhr"],
            "Ashar": jadwal["Asr"],
            "Maghrib": jadwal["Maghrib"],
            "Isya": jadwal["Isha"]
        }
    }