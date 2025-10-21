# Bill Splitter Project

while True:
    print("\n--- Bill Splitter ---")
    amounts = []
    
    print("Enter item amounts one by one (press Enter without value to stop):")
    
    while True:
        item = input("Enter amount: ")
        if item == "":   # agar user sirf Enter press kare
            break
        else:
            amounts.append(float(item))   # list me add karna
    
    if not amounts:   # agar kuch bhi add nahi hua
        print("No items entered!")
        continue
    
    total = sum(amounts)
    print("\nTotal Amount =", total)
    
    persons = int(input("Enter number of persons: "))
    
    if persons > 0:
        per_person = total / persons
        print("Amount per person =", per_person)
    else:
        print("Number of persons must be greater than 0!")

    # fir se chalane ke liye
    again = input("\nDo you want to calculate again? (yes/no): ")
    if again.lower() != "yes":
        print("Thank you! 🙌")
        break
