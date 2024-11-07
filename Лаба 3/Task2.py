def find_common_participants(participants_first_group, participants_second_group, delimiter=","):
    first_group = participants_first_group.split(delimiter)
    second_group = participants_second_group.split(delimiter)
    common_participants = sorted(set(first_group) & set(second_group))
    return common_participants


# Проверка работы функции с разделителем "|"
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(
    participants_first_group,
    participants_second_group,
    delimiter="|"
)
print(f"Общие участники: {common_participants}")

# Проверка работы функции с разделителем ","
participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"

common_participants = find_common_participants(
    participants_first_group,
    participants_second_group
)
print(f"Общие участники: {common_participants}")
