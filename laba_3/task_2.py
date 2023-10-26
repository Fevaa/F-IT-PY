def find_common_participants(participants_first_group, participants_second_group, delimiter=','):
    participants_first_group = participants_first_group.split(delimiter)
    participants_second_group = participants_second_group.split(delimiter)
    common_participants = list(set(participants_first_group) & set(participants_second_group))

    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group))
