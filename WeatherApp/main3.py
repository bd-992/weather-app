import tkinter as tk
import requests
from PIL import ImageTk, Image
from io import BytesIO

def get_weather():
    city = city_entry.get()
    api_key="5d0d495ebc8027f5ea0ec131bfe857a3"
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=tr"

    response = requests.get(api_url)
    data = response.json()

    try: 
        temperature = data["main"]["temp"]
        description = data["weather"]["description"]
        icon_code = data["weather"][0]["icon"]

        icon_url=f"http://openweathermap.org/img/wn{icon_code}@2x.png"
        icon_response = requests.get(icon_url)
        icon_data = icon_response.content
        icon_image = ImageTk.PhotoImage(Image.open(BytesIO(icon_data)))
        icon_label.config(image=icon_image)
        icon_label.image = icon_image

        result_label.config(text=f"{city} için hava durumu:\nSıcaklık: {temperature}°C\nDurum: {description}")
    
    except KeyError:
        result_label.config(text="Şehir bulunamadı veya veri alınamadı.")

window= tk.Tk()
window.title("Hava Durumu")
window.geometry("400x400")

city_entry = tk.Entry(window, font=("Helvetica",14))
city_entry.pack(pady=10)

search_button = tk.Button(window, text="Hava Durumunu Getir", command=get_weather)
search_button.pack(pady=10)

icon_label = tk.Label(window)
icon_label.pack()

result_label = tk.Label(window,text="",font=("Helvetica",12))
result_label.pack(pady=20)

window.mainloop()