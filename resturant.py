import random 
from tkinter import *
from tkinter import messagebox
#from PIL import ImageTk,Image
from tkinter import ttk
	
class Main_menu():
	def __init__(self,mas=""):
		if mas:
			mas.destroy()

		self.root=Tk()
		self.root.configure(background="Orange")
		self.root.title("Main Menu")	
		self.root.geometry("540x400")
		self.Variable()
		self.Grid()
		self.Label()
		self.Entry()
		self.Radio_but()
		self.Button()
		self.gframe.place(x=50,y=50)
		self.root.mainloop()	
	def Variable(self):
		self.__n=StringVar(self.root)
		self.__con=StringVar(self.root)
		self.__ty=StringVar(self.root)
	def Entry(self):
		self.entyn=Entry(self.gframe1,textvariable=self.__n).grid(row=1,column=1,sticky=W)	
		self.entycon=Entry(self.gframe1,textvariable=self.__con).grid(row=2,column=1,sticky=W)
	def Label(self):
		self.lb1=Label(self.gframe1,text="Resturant Management System",font=14).grid(row=0,pady=40,columnspan=3)	
		self.lbun=Label(self.gframe1,text="Customer Name:").grid(row=1,column=0,sticky=E)
		self.lbcon=Label(self.gframe1,text="Contact No:").grid(row=2,column=0,sticky=E)	
		self.lbcon=Label(self.gframe1,text="Type Of Customer:").grid(row=3,column=0,sticky=E)	
	def Radio_but(self):
		self.R1 = Radiobutton(self.gframe1, text="Dinning", variable=self.__ty, value="Dinning",font=14,justify='center',bd=0).grid(row=3,column=1,sticky=W)
		self.R2 = Radiobutton(self.gframe1, text="Take Away", variable=self.__ty, value="Take Away",font=14,justify='center',bd=0).grid(row=3,column=2,sticky=W)
	def Get_dt(self):
		self.na=self.__n.get()
		self.con=self.__con.get()
		self.ty=self.__ty.get()
		self.__n.set("")
		self.__con.set("")
		self.__ty.set("")
		self.Give_dt()
	def Give_dt(self):
		if self.ty=='Dinning':
			self.d=Dinning_customer(self.na,self.con,self.root)
			self.d.Reserve()

		elif self.ty=='Take Away':
			self.t=Take_away_customer(self.na,self.con,self.root)
	
			self.t.Go_to_fmenu()
			
	def Grid(self):
		#self.gframe1=Frame(self.root)
		self.gframe=Frame(self.root,bg="blue",height=1000)
		#self.gframe.place(height=300,width=300)
		#self.gframe.grid(rowspan=2)	
		'''self.gframe0=LabelFrame(self.gframe,bd=12)
		self.gframe0.grid(row=0,column=3,sticky=NW)'''
		self.gframe1=LabelFrame(self.gframe,bd=12,height=100,width=100)
		self.gframe1.grid(row=0,column=1)	
		self.gframe2=LabelFrame(self.gframe,height=100,width=100,bd=12)
		self.gframe2.grid(row=1,column=1)
	def Button(self):
		self.but_choose=Button(self.gframe2,text="Submmit",width=48,command=self.Get_dt).grid(row=4,columnspan=3)
