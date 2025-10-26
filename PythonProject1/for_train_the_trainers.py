n = int(input())

total_sum = 0
total_count = 0

while True:
    presentation_name = input()

    if presentation_name == "Finish":
        break

    presentation_sum = 0
    for _ in range(n):
        grade = float(input())
        presentation_sum += grade

    average_grade = presentation_sum / n
    print(f'{presentation_name} - {average_grade:.2f}.')

    total_sum += presentation_sum
    total_count += n

final_assessment = total_sum / total_count
print(f'Student\'s final assessment is {final_assessment:.2f}.')