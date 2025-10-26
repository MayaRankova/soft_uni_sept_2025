start_interval = int(input())
end_interval = int(input())

for number in range(start_interval, end_interval + 1):
    number_str = str(number)
    even_sum = 0
    odd_sum = 0

    for position in range(6):
        digit = int(number_str[position])

        if (position + 1) % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    if even_sum == odd_sum:
        print(number, end=' ')
