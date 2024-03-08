from tkinter import *
from tkinter import ttk
import random
from tkinter import messagebox 
def main():
    window = Tk()
    app = LoginPage(window)
    window.mainloop()

class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1270x600")
        self.window.title('Restaurant Management System')
        window.title("Restaurant Management System")
        self.window.config(bg= 'dark slate gray')
        self.main_win = Label(window, text='Restaurant Management System', font=('Arial', 35, 'bold'),
                bg='lemon chiffon', relief= GROOVE,bd= 10)
        self.main_win.pack(side= 'top',fill= X)

        #-------------Now login details setup__________________________________________________

        self.frame = Frame(window, bg= 'papaya whip', relief=GROOVE, bd=5,borderwidth=10)
        self.frame.place(x= 350, y = 200, width= 700, height= 400)
        self.login = Label(self.frame, text='Login', font=('sans-serif',20,'bold'),
                      bd=5, relief=RAISED, bg='light grey')
        self.login.pack(side= 'top', fill= X)

        self.login_details = Label(self.frame,text= 'Please enter your login details',
                      font=('sans-serif', 15,'bold'),bg='papaya whip')
        self.login_details.place(x=190, y= 60)

##--------------Entry details___________------------------------------------
## make function
        username = StringVar()
        passwordString = StringVar()
       
#=====================================================================================
        self.user = Label(self.frame, text= 'Enter Username: ', font=('Arial', 13,'bold'),
             bg='papaya whip')
        self.entry = Entry(self.frame,bg= 'ghost white', borderwidth= 1, width= 25, border=3
                      ,textvariable=username)

        self.password = Label(self.frame, text='Enter Password: ', font=('Arial', 13,'bold'),
                         bg='papaya whip')
        self.entry_pass = Entry(self.frame,bg= 'ghost white', borderwidth= 1, width= 25, border=3,show = '*'
                           ,textvariable=passwordString)

        self.user.place(x= 5, y= 120)
        self.entry.place(x = 150, y= 120)
        self.password.place(x = 5, y = 160)
        self.entry_pass.place(x = 150, y= 160)

        ##-----------------Making Function for buttons----------------------------------
        def check_login():
            """This function will check login details are correct or not"""
            if (username.get()=='12345' and passwordString.get()=='12345'):
                messagebox.showinfo('Login','Successfully login now you can access billing section')
                self.billing_btn.config(state='normal')
            elif (username.get()=='' and passwordString.get()==''):
                messagebox.showwarning('Login','Please enter login details')
            else:
                messagebox.showerror('Login', 'Login details are wrong')


        def reset():
            username.set("")
            passwordString.set("")
            self.billing_btn.config(state='disabled')

        def billing_new():
            self.newwindow = Toplevel(window)
            self.app= window2(self.newwindow)
        def register():
            self.registerWindow = Toplevel(window)
            self.app = window3(self.registerWindow)

        #-------------------Button-------------------------------------------------------------

        self.lgn_btn = Button(self.frame, text='Login', relief=RAISED,bd=3, bg='sienna3',
                        width=8,height=1,activeforeground='white',
                        font=('sans-serif',12,'bold'),command=check_login)
        self.btn_frame = Frame(self.frame,bg= 'mint cream', relief=SUNKEN,
                        width=600, height=110,borderwidth=5)
        self.btn_frame.place(x=45, y=230)
        self.billing_btn = Button(self.frame, text='Billing', relief=RAISED,bd=3, bg='gold2',
                        width=8,height=1,activeforeground='white',
                        font=('sans-serif',12,'bold'),command=billing_new)
        self.reset_btn = Button(self.frame, text='Reset', relief=RAISED,bd=3, bg='gold2',
                        width=8,height=1,activeforeground='white',
                        font=('sans-serif',12,'bold'),command=reset)
        self.register_btn = Button(self.frame, text='Register', relief=RAISED,bd=3, bg='gold2',
                        width=8,height=1,activeforeground='white',
                        font=('sans-serif',12,'bold'),command=register)
