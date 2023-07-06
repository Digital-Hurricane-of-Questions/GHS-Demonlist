import random, sys, sqlite

correspondences = {"show": "SELECT", "add" : "INSERT", "change" : "UPDATE", "delete" : "DELETE"}

def show(table, filters):
    query = "SELECT * FROM " + table + " WHERE "
    for i in range(0, filters.size(), 2):
        query += filters[i] " = " + filters[i+1] + " "
    return query

if __name__ == "__main__":
    func = sys.argv[1]
    if func in correspondences.keys():
        eval(func + "(\""+ sys.argv[2] + "\"[\"" + sys.argv[3:].split("\", \"")[:-2] + "\"])")
    else:
        print("Invalid function :(")