import requests as rq
import time

print("PAK REQUESTS")
print("Create File")
f = open("Test99.txt", "w+",  encoding="utf-8")
#for i in range(100):
#    f.write("This is line %d\r\n" % (i + 1))
print("==================== Tracking Website =========================")
cookies = {'PHPSESSID': 'cpihfb42iukgk0b8llrmdr6044', '_ga':'GA1.3.844880961.1557544362','_gat':'1','_gid':'GA1.3.1691361320.1558162498', 'authentic':'a%3A7%3A%7Bs%3A5%3A%22email%22%3Bs%3A17%3A%22pakpham%40gmail.com%22%3Bs%3A8%3A%22password%22%3Bs%3A8%3A%22qfmqtpaq%22%3Bs%3A8%3A%22lydokhoa%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22trangthai%22%3Bi%3A1%3Bs%3A4%3A%22date%22%3Bi%3A1557547248%3Bs%3A8%3A%22checksum%22%3Bs%3A40%3A%220a28960b6e87faa6552c2896e60b943f67ec8f22%22%3Bs%3A4%3A%22type%22%3Bi%3A2%3B%7D'}
#web = rq.get('https://vieclamcantho.com.vn/ho-so-chi-tiet-29623-la-thi-thuy-trang.html', cookies = cookies)
web = rq.get('https://vieclamcantho.com.vn/ho-so-chi-tiet-34126-trinh-cam-nghi.html', cookies = cookies)
req = rq.get('https://zing.vn/')
print (req.encoding)
print (req.status_code)
#print (duy.headers)
print ('======================Find there=============================')
# print (duy.text)
text = web.text
f.write(text)
f.close();

##################################################
class TextFind:
	"""docstring for TextFind"""
	def __init__(self, text):
		#super(TextFind, self).__init__()
		self.text = text
		self.temp = 111

	def displayText(self):
		print("The text: " , self.text)
		pass
	def findText(self, obj, par1, par2):
		pos_text = 0
		length_text  = len(self.text)
		pos_text = self.text.find(obj, pos_text, length_text)
		# while pos_text != -1:
		# 	print('The number:   ', text[pos_text+111:pos_text+121], "   --at position: ", pos_text)
		# 	pos_text = self.text.find(self.obj, pos_text + 12, length_text)
		# pass
		return text[pos_text+par1:pos_text+par2]
		pass
	def test(self):
		print(self.temp)
		pass

class member:
	"""docstring for member"""
	def __init__(self):
		super(member, self).__init__()
		self.phone = "NOT FOUND"
		self.add = "NOT FOUND"
		self.name = "NOT FOUND"
		self.age = "NOT FOUND"
		self.fb = "NOT FOUND"
		self.mail = "NOT FOUND"
		self.link = "NOT FOUND"
	def showInfo(self):
		print('==========================================')
		print("================   INFO  =================")
		print("Name: 		" , self.name)
		print("Phone Number:", self.phone)
		print("Year born:   ", self.age)
		print("Email:		", self.mail)
		print("Address:     ", self.add)
		print("Facebook:    ", self.fb)
		print('==========================================')
		print('==========================================')
		pass

web 	= TextFind(text)
member 	= member()

member.showInfo()


numb_member = 10
# members = [member() for i in range(numb_member)]
# for member in members:
# 	member.name
# 	pass


