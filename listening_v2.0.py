#輸入網址後直接跑出題目#
#todo: 1.i=input('這一回有幾題？')，用range(0,i-1),最後一個為輸出script
#todo:輸入網址後把輸出內容直接存入檔案#
from pyquery import PyQuery
x=input("1→")
html=PyQuery(x)
title = html('hl.last_crumbs').text()
q = html('div.question_option').text()
answer =html('div.left.correctAnswer').text()

print(title)
print(q)
print(answer) 

if input("y/n") == str('y') or input("y/n") == str("Y"):
    m2 = input("2→ ")
    html=PyQuery(m2)
    title2 = html('hl.last_crumbs').text()
    q2 = html('div.question_option').text()
    answer2 =html('div.left.correctAnswer').text()
    print(title2)
    print(q2)
    print(answer2)
else:
    x=input("請輸入正確指令：")
    
if input("y/n?") == str('y') or input("y/n?") == str("Y"):    
    m3 = input("3→ ")
    html=PyQuery(m3)
    title3 = html('hl.last_crumbs').text()
    q3 = html('div.question_option').text()
    answer3 =html('div.left.correctAnswer').text()
    print(title3)
    print(q3)
    print(answer3)
else:
    x=input("請輸入正確指令：")

if input("y/n?") ==str("y") or input("y/n?") ==str("Y"): 
    m4 = input("4→ ")
    html=PyQuery(m4)
    title4 = html('hl.last_crumbs').text()
    q4 = html('div.question_option').text()
    answer4 =html('div.left.correctAnswer').text()
    print(title4)
    print(q4)
    print(answer4)
else:
    x=input("請輸入正確指令：")

if input("y/n?") == str("y") or input("y/n?") == str("Y"):  
    m5 = input("5→ ")
    html=PyQuery(m5)
    title5 = html('hl.last_crumbs').text()
    q5 = html('div.question_option').text()
    answer5 =html('div.left.correctAnswer').text()
    print(title5)
    print(q5)
    print(answer5)
else:
    article = html('div.ielts_listen_review_scroll.newscrollHeight.nano.customize-style-scroll.js_lexicon').text()
    print('\n')
    print('script')
    print(article)

if input("y/n?") == str("y") or input("y/n?") == str("Y"): 
    m6 = input("6→ ")
    html=PyQuery(m6)
    title6 = html('hl.last_crumbs').text()
    q6 = html('div.question_option').text()
    answer6 =html('div.left.correctAnswer').text()
    print(title6)
    print(q6)
    print(answer6)
    article = html('div.ielts_listen_review_scroll.newscrollHeight.nano.customize-style-scroll.js_lexicon').text()
    print('\n')
    print('script')
    print(article)
else:
    article = html('div.ielts_listen_review_scroll.newscrollHeight.nano.customize-style-scroll.js_lexicon').text()
    print('\n')
    print('script')
    print(article)