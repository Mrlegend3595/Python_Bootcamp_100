# کتابخانه tkinter برای ساخت رابط گرافیکی در پایتون استفاده می‌شود.
# نام کوتاه tk باعث می‌شود هنگام استفاده از tkinter کد مختصرتر باشد.
import tkinter as tk


# --------------------------------------------------
# توابع مربوط به رویدادهای برنامه
# --------------------------------------------------

# این تابع هنگام کلیک روی دکمه اجرا می‌شود.
def button_clicked():
    # متن نوشته‌شده داخل Entry را دریافت می‌کنیم.
    entered_text = entry.get()

    # متن Label را با متن Entry جایگزین می‌کنیم.
    my_label.config(text=entered_text)


# این تابع هنگام تغییر مقدار Spinbox اجرا می‌شود.
def spinbox_used():
    # دریافت و چاپ مقدار فعلی Spinbox
    print("Spinbox value:", spinbox.get())


# این تابع هنگام حرکت دادن Scale اجرا می‌شود.
# tkinter مقدار فعلی Scale را به‌صورت خودکار به تابع ارسال می‌کند.
def scale_used(value):
    print("Scale value:", value)


# این تابع هنگام تغییر وضعیت Checkbutton اجرا می‌شود.
def checkbutton_used():
    # مقدار 1 یعنی Checkbutton فعال است.
    # مقدار 0 یعنی Checkbutton غیرفعال است.
    print("Checkbutton value:", checked_state.get())


# این تابع هنگام انتخاب یکی از RadioButtonها اجرا می‌شود.
def radio_used():
    # مقدار گزینه انتخاب‌شده را دریافت و چاپ می‌کنیم.
    print("Selected radio value:", radio_state.get())


# این تابع هنگام انتخاب یک آیتم از Listbox اجرا می‌شود.
# پارامتر event اطلاعات مربوط به رویداد انتخاب را دریافت می‌کند.
def listbox_used(event):
    # curselection ایندکس آیتم‌های انتخاب‌شده را برمی‌گرداند.
    selected_indices = listbox.curselection()

    # بررسی می‌کنیم که حداقل یک آیتم انتخاب شده باشد.
    if selected_indices:
        # اولین ایندکس انتخاب‌شده را دریافت می‌کنیم.
        selected_index = selected_indices[0]

        # با استفاده از ایندکس، متن آیتم را دریافت می‌کنیم.
        selected_item = listbox.get(selected_index)

        print("Selected fruit:", selected_item)


# --------------------------------------------------
# ساخت پنجره اصلی برنامه
# --------------------------------------------------

# ساخت یک نمونه از پنجره اصلی tkinter
window = tk.Tk()

# مشخص کردن عنوان پنجره
window.title("GUI Program")

# مشخص کردن حداقل اندازه پنجره
window.minsize(width=500, height=300)


# --------------------------------------------------
# Label
# --------------------------------------------------

# Label برای نمایش متن در پنجره استفاده می‌شود.
my_label = tk.Label(
    window,                              # والد این ویجت، پنجره اصلی است.
    text="I am a Label",                 # متن اولیه Label
    font=("Arial", 24, "italic"),        # نوع، اندازه و حالت فونت
)

# نمایش Label در پنجره
my_label.pack()

# چند روش برای تغییر متن Label:
# my_label["text"] = "New text"
# my_label.config(text="New text")


# --------------------------------------------------
# Entry
# --------------------------------------------------

# Entry یک ورودی متنی تک‌خطی است.
entry = tk.Entry(
    window,
    width=20,  # عرض Entry بر اساس تعداد تقریبی کاراکترها
)

# قرار دادن یک متن اولیه داخل Entry
# عدد 0 یعنی متن از ابتدای Entry وارد شود.
entry.insert(0, "Hello World")

# نمایش Entry در پنجره
entry.pack()

# دریافت مقدار فعلی Entry و چاپ آن
print("Entry value:", entry.get())


# --------------------------------------------------
# Button
# --------------------------------------------------

# Button برای ساخت دکمه استفاده می‌شود.
button = tk.Button(
    window,
    text="Click Me",

    # با کلیک روی دکمه، تابع button_clicked اجرا می‌شود.
    # توجه: نام تابع را بدون پرانتز می‌نویسیم.
    command=button_clicked,
)

# نمایش دکمه در پنجره
button.pack()


# --------------------------------------------------
# Text
# --------------------------------------------------

