from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
from datetime import datetime
import socket


# Logo_Image // Properties // Execute // Project_Info

class Logo_Image():
    def __init__(self, window):
        frame = Frame(window)
        frame.grid(row=0, column=2, sticky=NW, pady=10)
        self.width = 480
        self.height = 230
        self.image = Image.open('/Users/hannahlee/PycharmProjects/AwesomeProject/controllers/resources/Logo.png').convert("RGB")
        self.copy = self.image.copy()
        self.photo = ImageTk.PhotoImage(self.image)
        self.label = Label(frame, image=self.photo)
        self.label.bind('<Configure>', self.resize_image())
        self.label.grid(row=0, column=2, sticky=NW)

        Properties(frame).__init__(frame)
        Execute(frame).__init__(frame)

    def resize_image(event):
        new_width = event.width
        new_height = event.height
        image = event.copy.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        event.label.config(image = photo)
        event.label.image = photo


class Properties():
    def __init__(self, window):
        frame = Frame(window)
        frame.grid(row=1, column=2, sticky=NW, pady=30)

        label0 = Label(frame, text="Properties", font=("Arial", 13))
        label0.grid(row=0, column=0, sticky=NW)

        label1 = Label(frame)
        label1.grid(row=1, column=0, sticky=NW, pady=10)
        label_wave = Label(label1, text="WaveLength Range(nm) : ")
        entry1 = Entry(label1)
        label_wave.grid(row=0, column=0, sticky=NW)
        entry1.grid(row=0, column=1, sticky=NW)

        label2 = Label(frame)
        label2.grid(row=2, column=0, sticky=NW, pady=10)
        label_angle = Label(label2, text="Angle Range(degree) : ")
        entry2 = Entry(label2)
        label_angle.grid(row=0, column=0, sticky=NW)
        entry2.grid(row=0, column=1, sticky=NW)

        label3 = Label(frame)
        label3.grid(row=3, column=0, sticky=NW, pady=10)
        label_calc = Label(label3, text="Calculation Types:")
        label_calc.grid(row=1, column=0, sticky=NW)
        box0 = Checkbutton(label3, variable=IntVar(), text="Mode Analysis")
        box0.grid(row=1, column=1, sticky=NW, padx=5)
        box1 = Checkbutton(label3, variable=IntVar(), text="Emission Spectrum")
        box1.grid(row=2, column=1, sticky=NW, padx=5)
        box2 = Checkbutton(label3, variable=IntVar(), text="Power Dissipation")
        box2.grid(row=3, column=1, sticky=NW, padx=5)

        label4 = Label(frame)
        label4.grid(row=4, column=0, sticky=NW, pady=10)
        label40 = Label(label0, text="Progress", font=("Arial", 13))
        label40.grid(row=0, column=0, sticky=NW)
        self.progress_bar = Progressbar(label4, orient='horizontal', length=480, mode='determinate', style="TProgressbar")
        self.progress_bar.grid(row=0, column=0, columnspan=3, sticky=NW)
        button = Button(label4, text="GPU Calc.", command=self.run_progressbar)
        button.grid(row=1, column=0, sticky=NW, pady=5)
        stop_button = Button(label4, text="Stop", command=self.stop_progressbar)
        stop_button.grid(row=1, column=1, sticky=NW, pady=5)
        view_result = Button(label4, text="View Result")
        view_result.grid(row=1, column=2, sticky=NW, pady=5)

    def run_progressbar(self):
        self.progress_bar["maximum"] = 100
        for i in range(101):
            self.progress_bar["value"] = i
            self.progress_bar.update()
        self.progress_bar["value"] = 0

    def stop_progressbar(self):
        self.progress_bar.stop()


class Execute():
    def __init__(self, window):
        frame = Frame(window)
        frame.grid(row=2, column=2, sticky=NW)

        label1 = Label(frame)
        label11 = Label(label1, text="Project Information", font=("Arial", 13))
        label_name = Label(label1, text="Name:")
        label_design = Label(label1, text="Designer:")
        label_operator = Label(label1, text="Operator:")
        label_analyze = Label(label1, text="Analyzer:")
        label_cdate = Label(label1, text="Creation Date:")
        label_mdate = Label(label1, text="Modified Date:")
        label_macaddr = Label(label1, text="Mac Addr.:")
        label_ipaddr = Label(label1, text="IP Addr.:")

        label_name_a = Label(label1, text="2PPlAn_PL")
        label_design_a = Label(label1, text="Hannah Lee")
        label_operator_a = Label(label1, text="Hannah Lee")
        label_analyze_a = Label(label1, text="Hannah Lee")
        label_cdate_a = Label(label1, text=datetime.today().strftime('%Y-%m-%d'))
        label_mdate_a = Label(label1, text=datetime.today().strftime('%Y-%m-%d'))
        label_macaddr_a = Label(label1, text=self.get_ip())
        label_ipaddr_a = Label(label1, text=self.get_ip())

        label1.grid(row=0, column=0, sticky=NW)
        label11.grid(row=0, column=0, sticky=NW, pady=5)
        label_name.grid(row=1, column=0, sticky=NW)
        label_design.grid(row=2, column=0, sticky=NW)
        label_operator.grid(row=3, column=0, sticky=NW)
        label_analyze.grid(row=4, column=0, sticky=NW)
        label_cdate.grid(row=5, column=0, sticky=NW)
        label_mdate.grid(row=6, column=0, sticky=NW)
        label_macaddr.grid(row=7, column=0, sticky=NW)
        label_ipaddr.grid(row=8, column=0, sticky=NW)

        label_name_a.grid(row=1, column=1, sticky=NW)
        label_design_a.grid(row=2, column=1, sticky=NW)
        label_operator_a.grid(row=3, column=1, sticky=NW)
        label_analyze_a.grid(row=4, column=1, sticky=NW)
        label_cdate_a.grid(row=5, column=1, sticky=NW)
        label_mdate_a.grid(row=6, column=1, sticky=NW)
        label_macaddr_a.grid(row=7, column=1, sticky=NW)
        label_ipaddr_a.grid(row=8, column=1, sticky=NW)

    def get_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP