import tkinter as tk
from tkinter import messagebox
import random
# GIF handle karne ke liye PIL library chahiye
try:
    from PIL import Image, ImageTk
except ImportError:
    messagebox.showerror("Error", "Is animated pop-up ko chalane ke liye 'Pillow' library install karni hogi. Terminal mein likho: pip install Pillow")
    exit()

# Global variables animation frames aur counter ke liye
frames = []
frame_index = 0
animation_id = None

# GIF animate karne wala function
def animate_gif(label, delay=100): # delay ms mein hai
    global frame_index, animation_id
    if len(frames) > 0:
        # Agla frame show karna
        frame_index = (frame_index + 1) % len(frames)
        label.configure(image=frames[frame_index])
        # function ko dobara 'after' delay ke saath call karna
        animation_id = label.after(delay, animate_gif, label, delay)

# Jab wo 'Yes' dabaye, animated pop-up dikhane ke liye
def maan_gayi():
    # 'No' button ki logic cancel karna (agar applicable ho, yahan animated nahi hai par good practice hai)
    
    # Naya custom Toplevel window (pop-up) banana
    pop_up = tk.Toplevel(root)
    pop_up.title("CELEBRATION! 🎉")
    pop_up.geometry("400x350")
    pop_up.configure(bg="#ffe4e1")

    # Celebration animation (GIF) load karna
    gif_path = "celebration.gif" # <- YAHAN APNI GIF FILE KA NAAM LIKHO
    
    # Global frames list reset karna is animation ke liye
    global frames, frame_index
    frames = [] 
    frame_index = 0

    try:
        with Image.open(gif_path) as img:
            # Saare frames nikal kar frames list mein dalna
            for frame_num in range(0, img.n_frames):
                img.seek(frame_num)
                frames.append(ImageTk.PhotoImage(img.copy()))
        
        # Animation display karne wala label
        gif_label = tk.Label(pop_up, bg="#ffe4e1")
        gif_label.pack(pady=20)
        # Animation start karna
        animate_gif(gif_label, 50) # delay 50ms (is loop concept ko samajhne ke liye diagram dekho)
        
    except FileNotFoundError:
        # Agar GIF nahi mili, toh standard message show karna
        lbl_msg = tk.Label(pop_up, text="Aishu maan gayi! ❤️\n(Animation missing - GIF file not found)", font=("Helvetica", 12), bg="#ffe4e1", fg="#cc0000")
        lbl_msg.pack(pady=50)

    # Tumhara final wording wala celebration message display karna
    final_text = (
        "Thank you meri Chuzuuuu! ❤️\n"
        "Mera din ban gaya! I promise aage se apka Chomu aisi ghalti nahi karega.\n"
        "I love you Aishu!"
    )
    lbl_celebration = tk.Label(pop_up, text=final_text, font=("Helvetica", 12, "bold"), bg="#ffe4e1", fg="#4a0e2e", justify="center")
    lbl_celebration.pack(pady=20)

    # 5 seconds baad, sab windows band kar dena automatically
    root.after(5000, lambda: [root.destroy(), pop_up.destroy()])

# Jab mouse 'No' button par aaye
def bhaag_jao(event):
    # Button ko nayi jagah par bhejna
    new_x = random.randint(50, 400)
    new_y = random.randint(150, 450)
    btn_no.place(x=new_x, y=new_y)
    
    # Har dafa naya emotional aur cute message show karna
    pleads = [
        "Aise na karo na chuzu 🥺",
        "Maan jao meri kuchu puchu 😭",
        "Chuzuu please ek chance dedo! 🙏",
        "Main rone lag jaunga ab sach mein 😢",
        "Aishu please thoda sa taras khao apne Naufel par 🥺",
        "Nahi ka option hi nahi hai madam jii! ❤️",
        "Tumhari smile ke bina sab bekaar hai 😔",
        "Acha kan pakar ke sorry! Ab toh maan jao 🥺"
    ]
    lbl_msg.config(text=random.choice(pleads), fg="#cc0000", font=("Helvetica", 16, "bold"))

# Main GUI Window setup
root = tk.Tk()
root.title("Apology for My Aishu ❤️")
root.geometry("650x550")
root.configure(bg="#ffb6c1") # Premium Light Pink background

# Header Title
lbl_title = tk.Label(root, text="I'm So Sorry Aishu! 🥺", font=("Comic Sans MS", 28, "bold"), bg="#ffb6c1", fg="#8b0000")
lbl_title.pack(pady=30)

# Pehla Dil ki baat wala message
initial_msg = (
    "Meri pyari chuzu, kuchu puchu, aur meri sab se sweet Chuzuuuuu,\n\n"
    "Mujhe pata hai mujhse ghalti hui hai aur tum naraz ho.\n"
    "Lekin tumhare bina mera din bilkul acha nahi guzarta.\n"
    "Please mujhe maaf kar do na? 🥺"
)
lbl_msg = tk.Label(root, text=initial_msg, font=("Helvetica", 14, "bold"), bg="#ffb6c1", fg="#4a0e2e", justify="center")
lbl_msg.pack(pady=30)

# Button 1: Maan Gayi (Yes) - Yeh button hamesha ek jagah rahega
# Is button ko triggers maan_gayi() jo custom animated pop-up banata hai
btn_yes = tk.Button(root, text="Theek hai, Maan gayi ❤️", font=("Helvetica", 14, "bold"), 
                    bg="#ff1493", fg="white", command=maan_gayi, width=20, relief="raised", bd=4, cursor="heart")
btn_yes.place(x=80, y=400)

# Button 2: Gussa Hu (No) - Yeh button bhaagega
btn_no = tk.Button(root, text="Nahi, abhi bhi gussa hu 😡", font=("Helvetica", 14, "bold"), 
                   bg="#333333", fg="white", width=20, relief="raised", bd=4)
btn_no.place(x=350, y=400)

# Mouse hover event ko link karna
btn_no.bind("<Enter>", bhaag_jao)

# Animation loop concept samajhne ke liye diagram dekho
# 
root.mainloop()