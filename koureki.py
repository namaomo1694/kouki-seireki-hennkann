# -*- coding: utf-8 -*-
print("西暦から皇紀は１を、皇紀から西暦は２を押してください。")
a = input (":")
if a==1:
    print("皇紀に変換したい西暦を入力してください。")
    print("紀元前の場合は-で入力してください。")
    year =input(":")
    kouki=year+660
    print("皇紀" + str(kouki) + "年です。")
elif a==2:
    print("西暦に変換したい皇紀を入力してください。")
    print("紀元前の場合は-で入力してください")
    year =input(":")
    seireki=year-660
    print("西暦" + str(seireki) + "年です。")
else: 
    print("エラー")
    print("1または2を入力してください。")

