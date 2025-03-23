
def main():

    num = float(input())
    msg = "Intervalo "

    if num < 0 or num > 100:
        msg= "Fora de intervalo"
    elif num <= 25:
        msg+="[0,25]"
    elif num <= 50:
        msg+="(25,50]"
    elif num <= 75:
        msg+="(50,75]"
    elif num <= 100:
        msg+="(75,100]"

    print(msg)

main()