class Fmenu():
	def __init__(self,name,contact,table=""):
		self.name=name
		self.contact=contact
		if(table):
			self.table=table
		else:
			self.table=""
		self.it=Item()
		self.allitems=self.it.items
		self.pricesall=self.it.prices
		self.quanall=self.it.quantity
		self.root=Tk()
		self.root.configure(background="Orange")
		self.root.title("Menu")	
		self.root.geometry("500x500")
		self.Variable()
		self.Grid()
		self.Label()
		#self.Entry()
		self.Check_but()
		self.Button()
		self.gframe.place(x=50,y=50)
		self.root.mainloop()
	def Variable(self):
		self.qq=[]
		self.ittt=[]
		self.prrr=[]
		self.q=[]
		self.chose_it=[]
		self.pos=[]
		self.ii=[]
		self.qun=[]
		
		for i in range(len(self.allitems)):
			
			self.q.append(IntVar(self.root))
			self.chose_it.append(IntVar(self.root))
			self.pos.append(i)
		print(self.pos)
	def Label(self):
		self.lb1=Label(self.gframe1,text="Resturant Menu",font=14).grid(row=0,pady=40,columnspan=3)	
		self.lbIte=Label(self.gframe1,text="Items").grid(row=1,column=0)
		self.lbPrice=Label(self.gframe1,text="Prices").grid(row=1,column=1,sticky=E)	
		self.lbQuantity=Label(self.gframe1,text="Quantity").grid(row=1,column=2,sticky=E)	
		self.lb=[]
		for i in range(len(self.allitems)):
			self.lb.append(Label(self.gframe1,text=self.pricesall[i]).grid(row=i+2,column=1))
	def Grid(self):
		#self.gframe1=Frame(self.root)
		self.gframe=Frame(self.root,bg="blue",height=1000)
		#self.gframe.place(height=300,width=300)
		#self.gframe.grid(rowspan=2)	
		'''self.gframe0=LabelFrame(self.gframe,bd=12)
		self.gframe0.grid(row=0,column=3,sticky=NW)'''
		self.gframe1=LabelFrame(self.gframe,bd=12,height=100,width=100)
		self.gframe1.grid(row=0,column=1)	
		self.gframe2=LabelFrame(self.gframe,height=100,width=100,bd=12)
		self.gframe2.grid(row=1,column=1)
	def Check_but(self):
		#self.c1=[]
		self.c0=Checkbutton(self.gframe1, text=self.allitems[0],onvalue = self.pos[0], offvalue = 0,variable=self.chose_it[0],command=lambda:self.Choose_ittems(0),font=14,justify='center',bd=0).grid(row=2,column=0,sticky=W)
		self.c1=Checkbutton(self.gframe1, text=self.allitems[1],onvalue = self.pos[1], offvalue = 0,variable=self.chose_it[1],command=lambda:self.Choose_ittems(1),font=14,justify='center',bd=0).grid(row=3,column=0,sticky=W)
		self.c2=Checkbutton(self.gframe1, text=self.allitems[2],onvalue = self.pos[2], offvalue = 0,variable=self.chose_it[2],command=lambda:self.Choose_ittems(2),font=14,justify='center',bd=0).grid(row=4,column=0,sticky=W)
		self.c3=Checkbutton(self.gframe1, text=self.allitems[3],onvalue = self.pos[3], offvalue = 0,variable=self.chose_it[3],command=lambda:self.Choose_ittems(3),font=14,justify='center',bd=0).grid(row=5,column=0,sticky=W)
		self.c4=Checkbutton(self.gframe1, text=self.allitems[4],onvalue = self.pos[4], offvalue = 0,variable=self.chose_it[4],command=lambda:self.Choose_ittems(4),font=14,justify='center',bd=0).grid(row=6,column=0,sticky=W)
		self.c5=Checkbutton(self.gframe1, text=self.allitems[5],onvalue = self.pos[5], offvalue = 0,variable=self.chose_it[5],command=lambda:self.Choose_ittems(5),font=14,justify='center',bd=0).grid(row=7,column=0,sticky=W)
		self.c6=Checkbutton(self.gframe1, text=self.allitems[6],onvalue = self.pos[6], offvalue = 0,variable=self.chose_it[6],command=lambda:self.Choose_ittems(6),font=14,justify='center',bd=0).grid(row=8,column=0,sticky=W)
		self.c7=Checkbutton(self.gframe1, text=self.allitems[7],onvalue = self.pos[7], offvalue = 0,variable=self.chose_it[7],command=lambda:self.Choose_ittems(7),font=14,justify='center',bd=0).grid(row=9,column=0,sticky=W)
		self.c8=Checkbutton(self.gframe1, text=self.allitems[8],onvalue = self.pos[8], offvalue = 0,variable=self.chose_it[8],command=lambda:self.Choose_ittems(8),font=14,justify='center',bd=0).grid(row=10,column=0,sticky=W)

		'''self.c0.bind('<Button-1>', lambda:self.Choose_ittems(0))
		self.c0.bind('<Button-2>', lambda:self.dis_select(0))
		self.c1.bind('<Button-1>', lambda:self.Choose_ittems(1))
		self.c1.bind('<Button-2>', lambda:self.dis_select(1))
		self.c2.bind('<Button-1>', lambda:self.Choose_ittems(2))
		self.c2.bind('<Button-2>', lambda:self.dis_select(2))
		self.c3.bind('<Button-1>', lambda:self.Choose_ittems(3))
		self.c3.bind('<Button-2>', lambda:self.dis_select(3))
		self.c4.bind('<Button-1>', lambda:self.Choose_ittems(4))
		self.c4.bind('<Button-2>', lambda:self.dis_select(4))
		self.c5.bind('<Button-1>', lambda:self.Choose_ittems(5))
		self.c5.bind('<Button-2>', lambda:self.dis_select(5))
		self.c6.bind('<Button-1>', lambda:self.Choose_ittems(6))
		self.c6.bind('<Button-2>', lambda:self.dis_select(6))
		self.c7.bind('<Button-1>', lambda:self.Choose_ittems(7))
		self.c7.bind('<Button-2>', lambda:self.dis_select(7))
		self.c8.bind('<Button-1>', lambda:self.Choose_ittems(8))
		self.c8.bind('<Button-2>', lambda:self.dis_select(8))'''
		'''for self.i in range(len(self.allitems)):
			self.c1.append(Checkbutton(self.gframe1, text=self.allitems[self.i],onvalue = self.pos[self.i], offvalue = 0,variable=self.chose_it[self.i],command=self.Choose_ittems,font=14,justify='center',bd=0).grid(row=self.i+2,column=0,sticky=W))'''
	def Button(self):
		self.but_choose=Button(self.gframe2,text="Order",width=48,command=self.Get_dt).grid(row=len(self.allitems)+2,columnspan=3)	
	def Choose_ittems(self,i):
		self.i=i
		self.c=self.chose_it[self.i].get()
		print(self.i,' ',self.c)
		if(self.c==self.i):
			self.ii.append(self.i)
			self.Entry()
		self.chose_it[self.i].set("")
		self.c=0
	def dis_select(self,i):
		self.ii.remove(i)
		self.ent[self.i]=''
				
	def Get_dt(self):
		self.ii.sort()
		print(self.ii)
		for i in range(len(self.ii)):
			self.ittt.append(self.allitems[self.ii[i]])
			self.prrr.append(self.pricesall[self.ii[i]])
			self.qun.append(self.quanall[self.ii[i]])
			self.qq.append(self.q[self.ii[i]].get())
			#self.q[self.ii[i]].set("")
		print(self.ittt)
		print(self.prrr)
		print(self.qq)
		self.Pass_dt()
	def Pass_dt(self):
		if(self.table):
			self.bill=Bmenu(self.name,self.contact,self.ittt,self.prrr,self.qq,self.qun,self.table,self.root)	
		else:
			self.bill=Bmenu(self.name,self.contact,self.ittt,self.prrr,self.qq,self.qun,mas=self.root)				
			
					
	def Entry(self):
		self.ent=['','','','','','','','','']
		self.ent[self.i]=Entry(self.gframe1,textvariable=self.q[self.i]).grid(row=self.i+2,column=2,sticky=W)			
