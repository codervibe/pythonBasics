import json
import random
import requests
import os
from datetime import datetime

# 从环境变量中读取API URL和Cookie信息
api_url = os.getenv('BILIBILI_API_URL', 'https://api.bilibili.com/x/v2/reply/wbi/main?oid=113655756687306&type=1&mode=2&pagination_str=%7B%22offset%22:%22%22%7D&plat=1&seek_rpid=&web_location=1315875&w_rid=e4daf57743e496a55b309acfdd0a9e71&wts=1734759477')
cookie = os.getenv('BILIBILI_COOKIE', 'buvid3=7C93E44A-C719-6970-D124-BC5EF99BF56951575infoc; b_nut=1716979951; _uuid=666D6255-BEF2-31E9-ADA10-8493AECFE103567005infoc; buvid4=6B2DB6B3-E845-7845-0D7D-0B2F894E4C0387063-024052910-IFYHw%2B%2B0jr49dnp%2FUT8KwA%3D%3D; enable_web_push=DISABLE; rpdid=|(kJk|R~lkR0J\'u~u~R|kR~J; header_theme_version=CLOSE; buvid_fp_plain=undefined; hit-dyn-v2=1; LIVE_BUVID=AUTO2917233493264529; DedeUserID=544166891; DedeUserID__ckMd5=ed1a512ca38f5634; fingerprint=68f1dd695365b2fefe6aa752774377d7; buvid_fp=68f1dd695365b2fefe6aa752774377d7; browser_resolution=1280-639; home_feed_column=4; CURRENT_FNVAL=16; PVID=3; CURRENT_QUALITY=64; bp_t_offset_544166891=1011755657688252416; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzQ4NjAxNDgsImlhdCI6MTczNDYwMDg4OCwicGx0IjotMX0.JFhbpYGewyeVcvMPuf1Z_pwqRCAMc9QHvm9tZMBC078; bili_ticket_expires=1734860088; SESSDATA=723116a3%2C1750152949%2C9ebb5%2Ac2CjDXKT05CWeJb_-kaEFK6ShLafDL40CeK-as4ueBdBRq_J3eG_jzSiBE-KexQUlL5xQSVm1DempoTWxzVWFiLW1NbzJRYXRUUEYwbkNiWEh6TzhrN1JvelpFMEpTZ0pZVkE5MVVEU1o3SW4yS1RxT1k0NE56Q2c5SExJRUxxcWs4c0J3dHVPQnV3IIEC; bili_jct=3f4a6807feb2e2e6ba416b2696bbc48f;')

# User-Agent 列表，用于模拟不同的浏览器请求
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
]

# 构造请求头，包含随机选择的User-Agent和Cookie信息
headers = {
    'User-Agent': random.choice(user_agents),
    'Cookie': cookie
}

try:
    # 发起GET请求，获取数据
    response = requests.get(url=api_url, headers=headers)

    # 检查HTTP响应状态码
    if response.status_code == 200:
        jsonData = response.json()

        # 动态生成文件名
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        filename = f'b站评论_{timestamp}.json'

        # 将 jsonData 保存成json 文件
        with open(filename, 'w', encoding='utf-8') as f:
            # 写入文件，确保字符正确编码，且格式化输出
            json.dump(jsonData, f, ensure_ascii=False, indent=4)
        print(f"数据已成功保存到 {filename}")
    else:
        print(f"请求失败，状态码: {response.status_code}")
except requests.RequestException as e:
    print(f"请求过程中发生错误: {e}")
except json.JSONDecodeError as e:
    print(f"JSON解析失败: {e}")
except Exception as e:
    print(f"发生未知错误: {e}")