#=+============================================================================================
        self.lgn_btn.place(x = 460, y = 128)
        self.register_btn.place(x = 57, y = 265)
        self.billing_btn.place(x = 305 ,y = 265)
        self.reset_btn.place(x = 540, y = 265)
        self.billing_btn.config(state='disabled')
#==============================================================================================
class window2:
    def __init__(self,window):
        self.window = window
        self.window.geometry("1270x800")
        self.window.title('Restaurant Management System')
        self.window.config(bg= 'dark slate gray')
        self.main_win = Label(window, text='Billing Section', font=('Arial', 35, 'bold'),
                bg='lemon chiffon', relief= GROOVE,bd= 10)
        self.main_win.pack(side= 'top',fill= X)
##======================= Random variable===================================================
        bill_no = random.randint(1,10000)
        bill_no_tk = IntVar()
        bill_no_tk.set(bill_no)

#==================================Frame creation============================================
        self.frame = Frame(window, bg= 'papaya whip', relief=GROOVE, bd=5,borderwidth=10)
        self.frame.place(x=5, y = 80, width= 450, height= 615)
        self.dtl = Label(self.frame, text='Please enter details', font=('sans-serif',20,'bold'),
                      bd=5, relief=RAISED, bg='light grey')
        self.dtl.pack(side= 'top', fill= X)
#==================================Creat Entries===========================================
        self.bill_no = Label(self.frame, font=('Arial',12,'bold'),text='Enter bill no: ',
                            bg='papaya whip')
        self.bill_no.place(x=3, y=50)
        self.entry_bill = Entry(self.frame,bg= 'ghost white', borderwidth= 5, width= 25, 
                                textvariable=bill_no_tk,border=3 )
        self.entry_bill.place(x=180, y=50)
        self.customer_name = Label(self.frame, font=('Arial',12,'bold'),text='Customer name: ',
                             bg='papaya whip')                 
        self.customer_name.place(x=3, y=100)
        self.entry_cus_na = Entry(self.frame,bg= 'ghost white', borderwidth= 5, width= 25, 
                                textvariable=None,border=3 )
        self.entry_cus_na.place(x=180, y=100)

        self.customer_num = Label(self.frame, font=('Arial',12,'bold'),text='Customer Mobile No: ',
                             bg='papaya whip')                 
        self.customer_num.place(x=3, y=150)
        self.entry_cus_num = Entry(self.frame,bg= 'ghost white', borderwidth= 5, width= 25, 
                                textvariable=None,border=3 )
        self.entry_cus_num.place(x=180, y=150)
        self.date = Label(self.frame, font=('Arial',12,'bold'),text='Date: ',
                             bg='papaya whip')                 
        self.date.place(x=3, y=200)
        self.entry_date = Entry(self.frame,bg= 'ghost white', borderwidth= 5, width= 25, 
                                textvariable=None,border=3 )
        self.entry_date.place(x=180, y=200)
        self.day = Label(self.frame, font=('Arial',12,'bold'),text='Day: ',
                             bg='papaya whip')                 
        self.day.place(x=3, y=250)
        self.entry_day = Entry(self.frame,bg= 'ghost white', borderwidth= 5, width= 25, 
                                textvariable=None,border=3 )
        self.entry_day.place(x=180, y=250)
        self.item = Label(self.frame, font=('Arial',12,'bold'),text='Item purchased: ',
                             bg='papaya whip')                 
        self.item.place(x=3, y=300)
        self.entry_item = Entry(self.frame,bg= 'ghost white', borderwidth= 5, width= 25, 
                                textvariable=None,border=3 )
        self.entry_item.place(x=180, y=300)
        self.item_qunt = Label(self.frame, font=('Arial',12,'bold'),text='Item Quantity: ',
                             bg='papaya whip')                 
        self.item_qunt.place(x=3, y=350)
        self.entry_item_qunt = Entry(self.frame,bg= 'ghost white', borderwidth= 5, width= 25, 
                                textvariable=None,border=3 )
        self.entry_item_qunt.place(x=180, y=350)
        self.item_price = Label(self.frame, font=('Arial',12,'bold'),text='Price of one item: ',
                             bg='papaya whip')                 
        self.item_price.place(x=3, y=400)
        self.entry_item_price = Entry(self.frame,bg= 'ghost white', borderwidth= 5, width= 25, 
                                textvariable=None,border=3 )
        self.entry_item_price.place(x=180, y=400)

