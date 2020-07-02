import requests,  random, bs4, csv
grade=open('grade.csv', 'w', newline='')
writer = csv.writer(grade)
# 用csv.writer()函数创建一个writer对象。
writer.writerow(['序号', '姓名', '一', '二', '三','四','五','总分'])
url = 'https://ahr105874.github.io/test/check.html'
res = requests.get(url)
bs = bs4.BeautifulSoup(res.text, 'html.parser')
bs= bs.find('tbody')
tr = bs.find_all('tr')
for i in tr:
    number=i.find('td',class_="number").text
    name=i.find('td',class_="name").text
    yi=i.find('td',class_="yi").text
    er=i.find('td',class_="er").text
    san=i.find('td',class_="san").text
    si=i.find('td',class_="si").text
    wu=i.find('td',class_="wu").text
    zong=i.find('td',class_="zong").text
    writer.writerow([number,name,yi,er,san,si,wu,zong])
grade.close()
    
