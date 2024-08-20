def median(lst):
    quotient, remainder = divmod(len(lst), 2)
    if remainder:
        return sorted(lst)[quotient]
    return sum(sorted(lst)[quotient - 1:quotient + 1]) / 2
    
lst = []
  
n = int(input("Digite o número de elementos: "))
  
for i in range(0, n):
    ele = int(input())
  
    lst.append(ele) 
      
print(lst)

print(median(lst))