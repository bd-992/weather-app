import requests
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from io import BytesIO

def get_weather():
    city = city_entry.get()
    data = response.json()
    if not city:
        messagebox.showwarning("Uyarı","Lütfen bir şehir adı girin.")
        return
    
    api_key = "5d0d495ebc8027f5ea0ec131bfe857a3"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=tr"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        if response.status_code == 200:
            
            
            temperature = data["main"]["temp"]
            weather_description = data["weather"][0]["description"]

            result_label.config(text=f"{city} için hava durumu:\nSıcaklık: {temperature}°C\nDurum: {weather_description}")
        else: 
            messagebox.showerror("Hata","Şehir bulunamadı.Lütfen doğru yazdığınızdan emin olun.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Hata",f"API bağlantısı başarısız. Hata: {e}")
#ana pencere
window = tk.Tk()
window.title("Hava durumu uygulaması")
window.geometry("400x300")  
window.config(bg="#f0f0f0")

#şehir ismi girişi
city_entry = tk.Entry(window,width=30,font=("Helvetica",14), bg="#e0e0e0",fg="#333")
city_entry.pack(pady=10)

#sorgulama buttonu
search_button = tk.Button(window, text="Hava Durumunu Getir", command=get_weather,font=("Arial",12),bg="#4CAF50",fg="white",relief="raised")
search_button.pack(pady=10)

#sonuç etiketi
result_label = tk.Label(window, text="", font=("Helvetica",12),bg="#f0f0f0",fg="blue")
result_label.pack(pady=20)

#hava durumu simgesi
icon_code = data["weather"][0]["icon"]
icon_url = f"http://openweathermap.org/img/wn{icon_code}.png"
icon_image = tk.PhotoImage(file=icon_url)
icon_label = tk.Label(window, image=icon_image)
icon_label.pack()
#pencereyi açık tut
window.mainloop()