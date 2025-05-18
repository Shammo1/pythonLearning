#simple class Declearation
"""
class Phone:

 price = 19000

 color = 'blue'

 brand = 'samsung'

 

myphone = Phone()

print(myphone.brand) """# output: samsung

#method create
#remind that in python we have to use self peretmiter for method create
#মেথড হল একটি ফাংশন যা ক্লাসের ভিতরে ডিফাইন করা হয় এবং এটি সংশ্লিষ্ট অবজেক্টের উপর কাজ করে।
# প্রতিটি মেথড অটোমেটিকভাবে self প্যারামিটার নেয়, যা বর্তমান অবজেক্টকে রেফার করে।
#example
#def output(self):
       #x=(self.base*self.height)/2
        # print(f"area = {x}")
        
class Phone:

 price = 19000

 color = 'blue'

 brand = 'samsung'

 
def call(self):

    print('Calling one person')

 

def send_message(self, message):

 return f"Sending message: {message}"

 

myphone = Phone()

myphone.call() #output: Calling one person

print(myphone.send_message("Hello World")) #output:Sending message: Hello World 


#constructor and __init__ in python
#Constructor হল একটি স্পেশাল মেথড যা অটোমেটিক কল হয় যখন কোনো অবজেক্ট ক্রিয়েট করা হয়। 
# এটি দিয়ে অবজেক্টের প্রাথমিক স্টেট (attributes/ভেরিয়েবল) সেটআপ করা হয়।

#Python-এ __init__ হলো কন্সট্রাক্টরের মতো কাজ করে (আসল কন্সট্রাক্টর __new__,
# কিন্তু আমরা সাধারণত __init__ ব্যবহার করি)।

#এটি অটোমেটিক কল হয় অবজেক্ট বানানোর সময়।

#এর মাধ্যমে অবজেক্টের প্রোপার্টিগুলো ইনিশিয়ালাইজ করা হয়।
class Phone:

 def __init__(self, brand, price):

    self.brand = brand

    self.price = price

 

 def call(self):

    pass

 

samsung = Phone("Samsung", "90000")

iphone = Phone('Apple', '150000')

print(samsung.brand) #output: Samsung

print(iphone.brand) #output: Apple
