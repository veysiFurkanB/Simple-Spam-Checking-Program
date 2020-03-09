from Tkinter import *
import csv
import tkFileDialog
import docclass

class movie_engine(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.grid()
        self.parent = parent
        self.cl = docclass.naivebayes(docclass.getwords)
        self.initUI()

    def initUI(self):
        # Top Header Label
        self.header = Label(self, text="SPAM Checker", font="Arial 10 bold")
        self.header.grid(row=0, column=0, sticky=NSEW, padx=100, pady=5)

        # The Upload Button
        self.upload_button = Button(self, text="Upload SPAM Training File", height=2, width=25, command=self.upload_training_data)
        self.upload_button.grid(row=1, column=0, padx=100, pady=10, sticky=NSEW)

        # Text Box Label
        self.entry_label = Label(self, text="Enter The Text to Check Below")
        self.entry_label.grid(row=2, column=0, padx=100)

        # Input Text Box
        self.entry_box = Text(self, height=10, width=25)
        self.entry_box.grid(row=3, column=0, padx=100, pady=5)

        # Threshold Label
        self.threshold_label = Label(self, text="Threshold Value")
        self.threshold_label.grid(row=4, column=0, padx=100, pady=5, sticky=SW)

        # Threshold Entry Box
        self.threshold_entry = Entry(self)
        self.threshold_entry.grid(row=5, column=0, padx=100, pady=5, sticky=NW)
        self.threshold_entry.insert(END, "3")

        # Tha Analysis Button
        self.analysis_button = Button(self, text="Run Naive Bayes SPAM Checker", height=2, width=25, command=self.run_analysis)
        self.analysis_button.grid(row=6, column=0, padx=100, pady=10, sticky=NSEW)

        # Final Result Text Label
        self.result_text = Label(self, text="Result")
        self.result_text.grid(row=7, column=0, pady=15, sticky=N)

    def upload_training_data(self):                     #
        file_path = tkFileDialog.askopenfilename()      #
        with open(file_path, mode='r') as infile:       # Takes the input from user selection and calls the training function
            reader = csv.reader(infile)                 # with the inputs; ham/spam and text examples
            for i in reader:                            #
                self.cl.train(i[1], i[0])               #

    def run_analysis(self):
        self.text = str(self.entry_box.get("0.0", END))     # The input put by the user into textbox

        # The if statement for if the treshold box is empty, well it has default value but just in case.
        if self.threshold_entry.get() == "":
            self.threshold = 0.0
        else:
            self.threshold = float(self.threshold_entry.get())

        # The try functionalty is for checking wether the training data has selected or not.
        try:
            self.ham_or_spam = str(self.cl.classify(self.text, self.threshold))
            if self.ham_or_spam == "ham":
                self.result_text.config(text=self.ham_or_spam.capitalize(), foreground="darkgreen", font="Arial 10")
            else:
                self.result_text.config(text=self.ham_or_spam.capitalize(), foreground="red", font="Arial 10")
        except(UnboundLocalError):
            self.result_text.config(text="Please upload the spam training set!", foreground='red', font="Arial 10")

root = Tk()
root.title("SPAM CHECKER")
app = movie_engine(root)
app.pack(fill=BOTH, expand=True)
root.mainloop()