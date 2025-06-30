# Из исходного текстового файла (experience.txt) выбрать стаж работы. Посчитать
# количество полученных элементов. 


import re

with open('algorithm\Pz Sapronov Daniil\Pz_14\experience.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

experience = []
for line in lines:
    
    match = re.search(r'\d+\s*(лет|год|года)\s*\d*\s*(месяцев|месяца|месяц)?', line)
    if match:
        experience.append(match.group(0))  

print("Стаж:", *experience)
print("Количество записей:", len(experience))