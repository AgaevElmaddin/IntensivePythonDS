import sys


def get_dict_key(dict, value_dict):
	for key_dict,val_dict in dict.items():
		if value_dict == val_dict:
			return key_dict


def ticker_symbols():
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
	if len(sys.argv) != 2:
		return
	company_stocks_name = sys.argv[1].upper()
	if company_stocks_name not in STOCKS:
		print('Unknown ticker')
		return
	print(get_dict_key(COMPANIES, company_stocks_name), STOCKS[company_stocks_name])


if __name__ == '__main__':
	ticker_symbols()