##=========================Make Buttons===================================================
        self.frm = Frame(self.frame, bg= 'azure', relief=GROOVE, bd=5,borderwidth=5)
        self.frm.place(x=15, y = 430, width= 400, height=152)
        self.add_btn = Button(self.frm, text='Add item', relief=RAISED, bd=3,
                              bg= 'goldenrod1',
                        width=8,height=1,activeforeground='salmon',
                        font=('sans-serif',12,'bold'))
        self.add_btn.place(x =12, y = 20)
        self.total_btn = Button(self.frm, text='Total', relief=RAISED, bd=3,
                              bg= 'goldenrod1',
                        width=8,height=1,activeforeground='salmon',
                        font=('sans-serif',12,'bold'))
        self.total_btn.place(x =280, y = 20)
        self.generate_btn = Button(self.frm, text='Generate bill', relief=RAISED, bd=3,
                              bg= 'goldenrod1',
                        width=10,height=1,activeforeground='salmon',
                        font=('sans-serif',12,'bold'))
        self.generate_btn.place(x = 140, y= 60)
        self.reset_btn = Button(self.frm, text='Reset', relief=RAISED, bd=3,
                              bg= 'goldenrod1',
                        width=8,height=1,activeforeground='salmon',
                        font=('sans-serif',12,'bold'))
        self.reset_btn.place(x =12, y = 90)
        self.save_btn = Button(self.frm, text='Save', relief=RAISED, bd=3,
                              bg= 'goldenrod1',
                        width=8,height=1,activeforeground='salmon',
                        font=('sans-serif',12,'bold'))
        self.save_btn.place(x =280, y = 90)
##========================Making Calculator at another section============================
        ## Making entry table
        self.cal_frm = Frame(window, bg= 'papaya whip', relief=GROOVE, bd=5,borderwidth=10)
        self.cal_frm.place(x=455, y =80, width=815, height= 615)
        self.cal_dtl = Label(self.cal_frm, text='Calculate price', font=('sans-serif',20,'bold'),
                      bd=5, relief=RAISED, bg='SeaGreen3')
        self.cal_dtl.pack(side='top', fill = X)
        self.e = Entry(self.cal_frm, width=100, borderwidth=9, background='white',
                       textvariable=None)
        self.e.place(x =80,y=55)
