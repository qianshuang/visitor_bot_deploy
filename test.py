# -*- coding: utf-8 -*-

query = "aaaaa"
print(query.split(" ")[-1])
print(query.split(" ")[:-1])

pres_fuzzy = " ".join([w + "~2" for w in []])
print(pres_fuzzy)
