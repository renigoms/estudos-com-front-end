def function():
    print(
    f"O número {num} é par !" 
    if (num := int(input("Digite um número"))) % 2 == 0 
    else f"O número {num} é impar !"
    )
    if num == 0: return
    return function()

if '__main__' == __name__:
    function()
