from fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Restaurant")

@mcp.tool()
def get_food_menu() -> str:
    """
    Получить меню блюд ресторана в виде таблицы в формате Markdown.
    """
    with open("data/menu/food.md", encoding="utf8") as file:
        return file.read()

# Определение инструмента для получения меню напитков
@mcp.tool()
def get_drinks_menu() -> str:
    """
    Получить меню напитков в виде таблицы в формате Markdown.
    """
    with open("data/menu/drinks.md", encoding="utf8") as file:
        return file.read()


if __name__ == "__main__":
    mcp.run()