class Bmenu():	
	def __init__(self,name,contact,items,price,quantiy,quan,table="",mas=''):
		self.name=name
		self.contact=contact
		self.items=[]
		self.prices=[]
		self.quantity=[]
		self.total=0
		if(mas):
			mas.destroy()
		for i in range(len(items)):
			self.items.append(items[i])
			self.prices.append(price[i])
			print(quantiy[i],' ',quan[i])	
			if int(quantiy[i])<int(quan[i]):
				self.quantity.append(quantiy[i])
				self.total=self.total+(int(quantiy[i])*int(price[i]))
			elif int(quantiy[i])>int(quan[i]) and int(quan[i])>0:
				self.quantity.append(quan[i])
				self.total=self.total+(int(quan[i])*int(price[i]))
			elif int(quantiy[i])>int(quan[i]) and int(quan[i])==0:
				self.quantity.append(0)
				#self.total=self.total+(int(quan[i])*int(price[i]))			
		print(self.total)
		if(table):
			self.table=table
		else:
			self.table=""

		self.root=Tk()
		self.root.configure(background="Orange")
		self.root.title("Bill Menu")	
		self.root.geometry("500x500")
		self.Grid()
		
		self.Label()

		#self.Button()
		self.gframe.place(x=50,y=50)
		self.root.mainloop()	
	def Label(self):
		self.lb1=Label(self.gframe1,text="Bill Menu",font=14).grid(row=0,pady=40,columnspan=4)
		self.lbname=Label(self.gframe1,text="Customer Name:").grid(row=1,column=0)
		self.lbCus=Label(self.gframe1,text=self.name).grid(row=1,column=1)
		self.lbCon=Label(self.gframe1,text="Contact NO:").grid(row=2,column=0)
		self.lbconn=Label(self.gframe1,text=self.contact).grid(row=2,column=1)
		
		if(self.table):
			self.lbty=Label(self.gframe1,text="Type:").grid(row=3,column=0)
			self.lbtyn=Label(self.gframe1,text="Dinning").grid(row=3,column=1)
			self.lbta=Label(self.gframe1,text="Table No:").grid(row=3,column=2)
			self.lbtan=Label(self.gframe1,text=self.table).grid(row=3,column=3)
		else:
			self.lbty=Label(self.gframe1,text="Type:").grid(row=3,column=0)
			self.lbtyn=Label(self.gframe1,text="Take Away").grid(row=3,column=1)
		self.lbIte=Label(self.gframe1,text="Items").grid(row=4,column=0)
		self.lbPrice=Label(self.gframe1,text="Price per item").grid(row=4,column=1,sticky=E)	
		self.lbQuantity=Label(self.gframe1,text="Quantity").grid(row=4,column=2,sticky=E)
		self.lbttprice=Label(self.gframe1,text="Price").grid(row=4,column=3,sticky=E)
		self.lbi=[]
		self.lbp=[]
		self.lbq=[]
		self.lbtp=[]
		for i in range(len(self.items)):
			self.lbi.append(Label(self.gframe1,text=self.items[i]).grid(row=i+5,column=0))	
			self.lbi.append(Label(self.gframe1,text=self.prices[i]).grid(row=i+5,column=1))	
			#self.lbi.append(Label(self.gframe1,text=self.quantity[i]).grid(row=i+5,column=2))
			if self.quantity[i]==0:	
				#self.lbi.append(Label(self.gframe1,text=self.quantity[i]).grid(row=i+5,column=2))
				self.lbi.append(Label(self.gframe1,text="Not Available").grid(row=i+5,column=2,columnspan=2))
			else:
				self.lbi.append(Label(self.gframe1,text=self.quantity[i]).grid(row=i+5,column=2))
				self.lbi.append(Label(self.gframe1,text=self.prices[i]*self.quantity[i]).grid(row=i+5,column=3))
		self.lbtt=Label(self.gframe1,text="Total:").grid(row=i+6,columnspan=3)
		self.lbttn=Label(self.gframe1,text=self.total).grid(row=i+6,column=3)	
		self.Button(i)
	def Grid(self):
		#self.gframe1=Frame(self.root)
		self.gframe=Frame(self.root,bg="blue",height=1000)
		#self.gframe.place(height=300,width=300)
		#self.gframe.grid(rowspan=2)	
		'''self.gframe0=LabelFrame(self.gframe,bd=12)
		self.gframe0.grid(row=0,column=3,sticky=NW)'''
		self.gframe1=LabelFrame(self.gframe,bd=12,height=100,width=100)
		self.gframe1.grid(row=0,column=1)	
		self.gframe2=LabelFrame(self.gframe,height=100,width=100,bd=12)
		self.gframe2.grid(row=1,column=1)
	def Button(self,i):
		self.but_choose=Button(self.gframe2,text="Exit",width=48,command=self.Exit).grid(row=i+7,columnspan=4)	
	def Exit(self):
		self.new=Main_menu(self.root)			
