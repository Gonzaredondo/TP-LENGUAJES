import random

opciones = ["piedra", "papel", "tijera"]
rondas_totales = 5 
rondas_para_ganar = (rondas_totales // 2) + 1

print("¡Bienvenido! Vamos a jugar a Piedra, Papel o Tijera.")
print(f"Jugamos al mejor de {rondas_totales} rondas. Quien gane {rondas_para_ganar} primero, gana el juego.")
print("Escribí tu jugada (piedra/papel/tijera).")

puntos_usuario = 0
puntos_pc = 0
ronda = 1

while ronda <= rondas_totales:
    print(f"\nRonda {ronda}")
    jugada_usuario = input("Tu jugada: ").strip().lower()

    if jugada_usuario not in opciones:
        print("Entrada no valida. Debe ser piedra, papel o tijera.")
        continue 

    jugada_pc = random.choice(opciones)
    print(f"La computadora eligio: {jugada_pc}")

    if jugada_usuario == jugada_pc:
        print("Empate.")
    elif (
        (jugada_usuario == "piedra" and jugada_pc == "tijera") or
        (jugada_usuario == "papel" and jugada_pc == "piedra") or
        (jugada_usuario == "tijera" and jugada_pc == "papel")
    ):
        print("¡Ganaste la ronda!")
        puntos_usuario += 1
    else:
        print("Perdiste la ronda.")
        puntos_pc += 1

   
    if puntos_usuario == rondas_para_ganar or puntos_pc == rondas_para_ganar:
        break

    ronda += 1


print("\n=== Resultado final ===")
print(f"Tus puntos: {puntos_usuario} | Puntos de la PC: {puntos_pc}")

if puntos_usuario > puntos_pc:
    print("¡Ganaste el juego! 🎉")
elif puntos_usuario < puntos_pc:
    print("La computadora gano el juego.")
else:
    print("Empate total.")
