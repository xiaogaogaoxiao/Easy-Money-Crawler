import requests
import pandas as pd
import json

stocks = ['000998.SZ', '600265.SH', '002556.SZ', '002385.SZ', '000713.SZ', '002714.SZ', '002891.SZ', '600371.SH', '600598.SH', '000860.SZ', '600354.SH', '600506.SH', '601952.SH', '600313.SH', '603668.SH', '603336.SH', '300189.SZ', '600108.SH', '002746.SZ', '002041.SZ', '002157.SZ', '601118.SH', '002311.SZ', '300498.SZ', '002299.SZ', '002696.SZ', '002124.SZ', '600359.SH', '002086.SZ', '002240.SZ', '600076.SH', '300094.SZ', '300106.SZ', '002200.SZ', '600275.SH', '000592.SZ', '300087.SZ', '002069.SZ', '002234.SZ', '300313.SZ', '600540.SH', '600467.SH', '600257.SH', '002679.SZ', '300262.SZ', '300761.SZ', '600097.SH', '002321.SZ', '000798.SZ', '000663.SZ', '600975.SH', '002458.SZ', '002688.SZ', '002100.SZ', '000735.SZ', '600965.SH', '603363.SH', '300511.SZ']
info_table = pd.DataFrame(columns=['name', '2019-9-30', '930主营业务收入mainBusinessIncome', '930总利润contributionMargin', '930净利润retainedProfits', '930总资产totalAssets', '930总负债totalLiabilities',
                                   '2019-6-30', '630主营业务收入mainBusinessIncome', '630总利润contributionMargin','630净利润retainedProfits', '630总资产totalAssets', '630总负债totalLiabilities',
                                   '2019-3-31', '331主营业务收入mainBusinessIncome', '331总利润contributionMargin','331净利润retainedProfits', '331总资产totalAssets', '331总负债totalLiabilities',
                                   '2018-12-31', '1231主营业务收入mainBusinessIncome', '1231总利润contributionMargin','1231净利润retainedProfits', '1231总资产totalAssets', '1231总负债totalLiabilities',
                                   '2018-9-30', '8930主营业务收入mainBusinessIncome', '8930总利润contributionMargin', '8930净利润retainedProfits', '8930总资产totalAssets', '8930总负债totalLiabilities'])

def run():
    global info_table
    global stocks

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Host': 'data.eastmoney.com'}
    url_head = 'http://data.eastmoney.com/DataCenter_V3/stockdata/cwzy.ashx?code='
    for j in range(0, len(stocks)):
        url = url_head + stocks[j]
        response = requests.get(url, headers=headers)
        response_json = json.loads(response.text)
        temp = []
        temp.append(stocks[j])
        for i in range(0, len(response_json)):
            temp.append(' ')
            temp.append(response_json[i]['mainBusinessIncome'])
            temp.append(response_json[i]['contributionMargin'])
            temp.append(response_json[i]['retainedProfits'])
            temp.append(response_json[i]['totalAssets'])
            temp.append(response_json[i]['totalLiabilities'])
        for i in range(len(temp), 31):
            temp.append(' ')
        info_table.loc[j] = temp
        print('完成了'+stocks[j])
    print(info_table)
    info_table.to_csv('第四个表.csv', encoding='gbk')

if __name__ == '__main__':
    run()