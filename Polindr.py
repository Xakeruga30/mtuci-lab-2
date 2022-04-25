input_string = input()
input_length = len(input_string) // 2
for i in range(input_length):
    if input_string[i] != input_string[-1-i]:
        print("Не полиндром!")
        quit()
print("Полиндром!")