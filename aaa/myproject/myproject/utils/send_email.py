import smtplib,poplib,sys,getpass,email
from email.mime.text import MIMEText
from poplib import POP3


# 用于发送邮件
def send_email(from_addr, to_addr, subject, password,news):
    try:
        msg = MIMEText(news,'html','utf-8')
        msg['From'] = '<%s>' % from_addr
        msg['To'] = '<%s>' % to_addr
        msg['Subject'] = subject
        smtp = smtplib.SMTP_SSL('smtp.163.com', 465)
        # smtp.set_debuglevel(1)
        smtp.ehlo("smtp.163.com")
        smtp.login(from_addr, password)
        smtp.sendmail(from_addr, [to_addr], msg.as_string())
        print("发送成功")
        return 0
    except Exception as e:
        print(e)
        return 1
# 接收邮件,不知道用来干啥的,将邮件获取到本低
def accpet_mail():
    p = POP3('pop.163.com')
    try:
        p.user('kousq_kousq@163.com')
        p.pass_('5sendeamil')
        ret = p.stat()
        print("登录成功")
    except poplib.error_proto as e:
        print(e)
        sys.exit(1)
    else:
        number = ""
        response, listings, octets = p.list()
        for listing in listings:  # 每次需要一个listing
            number, size = listing.split()  # 由于number和size是以空格分隔，所以利用split()函数分开，split()默认以' '为分隔
            number = bytes.decode(number)
            size = bytes.decode(size)
            print('Message', number, '( size is ', size, 'bytes)')
            print()
        response, lines, octets = p.top(number, 0)
        # 继续把Byte类型转化成普通字符串
        for i in range(0, len(lines)):
            lines[i] = bytes.decode(lines[i])
        # 利用email库函数转化成Message类型邮件
        message = email.message_from_string('\n'.join(lines))
        # 输出From, To, Subject, Date头部及其信息
        for header in 'From', 'To', 'Subject', 'Date':
            if header in message:
                print(header + ':', message[header])
        # 与用户交互是否想查看邮件内容
        print('Read this message [ny]')
        answer = input()
        if answer.lower().startswith('y'):
            response, lines, octets = p.retr(number)  # 检索message并返回
            for i in range(0, len(lines)):
                lines[i] = bytes.decode(lines[i])
            message = email.message_from_string('\n'.join(lines))
            print('-' * 72)
            maintype = message.get_content_maintype()
            if maintype == 'multipart':
                for part in message.get_payload():
                    if part.get_content_maintype() == 'text':
                        mail_content = part.get_payload(decode=True).strip()
            elif maintype == 'text':
                mail_content = e.get_payload(decode=True).strip()
            try:
                mail_content = mail_content.decode('gbk')
            except UnicodeDecodeError:
                print('Decoding to gbk error')
                sys.exit(1)
            print(mail_content)
        print()
        print('Delete this message? [ny]')
        answer = input()
        if answer.lower().startswith('y'):
            p.dele(number)
            print('Deleted')
    finally:
        print('log out')
        p.quit()





if __name__ == "__main__":
    # 这里的密码是开启smtp服务时输入的客户端登录授权码，并不是邮箱密码
    # 现在很多邮箱都需要先开启smtp才能这样发送邮件
    # send_email("kousq_kousq@163.com","961094263@qq.com","爬虫","5sendeamil","123456")
    accpet_mail()