### Making buttons for number in calculator
        self.b1 = Button(self.cal_frm, text='AC', width=15, bg='orange', borderwidth=2,
                         height=2,font=('Arial',10,'bold'))
        self.b1.place(x= 80, y=100)
        self.b2 = Button(self.cal_frm, text='Clear', width=15, bg='orange', borderwidth=2,
                        height=2,font=('Arial',10,'bold'))
        self.b2.place(x= 240, y=100)
        self.b3 = Button(self.cal_frm, text='%', width=15, bg='orange', borderwidth=2,
                         height=2,font=('Arial',10,'bold'))
        self.b3.place(x= 400, y=100)
        self.b4 = Button(self.cal_frm, text='/', width=15, bg='orange', borderwidth=2,
                         height=2,font=('Arial',10,'bold'))
        self.b4.place(x= 568, y=100)
        #------------------------------------------------------------------------------
        self.b5 = Button(self.cal_frm,relief=GROOVE, text='1', width=15, 
                         command=lambda:click(1),bg='white', height=2, borderwidth=2,font=('Arial',10,'bold'))
        self.b5.place(x= 80, y=140)
        self.b6 = Button(self.cal_frm,relief=GROOVE, text='2', 
                         command=lambda:click(2),width=15, bg='white', height=2, borderwidth=2,font=('Arial',10,'bold'))
        self.b6.place(x= 240, y=140)
        self.b7 = Button(self.cal_frm,relief=GROOVE, text='3',
                         command=lambda:click(3), width=15, bg='white', height=2, borderwidth=2,font=('Arial',10,'bold'))
        self.b7.place(x= 400, y=140)
        self.b8 = Button(self.cal_frm,relief=GROOVE, text='X', width=15, bg='orange', height=2, borderwidth=2,font=('Arial',10,'bold'))
        self.b8.place(x= 568, y=140)
        # #---------------------------------------------------------------------------------
        self.b9 = Button(self.cal_frm,relief=GROOVE, text='4',
                         command=lambda:click(4), width=15, bg='white',height=2,borderwidth=2,font=('Arial',10,'bold'))
        self.b9.place(x= 80, y=180)
        self.b10 = Button(self.cal_frm,relief=GROOVE, text='5', 
                          command=lambda:click(5),width=15, bg='white',height=2, borderwidth=2,font=('Arial',10,'bold'))
        self.b10.place(x= 240, y=180)
        self.b11 = Button(self.cal_frm,relief=GROOVE, text='6',
                          command=lambda:click(6), width=15, bg='white',height=2, borderwidth=2,font=('Arial',10,'bold'))
        self.b11.place(x= 400, y=180)
        self.b12 = Button(self.cal_frm,relief=GROOVE, text='-', width=15, bg='orange',height=2,borderwidth=2,font=('Arial',10,'bold'))
        self.b12.place(x= 568, y=180)
        # #=------------------------------------------------------------------------------------
        self.b13 = Button(self.cal_frm, relief=GROOVE,text='7', 
                          command=lambda:click(7),width=15, bg='white',height=2, borderwidth=2,font=('Arial',10,'bold'))
        self.b13.place(x= 80, y=220)
        self.b14 = Button(self.cal_frm,relief=GROOVE,text='8', 
                          command=lambda:click(8),width=15, bg='white',height=2, borderwidth=2,font=('Arial',10,'bold'))
        self.b14.place(x= 240, y=220)
        self.b15 = Button(self.cal_frm,relief=GROOVE, text='9',
                          command=lambda:click(9), width=15, bg='white',height=2, borderwidth=2,font=('Arial',10,'bold'))
        self.b15.place(x= 400, y=220)
        self.b16 = Button(self.cal_frm,relief=GROOVE, text='+',
                           width=15, bg='orange',height=2, borderwidth=2,font=('Arial',10,'bold'))
        self.b16.place(x= 568, y=220)
        # #-------------------------------------------------------------------------------------
        self.b17 = Button(self.cal_frm, relief=GROOVE,text='//', width=15, bg='white',height=2, borderwidth=2,font=('Arial',10,'bold'))
        self.b17.place(x= 80, y=260)
        self.b18 = Button(self.cal_frm,relief=GROOVE, text='0',
                          command=lambda:click(0), width=15, bg='white',height=2, borderwidth=2,font=('Arial',10,'bold'))
        self.b18.place(x= 240, y=260)
        self. b19 = Button(self.cal_frm,relief=GROOVE, text='00', width=15, 
                           command=lambda:click(00),bg='white',height=2, borderwidth=2,font=('Arial',10,'bold'))
        self.b19.place(x= 400, y=260)
        self.b20 = Button(self.cal_frm,relief=GROOVE, text='=', width=15, bg='orange',height=2, borderwidth=2,font=('Arial',10,'bold'))
        self.b20.place(x= 568, y=260)
###==================================Making Bill area where bill will be printed===========================
        self.bill_area_frame = Frame(window, bg= 'papaya whip', relief=GROOVE, bd=5,borderwidth=10)
        self.bill_area_frame.place(x=465, y = 400, width=795, height= 295)
        self.bill_area_detail = Label(self.bill_area_frame, text = 'Bill receipt',
                                     bg='pale goldenrod', bd=5,borderwidth=10, font=('sans-serif',20,'bold'),relief=GROOVE)
        self.bill_area_detail.pack(side = 'top', fill = X)
##===========================Text method in bill area======================================
        self.area_text = Text(self.bill_area_frame, bg='ghost white')
  
        self.area_text.pack(fill = BOTH, expand=True)

##====================================Functions for Calculator====================================
        def click(num):
            result = self.e.get()
            self.e.delete(0,END)
            self.e.insert(0, str(result) + str(num))

        # def add():
        #     n1 = self.e.get()
        #     global math
        #     math = 'Addition'
        #     global i
        #     i = int(n1)
        #     self.e.delete(0, END)
            