# Text برای دریافت متن‌های چندخطی استفاده می‌شود.
text_box = tk.Text(
    window,
    width=50,  # عرض Text
    height=2,  # ارتفاع Text بر اساس تعداد خطوط
)

# قرار دادن یک متن اولیه داخل Text
# "1.0" یعنی خط اول، کاراکتر صفر
text_box.insert("1.0", "Writing some characters")

# نمایش Text در پنجره
text_box.pack()

# قرار دادن مکان‌نما داخل Text
text_box.focus_set()

# دریافت تمام محتوای Text
# "1.0" یعنی از اولین کاراکتر
# "end-1c" یعنی تا انتهای متن، منهای یک کاراکتر
# این کاراکتر حذف‌شده همان Enter اضافی tkinter است.
text_content = text_box.get("1.0", "end-1c")
print("Text content:", text_content)


# --------------------------------------------------
# Spinbox
# --------------------------------------------------

# Spinbox به کاربر اجازه می‌دهد یک مقدار را
# با دکمه‌های بالا و پایین انتخاب کند.
spinbox = tk.Spinbox(
    window,
    from_=0,                 # حداقل مقدار
    to=10,                   # حداکثر مقدار
    width=5,                 # عرض Spinbox
    command=spinbox_used,    # تابعی که هنگام تغییر مقدار اجرا می‌شود
)

# نمایش Spinbox در پنجره
spinbox.pack()


# --------------------------------------------------
# Scale
# --------------------------------------------------

# Scale یک نوار لغزنده برای انتخاب مقدار است.
scale = tk.Scale(
    window,
    from_=0,             # حداقل مقدار
    to=100,              # حداکثر مقدار
    command=scale_used,  # هنگام حرکت دادن Scale اجرا می‌شود
)

# نمایش Scale در پنجره
scale.pack()


# --------------------------------------------------
# Checkbutton
# --------------------------------------------------

# IntVar یک متغیر مخصوص tkinter است.
# وضعیت Checkbutton داخل این متغیر ذخیره می‌شود.
checked_state = tk.IntVar(value=0)

# ساخت Checkbutton
checkbutton = tk.Checkbutton(
    window,
    text="Is On?",

    # اتصال وضعیت Checkbutton به متغیر checked_state
    variable=checked_state,

    # اجرای تابع هنگام فعال یا غیرفعال کردن Checkbutton
    command=checkbutton_used,
)

# نمایش Checkbutton در پنجره
checkbutton.pack()


# --------------------------------------------------
# RadioButton
# --------------------------------------------------

# متغیر مشترک برای RadioButtonها
# مقدار گزینه انتخاب‌شده داخل این متغیر ذخیره می‌شود.
radio_state = tk.IntVar(value=1)

# گزینه اول
radio_button1 = tk.Radiobutton(
    window,
    text="Option 1",
    variable=radio_state,  # متغیر مشترک بین گزینه‌ها
    value=1,               # مقدار این گزینه
    command=radio_used,
)

# گزینه دوم
radio_button2 = tk.Radiobutton(
    window,
    text="Option 2",
    variable=radio_state,  # همان متغیر مشترک
    value=2,               # مقدار متفاوت برای این گزینه
    command=radio_used,
)

# نمایش RadioButtonها در پنجره
radio_button1.pack()
radio_button2.pack()


# --------------------------------------------------
# Listbox
# --------------------------------------------------

# Listbox برای نمایش یک لیست از آیتم‌ها استفاده می‌شود.
listbox = tk.Listbox(
    window,
    height=4,  # تعداد ردیف‌هایی که نمایش داده می‌شوند
)

# لیست میوه‌ها
fruits = ["Apple", "Pear", "Orange", "Banana"]

# اضافه کردن میوه‌ها به Listbox
for fruit in fruits:
    # "end" یعنی آیتم جدید به انتهای Listbox اضافه شود.
    listbox.insert("end", fruit)

# اتصال رویداد انتخاب یک آیتم به تابع listbox_used
# هر بار که انتخاب Listbox تغییر کند، این تابع اجرا می‌شود.
listbox.bind("<<ListboxSelect>>", listbox_used)

# نمایش Listbox در پنجره
listbox.pack()


# --------------------------------------------------
# اجرای برنامه
# --------------------------------------------------

# mainloop پنجره را باز نگه می‌دارد و منتظر رویدادهایی
# مانند کلیک، تایپ و انتخاب کاربر می‌ماند.
# این دستور معمولاً باید آخرین دستور برنامه tkinter باشد.
window.mainloop()
