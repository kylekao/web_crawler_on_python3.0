#輸入網址後直接跑出題目#
from pyquery import PyQuery
x=input("add ")
html=PyQuery(x)
title = html('hl.last_crumbs').text()
q = html('div.question_option').text()
answer =html('div.left.correctAnswer').text()

print(title)
print(q)
print(answer)