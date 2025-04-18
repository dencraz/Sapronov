
group1 = {"Анна", "Мария", "Елена", "Ольга"}
group2 = {"Мария", "Елена", "Светлана", "Ирина"}
group3 = {"Анна", "Елена", "Ирина", "Татьяна"}
group4 = {"Вика"}

all_names = group1 | group2 | group3 |group4


some_name = all_names - (group1 & group2 & group3)
one_name  = group4 - (group1 | group2 | group3)


# Выводим результаты
print("Имена которые встречаются во всех группах:", *all_names)
print("Имена которые встречаются только в некоторых группах:", *some_name)
print("Имена которые не встречаются ни в одной из групп:", *one_name)
