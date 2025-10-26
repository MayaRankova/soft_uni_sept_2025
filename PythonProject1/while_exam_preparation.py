poor_grades_limit = int(input())

poor_grades_count = 0
grades_sum = 0
problems_count = 0
last_problem_name = ''

while True:
    problem_name = input()

    if problem_name == 'Enough':
        if problems_count > 0:
            average_score = grades_sum / problems_count
            print(f'Average score: {average_score:.2f}')
        else:
            print('No problems given.')
        print(f'Number of problems: {problems_count}')
        print(f'Last problem: {last_problem_name}')
        break

    grade = int(input())
    grades_sum += grade
    problems_count += 1
    last_problem_name = problem_name

    if grade <= 4:
        poor_grades_count += 1
        if poor_grades_count == poor_grades_limit:
            print(f'You need a break, {poor_grades_count} poor grades.')
            break
