import random

secret_number = random.randint(1, 100)
guesses = []
max_guesses = 7

print("Salam! 1 ve 100 arasında bir reqem texmin et.")

while len(guesses) < max_guesses:
    guess = input("Texminin nedir? ")
    try:
        guess = int(guess)
    except ValueError:
        print("Zehmet olmasa tam bir reqem yaz.")
        continue

    if guess == secret_number:
        print(f"Tebrikler, doğru reqemi tapdiniz! {secret_number} dogru cavab!")
        break
    elif guess < secret_number:
        print("Daha Yuksek reqem texmin et.")
    else:
        print("Daha Asagi reqem texmin et.")

    guesses.append(guess)

if len(guesses) == max_guesses:
    print(f"Teessufler olsun, yoxlama sansiniz bitti. Dogru cavab {secret_number} idi.")
