P=int(input())
discount1=P*0.1 
discount2=100
max_discount=max(discount1,discount2)
final_amount=P-max_discount
print(int(final_amount))
