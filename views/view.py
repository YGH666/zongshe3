import json
from flask import Flask, render_template, request, Blueprint
import smtplib
import random
import time
from email.mime.text import MIMEText
from email.utils import formataddr

analysis = Blueprint('webaccess', __name__)

@analysis.route('/')
def hello_world():
    return 'Hello World!'


@analysis.route('/login')
def login():
    return render_template("login.html")


@analysis.route('/index1')
def index1():
    return render_template("index1.html")


@analysis.route('/details')
def details():
    return render_template("details.html")

@analysis.route('/company')
def company():
    return render_template("company.html")

@analysis.route('/cookie')
def cookie():
    return render_template("cookie.html")


@analysis.route('/get_table', methods=["GET"])
def get_tabledata():
        # data_item = {"code":0,"msg":"","count":30,"data":[{"id":10000,"username":"user-0","sex":"女","city":"城市-0","sign":"签名-0","experience":255,"logins":24,"wealth":82830700,"classify":"作家","score":57},{"id":10001,"username":"user-1","sex":"男","city":"城市-1","sign":"签名-1","experience":884,"logins":58,"wealth":64928690,"classify":"词人","score":27},{"id":10002,"username":"user-2","sex":"女","city":"城市-2","sign":"签名-2","experience":650,"logins":77,"wealth":6298078,"classify":"酱油","score":31},{"id":10003,"username":"user-3","sex":"女","city":"城市-3","sign":"签名-3","experience":362,"logins":157,"wealth":37117017,"classify":"诗人","score":68},{"id":10004,"username":"user-4","sex":"男","city":"城市-4","sign":"签名-4","experience":807,"logins":51,"wealth":76263262,"classify":"作家","score":6},{"id":10005,"username":"user-5","sex":"女","city":"城市-5","sign":"签名-5","experience":173,"logins":68,"wealth":60344147,"classify":"作家","score":87},{"id":10006,"username":"user-6","sex":"女","city":"城市-6","sign":"签名-6","experience":982,"logins":37,"wealth":57768166,"classify":"作家","score":34},{"id":10007,"username":"user-7","sex":"男","city":"城市-7","sign":"签名-7","experience":727,"logins":150,"wealth":82030578,"classify":"作家","score":28},{"id":10008,"username":"user-8","sex":"男","city":"城市-8","sign":"签名-8","experience":951,"logins":133,"wealth":16503371,"classify":"词人","score":14},{"id":10009,"username":"user-9","sex":"女","city":"城市-9","sign":"签名-9","experience":484,"logins":25,"wealth":86801934,"classify":"词人","score":75},{"id":10010,"username":"user-10","sex":"女","city":"城市-10","sign":"签名-10","experience":1016,"logins":182,"wealth":71294671,"classify":"诗人","score":34},{"id":10011,"username":"user-11","sex":"女","city":"城市-11","sign":"签名-11","experience":492,"logins":107,"wealth":8062783,"classify":"诗人","score":6},{"id":10012,"username":"user-12","sex":"女","city":"城市-12","sign":"签名-12","experience":106,"logins":176,"wealth":42622704,"classify":"词人","score":54},{"id":10013,"username":"user-13","sex":"男","city":"城市-13","sign":"签名-13","experience":1047,"logins":94,"wealth":59508583,"classify":"诗人","score":63},{"id":10014,"username":"user-14","sex":"男","city":"城市-14","sign":"签名-14","experience":873,"logins":116,"wealth":72549912,"classify":"词人","score":8},{"id":10015,"username":"user-15","sex":"女","city":"城市-15","sign":"签名-15","experience":1068,"logins":27,"wealth":52737025,"classify":"作家","score":28},{"id":10016,"username":"user-16","sex":"女","city":"城市-16","sign":"签名-16","experience":862,"logins":168,"wealth":37069775,"classify":"酱油","score":86},{"id":10017,"username":"user-17","sex":"女","city":"城市-17","sign":"签名-17","experience":1060,"logins":187,"wealth":66099525,"classify":"作家","score":69},{"id":10018,"username":"user-18","sex":"女","city":"城市-18","sign":"签名-18","experience":866,"logins":88,"wealth":81722326,"classify":"词人","score":74},{"id":10019,"username":"user-19","sex":"女","city":"城市-19","sign":"签名-19","experience":682,"logins":106,"wealth":68647362,"classify":"词人","score":51},{"id":10020,"username":"user-20","sex":"男","city":"城市-20","sign":"签名-20","experience":770,"logins":24,"wealth":92420248,"classify":"诗人","score":87},{"id":10021,"username":"user-21","sex":"男","city":"城市-21","sign":"签名-21","experience":184,"logins":131,"wealth":71566045,"classify":"词人","score":99},{"id":10022,"username":"user-22","sex":"男","city":"城市-22","sign":"签名-22","experience":739,"logins":152,"wealth":60907929,"classify":"作家","score":18},{"id":10023,"username":"user-23","sex":"女","city":"城市-23","sign":"签名-23","experience":127,"logins":82,"wealth":14765943,"classify":"作家","score":30},{"id":10024,"username":"user-24","sex":"女","city":"城市-24","sign":"签名-24","experience":212,"logins":133,"wealth":59011052,"classify":"词人","score":76},{"id":10025,"username":"user-25","sex":"女","city":"城市-25","sign":"签名-25","experience":938,"logins":182,"wealth":91183097,"classify":"作家","score":69},{"id":10026,"username":"user-26","sex":"男","city":"城市-26","sign":"签名-26","experience":978,"logins":7,"wealth":48008413,"classify":"作家","score":65},{"id":10027,"username":"user-27","sex":"女","city":"城市-27","sign":"签名-27","experience":371,"logins":44,"wealth":64419691,"classify":"诗人","score":60},{"id":10028,"username":"user-28","sex":"女","city":"城市-28","sign":"签名-28","experience":977,"logins":21,"wealth":75935022,"classify":"作家","score":37},{"id":10029,"username":"user-29","sex":"男","city":"城市-29","sign":"签名-29","experience":647,"logins":107,"wealth":97450636,"classify":"酱油","score":27}]}
        data_item={"code":0,"msg":"","count":10,"data":[{"id":"00001","shortname":"万达","reg_place":"深圳","market_time":"1999-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"王健林"},{"id":"00005","shortname":"万达1","reg_place":"深圳1","market_time":"1989-6-12","executive":"杨晓帅"}]}
        return json.dumps(data_item)


@analysis.route('/get_interested_table', methods=["GET"])
def get_interested_table():
        data_item={"code":0,"msg":"","count":5,"data":[{"id":"01010","shortname":"万达"},{"id":"01010","shortname":"万达"},{"id":"01010","shortname":"万达"},{"id":"01010","shortname":"万达"},{"id":"01010","shortname":"万达"}]}
        return json.dumps(data_item)


@analysis.route('/get_top10member_table', methods=["GET"])
def get_top10member_table():
        data_item={"code":0,"msg":"","count":10,"data":[{"ranking":"1","membertname":"杨国豪","sharehold_num":"2010","sharehold_pro":"20%","nature":"A股"},{"ranking":"1","membertname":"杨国豪","sharehold_num":"2010","sharehold_pro":"20%","nature":"A股"},{"ranking":"2","membertname":"杨国豪","sharehold_num":"2010","sharehold_pro":"20%","nature":"A股"},{"ranking":"3","membertname":"杨国豪","sharehold_num":"2010","sharehold_pro":"20%","nature":"A股"},{"ranking":"4","membertname":"杨国豪","sharehold_num":"2010","sharehold_pro":"20%","nature":"A股"},{"ranking":"5","membertname":"杨国豪","sharehold_num":"2010","sharehold_pro":"20%","nature":"A股"},{"ranking":"6","membertname":"杨国豪","sharehold_num":"2010","sharehold_pro":"20%","nature":"A股"},{"ranking":"7","membertname":"杨国豪","sharehold_num":"2010","sharehold_pro":"20%","nature":"A股"},{"ranking":"8","membertname":"杨国豪","sharehold_num":"2010","sharehold_pro":"20%","nature":"A股"},{"ranking":"9","membertname":"杨国豪","sharehold_num":"2010","sharehold_pro":"20%","nature":"A股"}]}
        return json.dumps(data_item)


@analysis.route('/get_sharesstruct_table', methods=["GET"])
def get_sharesstruct_table():
        data_item={"code":0,"msg":"","count":5,"data":[{"change_date":"2017-5-5","change_reason":"定期报告","total_shares":"2002","liutong_shares":"32132.2251","limite_shares":"8.6122"},{"change_date":"2017-1-5","change_reason":"定期报告","total_shares":"2002","liutong_shares":"32132.2251","limite_shares":"8.6122"},{"change_date":"2017-5-30","change_reason":"定期报告","total_shares":"2002","liutong_shares":"32132.2251","limite_shares":"8.6122"},{"change_date":"2017-5-7","change_reason":"定期报告","total_shares":"2002","liutong_shares":"32132.2251","limite_shares":"8.6122"},{"change_date":"2017-6-5","change_reason":"定期报告","total_shares":"2002","liutong_shares":"32132.2251","limite_shares":"8.6122"},]}
        return json.dumps(data_item)


@analysis.route('/getrandom', methods=["GET"])
def getrandom():
        return str(random.random())


@analysis.route('/company_gaikuang', methods=["GET"])
def company_gaikuang():
    strtime=time.strftime("%Y-%m-%d");
    data={"birthday":"1999-6-26","email":"841219366@qq.com","marketday":"2010-10-1","telephone":"1212121212","website":"www.baidu.com","fax":"0755-11201","registeraddress":"qjdkjaksnkcakcnzk","workaddress":"1as1d2a1d21as2d1a","shortname":"顺丰控股","code":"E12010","sub-trend-value":"48.19","time":strtime,"todayopen":"48.10","yesterdatclose":"47.20","maxx":"48.20","minn":"47.30","dealaccount":"245.2万","dealmonney":"1.02亿","zhenfu":"2.0%","huanshou":"0.6%","shiying":"6","shijing":"60","year":"10年","chairman":"杨国豪","generalmanager":"杨国豪","financialofficer":"杨国豪","secretary":"杨国豪","member":"杨国豪"}
    return json.dumps(data)


@analysis.route('/sendemailcode',methods=['POST'])
def sendemailcode():
    data = json.loads(request.form.get('data'))
    my_user =str(data['value'])

    checkcode = ''
    for i in range(5):
        current = random.randrange(0, 4)
        if current == i:
            tep = chr(random.randint(65, 90))
        else:
            tep = random.randint(0, 9)
        checkcode += str(tep)

    my_sender = '841219366@qq.com'  # 发件人邮箱账号
    my_pass = 'hfuflrpbcehnbeib'  # 发件人邮箱的授权码
    my_message='您的验证码是:'+checkcode

    msg = MIMEText(my_message, 'plain', 'utf-8')
    msg['From'] = formataddr(["From nicead.top", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg['To'] = formataddr(["FK", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
    msg['Subject'] = "验证码"  # 邮件的主题，也可以说是标题
    server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
    server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
    server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    server.quit()  # 关闭连接
    return checkcode
