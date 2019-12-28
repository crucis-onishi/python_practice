print("数値を入力してください")
number = int(input())
try:
    answer = 100 / number
    print(answer)
except ZeroDivisionError as e:
    print("0では割り算できません")
finally:
    print("実行終了")
