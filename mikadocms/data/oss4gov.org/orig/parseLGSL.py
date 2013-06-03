

import csv
    
csvfile = open("englishAndWelshServices.csv")
fo = open("lgsl.rst", "wb")
def brute(txt):
    out = ''
    for ltr in txt:
        if ord(ltr)>127: continue
        out += ltr
    return out
    
hdrs = ["Identifier","Label","Description","Created","Modified","History notes","Type"]
rdr = csv.DictReader(csvfile, hdrs)
for row in rdr:
    ID, label, desc = (row["Identifier"],
                       row["Label"],
                       row["Description"])
    fo.write("    <tr><td>%s-%s</td><td>%s</td></tr>" % (ID, brute(label), brute(desc)))

fo.close()