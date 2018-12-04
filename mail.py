# -*- coding: utf-8 -*-
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(host, port, username, password, sender, receivers, subject, content, image_dict={}, attachment_dict={}):
    """
    发邮件功能
    :param host: 服务器主机IP/域名
    :param port: SMTP 服务使用的端口号，一般情况下SMTP端口号为25
    :param username:用户名
    :param password:密码
    :param sender:发件人
    :param receivers:收件人
    :param subject:邮件主题
    :param content:邮件文本内容
    :param image_dict:图片信息{'key1':image_path; 'key2':image_path}
    :param attachment_dict:附件内容{'file_name1':file_path; 'file_name2':file_path}
    :return:bool
    """
    smtp = smtplib.SMTP_SSL()
    msg = MIMEMultipart('related')
    msg['From'] = sender
    msg['To'] = receivers
    # 邮件主题
    msg['Subject'] = subject

    msg_alternative = MIMEMultipart('alternative')
    msg.attach(msg_alternative)
    msg_alternative.attach(MIMEText(content, 'html', 'utf-8'))

    # for image_key in image_dict.keys():
    #     with open(image_dict[image_key], 'rb') as f:
    #         msg_image = MIMEImage(f.read())
    #     msg_image.add_header('Content-ID', image_key)
    #     msg.attach(msg_image)

    for attachment_key in attachment_dict.keys():
        with open(attachment_dict[attachment_key], 'rb') as f:
            msg_attachment = MIMEText(f.read(), 'base64', 'utf-8')
        msg_attachment['Content-Type'] = 'application/octet-stream'
        msg_attachment['Content-Disposition'] = 'attachment; filename="' + attachment_key + '"'
        msg.attach(msg_attachment)

    try:
        smtp.connect(host, port)
        smtp.login(username, password)
        smtp.sendmail(sender, receivers.split(';'), msg.as_string())
        print("邮件发送成功!")
        return True
    except smtplib.SMTPException as e:
        print(e)
        print("邮件发送失败!")
        return False

def get_file_content(file_path):
    """
    获取文件内容，返回字符串
    :param file_path: 文件路径
    :return: file_content
    """
    file_content = ''
    f = open(file_path, 'r')
    for line in f.readlines():
        file_content += line
    f.close()
    return file_content

if __name__ == '__main__':
    content = get_file_content('./reports/TestResult.html')
    attachment_dict = {'测试报告.html':'./reports/TestResult.html'}
    send_mail("smtp.qq.com", 465, "870463079@qq.com","efhkyrtghnwlbeab","870463079@qq.com","870463079@qq.com","实名认证接口的测试结果", content, {}, attachment_dict)
    # send_mail("smtp.tsign.cn", 465, "xianyue@tsign.cn","","xianyue@tsign.cn","xianyue@tsign.cn","实名认证接口的测试结果", content, {}, attachment_dict)

