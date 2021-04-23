
class Solution(object):
	def currencyConverter(self, convertionRates, conveters):
		self.d = {}
		for currency in convertionRates:
			if currency[0] not in self.d:
				temp1 = {}
				temp1[currency[1]] = currency[2]
				self.d[currency[0]] = temp1
			else:
				self.d[currency[0]][currency[1]] = currency[2]
			if currency[1] not in self.d:
				temp2 = {}
				temp2[currency[0]] = 1/currency[2]
				self.d[currency[1]] = temp2
			else:
				self.d[currency[1]][currency[0]] = 1/currency[2]
		self.res = []
		# print(self.d)
		for c in conveters:
			self.found = False
			self.visited = set()
			self.dfs(c[0],c[1],1.0)
			if not self.found:
				self.res.append(-1.0)
		return self.res

	def dfs(self, fromCurrency, toCurrency, convertionRate):
		if fromCurrency in self.d and toCurrency in self.d:
			self.visited.add(fromCurrency)
			for child in self.d[fromCurrency].keys():
				if child in self.visited:
					continue
				# print(fromCurrency)
				# print(child)
				# print(toCurrency)
				# print("------")
				rate = self.d[fromCurrency][child]*convertionRate
				if toCurrency == child:
					self.res.append(rate)
					self.found = True
					return
				self.dfs(child, toCurrency, rate)
		else:
			self.res.append(-1.0)
		return
        
param = Solution()
convertionRates = [['USD', 'GBP', 0.79], ['USD', 'YEN', 106.92], ['YEN', 'EUR', 0.0083], ['DIN','INR', 6.6]]
conveters = [['GBP','EUR'],['EUR','USD'],['YEN','INR']]
print(param.currencyConverter(convertionRates, conveters))


