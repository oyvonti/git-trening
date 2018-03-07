# Speilvendt pyramide i forhold til Pyramide1

def pypart3(n):

    # k er antall mellomrom som settes før stjernen
    k = 2*n - 2

    # Ytre løkke - styrer antall rader (n)
    for i in range(0, n):

        # Løkken håndterer antall mellomrom før stjernen
        for j in range(0, k):
            print(end=" ")

        # Forminsker k etter hver runde
        k = k - 1

        # Løkken håndterer antall kolonner
        for j in range(0, i+1):
            print("* ", end="")

        print("\r")


n=15
pypart3(n)