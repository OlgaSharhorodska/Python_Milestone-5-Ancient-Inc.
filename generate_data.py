import csv
from faker import Faker
import random
import sys

# Создаем экземпляр Faker для генерации фиктивных данных
fake = Faker()

def generate_fake_data(num_records):
    """Генерирует фиктивные данные о сотрудниках."""
    data = []
    for _ in range(num_records):
        name = fake.name()
        hire_date = fake.date_between(start_date='-10y', end_date='today')
        department = random.choice(['HR', 'Финансы', 'Инженерное дело', 'НИОКР', 'Маркетинг'])
        birth_date = fake.date_of_birth(minimum_age=20, maximum_age=70)
        data.append((name, hire_date, department, birth_date))
    return data

def write_to_csv(data, filename):
    """Записывает данные в CSV файл."""
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Hire Date', 'Department', 'Birth Date'])
        writer.writerows(data)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python generate_data.py <количество записей> <имя файла>")
        sys.exit(1)

    num_records = int(sys.argv[1])
    filename = sys.argv[2]

    fake_data = generate_fake_data(num_records)
    write_to_csv(fake_data, filename)
    print(f"Сгенерировано {num_records} записей и сохранено в файле {filename}.")
