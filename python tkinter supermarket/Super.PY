from tkinter import*
import math , random ,os
from tkinter import messagebox

class super:
    def __init__(self, root):
        self.root=root
        self.root.geometry('1300x700+30+10')
        self.root.title('Super-Market: سوبر ماركت')
        self.root.resizable(False, False)
        self .root.iconbitmap('c:\\super.ico')
        title= Label(self.root , text='Super-Market Management' , fg='orange' , bg='white', font=('tajawal',14,'bold'))
        title.pack(fill=X)
        
        #================== (Variables : المتغيرات)
        #====== [بقوليات : q1 => q18]== 
        self.q1=IntVar()
        self.q2=IntVar()
        self.q3=IntVar()
        self.q4=IntVar()
        self.q5=IntVar()
        self.q6=IntVar()
        self.q7=IntVar()
        self.q8=IntVar()
        self.q9=IntVar()
        self.q10=IntVar()
        self.q11=IntVar()
        self.q12=IntVar()
        self.q13=IntVar()
        self.q14=IntVar()
        self.q15=IntVar()
        self.q16=IntVar()
        self.q17=IntVar()
        self.q18=IntVar()
        
        #====== [لوازم منزليه : qq1 => qq18]==
        self.qq1=IntVar()
        self.qq2=IntVar()
        self.qq3=IntVar()
        self.qq4=IntVar()
        self.qq5=IntVar()
        self.qq6=IntVar()
        self.qq7=IntVar()
        self.qq8=IntVar()
        self.qq9=IntVar()
        self.qq10=IntVar()
        self.qq11=IntVar()
        self.qq12=IntVar()
        self.qq13=IntVar()
        self.qq14=IntVar()
        self.qq15=IntVar()
        self.qq16=IntVar()
        self.qq17=IntVar()
        self.qq18=IntVar()
        
        #====== [ ادوات كهربيه : qqq1 => qqq18]==
        self.qqq1=IntVar()
        self.qqq2=IntVar()
        self.qqq3=IntVar()
        self.qqq4=IntVar()
        self.qqq5=IntVar()
        self.qqq6=IntVar()
        self.qqq7=IntVar()
        self.qqq8=IntVar()
        self.qqq9=IntVar()
        self.qqq10=IntVar()
        self.qqq11=IntVar()
        self.qqq12=IntVar()
        self.qqq13=IntVar()
        self.qqq14=IntVar()
        self.qqq15=IntVar()
        
        #===== متغيرات بيانات المشتري  ===
        
        self.namo =StringVar( )
        self.phono =StringVar( )
        self.fatora  =StringVar( )
        x= random.randint(1000,9999)
        self.fatora.set(str(x))
         
        #===== متغيرات الحساب الكلي  =====
        self.bacoliat=StringVar( )      
        self.adoat =StringVar()
        self.kahraba =StringVar()
   
       
       
       
        #====== Customer Data =======
        
        F1 = Frame(root, bd=2 , width=338  , height=170 ,   bg='orange') 
        F1.place(x=961 , y=35)
        tit= Label(F1 , text='Customer Data ' ,fg=('white'), font=('tajawal',12,'bold'), bg='orange')
        tit.place(x=100 , y=0)
        his_name = Label(F1 , text='Customer Name', fg=('white'), font=('tajawal',9,'bold') , bg='orange')
        his_name.place(x=90, y=40 )
        his_Phone = Label(F1 , text='Customer Number', fg=('white'), font=('tajawal',9,'bold') , bg='orange')
        his_Phone.place(x=90, y=70 )
        bill_num = Label(F1 ,text='Bill Number', fg=('white'), font=('tajawal',9,'bold') , bg='orange')
        bill_num.place (x=90, y=100 )

        Ent_name = Entry(F1,textvariable=self.namo , justify='center')
        Ent_name.place(x=200 , y=42 )
        Ent_name = Entry(F1,textvariable=self.phono, justify='center' )
        Ent_name.place(x=200, y=72 )
        Ent_name = Entry(F1,textvariable=self.fatora, justify='center' )
        Ent_name.place(x=200 , y=102 )

        btn_customer = Button(F1 , text='Search',fg=('orange') , font=('tajawal',12) ,width=6,height=4, bg='white')
        btn_customer.place(x=7 , y=40 )
        
        #========= Fatoura : bill ======
        titdd = Label(F1 , text='[   Bills   ]' ,fg=('white'), font=('tajawal',14,'bold'), bg='orange')
        titdd.place(x=115 , y=135 )
        
        F3= Frame(root , bd=2 , width=338 , height=399 , bg='white')
        F3.place(x=961 , y=205)
        scrol_y= Scrollbar(F3 , orient=VERTICAL)
        self.textarea= Text(F3 , yscrollcommand=scrol_y.set)
        scrol_y.pack(side=LEFT , fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH , expand=1)
        
        #============ price =====================N:)
        F4 = Frame(root , bd=2 , width=657 , height=112 , bg='orange')
        F4.place(x=641, y=587)
        hesab = Button(F4 , text= 'The Price' ,fg=('black'), width=9 , height=1 , font='tajawal' , bg='white',command=self.total)
        hesab.place(x=537 , y=10)
        FATORA = Button(F4 , text='The Bill' ,fg=('black'), width=9 , height=1 , font='tajawal' , bg='white',command=self.billing)
        FATORA.place(x=537, y=55)
        clear = Button(F4 , text='Empty' ,fg=('black'), width=9 , height=1 , font='tajawal' , bg='white',command=self.clear )
        clear.place(x=417, y=10)
        
        exite = Button(F4 , text='Close' ,fg=('black'), width=9 , height=1 , font='tajawal' , bg='white',command=quit )
        exite.place(x=417 , y =55)
        
        lblol=Label(F4 , text=' الحساب الكلي للبقوليات',font=('tajawal',15,'bold'),bg='orange' , fg='white')
        lblol.place(x=220 , y =10 )
        lblo2=Label(F4 , text='  حساب اللوازم المنزليه ', font=('tajawal',15,'bold'),bg='orange' , fg='white')
        lblo2.place(x=220 , y =40 )
        lblo3=Label(F4 , text='  حساب ادوات الكهرباء', font=('tajawal',15,'bold'),bg='orange' , fg='white')
        lblo3.place(x=220 , y =70 )
        
        
        entol = Entry(F4 ,textvariable=self.bacoliat , width=24)
        entol.place(x=40 , y=12 )
        
        ento2 = Entry(F4, textvariable=self.adoat, width=24)
        ento2.place(x=40 , y=42 )
        
        ento3= Entry(F4 ,textvariable=self.kahraba, width=24)
        ento3.place(x=40 , y=72 )
        
        
        #================= products =====================N:)
        FF1=Frame(root , bd=2 , width=318 , height=664 , bg='orange')
        FF1.place(x=1 , y=35 )
        t = Label(FF1 , text='البقالة', font=('tajawal',17,'bold'),bg='orange' , fg='black')
        t.place(x=112 , y=0 )
        bq1= Label(FF1 , text='الرز', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        bq1.place(x=250 , y=50 )  
        bq2= Label(FF1 , text='بسله', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        bq2.place(x=250 , y=80 )      
        bq3= Label(FF1 , text='فاصوليا', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        bq3.place(x=250 , y=110 )        
        bq4= Label(FF1 , text='عدس', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        bq4.place(x=250 , y=140)     
        bq5= Label(FF1 , text='مكرونه', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        bq5.place(x=250 , y=170)
        bq6= Label(FF1 , text='سمسم', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        bq6.place(x=250 , y=200 )
        bq7= Label(FF1 , text='حمص', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        bq7.place(x=250 , y=230 )
        bq8= Label(FF1 , text='فول', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        bq8.place(x=250 , y=270 ) 
        bq9= Label(FF1 , text='الملح', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        bq9.place(x=250 , y=300 )
        bq10= Label(FF1 , text='سكر', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        bq10.place(x=250 , y=330 )
        bq11= Label(FF1 , text='فلفل اسود', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        bq11.place(x=230 , y=370 ) 
        bq12= Label(FF1 , text='فلفل احمر ', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        bq12.place(x=230 , y=400 )
        bq13= Label(FF1 , text='اللوبيا', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        bq13.place(x=250 , y=430 )
        bq14= Label(FF1 , text='زيت', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        bq14.place(x=250 , y=470 )
        bq15= Label(FF1 , text='القمح', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        bq15.place(x=250 , y=500 )
        bq16= Label(FF1 , text='الشعير', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        bq16.place(x=250 , y=530 )
        bq17= Label(FF1 , text='الشوفان', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        bq17.place(x=250 , y=570 )
       
        
        bqent1 = Entry(FF1,textvariable=self.q1, width=20)
        bqent1.place(x=70 , y=50 )
        
        bqent2 = Entry(FF1,textvariable=self.q2, width=20)
        bqent2.place(x=70 , y=80 )
        bqent3 = Entry(FF1,textvariable=self.q3, width=20)
        bqent3.place(x=70 , y=110 )
        bqent4 = Entry(FF1,textvariable=self.q4, width=20)
        bqent4.place(x=70 , y= 140)
        bqent5 = Entry(FF1,textvariable=self.q5, width=20)
        bqent5.place(x=70, y=170 ) 
        bqent6 = Entry(FF1, textvariable=self.q6,width=20)
        bqent6.place(x=70 , y=200 )
        bqent7 = Entry(FF1,textvariable=self.q17, width=20)
        bqent7.place(x=70 , y=230 )
        bqent8 = Entry(FF1,textvariable=self.q8, width=20)
        bqent8.place(x=70 , y=270 )
        bqent9= Entry(FF1,textvariable=self.q9, width=20)
        bqent9.place(x=70 , y=300 )
        bqent10 = Entry(FF1,textvariable=self.q10, width=20)
        bqent10.place(x=70 , y=330 )
        bqent11 = Entry(FF1,textvariable=self.q11, width=20)
        bqent11.place(x=70 , y=370 )
        bqent12 = Entry(FF1,textvariable=self.q12, width=20)
        bqent12.place(x=70 , y=400 )
        bqent13 = Entry(FF1,textvariable=self.q13, width=20)
        bqent13.place(x=70 , y=430 )
        bqent14 = Entry(FF1,textvariable=self.q14, width=20)
        bqent14.place(x=70 , y=470 )
        bqent15 = Entry(FF1,textvariable=self.q15 ,width=20)
        bqent15.place(x=70, y=500 )
        bqent16 = Entry(FF1,textvariable=self.q16, width=20)
        bqent16.place(x=70 , y=530 )
        bqent17 = Entry(FF1,textvariable=self.q17, width=20)
        bqent17.place(x=70, y=570 )
    
        #================= products 1=====================
        FF2=Frame(root , bd=2 , width=318 , height=664 , bg='orange')
        FF2.place(x=321 , y=35 )
        
        t = Label(FF2 , text=' اللوازم المنزليه', font=('tajawal',17,'bold'),bg='orange' , fg='black')
        t.place(x=112 , y=0 )
        bq1= Label(FF2 , text='مصفاه', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        bq1.place(x=250 , y=50 )  
        
        bq2= Label(FF2 , text='صحن', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        bq2.place(x=250 , y=80 ) 
             
        bq3= Label(FF2 , text='كاس', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        bq3.place(x=250 , y=110 )        
        bq4= Label(FF2 , text='ابريق', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        bq4.place(x=250 , y=140)     
        bq5= Label(FF2, text='سكين', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        bq5.place(x=250 , y=170)
        bq6= Label(FF2 , text='شوكه', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        bq6.place(x=250 , y=200 )
        bq7= Label(FF2 , text='حله', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        bq7.place(x=250 , y=230 )
        bq8= Label(FF2 , text='سله', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        bq8.place(x=250 , y=270 ) 
        bq9= Label(FF2 , text='معالق', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        bq9.place(x=250 , y=300 )
        bq10= Label(FF2, text='صينيه', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        bq10.place(x=250 , y=330 )
        bq11= Label(FF2 , text='وعاء ', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        bq11.place(x=250 , y=370 ) 
        bq12= Label(FF2 , text= 'فتاحه' , font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        bq12.place(x=250 , y=400 )
        bq13= Label(FF2 , text='مقشره', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        bq13.place(x=250 , y=430 )
        bq14= Label(FF2 , text=' لوح تقطيع', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        bq14.place(x=220 , y=470 )
        bq15= Label(FF2 , text='كوب', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        bq15.place(x=250 , y=500 )
        bq16= Label(FF2 , text='سلة ', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        bq16.place(x=250 , y=530 )
        bq17= Label(FF2, text='منفضه', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        bq17.place(x=250 , y=570 )
       
        
        bqent1 = Entry(FF2,textvariable=self.qq1, width=20)
        bqent1.place(x=70 ,y=50 )
        bqent2 = Entry(FF2, textvariable=self.qq2,width=20)
        bqent2.place(x=70 , y=80 )
        bqent3 = Entry(FF2,textvariable=self.qq3, width=20)
        bqent3.place(x=70 , y=110 )
        bqent4 = Entry(FF2,textvariable=self.qq4,width=20)
        bqent4.place(x=70 , y= 140)
        bqent5 = Entry(FF2,textvariable=self.qq5, width=20)
        bqent5.place(x=70, y=170 ) 
        bqent6 = Entry(FF2,textvariable=self.qq6, width=20)
        bqent6.place(x=70 , y=200 )
        bqent7 = Entry(FF2,textvariable=self.qq7, width=20)
        bqent7.place(x=70 , y=230 )
        bqent8 = Entry(FF2,textvariable=self.qq8,width=20)
        bqent8.place(x=70 , y=270 )
        bqent9= Entry(FF2,textvariable=self.qq9, width=20)
        bqent9.place(x=70 , y=300 )
        bqent10 = Entry(FF2,textvariable=self.qq10, width=20)
        bqent10.place(x=70 , y=330 )
        bqent11 = Entry(FF2,textvariable=self.qq11, width=20)
        bqent11.place(x=70 , y=370 )
        bqent12 = Entry(FF2,textvariable=self.qq12, width=20)
        bqent12.place(x=70 , y=400 )
        bqent13 = Entry(FF2,textvariable=self.qq13, width=20)
        bqent13.place(x=70 , y=430 )
        bqent14 = Entry(FF2,textvariable=self.qq14, width=20)
        bqent14.place(x=70 , y=470 )
        bqent15 = Entry(FF2,textvariable=self.qq15, width=20)
        bqent15.place(x=70, y=500 )
        bqent16 = Entry(FF2,textvariable=self.qq16, width=20)
        bqent16.place(x=70 , y=530 )
        bqent17 = Entry(FF2,textvariable=self.qq17, width=20)
        bqent17.place(x=70 , y=570 )
        
        #================= products 3=====================
        FF3=Frame(root , bd=2 , width=318 , height=550 , bg='orange')
        FF3.place(x=641 , y=35 )    
        t = Label(FF3 , text=' ادوات كهربيه ', font=('tajawal',17,'bold'),bg='orange' , fg='black')
        t.place(x=122 , y=0 )
        br1= Label(FF3 , text='مكنسه', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        br1.place(x=250 , y=50 )  
        
        br2= Label(FF3 , text='تلفزيون', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        br2.place(x=250 , y=80 ) 
             
        br3= Label(FF3 , text='غساله', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        br3.place(x=250 , y=110 )        
        br4= Label(FF3 , text='ميكرويف', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        br4.place(x=250 , y=140)     
        br5= Label(FF3, text='خلاط', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        br5.place(x=250 , y=170)
        br6= Label(FF3 , text='لمبه', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        br6.place(x=250 , y=200 )
        br7= Label(FF3 , text='فرن ', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        br7.place(x=250 , y=230 )
        br8= Label(FF3 , text='مقلاه ', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        br8.place(x=250 , y=270 ) 
        br9= Label(FF3 , text='مروحة ', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        br9.place(x=250 , y=300 )
        br10= Label(FF3, text=' كاتيل', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        br10.place(x=250 , y=330 )
        br11= Label(FF3 , text='TV32 ', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        br11.place(x=250 , y=370 ) 
        br12= Label(FF3 , text= 'TV 42' , font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        br12.place(x=250 , y=400 )
        br13= Label(FF3, text='فلتر', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        br13.place(x=250 , y=430 )
        br14= Label(FF3 , text='غساله اطباق', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        br14.place(x=227 , y=470 )
        br15= Label(FF3 , text='مكواه', font=('tajawal',15,'bold'),bg='orange' , fg='white' )
        br15.place(x=250 , y=500 )
        
        
        bqent1 = Entry(FF3,textvariable=self.qqq1,width=20)
        bqent1.place(x=70 , y=50 )
        bqent2 = Entry(FF3,textvariable=self.qqq2, width=20)
        bqent2.place(x=70 , y=80 )
        bqent3 = Entry(FF3,textvariable=self.qqq3, width=20)
        bqent3.place(x=70 , y=110 )
        bqent4 = Entry(FF3,textvariable=self.qqq4, width=20)
        bqent4.place(x=70 , y= 140)
        bqent5 = Entry(FF3,textvariable=self.qqq5, width=20)
        bqent5.place(x=70, y=170 ) 
        bqent6 = Entry(FF3,textvariable=self.qqq6, width=20)
        bqent6.place(x=70 , y=200 )
        bqent7 = Entry(FF3,textvariable=self.qqq7, width=20)
        bqent7.place(x=70 , y=230 )
        bqent8 = Entry(FF3,textvariable=self.qqq8, width=20)
        bqent8.place(x=70 , y=270 )
        bqent9= Entry(FF3,textvariable=self.qqq9, width=20)
        bqent9.place(x=70 , y=300 )
        bqent10 = Entry(FF3,textvariable=self.qqq10, width=20)
        bqent10.place(x=70 , y=330 )
        bqent11 = Entry(FF3, textvariable=self.qqq11,width=20)
        bqent11.place(x=70 , y=370 )
        bqent12 = Entry(FF3,textvariable=self.qqq12, width=20)
        bqent12.place(x=70 , y=400 )
        bqent13 = Entry(FF3,textvariable=self.qqq13, width=20)
        bqent13.place(x=70 , y=430 )
        bqent14 = Entry(FF3,textvariable=self.qqq14, width=20)
        bqent14.place(x=70 , y=470 )
        bqent15 = Entry(FF3 , textvariable=self.qqq15, width=20)
        bqent15.place(x=70, y=500 )
       #============= the price================N:)
        self.welcome()
    def total(self):
       self.rez =self.q1.get()*10
       self.por =self.q2.get()*5
       self.phos =self.q3.get()*12
       self.ads =self.q4.get()*6.5
       self.macr =self.q5.get()*16
       self.frik =self.q6.get()*13
       self.homs =self.q7.get()*10
       self.fole=self.q8.get()*11.5
       self.malh=self.q9.get()*20
       self.sokr =self.q10.get()*3
       self.black=self.q11.get()*9
       self.red =self.q12.get()*19
       self.lobia =self.q13.get()*10
       self.shof =self.q14.get()*7
       self.kmh =self.q15.get()*15
       self.sher =self.q16.get()*25
       self.dora =self.q17.get()*25
       self.shoof=self.q18.get()*12
       self.B= float(
           self.rez+
           self.por+
           self.phos+
           self.ads+
           self.macr+
           self.frik+
           self.homs+
           self.fole+
           self.malh+
           self.sokr+
           self.black+
           self.red+
           self.lobia+
           self.shof+
           self.kmh+
           self.sher+
           self.dora+
           self.shoof
           
       )
        
       self.bacoliat.set(str(self.B)+" $ ")

       self.rez1 =self.qq1.get()*1.5
       self.por1 =self.qq2.get()*2
       self.phos1 =self.qq3.get()*2
       self.ads1 =self.qq4.get()*5
       self.macr1 =self.qq5.get()*1.5
       self.frik1 =self.qq6.get()*1.5
       self.homs1 =self.qq7.get()*20
       self.fole1=self.qq8.get()*10
       self.malh1=self.qq9.get()*2
       self.sokr1 =self.qq10.get()*15
       self.black1=self.qq11.get()*7
       self.red1 =self.qq12.get()*5
       self.lobia1 =self.qq13.get()*6
       self.shof1 =self.qq14.get()*10
       self.kmh1 =self.qq15.get()*15
       self.sher1 =self.qq16.get()*8
       self.dora1 =self.qq17.get()*1.5
       self.shoof1=self.qq18.get()*12
       self.A = float(
           self.rez1+
           self.por1+
           self.phos1+
           self.ads1+
           self.macr1+
           self.frik1+
           self.homs1+
           self.fole1+
           self.malh1+
           self.sokr1+
           self.black1+
           self.red1+
           self.lobia1+
           self.shof1+
           self.kmh1+
           self.sher1+
           self.dora1+
           self.shoof1  
        ) 
       self.adoat.set(str(self.A)+"$")

       self.rez2 =self.qqq1.get()*100
       self.por2 =self.qqq2.get()*150
       self.phos2 =self.qqq3.get()*200
       self.ads2 =self.qqq4.get()*90
       self.macr2 =self.qqq5.get()*50
       self.frik2 =self.qqq6.get()*70
       self.homs2 =self.qqq7.get()*50
       self.fole2=self.qqq8.get()*100
       self.malh2=self.qqq9.get()*90
       self.sokr2 =self.qqq10.get()*200
       self.black2=self.qqq11.get()*300
       self.red2 =self.qqq12.get()*20
       self.lobia2 =self.qqq13.get()*15
       self.shof2 =self.qqq14.get()*300
       self.shoof2=self.qqq15.get()*60
       self. K= float(
           self.rez2+
           self.por2+
           self.phos2+
           self.ads2+
           self.macr2+
           self.frik2+
           self.homs2+
           self.fole2+
           self.malh2+
           self.sokr2+
           self.black2+
           self.red2+
           self.lobia2+
           self.shof2+
           self.shoof2
        ) 
       self.kahraba.set(str(self.K)+"$")

       self.all=float(self.B+
                      self.K+
                      self.A

                 )
   #=================bill body========================= N:)             
    def welcome(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\t سوبر ماركت يرحب بكم")
        self.textarea.insert(END,"\n ===========================================")
        self.textarea.insert(END,f"\n\t B.NUM  :{self.fatora.get()}")
        self.textarea.insert(END,f"\n\t NAME   :{self.namo.get()}")
        self.textarea.insert(END,f"\n\t PHONE  :{self.phono.get()}")
        self.textarea.insert(END,"\n ==========================================")
        self.textarea.insert(END,f"\nالسعر\t       العدد \t         المشتريات")
        self.textarea.insert(END,"\n ========================================")
       
     
   #=========افراغ الحقول ===========N:)
        
    def clear(self):    
        self.q1.set(0)
        self.q2.set(0)
        self.q3.set(0)
        self.q4.set(0)
        self.q5.set(0)
        self.q6.set(0)
        self.q7.set(0)
        self.q8.set(0)
        self.q9.set(0)
        self.q10.set(0)
        self.q11.set(0)
        self.q12.set(0)
        self.q13.set(0)
        self.q14.set(0)
        self.q15.set(0)
        self.q16.set(0)
        self.q17.set(0)
        self.q18.set(0)

        self.qq1.set(0)
        self.qq2.set(0)
        self.qq3.set(0)
        self.qq4.set(0)
        self.qq5.set(0)
        self.qq6.set(0)
        self.qq7.set(0)
        self.qq8.set(0)
        self.qq9.set(0)
        self.qq10.set(0)
        self.qq11.set(0)
        self.qq12.set(0)
        self.qq13.set(0)
        self.qq14.set(0)
        self.qq15.set(0)
        self.qq16.set(0)
        self.qq17.set(0)
        self.qq18.set(0)

        self.qqq1.set(0)
        self.qqq2.set(0)
        self.qqq3.set(0)
        self.qqq4.set(0)
        self.qqq5.set(0)
        self.qqq6.set(0)
        self.qqq7.set(0)
        self.qqq8.set(0)
        self.qqq9.set(0)
        self.qqq10.set(0)
        self.qqq11.set(0)
        self.qqq12.set(0)
        self.qqq13.set(0)
        self.qqq14.set(0)
        self.qqq15.set(0)

        self.bacoliat.set(0)
        self.adoat .set(0)
        self.kahraba.set(0)

        self.namo.set('')
        self.phono.set('')
        self.fatora.set('')
   
     #================prepar the bill=========================N:)
    def billing(self):
        if self.namo.get()==""or self.phono.get()=="":
            messagebox.showerror("Error","You forget name or number empty")
        else:
             self.welcome()
             if self.q1.get() !=0:
                self.textarea.insert(END,f"\n{self.rez}\t\t{self.q1.get()}\t\t الرز")
             if self.q2.get() !=0:
                self.textarea.insert(END,f"\n{self.por}\t\t{self.q2.get()}\t\t بسله")
             if self.q3.get() !=0:
                self.textarea.insert(END,f"\n{self.phos}\t\t{self.q3.get()}\t\t فاصولياء")
             if self.q4.get() !=0:
                self.textarea.insert(END,f"\n{self.ads}\t\t{self.q4.get()}\t\t عدس")
             if self.q5.get() !=0:
                self.textarea.insert(END,f"\n{self.macr}\t\t{self.q5.get()}\t\t مكرونة")
             if self.q6.get() !=0:
                self.textarea.insert(END,f"\n{self.frik}\t\t{self.q6.get()}\t\t سمسم")
             if self.q7.get() !=0:
                self.textarea.insert(END,f"\n{self.homs}\t\t{self.q7.get()}\t\t حمص")
             if self.q8.get() !=0:
                self.textarea.insert(END,f"\n{self.fole}\t\t{self.q8.get()}\t\t فول")
             if self.q9.get() !=0:
                self.textarea.insert(END,f"\n{self.malh}\t\t{self.q9.get()}\t\t ملح")
             if self.q10.get() !=0:
                self.textarea.insert(END,f"\n{self.sokr}\t\t{self.q10.get()}\t\t سكر")
             if self.q11.get() !=0:
                self.textarea.insert(END,f"\n{self.black}\t\t{self.q11.get()}\t\t فلفل اسود")
             if self.q12.get() !=0:
                self.textarea.insert(END,f"\n{self.red}\t\t{self.q12.get()}\t\t فلفل احمر ")
             if self.q13.get() !=0:
                self.textarea.insert(END,f"\n{self.lobia}\t\t{self.q13.get()}\t\t لوبيا")
             if self.q14.get() !=0:
                self.textarea.insert(END,f"\n{self.shof}\t\t{self.q14.get()}\t\t زيت")
             if self.q15.get() !=0:
                self.textarea.insert(END,f"\n{self.kmh}\t\t{self.q15.get()}\t\t القمح")
             if self.q16.get() !=0:
                self.textarea.insert(END,f"\n{self.sher}\t\t{self.q16.get()}\t\t الشعير")
             if self.q17.get() !=0:
                self.textarea.insert(END,f"\n{self.dora}\t\t{self.q17.get()}\t\t الشوفان")
             if self.q18.get() !=0:
                self.textarea.insert(END,f"\n{self.shoof}\t\t{self.q18.get()}\t\t الشوفان")
               # اللوازم المنزليه
             if self.qq1.get() !=0:
                self.textarea.insert(END,f"\n{self.rez1}\t\t{self.qq1.get()}\t\t مصفاه")
             if self.qq2.get() !=0:
                self.textarea.insert(END,f"\n{self.por1}\t\t{self.qq2.get()}\t\t صحن")
             if self.qq3.get() !=0:
                self.textarea.insert(END,f"\n{self.phos1}\t\t{self.qq3.get()}\t\t كأس")
             if self.qq4.get() !=0:
                self.textarea.insert(END,f"\n{self.ads1}\t\t{self.qq4.get()}\t\t ابريق")
             if self.qq5.get() !=0:
                self.textarea.insert(END,f"\n{self.macr1}\t\t{self.qq5.get()}\t\t سكين")
             if self.qq6.get() !=0:
                self.textarea.insert(END,f"\n{self.frik1}\t\t{self.qq6.get()}\t\t شوكه")
             if self.qq7.get() !=0:
                self.textarea.insert(END,f"\n{self.homs1}\t\t{self.qq7.get()}\t\t حله")
             if self.qq8.get() !=0:
                self.textarea.insert(END,f"\n{self.fole1}\t\t{self.qq8.get()}\t\t سله")
             if self.qq9.get() !=0:
                self.textarea.insert(END,f"\n{self.malh1}\t\t{self.qq9.get()}\t\t معالق")
             if self.qq10.get() !=0:
                self.textarea.insert(END,f"\n{self.sokr1}\t\t{self.qq10.get()}\t\t صينيه")
             if self.qq11.get() !=0:
                self.textarea.insert(END,f"\n{self.black1}\t\t{self.qq11.get()}\t\t وعاء خلط")
             if self.qq12.get() !=0:
                self.textarea.insert(END,f"\n{self.red1}\t\t{self.qq12.get()}\t\t فتاحه علب")
             if self.qq13.get() !=0:
                self.textarea.insert(END,f"\n{self.lobia1}\t\t{self.qq13.get()}\t\t مقشره")
             if self.qq14.get() !=0:
                self.textarea.insert(END,f"\n{self.shof1}\t\t{self.qq14.get()}\t\t لوح تقطيع")
             if self.qq15.get() !=0:
                self.textarea.insert(END,f"\n{self.kmh1}\t\t{self.qq15.get()}\t\t كوب")
             if self.qq16.get() !=0:
                self.textarea.insert(END,f"\n{self.sher1}\t\t{self.qq16.get()}\t\t سله")
             if self.qq17.get() !=0:
                self.textarea.insert(END,f"\n{self.dora1}\t\t{self.qq17.get()}\t\t منفضه")
             if self.qq18.get() !=0:
                self.textarea.insert(END,f"\n{self.shoof1}\t\t{self.qq18.get()}\t\t منفضه")
                #الادوات الكهربائيه
             if self.qqq1.get() !=0:
                self.textarea.insert(END,f"\n{self.rez2}\t\t{self.qqq1.get()}\t\t مكنسة")
             if self.qqq2.get() !=0:
                self.textarea.insert(END,f"\n{self.por2}\t\t{self.qqq2.get()}\t\t تلفزيون")
             if self.qqq3.get() !=0:
                self.textarea.insert(END,f"\n{self.phos2}\t\t{self.qqq3.get()}\t\t غسالة")
             if self.qqq4.get() !=0:
                self.textarea.insert(END,f"\n{self.ads2}\t\t{self.qqq4.get()}\t\t ميكرويف")
             if self.qqq5.get() !=0:
                self.textarea.insert(END,f"\n{self.macr2}\t\t{self.qqq5.get()}\t\t خلاط")
             if self.qqq6.get() !=0:
                self.textarea.insert(END,f"\n{self.frik2}\t\t{self.qqq6.get()}\t\t لمبه")
             if self.qqq7.get() !=0:
                self.textarea.insert(END,f"\n{self.homs2}\t\t{self.qqq7.get()}\t\t فرن كهربي")
             if self.qqq8.get() !=0:
                self.textarea.insert(END,f"\n{self.fole2}\t\t{self.qqq8.get()}\t\t مقلاه كهربيه")
             if self.qqq9.get() !=0:
                self.textarea.insert(END,f"\n{self.malh2}\t\t{self.qqq9.get()}\t\t مروحه")
             if self.qqq10.get() !=0:
                self.textarea.insert(END,f"\n{self.sokr2}\t\t{self.qqq10.get()}\t\t كاتيل")
             if self.qqq11.get() !=0:
                self.textarea.insert(END,f"\n{self.black2}\t\t{self.qqq11.get()}\t\t TV 32")
             if self.qqq12.get() !=0:
                self.textarea.insert(END,f"\n{self.red2}\t\t{self.qqq12.get()}\t\t TV 42")
             if self.qqq13.get() !=0:
                self.textarea.insert(END,f"\n{self.lobia2}\t\t{self.qqq13.get()}\t\t فلتر")
             if self.qqq14.get() !=0:
                self.textarea.insert(END,f"\n{self.shof2}\t\t{self.qqq14.get()}\t\t غساله اطباق ")
             if self.qqq15.get() !=0:          
                self.textarea.insert(END,f"\n{self.shoof2}\t\t{self.qqq15.get()}\t\t مكواه ")
       # ============total price ========================  N:)       
             self.textarea.insert(END,"\n.......................................")
             self.textarea.insert(END,f"\n\t{self.all} $ \t      :المجموع الكلي")
             self.textarea.insert(END,"\n.......................................")
             self.savee()
               
    


#======================save the bill============N:)
    def savee(self):
        op = messagebox.askyesno("Save","Do you want to save the bill ?")
        if op > 0:
            self.bb = self.textarea.get('1.0',END)
            f1 =open('C:\\bills\\'+str(self.fatora.get())+".txt","w",encoding="utf-8")
            f1.write(self.bb)
            f1.close()
        else:
         return
             
#=====TEAM PSG=======          
root=Tk()    
ob = super(root)
root.mainloop()