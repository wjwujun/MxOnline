
from users.models import EmailVerifyRecord
from random import Random
from django.core.mail import send_mail
from MxOnline.settings import EMAIL_FROM

def random_str(randomlength=8):
    str=''
    chars='QWERTYUIOPLKJHGFDSAZXCVBNMqazwsxedcrfvtgbyhnujmikolp0123456789'
    length=len(chars)-1
    random=Random()
    for i in range(randomlength):
        str+=chars[random.randint(0,length)]
    return str

def send_rigister_email(email,send_type='register'):
        email_record=EmailVerifyRecord()
        code=random_str(16)
        email_record.code=code
        email_record.email=email
        email_record.send_type=send_type
        email_record.save()

        email_title=""
        email_boby=""

        if send_type=="register":
            email_title="在线注册激活链接"
            email_boby="请点击下面链接激活你的账号:http://127.0.0.1:8000/active/{0}".format(code)

            send_status=send_mail(email_title,email_boby,EMAIL_FROM,[email])
            if send_status:
                pass
        elif send_type=='forget':
            email_title = "在线注册密码重置链接"
            email_boby = "请点击下面链接激活你的账号:http://127.0.0.1:8000/reset/{0}".format(code)

            send_status = send_mail(email_title, email_boby, EMAIL_FROM, [email])
            if send_status:
                pass

