from tkintertable import TableCanvas
from pandastable import Table
from tkinter import messagebox as msg
from tkinter import filedialog
import pandas as pd
import xlsxwriter
import io
from tkinter import *
import pip
import importlib
modules = ['pandas', 'tkinter', 'pandastable',
           'tkintertable', 'xlsxwriter', 'openpyxl']
for modname in modules:
    try:
        # try to import the module normally and put it in globals
        globals()[modname] = importlib.import_module(modname)
    except ImportError as e:
        result = pip.main(['install', modname])
        if result != 0:  # if pip could not install it reraise the error
            raise
        else:
            # if the install was sucessful, put modname in globals
            globals()[modname] = importlib.import_module(modname)

io = io.StringIO()

# Use a temp filename to keep pandas happy.
# writer = pd.ExcelWriter('temp.xlsx', engine='xlsxwriter')

# Set the filename/file handle in the xlsxwriter.workbook object.
# writer.book.filename = io

# Write the data frame to the StringIO object.
# pd.DataFrame().to_excel(writer, sheet_name='Sheet1')
# writer.save()
# xlsx_data = io.getvalue()


class csv_to_excel:

    def __init__(self, root):

        self.root = root
        self.file_name = ''
        self.f = Frame(self.root,
                       height=200,
                       width=300)

        # Place the frame on root window
        self.f.pack()

        # Creating label widgets
        self.message_label = Label(self.f,
                                   text='Welcome to Dunnhumby',
                                   font=('Arial', 19, 'underline'),
                                   fg='Green')
        self.message_label2 = Label(self.f,
                                    text='Converter of CSV to Excel file',
                                    font=('Arial', 14, 'underline'),
                                    fg='Red')

        # Buttons
        self.convert_button = Button(self.f,
                                     text='Convert',
                                     font=('Arial', 14),
                                     bg='Orange',
                                     fg='Black',
                                     command=self.convert_csv_to_xls)
        self.display_button = Button(self.f,
                                     text='Display',
                                     font=('Arial', 14),
                                     bg='Green',
                                     fg='Black',
                                     command=self.display_xls_file)
        self.exit_button = Button(self.f,
                                  text='Exit',
                                  font=('Arial', 14),
                                  bg='Red',
                                  fg='Black',
                                  command=root.destroy)

        # Placing the widgets using grid manager
        self.message_label.grid(row=1, column=1)
        self.message_label2.grid(row=2, column=1)
        self.convert_button.grid(row=3, column=0,
                                 padx=0, pady=15)
        self.display_button.grid(row=3, column=1,
                                 padx=10, pady=15)
        self.exit_button.grid(row=3, column=2,
                              padx=10, pady=15)

    def convert_csv_to_xls(self):
        try:
            self.file_name = filedialog.askopenfilename(initialdir='/Desktop',
                                                        title='Select a CSV file',
                                                        filetypes=(('csv file', '*.csv'),
                                                                   ('csv file', '*.csv')))

            df = pd.read_csv(self.file_name)

            # import module
            from datetime import datetime

            # get current date and time
            current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
            print("Current date & time : ", current_datetime)
            # convert datetime obj to string
            str_current_datetime = str(current_datetime)
            # Next - Pandas DF to Excel file on disk
            if (len(df) == 0):
                msg.showinfo('No Rows Selected', 'CSV has no rows')
            else:

                # saves in the current directory
                file_name = "OutputExample"+str_current_datetime+".xlsx"
                with pd.ExcelWriter(file_name, engine='xlsxwriter') as writer:
                    df.to_excel(writer, 'ProductSheet')
                    # writer.save()
                    writer.close()
                    msg.showinfo('Excel file created', 'Excel File created')

        except FileNotFoundError as e:
            msg.showerror('Error in opening file', e)

    def display_xls_file(self):
        try:
            self.file_name = filedialog.askopenfilename(initialdir='/Desktop',
                                                        title='Select a excel file',
                                                        filetypes=(('excel file', '*.xlsx'),
                                                                   ('excel file', '*.xlsx')))
            df = pd.read_excel(self.file_name)

            if (len(df) == 0):
                msg.showinfo('No records', 'No records')
            else:
                pass

            # Now display the DF in 'Table' object
            # under'pandastable' module
            self.f2 = Frame(self.root, height=200, width=300)
            self.f2.pack(fill=BOTH, expand=1)
            self.table = Table(self.f2, dataframe=df, read_only=True)
            self.table.show()

        except FileNotFoundError as e:
            print(e)
            msg.showerror('Error in opening file', e)


# Driver Code
root = Tk()
root.title('Dunnhumby---Convert CSV to Excel File')

obj = csv_to_excel(root)
root.geometry('800x600')
root.mainloop()
