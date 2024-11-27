f = input("give me the formulla: """)
if len(f) != 9:
    print ("please give a valid quadratic formula")
    quit()
else:
    pass

x2 = f.find("x^2")
x = f.find("x")

print(x2)

a = f[0]
b = f[5]
c = f[8]

