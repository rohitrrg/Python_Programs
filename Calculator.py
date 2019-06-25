print("\n****************************** CALCULATOR ******************************")
print('\nInstructions to use calculator:-\n'
      '1. Initially enter first operand then operator and then second operand\n'
      '2. After every input press ENTER\n'
      '3. Enter "q" as a operator to EXIT\n'
      '************************************************************************\n')
a = float(input())
i = 0
while 1 == 1:
    o = input()
    if o == 'q':
        break
    else:
        b = float(input())
        try:
            if o == "+":
                a = a + b
                print("-------")
            elif o == "-":
                a = a - b
                print("-------")
            elif o == "*":
                a = a * b
                print("-------")
            elif o == "/":
                    a = a / b
                    print("-------")
            else:
                print(" Invalid Operator...please try again !!")
        except Exception as e:
            print(e)

        print(" ", a)
        i = i + 1