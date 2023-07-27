import requests


class ClimaAPI:
    def __init__(self):
        self.api_key = "SUA_CHAVE_API"

    def informacoes_clima(self, city):
        link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&lang=pt_br"
        requisicao = requests.get(link)
        requisicao_dic = requisicao.json()
        descricao = requisicao_dic["weather"][0]["description"]
        temperatura = requisicao_dic["main"]["temp"]
        descricao_str = str(descricao).capitalize()
        temperatura_celcius = temperatura - 273.15
        return descricao_str, temperatura_celcius
