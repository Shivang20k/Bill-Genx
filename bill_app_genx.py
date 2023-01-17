from tkinter import *
from tkinter import messagebox
from datetime import date

import os
class bill_app:
  def __init__(self,root):
      self.root=root #initialize root
      self.root.geometry("1365x700+0+0")#giving geomtry size of tkinter window frame
      self.root.title("Simple Bill")
      bg_color="#696969"
      title=Label(self.root,text="BILL GENX",bd=12,relief=GROOVE,fg="white",bg="#696975",font=("times new roman",30,"bold"),pady=2).pack(fill=X)#adding properties to title block

      #=====================================================variables=========================================================================================

      #==================customer & information===================
      self.c_name=StringVar()
      self.c_address=StringVar()
      self.phone=StringVar()
      self.gstin=StringVar()
      self.state=StringVar()
      self.statecode=StringVar()
      self.invoice=StringVar()
      self.date=date.today()
      #====================particulars============================
      self.part1=StringVar()
      self.part2=StringVar()
      self.part3=StringVar()
      self.part4=StringVar()
      self.part5=StringVar()
      self.part6=StringVar()
      self.part7=StringVar()
      #====================size============================
      self.size1=StringVar()
      self.size2=StringVar()
      self.size3=StringVar()
      self.size4=StringVar()
      self.size5=StringVar()
      self.size6=StringVar()
      self.size7=StringVar()
      #====================hsn===================================
      self.hsn1=StringVar()
      self.hsn2=StringVar()
      self.hsn3=StringVar()
      self.hsn4=StringVar()
      self.hsn5=StringVar()
      self.hsn6=StringVar()
      self.hsn7=StringVar()
      #===================quantity==============================
      self.qt1=IntVar()
      self.qt2=IntVar()
      self.qt3=IntVar()
      self.qt4=IntVar()
      self.qt5=IntVar()
      self.qt6=IntVar()
      self.qt7=IntVar()
      #=================rate====================================
      self.r1=IntVar()
      self.r2=IntVar()
      self.r3=IntVar()
      self.r4=IntVar()
      self.r5=IntVar()
      self.r6=IntVar()
      self.r7=IntVar()
      #=================gst======================================
      self.g1=IntVar()
      self.g2=IntVar()
      self.g3=IntVar()
      self.g4=IntVar()
      self.g5=IntVar()
      self.g6=IntVar()
      self.g7=IntVar()
      #================total====================================
      self.tl1=StringVar()
      self.tl2=StringVar()
      self.tl3=StringVar()
      self.tl4=StringVar()
      self.tl5=StringVar()
      self.tl6=StringVar()
      self.tl7=StringVar()
      self.GT=StringVar()

      #=================================================CUSTOMER DETAIL FRAME=================================================================================
      F1=LabelFrame(self.root,bd=5,relief=GROOVE,text="Customer Details",font=("times new roman",19,"bold"),fg="white",bg=bg_color)#"f" is frame
      F1.place(x=0,y=75,relwidth=0.42,relheight=0.32)#customer frame in which all is written
      #======name=========
      cname_label=Label(F1,text="NAME",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=0,padx=20,pady=5)#name button
      cname_txt=Entry(F1,textvariable=self.c_name,width=35,font="arial 15",bd=4).grid(row=0,column=1,padx=6,pady=5)#name entry
      #======address=========
      address_label=Label(F1,text="ADDRESS",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=1,column=0,padx=20,pady=5)#address button
      address_txt=Entry(F1,textvariable=self.c_address,width=35,font="arial 15",bd=4).grid(row=1,column=1,padx=6,pady=5)#address entry
      #======gstin=========
      gstin_label=Label(F1,text="GSTIN",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=2,column=0,padx=20,pady=5)#gstin button
      gstin_txt=Entry(F1,width=35,textvariable=self.gstin,font="arial 15",bd=4).grid(row=2,column=1,padx=6,pady=5)#gstin entry
      #======state=========
      state_label=Label(F1,text="STATE",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=3,column=0,padx=20,pady=5)#state button
      state_txt=Entry(F1,textvariable=self.state,width=35,font="arial 15",bd=4).grid(row=3,column=1,padx=6,pady=5)#state entry

      #======================================================INVOICE DETAIL FRAME=================================================================================
      F2=LabelFrame(self.root,bd=5,relief=GROOVE,text="Invoice Details",font=("times new roman",19,"bold"),fg="white",bg=bg_color)
      F2.place(x=575,y=75,relwidth=0.469,relheight=0.32)#invoice  frame in which all is written
      #======customer phone number=========
      ph_label=Label(F2,text="PHONE NUMBER",bg=bg_color,fg="gold",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)#name button
      ph_txt=Entry(F2,textvariable=self.phone,width=35,font="arial 15",bd=4).grid(row=0,column=1,padx=6,pady=5)#phone number entry
      #======invoice number=========
      inv_label=Label(F2,text="INVOICE NUMBER",bg=bg_color,fg="gold",font=("times new roman",15,"bold")).grid(row=1,column=0,padx=20,pady=5)#address button
      inv_txt=Entry(F2,textvariable=self.invoice,width=35,font="arial 15",bd=4).grid(row=1,column=1,padx=6,pady=5)#invoice entry
      #======date===================
      date_label=Label(F2,text="DATE",bg=bg_color,fg="gold",font=("times new roman",15,"bold")).grid(row=2,column=0,padx=20,pady=5)#gstin button
      date_txt=Entry(F2,textvariable=self.date,width=35,font="arial 15",bd=4).grid(row=2,column=1,padx=6,pady=5)#destination entry
      #======state code=========
      code_label=Label(F2,text="STATE CODE",bg=bg_color,fg="gold",font=("times new roman",15,"bold")).grid(row=4,column=0,padx=20,pady=5)#state code button
      code_txt=Entry(F2,textvariable=self.statecode,width=35,font="arial 15",bd=4).grid(row=4,column=1,padx=6,pady=5)#state code entry

      #=======================================================item table==========================================================================================

      F3=LabelFrame(self.root,bd=5,relief=GROOVE,text="Invoice Details",font=("times new roman",19,"bold"),fg="white",bg=bg_color)
      F3.place(x=0,y=300,relwidth=0.624,relheight=0.5748)#invoice  frame in which all is written

      #======item particulars=========
      part1_label=Label(F3,text="Particulars",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=0,padx=20,pady=1.01)#name button
      part1_txt=Entry(F3,textvariable=self.part1,width=30,font="arial 15",bd=4).grid(row=1,column=0,padx=2,pady=5)#particulars entry
      part2_label=Label(F3,text="Particulars",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=0,padx=20,pady=1.01)#name button
      part2_txt=Entry(F3,textvariable=self.part2,width=30,font="arial 15",bd=4).grid(row=2,column=0,padx=2,pady=5)#particulars entry
      part3_label=Label(F3,text="Particulars",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=0,padx=20,pady=1.01)#name button
      part3_txt=Entry(F3,textvariable=self.part3,width=30,font="arial 15",bd=4).grid(row=3,column=0,padx=2,pady=5)#particulars entry
      part4_label=Label(F3,text="Particulars",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=0,padx=20,pady=1.01)#name button
      part4_txt=Entry(F3,width=30,textvariable=self.part4,font="arial 15",bd=4).grid(row=4,column=0,padx=2,pady=5)#particulars entry
      part5_label=Label(F3,text="Particulars",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=0,padx=20,pady=1.01)#name button
      part5_txt=Entry(F3,width=30,textvariable=self.part5,font="arial 15",bd=4).grid(row=5,column=0,padx=2,pady=5)#particulars entry
      part6_label=Label(F3,text="Particulars",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=0,padx=20,pady=1.01)#name button
      part6_txt=Entry(F3,width=30,textvariable=self.part6,font="arial 15",bd=4).grid(row=6,column=0,padx=2,pady=5)#particulars entry
      part7_label=Label(F3,text="Particulars",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=0,padx=20,pady=1.01)#name button
      part7_txt=Entry(F3,width=30,textvariable=self.part7,font="arial 15",bd=4).grid(row=8,column=0,padx=2,pady=5)#particulars entry
      #====== size ===================
      size1_label=Label(F3,text="Size",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=1,padx=1,pady=1.01)#name button
      size1_txt=Entry(F3,textvariable=self.size1,width=5,font="arial 15",bd=4).grid(row=1,column=1,padx=6,pady=5)#particulars entry
      size2_label=Label(F3,text="Size",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=1,padx=1,pady=1.01)#name button
      size2_txt=Entry(F3,textvariable=self.size2,width=5,font="arial 15",bd=4).grid(row=2,column=1,padx=6,pady=5)#particulars entry
      size3_label=Label(F3,text="Size",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=1,padx=1,pady=1.01)#name button
      size3_txt=Entry(F3,textvariable=self.size3,width=5,font="arial 15",bd=4).grid(row=3,column=1,padx=6,pady=5)#particulars entry
      size4_label=Label(F3,text="Size",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=1,padx=1,pady=1.01)#name button
      size4_txt=Entry(F3,width=5,textvariable=self.size4,font="arial 15",bd=4).grid(row=4,column=1,padx=6,pady=5)#particulars entry
      size5_label=Label(F3,text="Size",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=1,padx=1,pady=1.01)#name button
      size5_txt=Entry(F3,width=5,textvariable=self.size5,font="arial 15",bd=4).grid(row=5,column=1,padx=6,pady=5)#particulars entry
      size6_label=Label(F3,text="Size",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=1,padx=1,pady=1.01)#name button
      size6_txt=Entry(F3,width=5,textvariable=self.size6,font="arial 15",bd=4).grid(row=6,column=1,padx=6,pady=5)#particulars entry
      size7_label=Label(F3,text="Size",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=1,padx=1,pady=1.01)#name button
      size7_txt=Entry(F3,width=5,textvariable=self.size7,font="arial 15",bd=4).grid(row=8,column=1,padx=6,pady=5)#particulars entry

      #========hsn code===============
      hsn1_label=Label(F3,text="HSN",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=2,padx=1,pady=5)#name button
      hsn1_txt=Entry(F3,width=8,textvariable=self.hsn1,font="arial 15",bd=4).grid(row=1,column=2,padx=2,pady=5,)#particulars entry
      hsn2_label=Label(F3,text="HSN",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=2,padx=1,pady=5)#name button
      hsn2_txt=Entry(F3,width=8,textvariable=self.hsn2,font="arial 15",bd=4).grid(row=2,column=2,padx=2,pady=5)#particulars entry
      hsn3_label=Label(F3,text="HSN",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=2,padx=1,pady=5)#name button
      hsn3_txt=Entry(F3,width=8,textvariable=self.hsn3,font="arial 15",bd=4).grid(row=3,column=2,padx=2,pady=5)#particulars entry
      hsn4_label=Label(F3,text="HSN",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=2,padx=1,pady=5)#name button
      hsn4_txt=Entry(F3,width=8,textvariable=self.hsn4,font="arial 15",bd=4).grid(row=4,column=2,padx=2,pady=5)#particulars entry
      hsn5_label=Label(F3,text="HSN",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=2,padx=1,pady=5)#name button
      hsn5_txt=Entry(F3,width=8,textvariable=self.hsn5,font="arial 15",bd=4).grid(row=5,column=2,padx=2,pady=5)#particulars entry
      hsn6_label=Label(F3,text="HSN",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=2,padx=1,pady=5)#name button
      hsn6_txt=Entry(F3,width=8,textvariable=self.hsn6,font="arial 15",bd=4).grid(row=6,column=2,padx=2,pady=5)#particulars entry
      hsn7_label=Label(F3,text="HSN",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=2,padx=1,pady=5)#name button
      hsn7_txt=Entry(F3,width=8,textvariable=self.hsn7,font="arial 15",bd=4).grid(row=8,column=2,padx=2,pady=5)#particulars entry
      #=======qty====================
      qt1_label=Label(F3,text="Qnty",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=3,padx=3,pady=5)#name button
      qt1_txt=Entry(F3,width=5,textvariable=self.qt1,font="arial 15",bd=4).grid(row=1,column=3,padx=3,pady=5,)#particulars entry
      qt2_label=Label(F3,text="Qnty",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=3,padx=3,pady=5)#name button
      qt2_txt=Entry(F3,width=5,textvariable=self.qt2,font="arial 15",bd=4).grid(row=2,column=3,padx=3,pady=5)#particulars entry
      qt3_label=Label(F3,text="Qnty",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=3,padx=3,pady=5)#name button
      qt3_txt=Entry(F3,width=5,textvariable=self.qt3,font="arial 15",bd=4).grid(row=3,column=3,padx=3,pady=5)#particulars entry
      qt4_label=Label(F3,text="Qnty",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=3,padx=3,pady=5)#name button
      qt4_txt=Entry(F3,width=5,textvariable=self.qt4,font="arial 15",bd=4).grid(row=4,column=3,padx=3,pady=5)#particulars entry
      qt5_label=Label(F3,text="Qnty",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=3,padx=3,pady=5)#name button
      qt5_txt=Entry(F3,width=5,textvariable=self.qt5,font="arial 15",bd=4).grid(row=5,column=3,padx=3,pady=5)#particulars entry
      qt6_label=Label(F3,text="Qnty",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=3,padx=3,pady=5)#name button
      qt6_txt=Entry(F3,width=5,textvariable=self.qt6,font="arial 15",bd=4).grid(row=6,column=3,padx=3,pady=5)#particulars entry
      qt7_label=Label(F3,text="Qnty",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=3,padx=3,pady=5)#name button
      qt7_txt=Entry(F3,width=5,textvariable=self.qt7,font="arial 15",bd=4).grid(row=8,column=3,padx=3,pady=5)#particulars entry
      #=======rate===================
      r1_label=Label(F3,text="Rate",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=4,padx=3,pady=5)#name button
      r1_txt=Entry(F3,width=6,textvariable=self.r1,font="arial 15",bd=4).grid(row=1,column=4,padx=3,pady=5,)#particulars entry
      r2_label=Label(F3,text="Rate",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=4,padx=3,pady=5)#name button
      r2_txt=Entry(F3,width=6,textvariable=self.r2,font="arial 15",bd=4).grid(row=2,column=4,padx=3,pady=5)#particulars entry
      r3_label=Label(F3,text="Rate",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=4,padx=3,pady=5)#name button
      r3_txt=Entry(F3,width=6,textvariable=self.r3,font="arial 15",bd=4).grid(row=3,column=4,padx=3,pady=5)#particulars entry
      r4_label=Label(F3,text="Rate",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=4,padx=3,pady=5)#name button
      r4_txt=Entry(F3,width=6,textvariable=self.r4,font="arial 15",bd=4).grid(row=4,column=4,padx=3,pady=5)#particulars entry
      r5_label=Label(F3,text="Rate",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=4,padx=3,pady=5)#name button
      r5_txt=Entry(F3,width=6,textvariable=self.r5,font="arial 15",bd=4).grid(row=5,column=4,padx=3,pady=5)#particulars entry
      r6_label=Label(F3,text="Rate",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=4,padx=3,pady=5)#name button
      r6_txt=Entry(F3,width=6,textvariable=self.r6,font="arial 15",bd=4).grid(row=6,column=4,padx=3,pady=5)#particulars entry
      r7_label=Label(F3,text="Rate",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=4,padx=3,pady=5)#name button
      r7_txt=Entry(F3,width=6,textvariable=self.r7,font="arial 15",bd=4).grid(row=8,column=4,padx=3,pady=5)#particulars entry
      #========GSt============
      g1_label=Label(F3,text="GST",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=5,padx=3,pady=5)#name button
      g1_txt=Entry(F3,width=5,textvariable=self.g1,font="arial 15",bd=4).grid(row=1,column=5,padx=3,pady=5,)#particulars entry
      g2_label=Label(F3,text="GST",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=5,padx=3,pady=5)#name button
      g2_txt=Entry(F3,width=5,textvariable=self.g2,font="arial 15",bd=4).grid(row=2,column=5,padx=3,pady=5)#particulars entry
      g3_label=Label(F3,text="GST",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=5,padx=3,pady=5)#name button
      g3_txt=Entry(F3,width=5,textvariable=self.g3,font="arial 15",bd=4).grid(row=3,column=5,padx=3,pady=5)#particulars entry
      g4_label=Label(F3,text="GST",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=5,padx=3,pady=5)#name button
      g4_txt=Entry(F3,width=5,textvariable=self.g4,font="arial 15",bd=4).grid(row=4,column=5,padx=3,pady=5)#particulars entry
      g5_label=Label(F3,text="GST",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=5,padx=3,pady=5)#name button
      g5_txt=Entry(F3,width=5,textvariable=self.g5,font="arial 15",bd=4).grid(row=5,column=5,padx=3,pady=5)#particulars entry
      g6_label=Label(F3,text="GST",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=5,padx=3,pady=5)#name button
      g6_txt=Entry(F3,width=5,textvariable=self.g6,font="arial 15",bd=4).grid(row=6,column=5,padx=3,pady=5)#particulars entry
      g7_label=Label(F3,text="GST",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=5,padx=3,pady=5)#name button
      g7_txt=Entry(F3,width=5,textvariable=self.g7,font="arial 15",bd=4).grid(row=8,column=5,padx=3,pady=5)#particulars entry
      #========bill amount============
      tl1_label=Label(F3,text="Total",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=6,padx=3,pady=5)#name button
      tl1_txt=Entry(F3,width=7,textvariable=self.tl1,font="arial 15",bd=4).grid(row=1,column=6,padx=3,pady=5)#particulars entry
      tl2_label=Label(F3,text="Total",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=6,padx=3,pady=5)#name button
      tl2_txt=Entry(F3,width=7,textvariable=self.tl2,font="arial 15",bd=4).grid(row=2,column=6,padx=3,pady=5)#particulars entry
      tl3_label=Label(F3,text="Total",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=6,padx=3,pady=5)#name button
      tl3_txt=Entry(F3,width=7,textvariable=self.tl3,font="arial 15",bd=4).grid(row=3,column=6,padx=3,pady=5)#particulars entry
      tl4_label=Label(F3,text="Total",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=6,padx=3,pady=5)#name button
      tl4_txt=Entry(F3,width=7,textvariable=self.tl4,font="arial 15",bd=4).grid(row=4,column=6,padx=3,pady=5)#particulars entry
      tl5_label=Label(F3,text="Total",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=6,padx=3,pady=5)#name button
      tl5_txt=Entry(F3,width=7,textvariable=self.tl5,font="arial 15",bd=4).grid(row=5,column=6,padx=3,pady=5)#particulars entry
      tl6_label=Label(F3,text="Total",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=6,padx=3,pady=5)#name button
      tl6_txt=Entry(F3,width=7,textvariable=self.tl6,font="arial 15",bd=4).grid(row=6,column=6,padx=3,pady=5)#particulars entry
      tl7_label=Label(F3,text="Total",bg=bg_color,fg="gold",font=("times new roman",17,"bold")).grid(row=0,column=6,padx=3,pady=5)#name button
      tl7_txt=Entry(F3,width=7,textvariable=self.tl7,font="arial 15",bd=4).grid(row=8,column=6,padx=3,pady=5)#particulars entry

      #=======================================================================button area=========================================================================
      F4=LabelFrame(self.root,bd=5,relief=GROOVE,font=("times new roman",19,"bold"),fg="purple",bg="#658DAD")
      F4.place(x=1215,y=75,relwidth=0.12,relheight=0.32)
      generate_bill= Button(F4,command=self.bill_area,text="Generate Bill", fg="red",bg="#CEEAE8",bd=7,relief=GROOVE,font="arial 12 bold",width=13,height=2).grid(row=0,column=5,padx=1,pady=3)#command=quit)
      total_bill= Button(F4,command=self.total,text="Total", fg="red",bg="#CEEAE8",bd=7,relief=GROOVE,font="arial 12 bold",width=13,height=2).grid(row=1,column=5,padx=1,pady=3)#command=quit)
      clear_bill= Button(F4,command=self.clear,text="Clear", fg="red",bg="#CEEAE8",bd=7,relief=GROOVE,font="arial 12 bold",width=13,height=2).grid(row=2,column=5,padx=1,pady=3)#command=quit)
      #=======================================================================bill area==============================================================================

      F5=Frame(self.root,bd=5,relief=GROOVE,bg="#E3E8E4")
      F5.place(x=853,y=300,relwidth=0.374,relheight=0.578)#frame in which bill is to be displayed
      #bill_title=Label(F5,text="BILL GENX",font="arial 12 bold",bd=4,relief=GROOVE).pack(fill=X)
      scroll=Scrollbar(F5,orient=VERTICAL)
      self.txtarea=Text(F5,yscrollcommand=scroll.set,font=("arial",13,"bold"))
      scroll.pack(side=RIGHT,fill=Y)
      scroll.config(command=self.txtarea.yview)#configuring scrollbar
      self.txtarea.pack(fill=BOTH)#filling text area
      #===================================
      self.welcome_bill()#calling welcome bill in bill area
  #============================================================calculation part===========================================================================================
  def total(self):
      self.t11=(self.qt1.get()*self.r1.get())
      self.t1=self.t11+(((self.t11)*self.g1.get())/100)
      self.tl1.set(str(round((self.t1),1)))

      self.t22=(self.qt2.get()*self.r2.get())
      self.t2=self.t22+(((self.t22)*self.g2.get())/100)
      self.tl2.set(str(round((self.t2),1)))

      self.t33=(self.qt3.get()*self.r3.get())
      self.t3=self.t33+(((self.t33)*self.g3.get())/100)
      self.tl3.set(str(round((self.t3),1)))

      self.t44=(self.qt4.get()*self.r4.get())
      self.t4=self.t44+(((self.t44)*self.g4.get())/100)
      self.tl4.set(str(round((self.t4),1)))

      self.t55=(self.qt5.get()*self.r5.get())
      self.t5=self.t55+(((self.t55)*self.g5.get())/100)
      self.tl5.set(str(round((self.t5),1)))

      self.t66=(self.qt6.get()*self.r6.get())
      self.t6=self.t66+(((self.t66)*self.g6.get())/100)
      self.tl6.set(str(round((self.t6),1)))

      self.t77=(self.qt7.get()*self.r7.get())
      self.t7=self.t77+(((self.t77)*self.g7.get())/100)
      self.tl7.set(str(round((self.t7),1)))


      self.gt=float(self.t1+self.t2+self.t3+self.t4+self.t5+self.t6+self.t7)
      self.GT.set(str(round((self.gt),1)))
  #======================================================================================================================================================
  def welcome_bill(self):
      self.txtarea.delete('1.0',END)
      self.txtarea.insert(END,"\t\tBILL GENX\n\n")
      self.txtarea.insert(END,"Address:\t 79/14,Shukla Market,Latouche Road,Kanpur")
      self.txtarea.insert(END,"\nMobile Number:\t\t 8874537328\n")
      self.txtarea.insert(END,"================================================\n")
      self.txtarea.insert(END,f"      Name:  {self.c_name.get()}")
      self.txtarea.insert(END,f"\t\t\t\tPhone:  {self.phone.get()}\n")
      self.txtarea.insert(END,f"      Invoice Number:  {self.invoice.get()}")
      self.txtarea.insert(END,f"\t\t\t\tGSTIN:  {self.gstin.get()}\n")
      self.txtarea.insert(END,f"      Date:  {self.date}")
      self.txtarea.insert(END,f"\t\t\t\tState:  {self.state.get()}\n")
      self.txtarea.insert(END,"================================================\n")
      self.txtarea.insert(END,f"    GRAND TOTAL:    RS. {self.GT.get()}\n")
      self.txtarea.insert(END,"================================================\n")
      self.txtarea.insert(END,"\tParticulars|\tSize|\tQty.|\tRate   | GST   |Total\n")
      self.txtarea.insert(END,"--------------------------------------------------------------------------------\n")

  def bill_area(self):
     if self.qt1.get()==0:
         messagebox.showerror("Error","Nothing is purchased")
     else:
         self.total()
         self.welcome_bill()
         if self.qt1.get()>0:
             self.txtarea.insert(END,f"         {self.part1.get()[0:10]} |\t     {self.size1.get()} |\t\t{self.qt1.get()}|\t{self.r1.get()}/-|\t{self.g1.get()}%|   {self.tl1.get()}\n")
         if self.qt2.get()>0:
             self.txtarea.insert(END,f"         {self.part2.get()[0:10]} |\t     {self.size2.get()} |\t\t{self.qt2.get()}|\t{self.r2.get()}/-|\t{self.g2.get()}%|    {self.tl2.get()}\n")
         if self.qt3.get()>0:
             self.txtarea.insert(END,f"         {self.part3.get()[0:10]} |\t     {self.size3.get()} |\t\t{self.qt3.get()}|\t{self.r3.get()}/-|\t{self.g3.get()}%|    {self.tl3.get()}\n")
         if self.qt4.get()>0:
             self.txtarea.insert(END,f"         {self.part4.get()[0:10]} |\t     {self.size4.get()} |\t\t{self.qt4.get()}|\t{self.r4.get()}/-|\t{self.g4.get()}%|    {self.tl4.get()}\n")
         if self.qt5.get()>0:
             self.txtarea.insert(END,f"         {self.part5.get()[0:10]} |\t     {self.size5.get()} |\t\t{self.qt5.get()}|\t{self.r5.get()}/-|\t{self.g5.get()}%|    {self.tl5.get()}\n")
         if self.qt6.get()>0:
             self.txtarea.insert(END,f"         {self.part6.get()[0:10]} |\t     {self.size6.get()} |\t\t{self.qt6.get()}|\t{self.r6.get()}/-|\t{self.g6.get()}%|    {self.tl6.get()}\n")
         if self.qt7.get()>0:
             self.txtarea.insert(END,f"         {self.part7.get()[0:10]} |\t     {self.size7.get()} |\t\t{self.qt7.get()}|\t{self.r7.get()}/-|\t{self.g7.get()}%|    {self.tl7.get()}\n")
         self.save_bill()
  def save_bill(self):
       ch=messagebox.askyesno("SAVE BILL","Do you want to Save the Bill?")
       if ch>0:
           self.bill_data=self.txtarea.get('1.0',END)
           f1=open("D://project/bill generator/"+str(self.invoice.get())+".txt","w")
           f1.write(self.bill_data)
           f1.close()
           messagebox.showinfo("Saved",f"Invoice Number:{self.invoice.get()} saved successfully")

       else:
           return
  def clear(self):
        self.c_name.set("")
        self.c_address.set("")
        self.phone.set("")
        self.gstin.set("")
        self.state.set("")
        self.statecode.set("")
        self.invoice.set("")

        #====================particulars============================
        self.part1.set("")
        self.part2.set("")
        self.part3.set("")
        self.part4.set("")
        self.part5.set("")
        self.part6.set("")
        self.part7.set("")
        #====================particulars============================
        self.size1.set("")
        self.size2.set("")
        self.size3.set("")
        self.size4.set("")
        self.size5.set("")
        self.size6.set("")
        self.size7.set("")
        #====================hsn===================================
        self.hsn1.set("")
        self.hsn2.set("")
        self.hsn3.set("")
        self.hsn4.set("")
        self.hsn5.set("")
        self.hsn6.set("")
        self.hsn7.set("")
        #===================quantity==============================
        self.qt1.set(0)
        self.qt2.set(0)
        self.qt3.set(0)
        self.qt4.set(0)
        self.qt5.set(0)
        self.qt6.set(0)
        self.qt7.set(0)
        #=================rate====================================
        self.r1.set(0)
        self.r2.set(0)
        self.r3.set(0)
        self.r4.set(0)
        self.r5.set(0)
        self.r6.set(0)
        self.r7.set(0)
        #=================gst======================================
        self.g1.set(0)
        self.g2.set(0)
        self.g3.set(0)
        self.g4.set(0)
        self.g5.set(0)
        self.g6.set(0)
        self.g7.set(0)
        #================total====================================
        self.tl1.set("")
        self.tl2.set("")
        self.tl3.set("")
        self.tl4.set("")
        self.tl5.set("")
        self.tl6.set("")
        self.tl7.set("")
        self.GT.set("")




root=Tk()
obj=bill_app(root)
root.mainloop()
