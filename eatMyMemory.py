
def eatMyMemory():
    megabyte = int(input("Ya', how much MB RAM should I eat?: "))

    if megabyte < 1:
        print("No, I can't eat less than 1 MB of RAM!\n")
        exit("=> ALL YOUR RAM WILL BE EATEN NOW BECAUSE YOU TRIED TO ESCAPE :P")

    else:
        print(f'Noice, I ate {megabyte} MB RAM from your system memory :p')



eatMyMemory()