##=======================Registration Class=====================================================

class window3:
    def __init__(self,window):
        self.window = window
        self.window.geometry("700x400")
        self.window.title('Restaurant Management System')
        self.window.config(bg= 'dark slate gray')
        self.reg_win = Label(window, text='Registration section', font=('Arial',25, 'bold'),
                bg='lemon chiffon', relief= GROOVE,bd= 10)
        self.reg_win.pack(side= 'top',fill= X)
###===============================Registration page frame==========================================
        
        self.reg_frm = Frame(window,bg= 'papaya whip', relief=GROOVE, bd=5,borderwidth=10)
        self.reg_frm.place(x=26, y =70, width= 650, height= 450)

##===============================Registration details========================================
        self.first_name = Label(self.reg_frm, text='First name:',
                             font=('sans-serif', 13,'bold'), bg='papaya whip')
        self.first_name.place(x =3, y= 20)
        self.fst_name_entry = Entry(self.reg_frm,bg= 'ghost white', borderwidth= 5, width =20, 
                                textvariable=None,border=3)
        self.fst_name_entry.place(x =100, y =20)

        self.lst_name = Label(self.reg_frm, text='Last name:',
                             font=('sans-serif', 13,'bold'), bg='papaya whip')
        self.lst_name.place(x =390, y= 20)
        self.lst_name_entry = Entry(self.reg_frm,bg= 'ghost white', borderwidth= 5, width =20, 
                                textvariable=None,border=3)
        self.lst_name_entry.place(x = 490, y =20)
       
        self.mail_id = Label(self.reg_frm, text='Mail-Id:',
                             font=('sans-serif', 13,'bold'), bg='papaya whip')
        self.mail_id.place(x =3, y= 70)
        self.mail_id_entry = Entry(self.reg_frm,bg= 'ghost white', borderwidth= 5, width =20, 
                                textvariable=None,border=3)
        self.mail_id_entry.place(x = 100, y =70)
       
        self.contact = Label(self.reg_frm, text='Contact no:',
                             font=('sans-serif', 13,'bold'), bg='papaya whip')
        self.contact.place(x =390, y= 70)
        self.contact_entry = Entry(self.reg_frm,bg= 'ghost white', borderwidth= 5, width =20, 
                                textvariable=None,border=3)
        self.contact_entry.place(x =490, y =70)
 
        self.place = Label(self.reg_frm, text='Address:',
                             font=('sans-serif', 13,'bold'), bg='papaya whip')
        self.place.place(x =3, y= 120)
        self.place_entry = Text(self.reg_frm,bg= 'ghost white', borderwidth= 5, width =20, 
                                height=4,textvariable=None,border=3)
        self.place_entry.place(x = 100, y =120)
                                
        self.state_name = Label(self.reg_frm, text='State:',
                             font=('sans-serif', 13,'bold'), bg='papaya whip')
        self.state_name.place(x =390, y= 120)
        self.state_entry = Entry(self.reg_frm,bg= 'ghost white', borderwidth= 5, width =20, 
                                textvariable=None,border=3)
        self.state_entry.place(x = 490, y =120)

        self.pas = Label(self.reg_frm, text='Password:',
                             font=('sans-serif', 13,'bold'), bg='papaya whip')
        self.pas.place(x =3, y= 200)
        self.pas_entry = Entry(self.reg_frm,bg= 'ghost white', borderwidth= 5, width =20, 
                                textvariable=None,border=3)
        self.pas_entry.place(x = 100, y =200)

        self.re_pas = Label(self.reg_frm, text='Re-type password:',
                             font=('sans-serif', 13,'bold'), bg='papaya whip')
        self.re_pas.place(x =3, y= 240)
        self.re_pas_entry = Entry(self.reg_frm,bg= 'ghost white', borderwidth= 5, width =20, 
                                textvariable=None,border=3)
        self.re_pas_entry.place(x =160, y =240)                        
                                
if __name__ == '__main__': 
    main()
