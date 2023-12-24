import customtkinter
import tkinter as tk
from tkinter import ttk
import random
from tkinter import ttk, messagebox, filedialog

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

def generate_fairy_tale(name, age, city, country, gender, occupation, goal, animal, villain, tale_type, adjective, item):
    tale_templates = {
        'Adventure': [
            f"{name}, {age} yaşında, {city} şehrinde yaşayan cesur bir {gender} {occupation}, bir gün {country} ülkesinin derin ormanlarına macera dolu bir yolculuk yapmaya karar vermiş. "
            f"Yolda, {animal} adlı sadık dostuyla karşılaşmış. Birlikte, {adjective} bir {villain} ile savaşmışlar ve krallıklarını kurtarmışlar. "
            f"Yolculuk boyunca {item} bulmuş ve bu ona büyük bir güç kazandırmış. Uzun bir süre sonra, kahramanlarımız krallıklarına sağ salim dönmüş ve halklarına huzur getirmişler."
        ],
        'Fantasy': [
            f"Bir zamanlar {name} adında bir büyücü, {age} yaşında, {city} şehrinde yaşarmış. "
            f"{name}, sihirli güçlere sahip ve {country} ülkesindeki insanlara yardım eden biriymiş. "
            f"Bir gün, sihirli bir ormanda kaybolmuş ve orada {animal} ile karşılaşmış. "
            f"Birlikte, {adjective} bir {villain} tarafından tehdit edilen krallığı kurtarmışlar. "
            f"Sonunda, büyülü bir {item} kullanarak barışı sağlamışlar. Halkları artık büyülü kahramanlarına minnettarlıkla bakıyor."
        ],
        'Mystery': [
            f"{name} adlı bir dedektif, {age} yaşında, {city} şehrinde gizemli olayları çözmeye kararlı bir şekilde çalışan biriydi. "
            f"{country} ülkesindeki esrarengiz bir vakayı çözmek için akıl almaz bir zekaya sahipti. "
            f"{animal} adlı bir hayvanın yardımıyla, karmaşık ipuçlarını çözmüş ve {adjective} bir {villain} ortaya çıkarmış. "
            f"Sonunda, kaybolan {item} bulmuş ve gerçeği ortaya çıkarmış. Dedektifimiz, çözdüğü gizemle ünlü bir kahraman olmuş."
        ],
        'Romance': [
            f"{name} adlı genç bir aşık, {age} yaşında, {city} şehrinde aşkı arayan biriydi. "
            f"Bir gün, {country} ülkesindeki güzel bir kır evinde karşılaştığı {animal} ile arasında özel bir bağ kurmuş. "
            f"Birlikte, hayatlarının aşkını bulmaya karar vermişler, ancak karşılarına çıkan engelleri aşmaları gerekecek. "
            f"Aşklarını güçlendirmek için birlikte {item} keşfetmişler. Birbirlerine olan sevgileri, krallıklarını birleştirmiş ve büyük bir düğünle kutlanmış."
        ],
        'Sci-Fi': [
            f"{name} adlı bir bilim kahramanı, {age} yaşında, {city} şehrinde geleceğin teknolojisini keşfetmeye karar vermiş. "
            f"Bir gün, {country} ülkesindeki gizemli bir laboratuvarda çalışırken, {animal} adlı bir yapay zeka ile tanışmış. "
            f"Birlikte, dünyayı kurtarmak için uzak galaksilere yolculuk yapacak ve bilinmeyen gezegenlerde {adjective} bir {villain} ile savaşacaklar. "
            f"Aynı zamanda, uzaylılarla iletişim kurmak için {item} kullanmışlar. Kahramanlarımız, gezegenler arası barışı sağlamış ve bilinmeyen uzaylılarla dostça ilişkiler kurmuşlar."
        ]
    }

    selected_template = random.choice(tale_templates.get(tale_type, []))
    tale = selected_template.format(
        name=name, age=age, city=city, country=country, gender=gender,
        occupation=occupation, goal=goal, animal=animal, villain=villain,
        tale_type=tale_type, adjective=adjective, item=item
    )
    return tale

def create_fairy_tale():
    name = entry_name.get()
    age = entry_age.get()
    city = entry_city.get()
    country = entry_country.get()
    gender = gender_var.get()
    occupation = entry_occupation.get()
    goal = entry_goal.get()
    animal = entry_animal.get()
    villain = entry_villain.get()
    tale_type = tale_type_var.get()
    adjective = entry_adjective.get()
    item = entry_item.get()
  
    if name and age and city and country and gender and occupation and goal and animal and villain and tale_type and adjective and item:
        tale = generate_fairy_tale(name, age, city, country, gender, occupation, goal, animal, villain, tale_type, adjective, item)
        text_output.config(state='normal')
        text_output.delete('1.0', 'end')
        text_output.insert('1.0', tale)
        text_output.config(state='disabled')

        text_output.configure(font=('Markasal Font', 12), bg='black', fg='white') 

    else:
        messagebox.showwarning("Hata", "Lütfen tüm bilgileri eksiksiz girin.")

