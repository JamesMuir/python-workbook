def int_input(string):
    while True:
        try:
            number = int(input(string))
            break
        except ValueError:
            print("Enter numerical value.")
        except:
            print("I'm speechless...")
    return number
        
def float_input(string):
    while True:
        try:
            number = float(input(string))
            break
        except ValueError:
            print("Enter numerical value.")
        except:
            print("I'm speechless...")
    return number
