x = input()
x = int(x)
y = 0
if x>500:
    y = pow(int(x),2) + pow(int(x),8)*0.15
elif int(x)<500:
    y = int(x) + 15
else:
    print("Ну якось так")
print(y)