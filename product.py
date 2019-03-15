product = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格:')	
	p = [name, price]
	#p = []
	#p.append(name)
	#p.append(price)
	product.append(p)
print(product)	

for p in product:
	print(p[0], '的價格是', p[1])