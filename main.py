import requests
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from io import BytesIO

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Uyarı", "Lütfen bir şehir adı girin.")
        return

    api_key = "5d0d495ebc8027f5ea0ec131bfe857a3"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=tr"

    try:
        response = requests.get(url)
        response.raise_for_status()
        if response.status_code == 200:
            data = response.json()

            temperature = data["main"]["temp"]
            weather_description = data["weather"][0]["description"]

            result_label.config(text=f"{city} için hava durumu:\nSıcaklık: {temperature}°C\nDurum: {weather_description}")

            # Hava durumu simgesi:
            icon_code = data["weather"][0]["icon"]
            icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
            icon_response = requests.get(icon_url)
            icon_data = Image.open(BytesIO(icon_response.content))
            icon_image = ImageTk.PhotoImage(icon_data)

            icon_label.config(image=icon_image)
            icon_label.image = icon_image  # referansı sakla
        else:
            messagebox.showerror("Hata", "Şehir bulunamadı. Lütfen doğru yazdığınızdan emin olun.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Hata", f"API bağlantısı başarısız. Hata: {e}")

# Ana pencere
window = tk.Tk()
window.title("Hava Durumu Uygulaması")
window.geometry("400x400")
window.config(bg="#f0f0f0")

# Şehir ismi girişi
city_entry = tk.Entry(window, width=30, font=("Helvetica", 14), bg="#e0e0e0", fg="#333")
city_entry.pack(pady=10)

# Sorgulama butonu
search_button = tk.Button(window, text="Hava Durumunu Getir", command=get_weather, font=("Arial", 12), bg="#4CAF50", fg="white")
search_button.pack(pady=10)

# Sonuç etiketi
result_label = tk.Label(window, text="", font=("Helvetica", 12), bg="#f0f0f0", fg="blue")
result_label.pack(pady=10)

# İkon etiketi (başta boş, sonradan doldurulacak)
icon_label = tk.Label(window, bg="#f0f0f0")
icon_label.pack()

# Pencereyi açık tut
window.mainloop()
