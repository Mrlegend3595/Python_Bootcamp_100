################debugging##################

#describe problem
#اگه با مشکلی در کد مواجه شدیم سعی کنیم توصیف کنیم کد رو
#تا بفهمیم موضوع از چه قراره و سپس فرضیات خودمون رو تست کنیم
#که آیا درست است یا اشتباه

# def my_function():
#     for i in range(1,20): # loop range is between [1,20) mean 1 to 19 | solution [1,21)
#         if i == 20:
#             print("I'm done!")
#
# my_function()



# reproduce the Bug

#یه سری کدا هستن که معمولا اجرا میشن اما یدفعه
#با یه خطا مواجه میشین این قضیه کار دیباگ رو سخت میکنه
# بازتولید خطا :کی کدمون خطا میده و براساس این دانش میتونیم کدمون رو اصلاح کنیم

# from random import randint
# dice_imgs = ["1️⃣","️2️⃣","3️⃣","4️⃣","5️","6️"]
# dice_nums = randint(1,6) # if dice_nums = 6 then get error because index from 0 started
# # solution | dice_nums = randint(0,5)
# print(dice_imgs[dice_nums])

#در این این روش میایم اشکال روخودمون تکرار میکنیم
#سعی میکنیم متوجه بشیم چه زمانی اتفاق می افته
# و بعد کد رو جوری تغییر بذیم که همیشه این خطایی که تو ترمینال هست رو بده



#Play Computer
# اینقدر ورودی بدید و بازی یازی کنید ببینید چخبره
# مقدار ورودی بده و منطق رو چک کن خودت تا بفهمی مشکل جیه
#بعد فیکسش کن
# year = int(input("What is your year of birth?"))
# if year > 1980 and year < 1994:# solution | use <= and >=
#     print("You are millenial.")
# elif year >1994:
#     print("You are Gen Z.")



#Fix The Errors
# ارور هایی که خود محیط برنامه نویسی به شما گوش زد میکنه
#در کنسول به شما خطا میده این خط و ارورش به شما سرنخی رو میده
#میتونید نوع ارور رو در گوگل سرچ کنید و کسانی هستن
#که به این مشکل برخورده باشن

# age = int(input("How old are you? "))#solution is convert str to int (output of input func is str type)
# #age = int(input(..................))
# if age > 18:
#     print("You can drive at age {age}")#solution fstring



#Print is Your Friend
#یه سری خطاها با ردیابی مقدار متوجهش میشی
#خو از پرینت استفاده کن
# pages = 0
# word_per_page = 0
#
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: ")) #solution | == wrong . true is =
#
# total_words = pages * word_per_page
# print(total_words)




#Use a Debugger
#بعضی مشکلات مثل این رو باید با دیباگر مرحله به مرحله چک بشه
#تا بفهمیم داستان از چه قراره
#بهترین ابزار ما دیباگره
#keywors : Breakpoint explore from breakpoint line to end
# def mutate(a_list):
#     b_list=[]
#     for item in a_list:
#         new_item=item*2
#     b_list.append(new_item)#solution | only a tab in current line
#     print(b_list)
#
# mutate([1,2,3,5,8,13])  #solution output =[2,4,6,10,16,26]


#Take a Break😪😀
#Ask a Friend
#Run often
#Ask Stackoverflow