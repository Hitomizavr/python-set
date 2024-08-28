n = int(input("Введите количество чисел: "))

listOfNumbers = list(map(int, input("Введите эти числа через пробел: ").split()))[:n]

setOfNumbers = set(listOfNumbers)

print("Число различных чисел среди введенных: ", len(setOfNumbers));