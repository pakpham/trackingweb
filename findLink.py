import requests as rq
import time
from tqdm import tqdm
import sys
import csv


def findText(url, obj1, obj2, par1, par2):
        cookies = {'PHPSESSID': 'cpihfb42iukgk0b8llrmdr6044', '_ga':'GA1.3.844880961.1557544362','_gat':'1','_gid':'GA1.3.1691361320.1558162498', 'authentic':'a%3A7%3A%7Bs%3A5%3A%22email%22%3Bs%3A17%3A%22pakpham%40gmail.com%22%3Bs%3A8%3A%22password%22%3Bs%3A8%3A%22qfmqtpaq%22%3Bs%3A8%3A%22lydokhoa%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22trangthai%22%3Bi%3A1%3Bs%3A4%3A%22date%22%3Bi%3A1557547248%3Bs%3A8%3A%22checksum%22%3Bs%3A40%3A%220a28960b6e87faa6552c2896e60b943f67ec8f22%22%3Bs%3A4%3A%22type%22%3Bi%3A2%3B%7D'}
        #web = rq.get('https://vieclamcantho.com.vn/ho-so-chi-tiet-29623-la-thi-thuy-trang.html', cookies = cookies)
        text = rq.get(url,cookies = cookies).text
        pos_text = 0
        length_text  = len(text)
        pos_text = text.find(obj1, pos_text, length_text)
        end_text = text.find(obj2, pos_text+par1, length_text)
        # while pos_text != -1:
        #   print('The number:   ', text[pos_text+111:pos_text+121], "   --at position: ", pos_text)
        #   pos_text = self.text.find(self.obj, pos_text + 12, length_text)
        # pass
        return text[pos_text+par1:end_text+par2]
        pass


class member:
	"""docstring for member"""
	def __init__(self):
		super(member, self).__init__()
		self.id = "0"
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
	def __repr__(self):
		return (self.__dict__)

class LinkFind:
	"""docstring for LinkFind"""
	def __init__(self, url):
		super(LinkFind, self).__init__()
		self.url = url
		self.text = ''
		self.length_text = 0
		self.pos_text = 0
		self.end_text = 0
		self.start_code = 'class="title-blockjob-sub hiddenwidth">'
		self.par_start_code = 90
		self.end_code = 'html"'
		self.par_end_code = 4
	def showMainLink(self):
		print(self.url)

	def trackingWeb(self):
		#print("==================== Tracking Website =========================")
		cookies = {'PHPSESSID': 'cpihfb42iukgk0b8llrmdr6044', '_ga':'GA1.3.844880961.1557544362','_gat':'1','_gid':'GA1.3.1691361320.1558162498', 'authentic':'a%3A7%3A%7Bs%3A5%3A%22email%22%3Bs%3A17%3A%22pakpham%40gmail.com%22%3Bs%3A8%3A%22password%22%3Bs%3A8%3A%22qfmqtpaq%22%3Bs%3A8%3A%22lydokhoa%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22trangthai%22%3Bi%3A1%3Bs%3A4%3A%22date%22%3Bi%3A1557547248%3Bs%3A8%3A%22checksum%22%3Bs%3A40%3A%220a28960b6e87faa6552c2896e60b943f67ec8f22%22%3Bs%3A4%3A%22type%22%3Bi%3A2%3B%7D'}	
		web = rq.get(self.url, cookies = cookies)
		# print (web.encoding)
		# print (web.status_code)
		self.text = web.text
		self.length_text = len(self.text)
		pass

	def findLink(self):
		temp = ''
		data = []
		id = 0
		with open('data.csv', newline='', mode='a', encoding="utf-8") as csv_file:
				fieldnames = ['id','name', 'age', 'phone','add','mail','fb','link']
				writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
				writer.writeheader()
		self.pos_text = self.text.find(self.start_code, self.pos_text +  self.par_start_code, self.length_text) 
		while self.pos_text != -1:
			id += 1
			#print("Post Code: " , self.pos_text)
			self.end_text = self.text.find(self.end_code, self.pos_text, self.length_text)
			#print("End text: ",  self.end_text)
			temp_url =  (self.text[self.pos_text +  self.par_start_code:self.end_text + self.par_end_code])
			#print(temp_url)

			member.name     =findText(temp_url,'data-name="', '"', 11, 0)
			member.phone    =findText(temp_url,"numberphone",'"', 111, 0)
			member.age      =findText(temp_url,"id='birthday'", '</', 77, 0)
			member.add      =findText(temp_url,"id='address'", '</div>', 73, 0)
			member.mail     =findText(temp_url,"data-email=",'"', 12, 0)
			member.link 	=temp_url
			member.id 		=id
			#data.insert(0, temp_url)
			# f = open("Test99.csv", "a",  encoding="utf-8")
			# f.write(member.__repr__()+'\n')
			# f.close();
			with open('data.csv', newline='', mode='a', encoding="utf-8") as csv_file:
				fieldnames = ['id','name', 'age', 'phone','add','mail','fb','link']
				writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
				#writer.writeheader()
				writer.writerow(member.__repr__())		

			self.pos_text = self.text.find(self.start_code, self.end_text +  self.par_start_code, self.length_text)
			sys.stdout.write("\r%d%%\r" % id)
			sys.stdout.flush()
		return data
			
link = []
numb_page = 3
member 	= member()
url = 'https://vieclamcantho.com.vn/ho-so-ung-vien-trang-2.html'

for x in tqdm(range(numb_page)):
	url = url.replace(str(x-1), str(x))
	data_url = LinkFind(url)	
	#dataurl.showMainLink()	
	data_url.trackingWeb()
	data_url.findLink()

# data_url = LinkFind(url)	
# data_url.trackingWeb()
# data_url.findLink()
# print("VALUE: ", len(link))


