actual_cost = float(input('enter the actual cost of the product:'))
sell_cost = float(input('enter the sell price of the product:'))

if sell_cost < actual_cost:
    profit = sell_cost - actual_cost
    print('the profit of this product is:', profit)
    
else:
    loss = actual_cost - sell_cost
    print('the loss of this product is:', loss)