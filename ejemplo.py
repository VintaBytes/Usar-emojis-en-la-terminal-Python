import time

def mostrar_estado_pedido():
    estados = [
        "📦 Pedido recibido",
        "👨‍🍳 Preparando tu comida",
        "🚚 Pedido en camino",
        "🍽️ Pedido entregado"
    ]
    
    for estado in estados:
        print(estado)
        time.sleep(2)  # Simula la espera de un proceso real

def mostrar_resumen_pedido():
    print("\nResumen del pedido:")
    print("🍕 Pizza Margherita")
    print("🥤 Bebida: Coca-Cola")
    print("🍰 Postre: Tarta de queso")
    print("💵 Total: $25.99")
    print("⏰ Tiempo estimado: 30 minutos")

def main():
    print("Bienvenido a FoodTrack 🛵🍴")
    print("Tu pedido está siendo procesado...\n")

    mostrar_estado_pedido()

    print("\n✅ ¡Tu pedido ha sido entregado!")
    mostrar_resumen_pedido()

if __name__ == "__main__":
    main()