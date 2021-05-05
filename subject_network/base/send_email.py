import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import time
class SendEmail:
    def __init__(self,email_host="smtp.qq.com",send_name="786528604@qq.com"):
        self.email_host = email_host
        self.send_name = send_name
        self.email_frame = MIMEMultipart()
    def email_message(self):
        self.send_user = "风之缘梦" + "<" +"786528604@qq.com" +">"
        self.receive_list = [
            '1316469308@qq.com','936540462@qq.com',
            'wq786528604@126.com'
        ]
        sub = '接口自动化测试报告'
        self.email_frame['From'] = self.send_user
        self.email_frame['To'] = ";".join(self.receive_list)
        self.email_frame['Subject'] = sub
    def email_content(self):
        content = '接口自动化测试报告正文内容，接口自动化测试报告正文内容！'
        email_content = MIMEText(content,_subtype='plain',_charset='utf-8')
        self.email_frame.attach(email_content)
    def email_accessory(self):
        accessory = r"D:\study\practice\sublime\data_table\001data01.xls"
        add_accessory = MIMEApplication(open(accessory,'rb').read())
        add_accessory["Content-Type"] = 'application/octet-stream'
        add_accessory["Content-Disposition"] = 'attachment; filename="PortTestReport.xls"'
        self.email_frame.attach(add_accessory)
    def email_server(self):
        server = smtplib.SMTP()
        server.connect(self.email_host)
        server.login(self.send_name,'dzqeezvfufbbbdde')
        server.sendmail(self.send_user,self.receive_list,self.email_frame.as_string())
        server.close()
    def email_main(self):
        self.email_message()
        self.email_content()
        self.email_accessory()
        self.email_server()


if __name__ == '__main__':
    sendeamil = SendEmail()
    sendeamil.email_main()


