numbers = list(range(1, 1000001))  # Your original list
guess = int(input("🤔 Tell me a number and I will tell you its position on the list: ")) #7
start_index = 0
end_index = len(numbers) - 1

has_finished = False
operations_count = 0

while not has_finished:
    operations_count += 1
    current_mid = (start_index + end_index) // 2

    if start_index > end_index:
        print("This number doest not exist 🚫 in the list")
        has_finished = True
    elif numbers[current_mid] < guess:
        start_index = current_mid + 1
    elif numbers[current_mid] > guess:
        end_index = current_mid - 1
    else:
        print(f"The index of your number({guess}) is:{current_mid} ✅")
        has_finished = True

print(f"The number of operations was: {operations_count} 📈")
