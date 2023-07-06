import random, sys, sqlite3

def show(table, filters):
    query = "SELECT * FROM " + table + " WHERE "
    for i in range(0, filters.size(), 2):
        query += "" + filters[i] " = \"" + filters[i+1] + "\" "
    return query

def add(table, filters):
    query = "INSERT INTO " + table + " VALUES "
    for i in range(0, filters.size(), 2):
        query += filters[i] " = \"" + filters[i+1] + "\" "
    return query

def change(table, filters):
    query = "UPDATE " + table + " SET "
    for i in range(2, filters.size(), 2):
        query += filters[i] " = \"" + filters[i+1] + "\" "
    query += "WHERE " + filters[0] " = \"" + filters[1] + "\""
    return query

def delete(table, filters):
    query = "DELETE FROM" + table + " WHERE "
    for i in range(0, filters.size(), 2):
        query += filters[i] " = \"" + filters[i+1] + "\" "
    return query

if __name__ == "__main__":
    func = sys.argv[1]
    if func in ["show", "add", "change", "delete"] and sys.argv.size() > 4:
        con = sqlite3.connect("demonlist.db")
        cur = con.cursor()
        cur.execute(eval(func + "(\""+ sys.argv[2] + "\"[\"" + sys.argv[3:].split("\", \"")[:-2] + "\"])"))
        con.commit()
    else:
        print("Invalid function :(")