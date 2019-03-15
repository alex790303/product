# 讀取檔案
product = []
with open('products.csv', 'r', encoding = 'utf-8') as f: #編碼讀取跟寫入要相同
	for line in f:
		if '商品,價格' in line:
			continue #跳到下一步
		name, price = line.strip().split(',') #split(切割）','為切割標準 .strip(去掉換行)
		product.append([name, price])
print(product)

#讓使用者輸入
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

#印出所有購買紀錄
for p in product:
	print(p[0], '的價格是', p[1])

#寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for p in product:
		f.write(p[0] + ',' + p[1] + '\n')