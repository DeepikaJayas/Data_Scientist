def find(price, eps, book):
pe = price/eps
pb = price/book
return pe, pb
x = find(100, 2, 4)
x
