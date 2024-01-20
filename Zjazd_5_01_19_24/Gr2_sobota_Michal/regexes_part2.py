import re

text = "Kupilem dzisiaj 2 arbuzy. Były przeterminowane. Rzygalem 5 razy."


matches = re.findall(r"((\W|^)\w+em\W)", text)
print(matches)
