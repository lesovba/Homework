n = 567

digit3  = n%10
n = n//10
digit2 = n%10
n =n//10

res = n+digit3+digit2

print("Сумма цифр трёхзначного числа", res)