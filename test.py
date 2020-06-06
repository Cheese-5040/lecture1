largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : 
        break
    try: 
        num = int(num)
    except Exception:
        print ("Invalid input")
    if largest== None and smallest == None:
        largest= num
        smallest=num
    elif type(num) is int and num > largest :
        largest=num
    elif type(num) is int and num < smallest: 
        smallest=num 
    
    #print(largest)

    #print(smallest)
print("Maximum", largest)
print("Minimum",smallest)