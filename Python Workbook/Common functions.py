def int_input(string):
    while True:
        try:
            int(input(string))
            break
        except ValueError:
            print("Enter numerical value.")
        except:
            print("I'm speechless...")
        
def float_input(string):
    while True:
        try:
            float(input(string))
            break
        except ValueError:
            print("Enter numerical value.")
        except:
            print("I'm speechless...")
        
