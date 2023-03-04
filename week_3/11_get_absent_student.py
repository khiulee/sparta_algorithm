all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


def get_absent_student(all_array, present_array):
    student_dict = {}
    for key in present_array:
        student_dict[key] = True
    for key in all_array:
        if student_dict[key]:
            del student_dict[key]
    for key in student_dict:
        return key


print(get_absent_student(all_students, present_students))
