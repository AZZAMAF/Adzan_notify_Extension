from fastapi import FastAPI
import requests

# open the app
app = FastAPI()

@app.get("/")
def menu_utama():
    
    return {"message": "mantap bro, Server backend lu udh nyala"}

@app.get("/adzan")
def jadwal_adzan(kota: str = "Jakarta"):
    
    url = f"http://api.aladhan.com/v1/timingsByCity?city={kota}&country=Indonesia"
    
    try:
        # Tambahkan timeout=10 agar maksimal nunggu 10 detik
        response = requests.get(url, timeout=10)
        data_mentah = response.json()
        
        jadwal = data_mentah["data"]["timings"]
        
        return {
            "lokasi": kota,
            "jadwal_sholat": jadwal
        }
    except Exception as e:
        # Kalau gagal/timeout, kasih tau errornya ke browser
        return {"error": f"Gagal ngambil API: {str(e)}"}