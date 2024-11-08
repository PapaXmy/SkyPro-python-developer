import functions


user_pk = int(input('Введите номер студента:\n'))
student_data = functions.get_students_by_pk(user_pk)

if not student_data:
    print('У на нет такого студента')
else:

    for student in student_data:
        print(f'Студент {student["full_name"]}\n'
              f'Знает {", ".join(student["skills"])}')

    user_profession = input(f'Выберите специальность для оценки '
                        f'студента {student["full_name"]}\n').capitalize()

    profession_data = functions.get_profession_bay_title(user_profession)

    if not profession_data:
        print('Унас нет такой специальности')

    else:
        for profession in profession_data:
            check_profession = functions.check_fitness(user_pk,
                                                        user_profession)
            print(f'Пригодность {check_profession["fit_percent"]}%\n'
                  f'Студент знает {", ".join(check_profession["has"])}\n'
                  f'Студент не знает {", ".join(check_profession["lacks"])}')
