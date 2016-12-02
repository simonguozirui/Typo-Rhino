file = open("lewa.txt")
article =  str(file.readlines())
file.close()
list0 = article.split(" ") 

print list0

value = True
print value
value = not value
print value
value = not value
print value