def save_fairy_tale():
    tale = text_output.get('1.0', 'end-1c')
    if tale:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(tale)
            messagebox.showinfo("Başarılı", "Masal başarıyla kaydedildi.")
    else:
        messagebox.showwarning("Hata", "Önce bir masal oluşturun.")

root = customtkinter.CTk()
root.geometry('1920x1080')
root.iconbitmap('./ico/icon.ico')
root.title("Kış Masalım")

paned_window = ttk.PanedWindow(root, orient=tk.HORIZONTAL)

left_pane = customtkinter.CTkFrame(paned_window)
left_pane.grid(row=0, column=0, sticky='nsew')
grs = customtkinter.CTkTabview(root)
grs.grid(row=0, column=0, sticky='nsew')

frame = customtkinter.CTkFrame(grs)
frame.grid(row=0, column=0, sticky='nsew')

label_name = customtkinter.CTkLabel(frame, text='Adınız:')
label_name.grid(row=0, column=0, padx=10, pady=10)

entry_name = customtkinter.CTkEntry(frame)
entry_name.grid(row=0, column=1, padx=10, pady=10)

label_age = customtkinter.CTkLabel(frame, text='Yaşınız:')
label_age.grid(row=1, column=0, padx=10, pady=10)

entry_age = customtkinter.CTkEntry(frame)
entry_age.grid(row=1, column=1, padx=10, pady=10)

label_city = customtkinter.CTkLabel(frame, text='Şehir:')
label_city.grid(row=2, column=0, padx=10, pady=10)

entry_city = customtkinter.CTkEntry(frame)
entry_city.grid(row=2, column=1, padx=10, pady=10)

label_country = customtkinter.CTkLabel(frame, text='Ülke:')
label_country.grid(row=3, column=0, padx=10, pady=10)

entry_country = customtkinter.CTkEntry(frame)
entry_country.grid(row=3, column=1, padx=10, pady=10)

label_gender = customtkinter.CTkLabel(frame, text='Cinsiyet:')
label_gender.grid(row=4, column=0, padx=10, pady=10)

gender_var = tk.StringVar()
gender_var.set('Erkek')

gender_options = ['Erkek', 'Kadın']
gender_menu = tk.OptionMenu(frame, gender_var, *gender_options)
gender_menu.grid(row=4, column=1, padx=10, pady=10)

label_occupation = customtkinter.CTkLabel(frame, text='Meslek:')
label_occupation.grid(row=5, column=0, padx=10, pady=10)

entry_occupation = customtkinter.CTkEntry(frame)
entry_occupation.grid(row=5, column=1, padx=10, pady=10)

label_goal = customtkinter.CTkLabel(frame, text='Hedef:')
label_goal.grid(row=6, column=0, padx=10, pady=10)

entry_goal = customtkinter.CTkEntry(frame)
entry_goal.grid(row=6, column=1, padx=10, pady=10)

label_animal = customtkinter.CTkLabel(frame, text='Evcil Hayvanınız:')
label_animal.grid(row=7, column=0, padx=10, pady=10)

entry_animal = customtkinter.CTkEntry(frame)
entry_animal.grid(row=7, column=1, padx=10, pady=10)

label_villain = customtkinter.CTkLabel(frame, text='Kötü Karakter:')
label_villain.grid(row=8, column=0, padx=10, pady=10)

entry_villain = customtkinter.CTkEntry(frame)
entry_villain.grid(row=8, column=1, padx=10, pady=10)

label_tale_type = customtkinter.CTkLabel(frame, text='Masal Türü:')
label_tale_type.grid(row=9, column=0, padx=10, pady=10)

tale_type_var = tk.StringVar()
tale_type_var.set('Adventure')

tale_type_options = ['Adventure', 'Fantasy', 'Mystery', 'Romance', 'Sci-Fi']
tale_type_menu = tk.OptionMenu(frame, tale_type_var, *tale_type_options)
tale_type_menu.grid(row=9, column=1, padx=10, pady=10)

label_adjective = customtkinter.CTkLabel(frame, text='Sıfat:')
label_adjective.grid(row=10, column=0, padx=10, pady=10)

entry_adjective = customtkinter.CTkEntry(frame)
entry_adjective.grid(row=10, column=1, padx=10, pady=10)

label_item = customtkinter.CTkLabel(frame, text='Özel Eşya:')
label_item.grid(row=11, column=0, padx=10, pady=10)


entry_item = customtkinter.CTkEntry(frame)
entry_item.grid(row=11, column=1, padx=10, pady=10)

button_generate = customtkinter.CTkButton(frame, text='Masal Oluştur', command=create_fairy_tale)
button_generate.grid(row=12, column=0, pady=10)

button_save = customtkinter.CTkButton(frame, text='Masalı Kaydet', command=save_fairy_tale)
button_save.grid(row=12, column=1, pady=10)

text_output = tk.Text(frame, wrap='word', state='disabled', height=20, width=90)
text_output.grid(row=13, column=0, columnspan=2, padx=50, pady=10)

root.configure(bg='black')

root.mainloop()
