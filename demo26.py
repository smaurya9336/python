class test:
	def __init__ (self):
		print("="*30)
		print("WELCOME TO TECHPILE")
		print("="*30)
		self.Name="TECHPILE"
		self.Passwd="12345"
   
	def demo(self):
		print("YOUR NAME IS: ",self.Name)
		print("YOUR PASSWORD IS: ",self.Passwd)



obj=test()
obj.demo()