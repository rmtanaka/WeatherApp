import requests
from tkinter import * 

def buscar_clima(cidade):
    chave_api = '1c23b93d565cb02c10bff9d10f12871a' 
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&units=metric&APPID={chave_api}")

    if weather_data.json()['cod'] == '404':
        return 'No city found!!!', None, None
    else:
        clima = weather_data.json()['weather'][0]['main']
        temp = round(weather_data.json()['main']['temp'])
        cidade = weather_data.json()['name']
        return clima, temp, cidade

def enter(event):
    cidade = entry_var.get()
    clima, temp, cidade = buscar_clima(cidade)
    if clima is not None and temp is not None:
        weather_info_label.config(text=f"The weather in {cidade} is {clima}.\nThe temperature is {temp} celsius.")
    else:
        weather_info_label.config(text="City not found or API error.")

janela = Tk()
janela.title('SimpleWeather')
txt_or = Label(janela, text="Type the city's name")
txt_or.pack(pady=10)

entry_var = StringVar()  
entry = Entry(janela, textvariable=entry_var, width=30)
entry.pack(pady=10)

entry.bind("<Return>", enter)

weather_info_label = Label(janela, text="", wraplength=300)
weather_info_label.pack(pady=10)

janela.mainloop()
