list = ["banana", "apple", "malina"]
text = open("txtfile.txt", "w")
text.write(", ".join(list))