import json

# JSON-строка с меню
menu_json = '''
{
  "menu": {
    "пиццы": [
      {
        "название": "бигблэкпицца",
        "цена": 1488
      },
      {
        "название": "фураваилдберрис",
        "цена": 2011
      }
    ],
    "алкоголь": [
      {
        "название": "Кorj heij",
        "цена": 676
      },
      {
        "название": "Afety kulimana",
        "цена": 3838
      }
    ],
    "безалкогольные напитки": [
      {
        "название": "смолвайткола",
        "цена": 785
      },
      {
        "название": "ямутакудасай",
        "цена": 768
      }
    ]
  }
}
'''

# Загружаем JSON в Python-объект
menu = json.loads(menu_json)

# Функция для вывода меню
def print_menu(menu):
    for category, items in menu['menu'].items():
        print(f"{category}:")
        for item in items:
            print(f"  {item['название']} - {item['цена']}р")
        print()  # Пустая строка для разделения категорий

# Выводим меню
print_menu(menu)
from tkinter.font import names









# JSON-строка с меню для несовершеннолетних
unmenu_json = '''
{
  "menu": {
    "пиццы": [
      {
        "название": "бигблэкпицца",
        "цена": 1488
      },
      {
        "название": "фураваилдберрис",
        "цена": 2011
      }
    ],
    "безалкогольные напитки": [
      {
        "название": "смолвайткола",
        "цена": 785
      },
      {
        "название": "ямутакудасай",
        "цена": 768
      }
    ]
  }
}
'''

# Загружаем JSON в Python-объект
menu = json.loads(unmenu_json)

# Функция для вывода меню
def print_menu(menu):
    for category, items in menu['menu'].items():
        print(f"{category}:")
        for item in items:
            print(f"  {item['название']} - {item['цена']}р")
        print()  # Пустая строка для разделения категорий

# Выводим меню
print_menu(menu)
from tkinter.font import names




