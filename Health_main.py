#importing all the modules
from tkinter import *
from tkinter import messagebox
import heart_main as hm
import diabetes_main as db
import breast_main as br
z=''
heart_names=['heart','HEART','Heart','heart disease','HEART DISEASE','Heart Disease']
diabetes_names=['diabetes','diabetes disease','DIABETES','DIABETES DISEASE','Diabetes','Diabetes Disease']
breast_cancer_names=['breast cancer','breast','BREAST','Breast','BREAST CANCER','Breast Cancer']
#Driver code
if __name__=='__main__':
    #Function for button to take input
    def button_in():
        global z
        z=str(name_field.get())
        if len(z)==0:
            messagebox.showerror('Model Error', 'No input given')
        else:
            name_field.insert(0,z)
            diseases=heart_names+diabetes_names+breast_cancer_names
            c=0
            for i in diseases:
                if i==z:
                    c+=1
                    print('Input Taken Successfully')
                    disease(z)
                    break
            if c==0:
                print('Invalid disease entered. Please try again..')
        
    
    def button_cl():
        name_field.delete(0,END)
        lre.delete(0,END)
        dte.delete(0,END)
        algo_field.delete(0, END)
        print('Fields Cleared')

    def disease(z):
        global heart_names, diabetes_names, breast_cancer_names
        if z in heart_names:
            hm._in_heart()
        elif z in diabetes_names:
            db._for_diabetes()
        elif z in breast_cancer_names:
            br._for_breast()
            
    def disease_dt():
        if z in heart_names:
            hm.call_dt()
            dte.insert(0,hm. _acc_dt)
        elif z in diabetes_names:
            db.call_dt()
            dte.insert(0,db._acc_dt)
        elif z in breast_cancer_names:
            br.call_dt()
            dte.insert(0,br._acc_dt)
    def disease_lr():
        if z in heart_names:
            hm.call_lr()
            lre.insert(0,hm._acc_lr)
        elif z in diabetes_names:
            db.call_lr()
            lre.insert(0,db._acc_lr)
        elif z in breast_cancer_names:
            br.call_lr()
            lre.insert(0,br._acc_lr)
    def algo():
        if z in heart_names:    
            algo_field.insert(0,hm.better_algo())
        elif z in diabetes_names:
            algo_field.insert(0,db.better_algo())
        elif z in breast_cancer_names:
            algo_field.insert(0,br.better_algo())
        
    #creating the GUI window
    root = Tk()
    root.geometry("900x500")
    root['background']='#856ff8'
    root.title("HEALTH-GUI")
    
    w2 = Label(root, justify=LEFT, text="DISEASE DETECTOR USING MACHINE LEARNING", fg="#4A274F", bg="#F0A07C")
    w2.config(font=('Algerian',18,'underline bold'))
    w2.grid(row=1, column=0, columnspan=2, padx=100, sticky=NE)
    w2 = Label(root, justify=LEFT, text="CONTRIBUTOR: SHANTANU KUNDU", fg='#EC4D37', bg='#1D1B1B')
    w2.config(font=('Bahnschrift SemiLight',15,'italic'))
    w2.grid(row=2, column=0, columnspan=2, padx=100, sticky=N)

    #Entry Fields and Buttons
    name_label = Label(root, text="NAME OF THE DISEASE", fg="red", bg="#FCE77D")
    name_label.config(font=("Eras Medium ITC",13,"bold"))
    name_label.grid(row=6, column=0, pady=15, sticky=N)
    
    name_field = Entry(root)
    name_field.grid(row=6, column=1)

    #Input button
    submit = Button(root, text = "SUBMIT",command=button_in,fg="Red", bg="Sky Blue", width = 20)
    submit.config(font=('Lucida Sans',10,'bold'))
    submit.grid(row = 7, column = 1)
    #Clear button
    clear = Button(root, text = "CLEAR",command=button_cl,fg="Red", bg="Sky Blue", width = 20)
    clear.config(font=('Lucida Sans',10,'bold'))
    clear.grid(row = 20, column = 1)


    #Logistic Regression
    lrb=Button(root, text = "LOGISTIC REGRESSION",command=disease_lr,fg="#DF678C", bg="#3D155F", width = 20)
    lrb.config(font=("Eras Medium ITC",13,"bold"))
    lrb.grid(row=14, column=0)

    lrl= Label(root, text="LOGISTIC REGRESSION ACCURACY", fg="White", bg="Red")
    lrl.config(font=("Eras Medium ITC",10,"bold"))
    lrl.grid(row=14, column=1, pady=15, sticky=W)
    
    lre=Entry(root)
    lre.grid(row=14, column=2)

    #Decision Tree
    dtb=Button(root, text = "DECISION TREE",command=disease_dt,fg="#CCF381", bg="#4831D4", width = 20)
    dtb.config(font=("Eras Medium ITC",13,"bold"))
    dtb.grid(row=16, column=0)
    
    dtl= Label(root, text="DECISION TREE ACCURACY", fg="White", bg="Red")
    dtl.config(font=("Eras Medium ITC",10,"bold"))
    dtl.grid(row=16, column=1, pady=15, sticky=W)
    
    dte=Entry(root)
    dte.grid(row=16, column=2)

    #Better Algorithm
    algo_butt=Button(root, text = "BETTER ALGORITHM",command=algo,fg="#F9D342", bg="#292826", width = 20)
    algo_butt.config(font=("Eras Medium ITC",13,"bold"))
    algo_butt.grid(row=18, column=0)

    algo_field=Entry(root)
    algo_field.grid(row=18, column=1)
    
    #Starting the GUI
    root.mainloop()

    print('Thank You...')
