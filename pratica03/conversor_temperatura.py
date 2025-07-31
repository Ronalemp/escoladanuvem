"""4- Conversor de Temperatura 
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
O usuário deve informar a temperatura, a unidade de origem e 
a unidade para qual deseja converter."""

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_para_kelvin(fahrenheit):
    celsius = fahrenheit_para_celsius(fahrenheit)
    return celsius_para_kelvin(celsius)

def kelvin_para_fahrenheit(kelvin):
    celsius = kelvin_para_celsius(kelvin)
    return celsius_para_fahrenheit(celsius)

if __name__ == "__main__":
    temperatura = float(input("Digite a temperatura: "))
    unidade_origem = input("Digite a unidade de origem (C, F, K): ").upper()
    unidade_destino = input("Digite a unidade de destino (C, F, K): ").upper()

    if unidade_origem == "C":
        if unidade_destino == "F":
            print(f"{temperatura}°C = {celsius_para_fahrenheit(temperatura)}°F")
        elif unidade_destino == "K":
            print(f"{temperatura}°C = {celsius_para_kelvin(temperatura)}K")
        else:
            print("Unidade de destino inválida.")
    elif unidade_origem == "F":
        if unidade_destino == "C":
            print(f"{temperatura}°F = {fahrenheit_para_celsius(temperatura)}°C")
        elif unidade_destino == "K":
            print(f"{temperatura}°F = {fahrenheit_para_kelvin(temperatura)}K")
        else:
            print("Unidade de destino inválida.")
    elif unidade_origem == "K":
        if unidade_destino == "C":
            print(f"{temperatura}K = {kelvin_para_celsius(temperatura)}°C")
        elif unidade_destino == "F":
            print(f"{temperatura}K = {kelvin_para_fahrenheit(temperatura)}°F")
        else:
            print("Unidade de destino inválida.")
    else:
        print("Unidade de origem inválida.")
# Fim do código

