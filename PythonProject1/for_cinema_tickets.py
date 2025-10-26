total_tickets = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0

movie_name = input()

while movie_name != 'Finish':
    free_seats = int(input())
    sold_for_movie = 0

    while True:
        ticket_type = input()

        if ticket_type == 'End':
            break

        sold_for_movie += 1
        total_tickets += 1

        if ticket_type == 'student':
            student_tickets += 1
        elif ticket_type == 'standard':
            standard_tickets += 1
        elif ticket_type == 'kid':
            kid_tickets += 1

        if sold_for_movie == free_seats:
            break

    percent_full = sold_for_movie / free_seats * 100
    print(f'{movie_name} - {percent_full:.2f}% full.')

    movie_name = input()


print(f'Total tickets: {total_tickets}')
print(f'{student_tickets / total_tickets * 100:.2f}% student tickets.')
print(f'{standard_tickets / total_tickets * 100:.2f}% standard tickets.')
print(f'{kid_tickets / total_tickets * 100:.2f}% kids tickets.')
