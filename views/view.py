import json
from flask import Flask, render_template, request, Blueprint, make_response
import smtplib
import random
import time
import pymysql
from email.mime.text import MIMEText
from email.utils import formataddr
from flask_uploads import configure_uploads,UploadSet
import os,base64

analysis = Blueprint('webaccess', __name__)


def getConn():
    conn = pymysql.connect(host='192.168.182.130', port=3306, database='test_db',
                               user='YgH1',
                               password='YgH1@513!', charset='utf8')
    return conn


@analysis.route('/')
def hello_world():
    return render_template("index1.html")


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


@analysis.route('/user')
def user():
    return render_template("user.html")


@analysis.route('/imageupdate')
def imageupdate():
    return render_template("imageupdate.html")


Basepath=os.path.abspath(os.path.dirname('static'))


@analysis.route('/upload',methods=['POST'])
def upload_img():
    if request.method=="POST":
        data = json.loads(request.form.get('data'))
        # 获取用户名
        username = str(data['username'])
        #辨别操作
        handle = str(data['handle'])
        # 获取图片
        if handle=='post':
            img=request.files.get('file')
            picname =username+"."+"jpg"
            # +str(img.filename).split(".")[-1]
            path=Basepath+'/static/upload/'
            img_path=path+picname
            # print(img_path)
            img.save(img_path)
            with open(img_path, 'rb') as f:
                img = base64.b64encode(f.read()).decode()
            return json.dumps({"code": 0, "msg": "", "data": {"src": img}})

        else:
            picname = username + "." + "jpg"
            moren_picname="moren.jpg"
            # +str(img.filename).split(".")[-1]
            path = Basepath + '/static/upload/'

            img_path = path + picname
            moren_path = path+moren_picname
            # print(img_path)
            if os.path.exists(img_path):
                with open(img_path, 'rb') as f:
                    img = base64.b64encode(f.read()).decode()
                # data_item = {img}
                return json.dumps(img)
            else:
                with open(moren_path, 'rb') as f:
                    img = base64.b64encode(f.read()).decode()
                # data_item = {img}
                return json.dumps(img)


@analysis.route('/download_img', methods=['POST'])
def download_img():
        data = json.loads(request.form.get('data'))
        # 获取用户名
        username = str(data['username'])
        return json.dumps({"res":username})


@analysis.route('/get_table', methods=["POST"])
def get_tabledata():
        limit = request.form.get("limit")
        page = request.form.get("page")
        print("limit= "+limit+" , page="+page)
        data = json.loads(request.form.get('data'))
        keyword = str(data['value'])

        conn=getConn()
        cs1 = conn.cursor()
        sql2 = "SELECT stock_code,stock_abbre,province,listing_date,industry_classification FROM listed_company3 "
        cs1.execute(sql2)
        data = []
        alldata = cs1.fetchall()
        for s in alldata:
            code = str(s[0]).zfill(6)
            if keyword in code or keyword in s[1] or keyword in s[2] or keyword in s[3] or keyword in s[4]:
                list_item = {"id": code, "shortname": s[1], "reg_place": s[2], "market_time": s[3], "executive": s[4]}
                data.append(list_item)
        # print(data)

        count=len(data)
        data=data[int(limit)*(int(page)-1):int(limit)*int(page)+1]
        cs1.close()
        conn.close()
        data_item={"code":0,"msg":"","count":count,"data":data}
        return json.dumps(data_item)


@analysis.route('/get_interested_table', methods=["GET"])
def get_interested_table():
        conn=getConn()
        cs1 = conn.cursor()
        sql2 = "SELECT stock_code,stock_abbre,province,listing_date,industry_classification FROM listed_company3 "
        cs1.execute(sql2)
        data = []
        alldata = cs1.fetchall()
        for s in alldata:
            code = str(s[0]).zfill(6)
            list_item = {"id": code, "shortname": s[1]}
            data.append(list_item)
        interesting_item=[]
        for x in range(10):
            interesting_item.append(data[random.randint(0, len(data))])

        cs1.close()
        conn.close()

        data_item={"code":0,"msg":"","count":5,"data":interesting_item}
        return json.dumps(data_item)


