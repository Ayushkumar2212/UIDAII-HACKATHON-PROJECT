from tkinter import *
from tkinter import filedialog, messagebox
import os

# ================= ROOT =================
root = Tk()
root.title("Aadhaar Suvidha Kendra")
root.geometry("1050x800")

# ================= HEADING =================
Label(root, text="AADHAAR SUVIDHA KENDRA",
      fg="red", font=("Arial", 18, "bold")).pack(pady=10)

# ================= TEXT AREA =================
text_area = Text(root, height=8, width=120, font=("Arial", 11))
text_area.pack(pady=8)

# ================= FILE UPLOAD =================
def read_file(file_no, name):
    file_path = filedialog.askopenfilename(
        title=f"Select {name} ZIP",
        initialdir=os.getcwd(),
        filetypes=[("ZIP Files", ".zip"), ("All Files", ".*")]
    )
    if file_path:
        text_area.insert(END, f"{name} File Uploaded:\n")
        text_area.insert(END, os.path.basename(file_path) + "\n")
        text_area.insert(END, "-" * 90 + "\n")

# ================= BUTTONS =================
btn = Frame(root)
btn.pack(pady=10)

Button(btn, text="Upload Enrollment ZIP",
       command=lambda: read_file(1, "Enrollment")).grid(row=0, column=0, padx=10)

Button(btn, text="Upload Biometric ZIP",
       command=lambda: read_file(2, "Biometric")).grid(row=0, column=1, padx=10)

Button(btn, text="Upload Demographic ZIP",
       command=lambda: read_file(3, "Demographic")).grid(row=0, column=2, padx=10)

# ================= DATA =================
age_data = {
    "Enrollment": {"0-15": 4200, "17-51": 3800},
    "Biometric": {"0-15": 2500, "17-51": 5200},
    "Demographic": {"0-15": 3100, "17-51": 2900}
}

region_data = {
    "Enrollment": {"Bihar": 500, "UP": 700, "Delhi": 300},
    "Biometric": {"Bihar": 450, "UP": 600, "Delhi": 550},
    "Demographic": {"Bihar": 400, "UP": 350, "Delhi": 480}
}

# ================= INFO =================
Label(root,
      text=("Press 1: Charges | Press 2: Max Age (All Services) | "
            "Press 4: Max Region (All Services)\n"
            "Press 5: Enrollment Graph | Press 6: Biometric Graph | Press 7: Demographic Graph"),
      fg="purple", font=("Arial", 12, "bold")).pack(pady=12)

output_frame = Frame(root)
output_frame.pack(pady=10)

# ================= GRAPH FUNCTION =================
def draw_graph(title, data_dict):
    win = Toplevel(root)
    win.title(title)
    win.geometry("700x500")

    Label(win, text=title, font=("Arial", 14, "bold")).pack(pady=10)
    canvas = Canvas(win, width=600, height=350, bg="white")
    canvas.pack()

    max_val = max(data_dict.values())
    bar_w, gap, x0, y0 = 80, 140, 150, 300

    for i, (k, v) in enumerate(data_dict.items()):
        h = (v / max_val) * 200
        x1 = x0 + i * gap
        y1 = y0 - h
        x2 = x1 + bar_w

        canvas.create_rectangle(x1, y1, x2, y0, fill="skyblue")
        canvas.create_text((x1+x2)//2, y1-10, text=v)
        canvas.create_text((x1+x2)//2, y0+15, text=k)

# ================= KEY HANDLER =================
def show_output(event):
    key = event.char
    for w in output_frame.winfo_children():
        w.destroy()

    if key == '1':
        Label(output_frame, text="Official Aadhaar Service Charges",
              font=("Arial", 15, "bold")).pack(anchor="w")
        for c in [
            "Aadhaar Enrolment: FREE",
            "Mandatory Biometric Update: FREE",
            "Biometric Update: ₹75",
            "PVC Card: ₹75"
        ]:
            Label(output_frame, text=c, font=("Arial", 12)).pack(anchor="w")

    elif key == '2':
        Label(output_frame, text="Max Age Group (Service-wise)",
              font=("Arial", 14, "bold")).pack(anchor="w")
        for service, ages in age_data.items():
            max_age = max(ages, key=ages.get)
            Label(output_frame,
                  text=f"{service} → {max_age} ({ages[max_age]})",
                  font=("Arial", 12)).pack(anchor="w")

    elif key == '4':
        Label(output_frame, text="Max Region (Service-wise)",
              font=("Arial", 14, "bold")).pack(anchor="w")
        for service, regions in region_data.items():
            max_reg = max(regions, key=regions.get)
            Label(output_frame,
                  text=f"{service} → {max_reg} ({regions[max_reg]})",
                  font=("Arial", 12)).pack(anchor="w")

    elif key == '5':
        draw_graph("Enrollment Age-wise Graph", age_data["Enrollment"])

    elif key == '6':
        draw_graph("Biometric Age-wise Graph", age_data["Biometric"])

    elif key == '7':
        draw_graph("Demographic Age-wise Graph", age_data["Demographic"])

root.bind("<Key>", show_output)
root.mainloop()
