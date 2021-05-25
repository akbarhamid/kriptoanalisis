import random

print("PROGRAM PRIME GENERATOR")
print("MUHAMMAD AKBAR HAMID (1808561064) - Sang Putu Febri Wira Pratama (1808561012) / KRIPTOANALISIS")

def prime_generate():
    print("PRIME NUMBER FINDER")
    num_start = int(input("Input Start Number : "))
    num_end = int(input("Input End Number   : "))
    list_num = [i for i in range(num_start, num_end + 1)]
    prime_num = []
    for i in list_num:
        if (i == 2 or i == 3 or i == 5 or i == 7) or (i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0):
            prime_num.append(i)
    print(prime_num)

    # confirm to choice random prime number
    conf = input("Choice Random Prime Number [y/n]? ")
    if conf.lower() in ['y', 'yes']:
        # choice the random prime number
        print("=======================")
        print("THE RANDOM PRIME NUMBER")
        print("=======================")
        rand_num1 = random.choice(prime_num)  # first random prime number
        print("Random Number 1 :", rand_num1)
        rand_num2 = random.choice(prime_num)  # second random prime number
        print("Random Number 2 :", rand_num2)
    elif conf.lower() in ['n', 'no']:
        print('End!')

def main():
    prime_generate()

main()