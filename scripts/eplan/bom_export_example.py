"""
Пример заготовки скрипта для обработки выгрузки спецификации из EPLAN.

Идея:
- прочитать CSV/Excel
- нормализовать номенклатуру
- сгруппировать по типам
- подготовить отчёт для закупки
"""

def process_bom(input_path: str, output_path: str):
    # TODO: реализовать логику обработки
    pass


if __name__ == "__main__":
    # Пример точки входа (дальше можно доработать)
    import sys
    if len(sys.argv) != 3:
        print("Использование: python bom_export_example.py input.csv output.csv")
        sys.exit(1)

    process_bom(sys.argv[1], sys.argv[2])
