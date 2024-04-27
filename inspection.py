from hanspell import spell_checker

p = ""
re = ""
im = ""
end = 0
Inindex = input(str("검사할 문장을 입력하세요!"))
Inindex += "/////"

test = '''새로운데이터가 주어졌을 때 (빨간 점) 이를 Class A로 분류할지, Class B로 분류할지 판단하는 문제입니다. k=3일 때, 즉 안 쪽 원을 먼저 살펴보겠습니다. k가 3이라는 것은 가장 가까운 주변의 3개 데이터를 본 뒤, 3개의 주변 데이터가 더 많이 포함되어 있는 범주로 분류하겠다는 것입니다. 빨간 점 주변에 노란색 점(Class A) 1개와 보라색 점(Class B) 2개가 있습니다. 따라서 k=3 일 때는 해당 데이터가 Class B (보라색 점)으로 분류됩니다. k=6일 때를 보겠습니다. 원이 더 커졌습니다. 이제 원 안에 노란색 점 4개와 보라색 점 2개가 있습니다. 따라서 k=6일 때는 노란색 점으로 분류합니다. KNN은 K를 어떻게 정하냐에 따라 결과 값이 바뀔 수 있습니다. K가 너무 작아서도 안 되고, 너무 커서도 안 됩니다. K의 default 값은 5입니다. 가장 가까운 주변 5개 데이터를 기반으로 분류한다는 것입니다. 일반적으로 K는 홀수를 사용합니다/////'''
for i in test:
    p += i
    if len(p) >= 499:
        im = spell_checker.check(p)
        p = im.checked
        re += p
        p = ""
    if i == "/":
        end += 1
        if end == 4:
            im = spell_checker.check(p)
            p = im.checked
            re += p
            p = ""
    else:
        end = 0
re = re.replace("////", "").strip()
print(re)
f = open("1.txt", 'w+' , encoding="utf8")
f.write(re)
f.close()