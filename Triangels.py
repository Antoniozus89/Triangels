a = int(input())
b = int(input())
c = int(input())
if a == b and b == c:
    print('Равносторонния треугольник')
elif a == b and b != c :
    print('Равнобедренный треугольник')
else:
    print('Разносторонний треугольник')