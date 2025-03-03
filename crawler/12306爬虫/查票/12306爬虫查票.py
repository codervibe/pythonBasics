import random
from prettytable import PrettyTable
import requests

# 定义API URL，此处的URL为12306查询票务信息的接口地址
API_URL = (
    "https://kyfw.12306.cn/otn/leftTicket/queryO?leftTicketDTO.train_date=2024-12-19&leftTicketDTO."
    "from_station=BJP&leftTicketDTO.to_station=SHH&purpose_codes=ADULT")

# 定义 User-Agent 列表，用于模拟不同的浏览器请求
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.TG 短信轰炸接口.15 (KHTML, like Gecko) Version/14.TG 短信轰炸接口.2 Safari/605.TG 短信轰炸接口.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
]

# 构造请求头部，包括随机选择一个User-Agent和Cookie信息
headers = {
    'User-Agent': random.choice(user_agents),
    'Cookie': '_uab_collina=173449375088168679444499; JSESSIONID=003C9E88F16CE95CAA005B9B6C852578; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; _jc_save_fromStation=%u5317%u4EAC%2CBJP; _jc_save_toStation=%u4E0A%u6D77%2CSHH; _jc_save_wfdc_flag=dc; BIGipServerotn=1658388746.50210.0000; BIGipServerpassport=921174282.50215.0000; route=6f50b51faa11b987e576cdb301e545c4; _jc_save_fromDate=2024-12-19; _jc_save_toDate=2024-12-19'
}

# 发起GET请求，获取票务信息
response = requests.get(url=API_URL, headers=headers)

# 将响应内容解析为JSON格式
json_data = response.json()
tb = PrettyTable()
tb.field_names = ['序号', '车次', '出发时间', '到达时间', '耗时', '特等座', '一等座', '二等座', '软卧', '硬卧', '软座', '硬座', '无座', '商务座', '一等卧', '二等卧', '高级软卧']
page = 1
result = json_data.get('data').get('result')
for i in result:
    index = i.split('|')
    trainNumber = index[3]
    departureTime = index[8]
    timeOfArrival = index[9]
    timeConsuming = index[10]
    premierClass = index[32]
    firstClassSeat = index[31]
    secondClass = index[30]
    softSleeper = index[23]
    hardSleeper = index[28]
    softSeat = index[33]
    hardSeat = index[29]
    withoutSeat = index[26]
    businessClass = index[35]
    firstClassSleeping = index[34]
    secondClassBedroom = index[36]
    superiorSoftSleeper = index[37]
    dit = {
        '车次': trainNumber,
        '出发时间': departureTime,
        '到达时间': timeOfArrival,
        '耗时': timeConsuming,
        '特等座': premierClass,
        '一等座': firstClassSeat,
        '二等座': secondClass,
        '软卧': softSleeper,
        '硬卧': hardSleeper,
        '软座': softSeat,
        '硬座': hardSeat,
        '无座': withoutSeat,
        '商务座': businessClass,
        '一等卧': firstClassSleeping,
        '二等卧': secondClassBedroom,
        '高级软卧': superiorSoftSleeper

    }
    tb.add_row([page, trainNumber, departureTime, timeOfArrival, timeConsuming, premierClass, firstClassSeat, secondClass, softSleeper, hardSleeper, softSeat, hardSeat, withoutSeat, businessClass, firstClassSleeping, secondClassBedroom, superiorSoftSleeper])
    page += 1
    # print(dit)

print(tb)

