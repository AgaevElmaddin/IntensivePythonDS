import sys


def manipulation(word):
	COMPANIES = {
					'Apple': 'AAPL',
					'Microsoft': 'MSFT',
					'Netflix': 'NFLX',
					'Tesla': 'TSLA',
					'Nokia': 'NOK'
				}
	STOCKS = 	{
					'AAPL': 287.73,
					'MSFT': 173.79,
					'NFLX': 416.90,
					'TSLA': 724.88,
					'NOK': 3.37
				}
	re_dict_companies = {value: key for key, value in COMPANIES.items()}
	ticker = word.upper()
	company = word.capitalize()
	if ticker in re_dict_companies:
		print(ticker, 'is a ticker symbol for', re_dict_companies[ticker])
	elif company in COMPANIES:
		print(company, 'stock price is', STOCKS[COMPANIES[company]])
	else:
		print(word, 'is an unknown company or an unknown ticker symbol')


def all_stocks():
	if len(sys.argv) != 2:
		return
	row = sys.argv[1]
	while ' ' in row:
		row = row.replace(' ', '')
	words = row.split(',')
	if '' in words:
		return
	for word in words:
		manipulation(word)


if __name__ == '__main__':
	all_stocks()