class Customer():
	def __init__(self,name,contact,mas):
		self.name=name
		self.contact=contact
		mas.destroy()
		
	
class Dinning_customer(Customer):
	def Tables(self):
		self.tab=['a','a','a']
		self.cus_tab=0
	def Reserve(self):
		self.Tables()
		flag=0
		while(flag!=1):
			self.table=random.randint(0,2)
			if self.tab[self.table] =='a':
				flag=1
				self.tab[self.table]='n'
				self.cus_tab=self.table+1
		self.Go_to_fmenu()
	def Go_to_fmenu(self):
		
		self.menu=Fmenu(self.name,self.contact,self.table)
		#self.d.Reserve()
		
class Take_away_customer(Customer):
				
	def Go_to_fmenu(self):
		
		self.menu=Fmenu(self.name,self.contact)
		#self.d.Reserve()	
class Item():
	def __init__(self):
		#self.name=name
		self.items=['Biriyani','Chicken Curry','Chicken kabab','Crispy Chicken','Fish','Rice','Samucha','Sanduich','Singara']
		self.prices=[100,60,10,50,50,25,5,15,5]
		self.quantity=[100,0,2,50,50,25,5,15,5]
		'''self.choice=-10
		self.price_total=0
		self.all_items=[]'''
'''class Menu(Item):

	def show(self):
		print("sl",'  ',"items",'       ',"price")
		for i in range(len(self.items)):
			print(i+1,'   ',self.items[i],'     ',self.prices[i])'''


class Order(Item):
	
		

	def Get_item(self,choi):
		self.choice=choi
		dh=self.items[self.choice-1]
		print("choose Items",dh)
		self.all_items.append(dh)
		pr=int(self.prices[self.choice-1])
		self.price_total+=pr
		#self.Deliver()
	
	
#main()
a=Main_menu()
'''n=0
cus1=Customer()
cust_name=input()
cus1.get_name(cust_name)
flag1=0
cus_type=str(input("customer type:"))
if(cus_type=='Dinning'):
	cus=Dinning_customer()
	cus.Reserve()
	print("reserve table:",cus.cus_tab)
else:
	flag1=1
	
while(n!=5):
	print("Chosse Your Option:")
	print("1.menu")
	print("2.order")
	print("5.Exit")
	n=int(input())
	if(n==1):

		a=Menu()
		a.show()
	elif(n==2):
		ch=Order()
		choos_item=-10
		while(choos_item!=0):
			choos_item=int(input('choose your Items:'))
			ch.Get_item(choos_item)
			print("total prices:",ch.price_total)
		n=5
print("Name:",cus1.name," Type:",cus_type," all items:",ch.all_items," total prices:",ch.price_total)
'''		
		

	
	

		
		
		
		
		
