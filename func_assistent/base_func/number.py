int_text_1 = {
0:	"",
1:	"один",
2:	"два",
3:	"три",
4:	"четыре",
5:	"пять",
6:	"шесть",
7:	"семь",
8:	"восемь",
9:	"девять",
}
int_text_10 = {
10:"десять",
11:"одиннадцать",
12:"двенадцать",
13:"тринадцать",
14:"четырнадцать",
15:"пятнадцать",
16:"шестнадцать",
17:"семнадцать",
18:"восемнадцать",
19:"девятнадцать",
20:"двадцать",
30:"тридцать",
40:"сорок",
50:"пятьдесят",
60:"шестьдесят",
70:"семьдесят",
80:"восемьдесят",
90:"девяносто",
}
int_text_100 = {
100:"сто",
200:"двести",
300:"триста",
400:"четыреста",
500:"пятьсот",
600:"шестьсот",
700:"семьсот",
800:"восемьсот",
900:"девятьсот",
}
int_text_1000 = {
1000:"тысяча",
2000:"две тысячи",
3000:"три тысячи",
4000:"четыре тысячи",
5000:"пять тысяч",
6000:"шесть тысяч",
7000:"семь тысяч",
8000:"восемь тысяч",
9000:"девять тысяч",
10000:"десять тысяч",
}


def int_translate_text(text):
    try:
        num = int(text)
    except ValueError:
        num = int("".join([i for i in text if i.isdigit()]))
    n1 = num % 10
    n2 = int(str(num % 100 // 10) + "0")
    n3 = int(str(num % 1000 // 100) + "00")
    n4 = int(str(num // 1000) + "000")
    if num < 10:
        return int_text_1.get(num)
    elif 10 <= num <= 20:
        return int_text_10.get(num)
    elif 20 < num < 100:
        return " ".join([int_text_10.get(n2), int_text_1.get(n1)])
    elif 100 < num < 1000:
        return " ".join([int_text_100.get(n3), int_text_10.get(n2), int_text_1.get(n1)])
    else:
        return " ".join([int_text_1000.get(n4), int_text_100.get(n3), int_text_10.get(n2), int_text_1.get(n1)])
