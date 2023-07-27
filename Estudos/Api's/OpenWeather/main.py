from Clima import ClimaAPI

cidade = str(input("Digite sua Cidade: ")).capitalize()

weather_api = ClimaAPI()
descricao, temperatura_celsius = weather_api.informacoes_clima(cidade)

print(f"Descrição: {descricao}")
print(f"Temperatura: {temperatura_celsius:.2f}°C")
