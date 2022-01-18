#!/usr/bin/env python3

# Created by: Abdul Basit
# Created on: Jan 2022
# This program finds the hex of letter


def main():
    # this function finds the hexadecimal of letter

    dictionary = {}
    some_info = {
        "item1": 1,
        "item2": 2,
    }
    characters = []

    # Adding Items
    dictionary[" "] = "0x20"
    dictionary["!"] = "0x21"
    dictionary["#"] = "0x23"
    dictionary["$"] = "0x24"
    dictionary["%"] = "0x25"
    dictionary["&"] = "0x26"
    dictionary["'"] = "0x27"
    dictionary["("] = "0x28"
    dictionary[")"] = "0x29"
    dictionary["*"] = "0x2a"
    dictionary["+"] = "0x2b"
    dictionary[","] = "0x2c"
    dictionary["-"] = "0x2d"
    dictionary["."] = "0x2e"
    dictionary["/"] = "0x2f"
    dictionary["0"] = "0x30"
    dictionary["1"] = "0x31"
    dictionary["2"] = "0x32"
    dictionary["3"] = "0x33"
    dictionary["4"] = "0x34"
    dictionary["5"] = "0x35"
    dictionary["6"] = "0x36"
    dictionary["7"] = "0x37"
    dictionary["8"] = "0x38"
    dictionary["9"] = "0x39"
    dictionary[":"] = "0x3a"
    dictionary[";"] = "0x3b"
    dictionary["<"] = "0x3c"
    dictionary["="] = "0x3d"
    dictionary[">"] = "0x3e"
    dictionary["?"] = "0x3f"
    dictionary["@"] = "0x40"
    dictionary["A"] = "0x41"
    dictionary["B"] = "0x42"
    dictionary["C"] = "0x43"
    dictionary["D"] = "0x44"
    dictionary["E"] = "0x45"
    dictionary["F"] = "0x46"
    dictionary["G"] = "0x47"
    dictionary["H"] = "0x48"
    dictionary["I"] = "0x49"
    dictionary["J"] = "0x4a"
    dictionary["K"] = "0x4b"
    dictionary["L"] = "0x4c"
    dictionary["M"] = "0x4d"
    dictionary["N"] = "0x4e"
    dictionary["O"] = "0x4f"
    dictionary["P"] = "0x50"
    dictionary["Q"] = "0x51"
    dictionary["R"] = "0x52"
    dictionary["S"] = "0x53"
    dictionary["T"] = "0x54"
    dictionary["U"] = "0x55"
    dictionary["V"] = "0x56"
    dictionary["W"] = "0x57"
    dictionary["X"] = "0x58"
    dictionary["Y"] = "0x59"
    dictionary["Z"] = "0x5a"
    dictionary["["] = "0x5b"
    dictionary["]"] = "0x5d"
    dictionary["^"] = "0x5e"
    dictionary["_"] = "0x5f"
    dictionary["`"] = "0x60"
    dictionary["a"] = "0x61"
    dictionary["b"] = "0x62"
    dictionary["c"] = "0x63"
    dictionary["d"] = "0x64"
    dictionary["e"] = "0x65"
    dictionary["f"] = "0x66"
    dictionary["g"] = "0x67"
    dictionary["h"] = "0x68"
    dictionary["i"] = "0x69"
    dictionary["j"] = "0x6a"
    dictionary["k"] = "0x6b"
    dictionary["l"] = "0x6c"
    dictionary["m"] = "0x6d"
    dictionary["n"] = "0x6e"
    dictionary["o"] = "0x6f"
    dictionary["p"] = "0x70"
    dictionary["q"] = "0x71"
    dictionary["r"] = "0x72"
    dictionary["s"] = "0x73"
    dictionary["t"] = "0x74"
    dictionary["u"] = "0x75"
    dictionary["v"] = "0x76"
    dictionary["w"] = "0x77"
    dictionary["x"] = "0x78"
    dictionary["y"] = "0x79"
    dictionary["z"] = "0x7a"
    dictionary["{"] = "0x7b"
    dictionary["|"] = "0x7c"
    dictionary["}"] = "0x7d"
    dictionary["~"] = "0x7e"

    some_string = input("Please enter a string tp be translated into hex: ")
    characters = list(some_string)

    for counter in characters:
        if counter in dictionary.keys():
            print("{0} ".format(dictionary[counter]), end="")
        else:
            print("That characters are not in dictionary.")
            break
    print("")
    print("\nDone.")


if __name__ == "__main__":
    main()
