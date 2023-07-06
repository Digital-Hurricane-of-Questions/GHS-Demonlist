import random, sys

correspondences = {"show": "SELECT", "add" : "INSERT", "change" : "UPDATE", "delete" : "DELETE"}


if __name__ == "__main__":
    func = sys.argv[1]
    if func in correspondences.keys():
        eval(func + "([" + sys.argv[2:].split(", ")[:-2] + "])")
    else:
        print("Invalid function :(")