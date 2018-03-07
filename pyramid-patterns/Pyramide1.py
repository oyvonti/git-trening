# Python code to demonstrate star pattern
# https://www.geeksforgeeks.org/programs-printing-pyramid-patterns-python/

# Function to demonstrate printing pattern
def pypart(n):

    # Ytre løkke for å håndtere antall rader (n rader)
    for i in range(0, n):

        # Indre løkke for å håndtere antall kolonner (like mange som det er rader)
        for j in range(0, i+1):
            print("* ", end="")

        print("\r")     # Linjeskift etter hver rad


n = 15
pypart(n)
