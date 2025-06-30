#Составить генератор (yield), который переведет символы строки из верхнего
#регистра в нижний.

def lower_c(input_str):
        yield input_str.lower()


input_str = input("Введите текст ")


print("".join(lower_c(input_str)))