@analysis.route('/get_caiwufengxi_data',methods=["POST"])
def get_caiwufengxi_data():
    data = json.loads(request.form.get('data'))
    code = str(data['code'])
    season = str(data['season'])
    conn = getConn()
    cs1 = conn.cursor()
    sql2 = "SELECT * FROM lr_%s" % code + "_%s" % season
    cs1.execute(sql2)
    s = cs1.fetchall()
    data_list = []

    title = []
    final_data = []
    for x in s:
        data_list_1 = []
        for y in x:
            data_list_1.append(y)
        data_list.append(data_list_1)

    # print(data_list)
    title.append(data_list[0][0])
    title.append(data_list[2][0])
    title.append(data_list[3][0])

    sql3 = "SELECT * FROM zcfz_%s" % code + "_%s" % season
    cs1.execute(sql3)
    ss = cs1.fetchall()

    data_list2 = []
    for x in ss:
        data_list_2 = []
        for y in x:
            data_list_2.append(y)
        data_list2.append(data_list_2)

    # print(data_list2)
    title.append(data_list2[4][0])
    title.append(data_list2[9][0])

    sql4 = "SELECT * FROM xjll_%s" % code + "_%s" % season
    cs1.execute(sql4)
    sss = cs1.fetchall()

    data_list3 = []
    for x in sss:
        data_list_3 = []
        for y in x:
            data_list_3.append(y)
        data_list3.append(data_list_3)
    # print(data_list3)
    title.append(data_list3[0][0])
    title.append(data_list3[1][0])
    title.append(data_list3[2][0])

    final_data.append(title)
    final_data.append(data_list[0][1:])
    final_data.append(data_list[2][1:])
    final_data.append(data_list[3][1:])

    final_data.append(data_list2[4][1:])
    final_data.append(data_list2[9][1:])

    final_data.append(data_list3[0][1:])
    final_data.append(data_list3[1][1:])
    final_data.append(data_list3[2][1:])

    # print(final_data)
    cs1.close()
    conn.close()
    return json.dumps(final_data)


@analysis.route('/get_top10member_table', methods=["POST"])
def get_top10member_table():
    data = json.loads(request.form.get('data'))
    code = str(data['code'])
    datetype=str(data['datetype'])
    conn = getConn()
    cs1 = conn.cursor()
    sql2 = "SELECT * FROM first_ten_%s" % code
    cs1.execute(sql2)
    s = cs1.fetchall()
    data_list = []
    for x in s:
        if x[0] == datetype:
            data_item = {"ranking": x[1], "membertname": x[2], "sharehold_num": x[3], "sharehold_pro": x[4],
                         "nature": x[5]}
            data_list.append(data_item)

    data_return = {"code": 0, "msg": "", "count": 5, "data": data_list}
    # print(data_return)
    return json.dumps(data_return)


@analysis.route('/get_sharesstruct_table', methods=["POST"])
def get_sharesstruct_table():
        data = json.loads(request.form.get('data'))
        code = str(data['value'])
        conn = getConn()
        cs1 = conn.cursor()
        sql2 = "SELECT * FROM shares_struct where stock_code=%s" % code
        cs1.execute(sql2)
        s = cs1.fetchall()
        data = []
        for x in s:
            list_item = {"change_date": x[2], "change_reason": x[3], "total_shares": x[4], "liutong_shares": x[5],
                         "limite_shares": x[6]}
            data.append(list_item)
        # print(data)

        cs1.close()
        conn.close()
        data_item={"code":0,"msg":"","count":5,"data": data}
        return json.dumps(data_item)


@analysis.route('/getK', methods=["POST"])
def getK():
    data = json.loads(request.form.get('data'))
    code = str(data['value'])
    conn = getConn()
    cs1 = conn.cursor()
    sql2 = "SELECT * FROM stock_%s" % code
    cs1.execute(sql2)
    s = cs1.fetchall()
    data = []
    for x in s:
        list_item = []
        list_item.append(x[0].strftime("%Y/%m/%d"))
        list_item.append(str(x[6]))
        list_item.append(str(x[3]))
        list_item.append('-')
        list_item.append('-')
        list_item.append(str(x[5]))
        list_item.append(str(x[4]))
        list_item.append('-')
        data.append(list_item)
    # print(data)

    cs1.close()
    conn.close()
    return json.dumps(data)


