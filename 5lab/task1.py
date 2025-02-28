import re
import json


def match_a_b(text):
    return bool(re.fullmatch(r'ab*', text))


def match_a_bbb(text):
    return bool(re.fullmatch(r'ab{2,3}', text))

def find_underscore_sequences(text):
    return re.findall(r'\b[a-z]+_[a-z]+\b', text)


def find_upper_lower_sequences(text):
    return re.findall(r'\b[A-Z][a-z]+\b', text)


def match_a_anything_b(text):
    return bool(re.fullmatch(r'a.*b', text))


def replace_special_chars(text):
    return re.sub(r'[ ,.]', ':', text)


def snake_to_camel(text):
    words = text.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])


def split_at_uppercase(text):
    return re.split(r'(?=[A-Z])', text)


def insert_spaces(text):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', text)

def camel_to_snake(text):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()

data_json = '''{
    "duplicate": true,
    "branch": "Филиал ТОО EUROPHARMA Астана",
    "BIN": "080841000761",
    "cash_register": "300-189",
    "cashier": "Аптека 17-1",
    "sale": [
      {"item": "Натрия хлорид 0,9%, 200 мл, фл", "quantity": 2, "price": 154.00, "total": 308.00},
      {"item": "Борный спирт 3%, 20 мл, фл.", "quantity": 1, "price": 51.00, "total": 51.00},
      {"item": "Шприц 2 мл, 3-х комп. (Bioject)", "quantity": 2, "price": 16.00, "total": 32.00},
      {"item": "Система для инфузии Vogt Medical", "quantity": 2, "price": 60.00, "total": 120.00},
      {"item": "Naturella прокладки Классик макси №8", "quantity": 1, "price": 310.00, "total": 310.00}
    ],
    "total": 18009.00,  
    "timestamp": "18.04.2019 11:13:58",
    "location": "г. Нур-Султан, Казахстан, Мангилик Ел, 19, нп-5"
}'''

data = json.loads(data_json)

branch_pattern = re.compile(r'Филиал ТОО (.*)')
branch_match = branch_pattern.search(data['branch'])
branch = branch_match.group(1) if branch_match else None


bin_pattern = re.compile(r'\d+')
bin_match = bin_pattern.search(data['BIN'])
bin_number = bin_match.group(0) if bin_match else None


def extract_items(sales):
    return [(item['item'], item['quantity'], item['price'], item['total']) for item in sales]

items = extract_items(data['sale'])


print("Branch:", branch)
print("BIN:", bin_number)
print("Sales Items:", items)
