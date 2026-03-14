# import tkinter as tk
# from tkinter import messagebox
# import random

# try:
#     from PIL import Image, ImageTk
# except ImportError:
#     messagebox.showerror("Error", "Pillow install nahi hai. Terminal mein likho: pip install Pillow")
#     exit()

# frames = []
# frame_index = 0
# animation_id = None

# # Celebration GIF animate karne wala function
# def animate_gif(label, delay=100):
#     global frame_index, animation_id
#     if len(frames) > 0:
#         frame_index = (frame_index + 1) % len(frames)
#         label.configure(image=frames[frame_index])
#         animation_id = label.after(delay, animate_gif, label, delay)

# # Jab wo 'Yes' dabaye
# def maan_gayi():
#     pop_up = tk.Toplevel(root)
#     pop_up.title("CELEBRATION! 🎉")
#     pop_up.geometry("450x450")
#     pop_up.configure(bg="#ffe4e1")

#     gif_path = "celebration.gif" # File yahan honi chahiye
#     global frames, frame_index
#     frames = [] 
#     frame_index = 0

#     try:
#         with Image.open(gif_path) as img:
#             for frame_num in range(0, img.n_frames):
#                 img.seek(frame_num)
#                 frames.append(ImageTk.PhotoImage(img.copy()))
        
#         gif_label = tk.Label(pop_up, bg="#ffe4e1")
#         gif_label.pack(pady=20)
#         animate_gif(gif_label, 50)
        
#     except FileNotFoundError:
#         lbl_msg = tk.Label(pop_up, text="Aishu maan gayi! ❤️\n(Animation missing - 'celebration.gif' not found)", font=("Helvetica", 12), bg="#ffe4e1", fg="#cc0000")
#         lbl_msg.pack(pady=50)

#     final_text = (
#         "Thank you meri Chuzuuuu! ❤️\n"
#         "Mera din ban gaya! I promise aage se apka Chomu aisi ghalti nahi karega.\n"
#         "I love you Aishu!"
#     )
#     lbl_celebration = tk.Label(pop_up, text=final_text, font=("Helvetica", 14, "bold"), bg="#ffe4e1", fg="#4a0e2e", justify="center")
#     lbl_celebration.pack(pady=20)

#     root.after(5000, lambda: [root.destroy(), pop_up.destroy()])

# # Jab mouse 'No' button par aaye
# def bhaag_jao(event):
#     # RESPONSIVE LOGIC: Screen ki current width aur height check karo
#     win_width = root.winfo_width()
#     win_height = root.winfo_height()
#     btn_width = btn_no.winfo_width()
#     btn_height = btn_no.winfo_height()
    
#     # Button ko screen se bahar jane se rokne ke liye boundaries
#     max_x = win_width - btn_width - 20
#     max_y = win_height - btn_height - 20
    
#     if max_x <= 0: max_x = 100
#     if max_y <= 0: max_y = 100
    
#     new_x = random.randint(20, max_x)
#     new_y = random.randint(100, max_y)
    
#     # Button ko nayi jagah par bhejna (relx/rely hatana padega absolute movement ke liye)
#     btn_no.place(x=new_x, y=new_y, relx=0, rely=0, anchor="nw")
    
#     pleads = [
#         "Aise na karo na chuzu 🥺",
#         "Maan jao meri kuchu puchu 😭",
#         "Chuzuu please ek chance dedo! 🙏",
#         "Main rone lag jaunga ab sach mein 😢",
#         "Aishu please thoda sa taras khao apne Naufel par 🥺",
#         "Nahi ka option hi nahi hai madam jii! ❤️",
#         "Tumhari smile ke bina sab bekaar hai 😔",
#         "Acha kan pakar ke sorry! Ab toh maan jao 🥺"
#     ]
#     lbl_msg.config(text=random.choice(pleads), fg="#cc0000")

# # Main GUI Window setup
# root = tk.Tk()
# root.title("Apology for My Aishu ❤️")
# root.geometry("700x550")
# root.configure(bg="#ffb6c1")

# # App ki window ko resizable banana
# root.resizable(True, True)

# # Responsive Layouts (Place command mein relx aur rely ka magic)
# lbl_title = tk.Label(root, text="I'm So Sorry Aishu! 🥺", font=("Comic Sans MS", 28, "bold"), bg="#ffb6c1", fg="#8b0000")
# lbl_title.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

# initial_msg = (
#     "Meri pyari chuzu, kuchu puchu, aur meri sab se sweet Chuzuuuuu,\n\n"
#     "Mujhe pata hai mujhse ghalti hui hai aur tum naraz ho.\n"
#     "Lekin tumhare bina mera din bilkul acha nahi guzarta.\n"
#     "Please mujhe maaf kar do na? 🥺"
# )
# lbl_msg = tk.Label(root, text=initial_msg, font=("Helvetica", 14, "bold"), bg="#ffb6c1", fg="#4a0e2e", justify="center")
# lbl_msg.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

# btn_yes = tk.Button(root, text="Theek hai, Maan gayi ❤️", font=("Helvetica", 14, "bold"), 
#                     bg="#ff1493", fg="white", command=maan_gayi, width=20, relief="raised", bd=4, cursor="heart")
# # 30% screen ki width par Left side
# btn_yes.place(relx=0.3, rely=0.75, anchor=tk.CENTER)

# btn_no = tk.Button(root, text="Nahi, abhi bhi gussa hu 😡", font=("Helvetica", 14, "bold"), 
#                    bg="#333333", fg="white", width=20, relief="raised", bd=4)
# # 70% screen ki width par Right side
# btn_no.place(relx=0.7, rely=0.75, anchor=tk.CENTER)

# btn_no.bind("<Enter>", bhaag_jao)

# # Ek trick takay bhaagte waqt window ka size update hota rahay
# root.update_idletasks()

# root.mainloop()