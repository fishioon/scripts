import requests

def send_phone_msg(phone):
    url = 'http://www.zigeer.com/Account/SendCaptcha'
    data = { 'mobile': phone, 'type': 1}
    r = requests.post(url, data)

def praise(num):
    url = 'http://newweixin.zigeer.com/Angel/Praise/'
    data = { 'pid': '2641', 'tk': 'c83956270105014bed27ce4a2b71c91a' }
    wechat_token = "OezXcEiiBSKSxW0eoylIeExakgRXKtV5gbLXEGw-YQj3JgcXGeoBBevyV2dHd8koQYTMuq3kxlEo6skkMTTKFfG32QIr47mZA2_t2GNKi-baHmwT5Wl3FmJZbcraHqXGqCmozr1H6Z1cMIXWvmjnFg"
    wechat_id = "oSzUVs4O4qPt_sswL86ApOj_2FrI" + num;
    cookies = cookies = dict(zigeer_wechat_access_token=wechat_token,
            zigeer_wechat_openid=wechat_id)
    r = requests.post(url, data, cookies=cookies)
    print r.json()

if __name__ == '__main__':
    # send_phone_msg('18651692880')
    for num in range(100,1000):
        praise(str(num));



