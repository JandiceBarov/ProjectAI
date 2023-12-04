import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
from keras.preprocessing import image
from keras.models import load_model

model = load_model('C:/Data/ModelEyes.h5')

def process_image():
    file_path = filedialog.askopenfilename()
    img = Image.open(file_path)
    img = img.resize((224, 224))  
    img = np.array(img)
    img = np.expand_dims(img, axis=0)

    predictions = model.predict(img)
    print(predictions)
    predicted_class = np.argmax(predictions)
    if predicted_class == 0:
        result = "Норма"
    elif predicted_class == 1:
        result = "Катаракта"
    elif predicted_class == 2:
        result = "Глаукома"
    elif predicted_class == 3:
        result = "Миопия"
    elif predicted_class == 4:
        result = "Возрастная макулодистрофия"
    result_label.config(text=result)
    
    if hasattr(process_image, 'photo'):
        process_image.photo_label.pack_forget()
    photo = ImageTk.PhotoImage(Image.open(file_path).resize((200, 200), Image.ANTIALIAS))
    process_image.photo_label = tk.Label(root, image=photo)
    process_image.photo_label.image = photo
    process_image.photo_label.pack(pady=10)

root = tk.Tk()
root.title("AppleEye")

width = root.winfo_screenwidth() // 2
height = root.winfo_screenheight() // 2
x = (root.winfo_screenwidth() - width) // 2
y = (root.winfo_screenheight() - height) // 2
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))


browse_button = tk.Button(root, text="Выбрать изображение", command=process_image)
browse_button.pack(pady=20)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
