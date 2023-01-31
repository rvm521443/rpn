import random

COIN = ('heads', 'tails')

def get_input():
    ans = ''
    while ans not in COIN:
        ans = input('heads or tails? ')
    return ans

def throw(ans):
    return ans == random.choice(COIN)

def main():
    ans = get_input()
    res = random.choice(COIN)
    print(f"it's {res}")
    msg = 'you win' if ans == res else 'you lose'
    print(msg)

if __name__ == '__main__':
    main()

