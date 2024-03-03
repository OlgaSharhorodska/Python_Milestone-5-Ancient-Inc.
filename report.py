import csv
import sys
from datetime import datetime

def load_data(filename):
    """Загружает данные из CSV файла."""
    data = []
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def filter_records_by_month(data, month):
    """Фильтрует записи по указанному месяцу."""
    filtered_records = []
    for record in data:
        hire_date = datetime.strptime(record['Hire Date'], '%Y-%m-%d')
        if hire_date.strftime('%B').lower() == month.lower():
            filtered_records.append(record)
    return filtered_records

def count_records_by_department(records):
    """Подсчитывает количество записей по отделам."""
    department_counts = {}
    for record in records:
        department = record['Department']
        department_counts[department] = department_counts.get(department, 0) + 1
    return department_counts

def display_report(month, birthdays, anniversaries, verbose=False):
    """Выводит отчет о днях рождения и юбилеях."""
    print(f"Отчет за {month.capitalize()} сформирован")
    print("--- Дни рождения ---")
    print(f"Всего: {len(birthdays)}")
    if verbose:
        for birthday in birthdays:
            print(f"- {birthday['Name']}: {birthday['Birth Date']}")

    print("--- Юбилеи ---")
    print(f"Всего: {len(anniversaries)}")
    if verbose:
        for anniversary in anniversaries:
            print(f"- {anniversary['Name']}: {anniversary['Hire Date']}")
    print("\nПо отделам:")
    for department, count in count_records_by_department(birthdays).items():
        print(f"- {department}: {count}")
    for department, count in count_records_by_department(anniversaries).items():
        print(f"- {department}: {count}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python report.py <имя файла> <месяц>")
        sys.exit(1)

    filename = sys.argv[1]
    month = sys.argv[2]

    data = load_data(filename)
    filtered_data = filter_records_by_month(data, month)
    birthdays = [record for record in filtered_data if record['Birth Date']]
    anniversaries = [record for record in filtered_data if record['Hire Date']]
    display_report(month, birthdays, anniversaries)
