"""
CTEC 121
<your name>
<assignment/lab name>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""

def main():
    print("Happy birthday to you!" )
    print("Happy birthday to you!" )
    print("Happy birthday, dear Fred...")
    print("Happy birthday to you!")
main()

def happy():
    print("happy birthday to you!")
happy()

def main2():
    print()
    happy()
    happy()
    print('Happy birthday, dear Fred...')
    happy()
    print()
main2()

#calling by function parameters

def happybday(name):
    print("happy bday dear ",name,"...", sep="")


def singhappybday(name):
    happy()
    happy()
    happybday(name)
    happy()
    print()


def main4():
    print()
    singhappybday("Bill")
    print()
main4()
