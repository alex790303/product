#搜尋檔案
import os # os = operating sysytem作業系統

# 讀取檔案
def read_file(filename):
	product = []
	with open(filename, 'r', encoding = 'utf-8') as f: #編碼讀取跟寫入要相同
		for line in f:
			if '商品,價格' in line:
				continue #跳到下一步
			name, price = line.strip().split(',') #split(切割）','為切割標準 .strip(去掉換行)
			product.append([name, price])
	return product

#讓使用者輸入
def user_input(product):
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
	return product

#印出所有購買紀錄
def print_products(product):
	for p in product:
		print(p[0], '的價格是', p[1])

#寫入檔案
def write_file(filename, product):
	with open(filename, 'w', encoding = 'utf-8') as f:
		f.write('商品,價格\n')
		for p in product:
			f.write(p[0] + ',' + p[1] + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename): #檢查檔案
		print('有')
		product = read_file(filename)
		print(product)	
	else:
		print('找不到檔案')

	product = user_input(product)
	print_products(product)
	write_file('products.csv', product)

main()