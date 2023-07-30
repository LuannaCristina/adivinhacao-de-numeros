import random

print("Seja muito bem vindo ao meu jogo de adivinhação!")
choise_number = input("Digite o número teto do desafio: ")

if choise_number.isdigit():
    choise_number = int(choise_number)
else:
    print("Erro. O valor informado não é numérico. Por favor, execute novamente e informe um número!")
    quit()

random_number = random.randint(0, choise_number)

n_choice = 0

while True:
    answer_user = input("Adivinhe o número: ")

    if answer_user.isdigit():
        answer_user = int(answer_user)
    else:
        print("Erro. O valor informado não é numérico. Por favor, execute novamente e informe um número!")
        continue

    n_choice = n_choice + 1
    if answer_user == random_number:
        print("Acertou!")
        break
    elif answer_user > random_number:
        print("Chutou alto! Quer uma dica... O numéro é menor!")
    else:
        print("Chutou baixo! Quer uma dica... O número é maior!")

print("Nº de tentativas " + str(n_choice))

