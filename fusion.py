from main import main
from cli import file_explorer, get_input, get_input_lst

print("Fusion 0.5.0")

usin = {"file_daddy": None,
        "uni_dad": None,
        "lst_dad": None,

        "file_mommy": None,
        "uni_mom": None,
        "lst_mom": None
        }

def ask_input(prompt,func_call):

    con = False
    while not con:
        print(prompt)
        rt = func_call()
        x = input("Continue? (y/n)")
        if x in ["y", "n"]:
            if x == "y":
                con = True
            else:
                print("ok")
        else:
            print("Enter a valid input.")
        return rt

usin["file_daddy"] = ask_input("Choose daddy file:\n", file_explorer)

usin["file_mommy"] = ask_input("Choose mommy file:\n",file_explorer)

usin["uni_dad"] = ask_input("Choose unique column (email) index for daddy file:\n", get_input)

usin["uni_mom"] = ask_input("Choose unique column (email) index for mommy file:\n", get_input)


uni_lst = []
c = ask_input("Enter the number of columns you gonna use from the daddy file:\n",get_input)
def lam():
    return get_input_lst(int(c),uni_lst)
o = ask_input("Ok,",lam)
usin["lst_dad"] = o[0]
print(o)
uni_lst+= o[1]

c = ask_input("Enter the number of columns you gonna use from the mommy file:\n",get_input)
def lam():
    return get_input_lst(int(c),uni_lst)
o = ask_input("Ok,",lam)
usin["lst_mom"] = o[0]
uni_lst += o[1]

print(usin)

main(usin)

print("File successfully generated.")
input("Press enter to quit the program.")







