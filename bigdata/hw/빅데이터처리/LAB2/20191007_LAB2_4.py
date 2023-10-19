#LAB2_4
market = [['A_market', 33, 30, 13550],
          ['B_market', 35, 24, 15960],
          ['C_market', 30, 33, 11990]]
A_price = market[0][3] / market[0][2] / market[0][1]
B_price = market[1][3] / market[1][2] / market[1][1]
C_price = market[2][3] / market[2][2] / market[2][1]
if A_price <= B_price and A_price <= C_price:
  min_market = market[0][0]
elif B_price <= A_price and B_price <= C_price:
  min_market = market[1][0]
elif C_price <= A_price and C_price <= B_price:
  min_market = market[2][0]
min_price = min(A_price, B_price, C_price)
print('{}이 1m당 {:.2f}으로 최저가이다'.format(min_market, min_price))