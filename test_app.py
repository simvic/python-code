from app import process_workbook
from pathlib import Path

path = Path()
for file in path.glob('*.xlsx'):
    process_workbook(open(file))