@analysis.route('/company_gaikuang', methods=["POST"])
def company_gaikuang():
    data = json.loads(request.form.get('data'))
    code = str(data['value'])
    # print(code)
    conn = getConn()
    cs1 = conn.cursor()
    sql2 = "SELECT * FROM company_data where stock_code=%s" % code
    cs1.execute(sql2)
    s = cs1.fetchall()[0]
    sql3 = "SELECT * FROM stock_%s" % code
    cs1.execute(sql3)
    e = cs1.fetchall()[0]

    list_item = {"code": s[1], "birthday": s[2], "email": s[3], "marketday": s[4], "telephone": s[5], "website": s[6],
                 "fax": s[7], "registeraddress": s[8], "workaddress": s[9], "chairman": s[10], "generalmanager": s[11],
                 "financialofficer": s[12], "secretary": s[13], "member": s[14]
        , "shortname": e[2], "sub-trend-value": "48.19", "time": e[0].strftime("%Y-%m-%d"), "todayopen": e[6],
                 "yesterdatclose": e[7], "maxx": e[4], "minn": e[5], "dealaccount": ('%.2f' % (e[11] / 10000)),
                 "dealmonney": ('%.2f' % (e[12] / 100000000)), "zhangdiee": ('%.3f' % e[8]), "zhangdiefu": ('%.3f' % e[9]),
                 "zongshizhi": ('%.2f' % (e[13] / 100000000)), "liutongshizhi": ('%.2f' % (e[14] / 100000000)),
                 "huanshou": ('%.3f' % e[10]),
                 }

    # print(list_item)
    cs1.close()
    conn.close()
    return json.dumps(list_item)


@analysis.route('/get_datetype',methods=['POST'])
def get_datetype():
    data = json.loads(request.form.get('data'))
    code = str(data['value'])
    conn = getConn()
    cs1 = conn.cursor()
    sql2 = "SELECT * FROM first_ten_%s" % code
    cs1.execute(sql2)
    s = cs1.fetchall()
    date_type = []
    date_type.append(s[0][0])
    for x in s:

        if x[0] not in date_type:
            date_type.append(x[0])
    # print(date_type)

    cs1.close()
    conn.close()
    return json.dumps(date_type)



@analysis.route('/get_allcode',methods=['POST'])
def get_allcode():
    conn = getConn()
    cs1 = conn.cursor()
    sql = 'select stock_code from listed_company3'
    data = []
    cs1.execute(sql)
    alldata = cs1.fetchall()
    for s in alldata:
        code = str(s[0]).zfill(6)
        if code[0] == '0' or code[0] == '3':
            code = 'sz' + code
        else:
            code = 'sh' + code
        data.append(code)

    # print(data)
    cs1.close()
    conn.close()
    return json.dumps(data)


@analysis.route('/getincometable',methods=['get'])
def getincometable():
    conn=getConn()
    cs1 = conn.cursor()
    sql = 'select main_bussiness_income from listed_company3'
    data = []
    cs1.execute(sql)
    num_1 = 0
    num_1to10 = 0
    num_10to100 = 0
    num_100to200 = 0
    num_200to400 = 0
    num_400to1000 = 0
    num_1000to10000 = 0
    num_10000 = 0
    alldata = cs1.fetchall()
    for s in alldata:
        s = s[0]
        if s[-1] == '万':
            num_1 = num_1 + 1
        elif s[-1] == '亿':
            s = s[0:-1]
            if s[-1] == '万':
                num_10000 = num_10000 + 1
            else:
                s = float(s)
                if s >= 1 and s < 10:
                    num_1to10 = num_1to10 + 1
                elif s >= 10 and s < 100:
                    num_10to100 = num_10to100 + 1
                elif s >= 100 and s < 200:
                    num_100to200 = num_100to200 + 1
                elif s >= 200 and s < 400:
                    num_200to400 = num_200to400 + 1
                elif s >= 400 and s < 1000:
                    num_400to1000 = num_400to1000 + 1
                elif s >= 1000 and s < 10000:
                    num_1000to10000 = num_1000to10000 + 1

    data = [{"value": num_1, "name": '低于1亿'}, {"value": num_1to10, "name": '1亿到10亿'},
            {"value": num_10to100, "name": '10亿到100亿'}, {"value": num_100to200, "name": '100亿到200亿'},
            {"value": num_200to400, "name": '200亿到400亿'}, {"value": num_400to1000, "name": '400亿到千亿'},
            {"value": num_1000to10000, "name": '千亿到万亿'}, {"value": num_10000, "name": '高于万亿'}]
    # print(data)
    conn.close()
    return json.dumps(data)


@analysis.route('/getNewest',methods=['get'])
def getNewest():
    conn=getConn()
    cs1 = conn.cursor()
    sql = 'select stock_code,stock_abbre,listing_date from listed_company3 order by listing_date desc limit 20'
    cs1.execute(sql)
    data = []
    alldata = cs1.fetchall()
    for s in alldata:
        data.append({"code": str(s[0]).zfill(6), "name": s[1], "date": s[2]})
    # print(len(data))
    conn.close()
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


