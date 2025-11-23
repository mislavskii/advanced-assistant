from fastmcp import Client
import asyncio

SERVER_PATH = "mcp-server/mcp-rest.py"
async def interact_with_server():
    print("--- Создаём клиент ---")
    # Подключаемся к серверу, запущенному через `python my_server.py` (stdio)
    client = Client(SERVER_PATH)  # указываем путь к файлу сервера

    # print(f"Клиент подключён к: {client.target}")
    try:
        async with client:
            print("--- Клиент подключился ---")

            # Вызываем инструмент `get_food_menu` (из вашего примера)
            food_menu = await client.call_tool("get_food_menu")
            print("Меню блюд:")
            print(food_menu)

            # Аналогично вызываем `get_drinks_menu`
            drinks_menu = await client.call_tool("get_drinks_menu")
            print("Меню напитков:")
            print(drinks_menu)

    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        print("--- Взаимодействие завершено ---")

if __name__ == "__main__":
    asyncio.run(interact_with_server())