# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 14:13:31 2021

@author: ASUS
"""
import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(
    page_title="Dashboard",
    page_icon=":flashlight:",
    layout="wide"
    )




st.write("""
ZAYYED AKHMED ASSIDQIE

FTDS 006
         
Milestone 1

""")

df = pd.read_csv("sales_clean.csv")

show_dataframe = st.checkbox("Show Dataframe")
st.write(show_dataframe)

if show_dataframe: 

    st.write(df)


st.write("Source: https://www.kaggle.com/aungpyaeap/supermarket-sales")

st.sidebar.title("Navigation")
select_page=st.sidebar.selectbox("Pages", ["Visualization", "Hypotesis Testing"])

if select_page == "Visualization":
    
    st.title("Data Visualization")

    select_page = st.radio("Select Branch", ("All", "Yangon", "Mandalay", "Naypyitaw"))
    select_month = st.selectbox("Select Month",("All", "January", "February", "March"))

    if select_page=="All" and select_month=="All":
        df = pd.read_csv("sales_clean.csv")
        st.write("HEAT MAP")

        fig, ax = plt.subplots()
        sns.heatmap(df.corr(), ax=ax)
        st.write(fig)

    #fig = plt.figure()
    #plt.figure(figsize=(18,9))
    #sns.heatmap(df.corr(), annot=True)
    #plt.show()
    #st.pyplot(fig)

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Jumlah Transaksi di tiap Branch ")
            A = df["City"].value_counts()
            A = pd.DataFrame(A)
            chart_data = A
            st.bar_chart(chart_data) #bar chart streamlit
            #fig = px.bar(A, x=A.index, y='City')
            #st.plotly_chart(fig)
            
            st.subheader("Jenis Customer yang Paling Banyak Melakukan Transaksi")
            B = df["Customer_type"].value_counts()
            B = pd.DataFrame(B)
            B_label = list(B.index)
            fig = px.pie(B, values='Customer_type', names=B_label, color=B_label,
                         color_discrete_map={'Member':'green',
                                             'Normal':'yellow'})
            st.plotly_chart(fig)
        
            st.subheader("Jenis Pembayaran yang Paling Banyak di pakai")
            CC = df["Payment"].value_counts()
            CC = pd.DataFrame(CC)
            CC_label = list(CC.index)
            fig = go.Figure(data=[go.Pie(labels=CC_label, values=CC["Payment"], hole=.3)])
            st.plotly_chart(fig)
            
            with col2:
                st.subheader("Produk yang Paling Banyak Terjual")
                D = df.groupby("Product_line")["Quantity"].sum()
                D = pd.DataFrame(D)
                D_label = list(D.index)
                fig = px.pie(D, values='Quantity', names=D_label)
                st.plotly_chart(fig)
                
                st.bar_chart(D) #barchart streamlit
        
        
        st.subheader("Jumlah Penjualan per Hari")
        Qual = df.groupby("Date")["Quantity"].sum()
        Qual=pd.DataFrame(Qual)
        #fig = px.line(Qual, x=Qual.index, y="Quantity")
        #st.plotly_chart(fig, use_container_width=True)
        st.line_chart(Qual) #line chart streamlit
            
        st.subheader("Jumlah Penjualan per Bulan")
        QQQ = {'Date':['January', 'February', 'March'],
               'Quantity':[1965, 1654, 1891]}
            
        QQQ = pd.DataFrame(QQQ)
        fig = px.line(QQQ, x="Date", y="Quantity")
        st.plotly_chart(fig, use_container_width=True)
        
    
        c1,c2 = st.columns(2)
        with c1:
        
            st.subheader("Branch dengan Gross Income Terbesar")
            GI = df.groupby("City")["gross_income"].sum()
            GI = pd.DataFrame(GI)
            st.bar_chart(GI)
        
        
            st.subheader("Produk yang Paling Banyak Memberikan Gross Income")
            GIP = df.groupby("Product_line")["gross_income"].sum()
            GIP = pd.DataFrame(GIP)
            GIP_label = list(GIP.index)
            fig = px.pie(GIP, values='gross_income', names=GIP_label)
            st.plotly_chart(fig)
            with c2:
        
                st.subheader("Jenis Customer yang Paling Banyak Memberikan Gross Income")
                Mem = df.groupby("Customer_type")["gross_income"].sum()
                Mem = pd.DataFrame(Mem)
                Mem_label=list(Mem.index)
                fig = px.pie(Mem, values='gross_income', names=Mem_label)
                st.plotly_chart(fig)
        
        st.subheader("Gross Income per Hari")
        GID = df.groupby("Date")["gross_income"].sum()
        GID=pd.DataFrame(GID)
        fig = px.line(GID, x=GID.index, y="gross_income")
        st.plotly_chart(fig, use_container_width=True)
        
        st.subheader("Gross Income per Bulan")
        dic = {'Date':['January', 'February', 'March'],
                   'gross_income':[1925.4610,1568.3325,1771.3830]}
        
        dic = pd.DataFrame(dic)
        fig = px.line(dic, x="Date", y="gross_income")
        st.plotly_chart(fig, use_container_width=True)
    
    if select_page=="All" and select_month == "January":
        df = df[df["Date"]<"2019-02-01"]
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Jumlah Transaksi di tiap Branch ")
            A = df["City"].value_counts()
            A = pd.DataFrame(A)
            chart_data = A
            st.bar_chart(chart_data) #bar chart streamlit
            #fig = px.bar(A, x=A.index, y='City')
            #st.plotly_chart(fig)
    
            st.subheader("Jenis Customer yang Paling Banyak Melakukan Transaksi")
            B = df["Customer_type"].value_counts()
            B = pd.DataFrame(B)
            B_label = list(B.index)
            fig = px.pie(B, values='Customer_type', names=B_label, color=B_label,
                         color_discrete_map={'Member':'green',
                                             'Normal':'yellow'})
            st.plotly_chart(fig)
            
            st.subheader("Jenis Pembayaran yang Paling Banyak di pakai")
            CC = df["Payment"].value_counts()
            CC = pd.DataFrame(CC)
            CC_label = list(CC.index)
            fig = go.Figure(data=[go.Pie(labels=CC_label, values=CC["Payment"], hole=.3)])
            st.plotly_chart(fig)
            
            with col2:
                st.subheader("Produk yang Paling Banyak Terjual")
                D = df.groupby("Product_line")["Quantity"].sum()
                D = pd.DataFrame(D)
                D_label = list(D.index)
                fig = px.pie(D, values='Quantity', names=D_label)
                st.plotly_chart(fig)
                
                st.bar_chart(D) #barchart streamlit
                
        
        st.subheader("Jumlah Penjualan per Hari")
        Qual = df.groupby("Date")["Quantity"].sum()
        Qual=pd.DataFrame(Qual)
        #fig = px.line(Qual, x=Qual.index, y="Quantity")
        #st.plotly_chart(fig, use_container_width=True)
        st.line_chart(Qual) #line chart streamlit
        
    
        c1,c2 = st.columns(2)
        with c1:
        
            st.subheader("Branch dengan Gross Income Terbesar")
            GI = df.groupby("City")["gross_income"].sum()
            GI = pd.DataFrame(GI)
            st.bar_chart(GI)
        
        
            st.subheader("Produk yang Paling Banyak Memberikan Gross Income")
            GIP = df.groupby("Product_line")["gross_income"].sum()
            GIP = pd.DataFrame(GIP)
            GIP_label = list(GIP.index)
            fig = px.pie(GIP, values='gross_income', names=GIP_label)
            st.plotly_chart(fig)
            with c2:
        
                st.subheader("Jenis Customer yang Paling Banyak Memberikan Gross Income")
                Mem = df.groupby("Customer_type")["gross_income"].sum()
                Mem = pd.DataFrame(Mem)
                Mem_label=list(Mem.index)
                fig = px.pie(Mem, values='gross_income', names=Mem_label)
                st.plotly_chart(fig)
        
        st.subheader("Gross Income per Hari")
        GID = df.groupby("Date")["gross_income"].sum()
        GID=pd.DataFrame(GID)
        fig = px.line(GID, x=GID.index, y="gross_income")
        st.plotly_chart(fig, use_container_width=True)
        
    
    if select_page=="All" and select_month == "February":
        df = df[(df['Date']< "2019-03-01") & (df['Date'] > "2019-01-31")]
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Jumlah Transaksi di tiap Branch ")
            A = df["City"].value_counts()
            A = pd.DataFrame(A)
            chart_data = A
            st.bar_chart(chart_data) #bar chart streamlit
            #fig = px.bar(A, x=A.index, y='City')
            #st.plotly_chart(fig)
    
            st.subheader("Jenis Customer yang Paling Banyak Melakukan Transaksi")
            B = df["Customer_type"].value_counts()
            B = pd.DataFrame(B)
            B_label = list(B.index)
            fig = px.pie(B, values='Customer_type', names=B_label, color=B_label,
                         color_discrete_map={'Member':'green',
                                             'Normal':'yellow'})
            st.plotly_chart(fig)
        
            st.subheader("Jenis Pembayaran yang Paling Banyak di pakai")
            CC = df["Payment"].value_counts()
            CC = pd.DataFrame(CC)
            CC_label = list(CC.index)
            fig = go.Figure(data=[go.Pie(labels=CC_label, values=CC["Payment"], hole=.3)])
            st.plotly_chart(fig)
    
        with col2:
            st.subheader("Produk yang Paling Banyak Terjual")
            D = df.groupby("Product_line")["Quantity"].sum()
            D = pd.DataFrame(D)
            D_label = list(D.index)
            fig = px.pie(D, values='Quantity', names=D_label)
            st.plotly_chart(fig)
        
            st.bar_chart(D) #barchart streamlit
        
        
        st.subheader("Jumlah Penjualan per Hari")
        Qual = df.groupby("Date")["Quantity"].sum()
        Qual=pd.DataFrame(Qual)
        #fig = px.line(Qual, x=Qual.index, y="Quantity")
        #st.plotly_chart(fig, use_container_width=True)
        st.line_chart(Qual) #line chart streamlit
        
    
    
        c1,c2 = st.columns(2)
        with c1:
        
            st.subheader("Branch dengan Gross Income Terbesar")
            GI = df.groupby("City")["gross_income"].sum()
            GI = pd.DataFrame(GI)
            st.bar_chart(GI)
        
        
            st.subheader("Produk yang Paling Banyak Memberikan Gross Income")
            GIP = df.groupby("Product_line")["gross_income"].sum()
            GIP = pd.DataFrame(GIP)
            GIP_label = list(GIP.index)
            fig = px.pie(GIP, values='gross_income', names=GIP_label)
            st.plotly_chart(fig)
            with c2:
        
                st.subheader("Jenis Customer yang Paling Banyak Memberikan Gross Income")
                Mem = df.groupby("Customer_type")["gross_income"].sum()
                Mem = pd.DataFrame(Mem)
                Mem_label=list(Mem.index)
                fig = px.pie(Mem, values='gross_income', names=Mem_label)
                st.plotly_chart(fig)
        
        st.subheader("Gross Income per Hari")
        GID = df.groupby("Date")["gross_income"].sum()
        GID=pd.DataFrame(GID)
        fig = px.line(GID, x=GID.index, y="gross_income")
        st.plotly_chart(fig, use_container_width=True)
            
    
    if select_page=="All" and select_month == "March":
        df = df[(df['Date']< "2019-03-32") & (df['Date'] > "2019-02-29")]
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Jumlah Transaksi di tiap Branch ")
            A = df["City"].value_counts()
            A = pd.DataFrame(A)
            chart_data = A
            st.bar_chart(chart_data) #bar chart streamlit
            #fig = px.bar(A, x=A.index, y='City')
            #st.plotly_chart(fig)
    
            st.subheader("Jenis Customer yang Paling Banyak Melakukan Transaksi")
            B = df["Customer_type"].value_counts()
            B = pd.DataFrame(B)
            B_label = list(B.index)
            fig = px.pie(B, values='Customer_type', names=B_label, color=B_label,
                         color_discrete_map={'Member':'green',
                                             'Normal':'yellow'})
            st.plotly_chart(fig)
        
            st.subheader("Jenis Pembayaran yang Paling Banyak di pakai")
            CC = df["Payment"].value_counts()
            CC = pd.DataFrame(CC)
            CC_label = list(CC.index)
            fig = go.Figure(data=[go.Pie(labels=CC_label, values=CC["Payment"], hole=.3)])
            st.plotly_chart(fig)
    
        with col2:
            st.subheader("Produk yang Paling Banyak Terjual")
            D = df.groupby("Product_line")["Quantity"].sum()
            D = pd.DataFrame(D)
            D_label = list(D.index)
            fig = px.pie(D, values='Quantity', names=D_label)
            st.plotly_chart(fig)
            
            st.bar_chart(D) #barchart streamlit
        
        
        st.subheader("Jumlah Penjualan per Hari")
        Qual = df.groupby("Date")["Quantity"].sum()
        Qual=pd.DataFrame(Qual)
        #fig = px.line(Qual, x=Qual.index, y="Quantity")
        #st.plotly_chart(fig, use_container_width=True)
        st.line_chart(Qual) #line chart streamlit
        
    
        c1,c2 = st.columns(2)
        with c1:
        
            st.subheader("Branch dengan Gross Income Terbesar")
            GI = df.groupby("City")["gross_income"].sum()
            GI = pd.DataFrame(GI)
            st.bar_chart(GI)
        
        
            st.subheader("Produk yang Paling Banyak Memberikan Gross Income")
            GIP = df.groupby("Product_line")["gross_income"].sum()
            GIP = pd.DataFrame(GIP)
            GIP_label = list(GIP.index)
            fig = px.pie(GIP, values='gross_income', names=GIP_label)
            st.plotly_chart(fig)
            with c2:
        
                st.subheader("Jenis Customer yang Paling Banyak Memberikan Gross Income")
                Mem = df.groupby("Customer_type")["gross_income"].sum()
                Mem = pd.DataFrame(Mem)
                Mem_label=list(Mem.index)
                fig = px.pie(Mem, values='gross_income', names=Mem_label)
                st.plotly_chart(fig)
        
        st.subheader("Gross Income per Hari")
        GID = df.groupby("Date")["gross_income"].sum()
        GID=pd.DataFrame(GID)
        fig = px.line(GID, x=GID.index, y="gross_income")
        st.plotly_chart(fig, use_container_width=True)
        
        st.subheader("Gross Income per Bulan")
        dic = {'Date':['January', 'February', 'March'],
               'gross_income':[1925.4610,1568.3325,1771.3830]}
            
        dic = pd.DataFrame(dic)
        fig = px.line(dic, x="Date", y="gross_income")
        st.plotly_chart(fig, use_container_width=True)

    if select_page=="Yangon" and select_month=="All":
        df_Y = df[df["City"]=="Yangon"]
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Jumlah Customer di Yangon")
            A = df_Y["Customer_type"].value_counts()
            A = pd.DataFrame(A)
            fig = px.bar(A, x=A.index, y='Customer_type')
            st.plotly_chart(fig)
    
            st.subheader("Jenis Customer yang Paling Banyak Melakukan Transaksi di Yangon")
            B = df_Y["Customer_type"].value_counts()
            B = pd.DataFrame(B)
            B_label = list(B.index)
            fig = px.pie(B, values='Customer_type', names=B_label, color=B_label,
                         color_discrete_map={'Member':'green',
                                             'Normal':'yellow'})
            st.plotly_chart(fig)
    
        with col2:
            st.subheader("Produk yang Paling Banyak Terjual di Yangon")
            D = df_Y.groupby("Product_line")["Quantity"].sum()
            D = pd.DataFrame(D)
            D_label = list(D.index)
            fig = px.pie(D, values='Quantity', names=D_label)
            st.plotly_chart(fig)
        
            st.subheader("Jenis Pembayaran yang Paling Banyak di pakai di Yangon")
            CC = df_Y["Payment"].value_counts()
            CC = pd.DataFrame(CC)
            CC_label = list(CC.index)
            fig = go.Figure(data=[go.Pie(labels=CC_label, values=CC["Payment"], hole=.3)])
            st.plotly_chart(fig)
        
        st.subheader("Jumlah Penjualan per Hari")
        Qual = df_Y.groupby("Date")["Quantity"].sum()
        Qual=pd.DataFrame(Qual)
        fig = px.line(Qual, x=Qual.index, y="Quantity")
        st.plotly_chart(fig, use_container_width=True)
        
        st.subheader("Jumlah Penjualan per Bulan")
        QQQ = {'Date':['January', 'February', 'March'],
               'Quantity':[685,493,681]}
 
        
        QQQ = pd.DataFrame(QQQ)
        fig = px.line(QQQ, x="Date", y="Quantity")
        st.plotly_chart(fig, use_container_width=True)
        
        
        st.subheader("Produk yang Paling Banyak Memberikan Gross Income")
        GIP = df_Y.groupby("Product_line")["gross_income"].sum()
        GIP = pd.DataFrame(GIP)
        GIP_label = list(GIP.index)
        fig = px.pie(GIP, values='gross_income', names=GIP_label)
        st.plotly_chart(fig)
        
        st.subheader("Jenis Customer yang Paling Banyak Memberikan Gross Income")
        Mem = df_Y.groupby("Customer_type")["gross_income"].sum()
        Mem = pd.DataFrame(Mem)
        Mem_label=list(Mem.index)
        fig = px.pie(Mem, values='gross_income', names=Mem_label)
        st.plotly_chart(fig)
        
        st.subheader("Gross Income per Hari")
        GID = df_Y.groupby("Date")["gross_income"].sum()
        GID=pd.DataFrame(GID)
        fig = px.line(GID, x=GID.index, y="gross_income")
        st.plotly_chart(fig, use_container_width=True)
        
        st.subheader("Gross Income per Bulan")
        dic = {'Date':['January', 'February', 'March'],
               'gross_income':[1841.9585,1421.9105,1793.2915]}
         
        dic = pd.DataFrame(dic)
        fig = px.line(dic, x="Date", y="gross_income")
        st.plotly_chart(fig, use_container_width=True)

    if select_page=="Yangon" and select_month=="January":
        df_A = df[df["City"]=="Yangon"]
        df_AA = df_A[df_A["Date"]<"2019-02-01"]
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Jumlah Customer di Yangon")
            A = df_AA["Customer_type"].value_counts()
            A = pd.DataFrame(A)
            fig = px.bar(A, x=A.index, y='Customer_type')
            st.plotly_chart(fig)
    
            st.subheader("Jenis Customer yang Paling Banyak Melakukan Transaksi di Yangon")
            B = df_AA["Customer_type"].value_counts()
            B = pd.DataFrame(B)
            B_label = list(B.index)
            fig = px.pie(B, values='Customer_type', names=B_label, color=B_label,
                         color_discrete_map={'Member':'green',
                                             'Normal':'yellow'})
            st.plotly_chart(fig)
    
        with col2:
            st.subheader("Produk yang Paling Banyak Terjual di Yangon")
            D = df_AA.groupby("Product_line")["Quantity"].sum()
            D = pd.DataFrame(D)
            D_label = list(D.index)
            fig = px.pie(D, values='Quantity', names=D_label)
            st.plotly_chart(fig)
        
            st.subheader("Jenis Pembayaran yang Paling Banyak di pakai di Yangon")
            CC = df_AA["Payment"].value_counts()
            CC = pd.DataFrame(CC)
            CC_label = list(CC.index)
            fig = go.Figure(data=[go.Pie(labels=CC_label, values=CC["Payment"], hole=.3)])
            st.plotly_chart(fig)
        
        st.subheader("Jumlah Penjualan per Hari")
        Qual = df_AA.groupby("Date")["Quantity"].sum()
        Qual=pd.DataFrame(Qual)
        fig = px.line(Qual, x=Qual.index, y="Quantity")
        st.plotly_chart(fig, use_container_width=True)
                
        
        st.subheader("Produk yang Paling Banyak Memberikan Gross Income")
        GIP = df_AA.groupby("Product_line")["gross_income"].sum()
        GIP = pd.DataFrame(GIP)
        GIP_label = list(GIP.index)
        fig = px.pie(GIP, values='gross_income', names=GIP_label)
        st.plotly_chart(fig)
        
        st.subheader("Jenis Customer yang Paling Banyak Memberikan Gross Income")
        Mem = df_AA.groupby("Customer_type")["gross_income"].sum()
        Mem = pd.DataFrame(Mem)
        Mem_label=list(Mem.index)
        fig = px.pie(Mem, values='gross_income', names=Mem_label)
        st.plotly_chart(fig)
        
        st.subheader("Gross Income per Hari")
        GID = df_AA.groupby("Date")["gross_income"].sum()
        GID=pd.DataFrame(GID)
        fig = px.line(GID, x=GID.index, y="gross_income")
        st.plotly_chart(fig, use_container_width=True)
        

    if select_page=="Yangon" and select_month=="February":
        df_Z = df[df["City"]=="Yangon"]
        df_Y = df_Z[(df_Z['Date']< "2019-03-01") & (df_Z['Date'] > "2019-01-31")]
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Jumlah Customer di Yangon")
            A = df_Y["Customer_type"].value_counts()
            A = pd.DataFrame(A)
            fig = px.bar(A, x=A.index, y='Customer_type')
            st.plotly_chart(fig)
    
            st.subheader("Jenis Customer yang Paling Banyak Melakukan Transaksi di Yangon")
            B = df_Y["Customer_type"].value_counts()
            B = pd.DataFrame(B)
            B_label = list(B.index)
            fig = px.pie(B, values='Customer_type', names=B_label, color=B_label,
                         color_discrete_map={'Member':'green',
                                             'Normal':'yellow'})
            st.plotly_chart(fig)
            
            with col2:
                st.subheader("Produk yang Paling Banyak Terjual di Yangon")
                D = df_Y.groupby("Product_line")["Quantity"].sum()
                D = pd.DataFrame(D)
                D_label = list(D.index)
                fig = px.pie(D, values='Quantity', names=D_label)
                st.plotly_chart(fig)
        
            st.subheader("Jenis Pembayaran yang Paling Banyak di pakai di Yangon")
            CC = df_Y["Payment"].value_counts()
            CC = pd.DataFrame(CC)
            CC_label = list(CC.index)
            fig = go.Figure(data=[go.Pie(labels=CC_label, values=CC["Payment"], hole=.3)])
            st.plotly_chart(fig)
        
        st.subheader("Jumlah Penjualan per Hari")
        Qual = df_Y.groupby("Date")["Quantity"].sum()
        Qual=pd.DataFrame(Qual)
        fig = px.line(Qual, x=Qual.index, y="Quantity")
        st.plotly_chart(fig, use_container_width=True)

        
        st.subheader("Produk yang Paling Banyak Memberikan Gross Income")
        GIP = df_Y.groupby("Product_line")["gross_income"].sum()
        GIP = pd.DataFrame(GIP)
        GIP_label = list(GIP.index)
        fig = px.pie(GIP, values='gross_income', names=GIP_label)
        st.plotly_chart(fig)
        
        st.subheader("Jenis Customer yang Paling Banyak Memberikan Gross Income")
        Mem = df_Y.groupby("Customer_type")["gross_income"].sum()
        Mem = pd.DataFrame(Mem)
        Mem_label=list(Mem.index)
        fig = px.pie(Mem, values='gross_income', names=Mem_label)
        st.plotly_chart(fig)
        
        st.subheader("Gross Income per Hari")
        GID = df_Y.groupby("Date")["gross_income"].sum()
        GID=pd.DataFrame(GID)
        fig = px.line(GID, x=GID.index, y="gross_income")
        st.plotly_chart(fig, use_container_width=True)
            

    if select_page=="Yangon" and select_month=="March":
        df_Z = df[df["City"]=="Yangon"]
        df_Y = df_Z[(df_Z['Date']< "2019-03-32") & (df_Z['Date'] > "2019-02-29")]
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Jumlah Customer di Yangon")
            A = df_Y["Customer_type"].value_counts()
            A = pd.DataFrame(A)
            fig = px.bar(A, x=A.index, y='Customer_type')
            st.plotly_chart(fig)
    
            st.subheader("Jenis Customer yang Paling Banyak Melakukan Transaksi di Yangon")
            B = df_Y["Customer_type"].value_counts()
            B = pd.DataFrame(B)
            B_label = list(B.index)
            fig = px.pie(B, values='Customer_type', names=B_label, color=B_label,
                         color_discrete_map={'Member':'green',
                                             'Normal':'yellow'})
            st.plotly_chart(fig)
    
        with col2:
            st.subheader("Produk yang Paling Banyak Terjual di Yangon")
            D = df_Y.groupby("Product_line")["Quantity"].sum()
            D = pd.DataFrame(D)
            D_label = list(D.index)
            fig = px.pie(D, values='Quantity', names=D_label)
            st.plotly_chart(fig)
        
            st.subheader("Jenis Pembayaran yang Paling Banyak di pakai di Yangon")
            CC = df_Y["Payment"].value_counts()
            CC = pd.DataFrame(CC)
            CC_label = list(CC.index)
            fig = go.Figure(data=[go.Pie(labels=CC_label, values=CC["Payment"], hole=.3)])
            st.plotly_chart(fig)
        
        st.subheader("Jumlah Penjualan per Hari")
        Qual = df_Y.groupby("Date")["Quantity"].sum()
        Qual=pd.DataFrame(Qual)
        fig = px.line(Qual, x=Qual.index, y="Quantity")
        st.plotly_chart(fig, use_container_width=True)
               
        
        st.subheader("Produk yang Paling Banyak Memberikan Gross Income")
        GIP = df_Y.groupby("Product_line")["gross_income"].sum()
        GIP = pd.DataFrame(GIP)
        GIP_label = list(GIP.index)
        fig = px.pie(GIP, values='gross_income', names=GIP_label)
        st.plotly_chart(fig)
        
        st.subheader("Jenis Customer yang Paling Banyak Memberikan Gross Income")
        Mem = df_Y.groupby("Customer_type")["gross_income"].sum()
        Mem = pd.DataFrame(Mem)
        Mem_label=list(Mem.index)
        fig = px.pie(Mem, values='gross_income', names=Mem_label)
        st.plotly_chart(fig)
        
        st.subheader("Gross Income per Hari")
        GID = df_Y.groupby("Date")["gross_income"].sum()
        GID=pd.DataFrame(GID)
        fig = px.line(GID, x=GID.index, y="gross_income")
        st.plotly_chart(fig, use_container_width=True)
        


    if select_page=="Mandalay" and select_month=="All":
        df_m = df[df["City"]=="Mandalay"]
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Jumlah Customer di Mandalay")
            A = df_m["Customer_type"].value_counts()
            A = pd.DataFrame(A)
            fig = px.bar(A, x=A.index, y='Customer_type')
            st.plotly_chart(fig)
            
            st.subheader("Jenis Customer yang Paling Banyak Melakukan Transaksi di Mandalay")
            B = df_m["Customer_type"].value_counts()
            B = pd.DataFrame(B)
            B_label = list(B.index)
            fig = px.pie(B, values='Customer_type', names=B_label, color=B_label,
                         color_discrete_map={'Member':'green',
                                             'Normal':'yellow'})
            st.plotly_chart(fig)
    
        with col2:
            st.subheader("Produk yang Paling Banyak Terjual di Mandalay")
            D = df_m.groupby("Product_line")["Quantity"].sum()
            D = pd.DataFrame(D)
            D_label = list(D.index)
            fig = px.pie(D, values='Quantity', names=D_label)
            st.plotly_chart(fig)
        
            st.subheader("Jenis Pembayaran yang Paling Banyak di pakai di Mandalay")
            CC = df_m["Payment"].value_counts()
            CC = pd.DataFrame(CC)
            CC_label = list(CC.index)
            fig = go.Figure(data=[go.Pie(labels=CC_label, values=CC["Payment"], hole=.3)])
            st.plotly_chart(fig)
        
        st.subheader("Jumlah Penjualan per Hari")
        Qual = df_m.groupby("Date")["Quantity"].sum()
        Qual=pd.DataFrame(Qual)
        fig = px.line(Qual, x=Qual.index, y="Quantity")
        st.plotly_chart(fig, use_container_width=True)
        
        st.subheader("Jumlah Penjualan per Bulan")
        QQQ = {'Date':['January', 'February', 'March'],
               'Quantity':[600,624,596]}
 
        
        QQQ = pd.DataFrame(QQQ)
        fig = px.line(QQQ, x="Date", y="Quantity")
        st.plotly_chart(fig, use_container_width=True)
            
        
        st.subheader("Produk yang Paling Banyak Memberikan Gross Income")
        GIP = df_m.groupby("Product_line")["gross_income"].sum()
        GIP = pd.DataFrame(GIP)
        GIP_label = list(GIP.index)
        fig = px.pie(GIP, values='gross_income', names=GIP_label)
        st.plotly_chart(fig)
        
        st.subheader("Jenis Customer yang Paling Banyak Memberikan Gross Income")
        Mem = df_m.groupby("Customer_type")["gross_income"].sum()
        Mem = pd.DataFrame(Mem)
        Mem_label=list(Mem.index)
        fig = px.pie(Mem, values='gross_income', names=Mem_label)
        st.plotly_chart(fig)
        
        st.subheader("Gross Income per Hari")
        GID = df_m.groupby("Date")["gross_income"].sum()
        GID=pd.DataFrame(GID)
        fig = px.line(GID, x=GID.index, y="gross_income")
        st.plotly_chart(fig, use_container_width=True)
        
        st.subheader("Gross Income per Bulan")
        dic = {'Date':['January', 'February', 'March'],
               'gross_income':[1770.2885,1639.2510,1647.4925]}
         
        dic = pd.DataFrame(dic)
        fig = px.line(dic, x="Date", y="gross_income")
        st.plotly_chart(fig, use_container_width=True)
    
    
    if select_page=="Mandalay" and select_month=="January":
        df_Y = df[df["City"]=="Mandalay"]
        df_Y = df_Y[df_Y["Date"]<"2019-02-01"]
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Jumlah Customer")
            A = df_Y["Customer_type"].value_counts()
            A = pd.DataFrame(A)
            fig = px.bar(A, x=A.index, y='Customer_type')
            st.plotly_chart(fig)
    
            st.subheader("Jenis Customer yang Paling Banyak Melakukan Transaksi")
            B = df_Y["Customer_type"].value_counts()
            B = pd.DataFrame(B)
            B_label = list(B.index)
            fig = px.pie(B, values='Customer_type', names=B_label, color=B_label,
                         color_discrete_map={'Member':'green',
                                             'Normal':'yellow'})
            st.plotly_chart(fig)
    
        with col2:
            st.subheader("Produk yang Paling Banyak Terjual")
            D = df_Y.groupby("Product_line")["Quantity"].sum()
            D = pd.DataFrame(D)
            D_label = list(D.index)
            fig = px.pie(D, values='Quantity', names=D_label)
            st.plotly_chart(fig)
        
            st.subheader("Jenis Pembayaran yang Paling Banyak di pakai")
            CC = df_Y["Payment"].value_counts()
            CC = pd.DataFrame(CC)
            CC_label = list(CC.index)
            fig = go.Figure(data=[go.Pie(labels=CC_label, values=CC["Payment"], hole=.3)])
            st.plotly_chart(fig)
        
        st.subheader("Jumlah Penjualan per Hari")
        Qual = df_Y.groupby("Date")["Quantity"].sum()
        Qual=pd.DataFrame(Qual)
        fig = px.line(Qual, x=Qual.index, y="Quantity")
        st.plotly_chart(fig, use_container_width=True)
        
        
        
        st.subheader("Produk yang Paling Banyak Memberikan Gross Income")
        GIP = df_Y.groupby("Product_line")["gross_income"].sum()
        GIP = pd.DataFrame(GIP)
        GIP_label = list(GIP.index)
        fig = px.pie(GIP, values='gross_income', names=GIP_label)
        st.plotly_chart(fig)
        
        st.subheader("Jenis Customer yang Paling Banyak Memberikan Gross Income")
        Mem = df_Y.groupby("Customer_type")["gross_income"].sum()
        Mem = pd.DataFrame(Mem)
        Mem_label=list(Mem.index)
        fig = px.pie(Mem, values='gross_income', names=Mem_label)
        st.plotly_chart(fig)
        
        st.subheader("Gross Income per Hari")
        GID = df_Y.groupby("Date")["gross_income"].sum()
        GID=pd.DataFrame(GID)
        fig = px.line(GID, x=GID.index, y="gross_income")
        st.plotly_chart(fig, use_container_width=True)
        
    
    if select_page=="Mandalay" and select_month=="February":
        df_Z = df[df["City"]=="Mandalay"]
        df_Y = df_Z[(df_Z['Date']< "2019-02-32") & (df_Z['Date'] > "2019-01-32")]
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Jumlah Customer")
            A = df_Y["Customer_type"].value_counts()
            A = pd.DataFrame(A)
            fig = px.bar(A, x=A.index, y='Customer_type')
            st.plotly_chart(fig)
    
            st.subheader("Jenis Customer yang Paling Banyak Melakukan Transaksi")
            B = df_Y["Customer_type"].value_counts()
            B = pd.DataFrame(B)
            B_label = list(B.index)
            fig = px.pie(B, values='Customer_type', names=B_label, color=B_label,
                         color_discrete_map={'Member':'green',
                                             'Normal':'yellow'})
            st.plotly_chart(fig)
    
        with col2:
            st.subheader("Produk yang Paling Banyak Terjual")
            D = df_Y.groupby("Product_line")["Quantity"].sum()
            D = pd.DataFrame(D)
            D_label = list(D.index)
            fig = px.pie(D, values='Quantity', names=D_label)
            st.plotly_chart(fig)
        
            st.subheader("Jenis Pembayaran yang Paling Banyak di pakai")
            CC = df_Y["Payment"].value_counts()
            CC = pd.DataFrame(CC)
            CC_label = list(CC.index)
            fig = go.Figure(data=[go.Pie(labels=CC_label, values=CC["Payment"], hole=.3)])
            st.plotly_chart(fig)
        
        st.subheader("Jumlah Penjualan per Hari")
        Qual = df_Y.groupby("Date")["Quantity"].sum()
        Qual=pd.DataFrame(Qual)
        fig = px.line(Qual, x=Qual.index, y="Quantity")
        st.plotly_chart(fig, use_container_width=True)
        
        
        st.subheader("Produk yang Paling Banyak Memberikan Gross Income")
        GIP = df_Y.groupby("Product_line")["gross_income"].sum()
        GIP = pd.DataFrame(GIP)
        GIP_label = list(GIP.index)
        fig = px.pie(GIP, values='gross_income', names=GIP_label)
        st.plotly_chart(fig)
        
        st.subheader("Jenis Customer yang Paling Banyak Memberikan Gross Income")
        Mem = df_Y.groupby("Customer_type")["gross_income"].sum()
        Mem = pd.DataFrame(Mem)
        Mem_label=list(Mem.index)
        fig = px.pie(Mem, values='gross_income', names=Mem_label)
        st.plotly_chart(fig)
        
        st.subheader("Gross Income per Hari")
        GID = df_Y.groupby("Date")["gross_income"].sum()
        GID=pd.DataFrame(GID)
        fig = px.line(GID, x=GID.index, y="gross_income")
        st.plotly_chart(fig, use_container_width=True)
        

    if select_page=="Mandalay" and select_month=="March":
        df_Z = df[df["City"]=="Mandalay"]
        df_Y = df_Z[(df_Z['Date']< "2019-03-32") & (df_Z['Date'] > "2019-02-32")]
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Jumlah Customer")
            A = df_Y["Customer_type"].value_counts()
            A = pd.DataFrame(A)
            fig = px.bar(A, x=A.index, y='Customer_type')
            st.plotly_chart(fig)
    
            st.subheader("Jenis Customer yang Paling Banyak Melakukan Transaksi")
            B = df_Y["Customer_type"].value_counts()
            B = pd.DataFrame(B)
            B_label = list(B.index)
            fig = px.pie(B, values='Customer_type', names=B_label, color=B_label,
                         color_discrete_map={'Member':'green',
                                             'Normal':'yellow'})
            st.plotly_chart(fig)
            
            with col2:
                st.subheader("Produk yang Paling Banyak Terjual")
                D = df_Y.groupby("Product_line")["Quantity"].sum()
                D = pd.DataFrame(D)
                D_label = list(D.index)
                fig = px.pie(D, values='Quantity', names=D_label)
                st.plotly_chart(fig)
                
                st.subheader("Jenis Pembayaran yang Paling Banyak di pakai")
                CC = df_Y["Payment"].value_counts()
                CC = pd.DataFrame(CC)
                CC_label = list(CC.index)
                fig = go.Figure(data=[go.Pie(labels=CC_label, values=CC["Payment"], hole=.3)])
                st.plotly_chart(fig)
        
        st.subheader("Jumlah Penjualan per Hari")
        Qual = df_Y.groupby("Date")["Quantity"].sum()
        Qual=pd.DataFrame(Qual)
        fig = px.line(Qual, x=Qual.index, y="Quantity")
        st.plotly_chart(fig, use_container_width=True)
 
        
        st.subheader("Produk yang Paling Banyak Memberikan Gross Income")
        GIP = df_Y.groupby("Product_line")["gross_income"].sum()
        GIP = pd.DataFrame(GIP)
        GIP_label = list(GIP.index)
        fig = px.pie(GIP, values='gross_income', names=GIP_label)
        st.plotly_chart(fig)
            
        st.subheader("Jenis Customer yang Paling Banyak Memberikan Gross Income")
        Mem = df_Y.groupby("Customer_type")["gross_income"].sum()
        Mem = pd.DataFrame(Mem)
        Mem_label=list(Mem.index)
        fig = px.pie(Mem, values='gross_income', names=Mem_label)
        st.plotly_chart(fig)
            
        st.subheader("Gross Income per Hari")
        GID = df_Y.groupby("Date")["gross_income"].sum()
        GID=pd.DataFrame(GID)
        fig = px.line(GID, x=GID.index, y="gross_income")
        st.plotly_chart(fig, use_container_width=True)
            
    
    if select_page=="Naypyitaw" and select_month=="All":
        df_N = df[df["City"]=="Naypyitaw"]
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Jumlah Customer di Naypyitaw")
            A = df_N["Customer_type"].value_counts()
            A = pd.DataFrame(A)
            fig = px.bar(A, x=A.index, y='Customer_type')
            st.plotly_chart(fig)
            
            st.subheader("Jenis Customer yang Paling Banyak Melakukan Transaksi di Naypyitaw")
            B = df_N["Customer_type"].value_counts()
            B = pd.DataFrame(B)
            B_label = list(B.index)
            fig = px.pie(B, values='Customer_type', names=B_label, color=B_label,
                         color_discrete_map={'Member':'green',
                                             'Normal':'yellow'})
            st.plotly_chart(fig)
            
            with col2:
                st.subheader("Produk yang Paling Banyak Terjual di Naypyitaw")
                D = df_N.groupby("Product_line")["Quantity"].sum()
                D = pd.DataFrame(D)
                D_label = list(D.index)
                fig = px.pie(D, values='Quantity', names=D_label)
                st.plotly_chart(fig)
                
                st.subheader("Jenis Pembayaran yang Paling Banyak di pakai di Naypyitaw")
                CC = df_N["Payment"].value_counts()
                CC = pd.DataFrame(CC)
                CC_label = list(CC.index)
                fig = go.Figure(data=[go.Pie(labels=CC_label, values=CC["Payment"], hole=.3)])
                st.plotly_chart(fig)
        
        st.subheader("Jumlah Penjualan per Hari")
        Qual = df_N.groupby("Date")["Quantity"].sum()
        Qual=pd.DataFrame(Qual)
        fig = px.line(Qual, x=Qual.index, y="Quantity")
        st.plotly_chart(fig, use_container_width=True)
        
        st.subheader("Jumlah Penjualan per Bulan")
        QQQ = {'Date':['January', 'February', 'March'],
               'Quantity':[680,537,614]}
 
        
        QQQ = pd.DataFrame(QQQ)
        fig = px.line(QQQ, x="Date", y="Quantity")
        st.plotly_chart(fig, use_container_width=True)
            
        
        st.subheader("Produk yang Paling Banyak Memberikan Gross Income")
        GIP = df_N.groupby("Product_line")["gross_income"].sum()
        GIP = pd.DataFrame(GIP)
        GIP_label = list(GIP.index)
        fig = px.pie(GIP, values='gross_income', names=GIP_label)
        st.plotly_chart(fig)
        
        st.subheader("Jenis Customer yang Paling Banyak Memberikan Gross Income")
        Mem = df_N.groupby("Customer_type")["gross_income"].sum()
        Mem = pd.DataFrame(Mem)
        Mem_label=list(Mem.index)
        fig = px.pie(Mem, values='gross_income', names=Mem_label)
        st.plotly_chart(fig)
        
        st.subheader("Gross Income per Hari")
        GID = df_N.groupby("Date")["gross_income"].sum()
        GID=pd.DataFrame(GID)
        fig = px.line(GID, x=GID.index, y="gross_income")
        st.plotly_chart(fig, use_container_width=True)
        
        st.subheader("Gross Income per Bulan")
        dic = {'Date':['January', 'February', 'March'],
               'gross_income':[1925.4610,1568.3325,1771.3830]}
             
        dic = pd.DataFrame(dic)
        fig = px.line(dic, x="Date", y="gross_income")
        st.plotly_chart(fig, use_container_width=True)
    
    if select_page=="Naypyitaw" and select_month=="January":
        df_Z = df[df["City"]=="Naypyitaw"]
        df_Y = df_Z[df_Z["Date"]<"2019-02-01"]
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Jumlah Customer")
            A = df_Y["Customer_type"].value_counts()
            A = pd.DataFrame(A)
            fig = px.bar(A, x=A.index, y='Customer_type')
            st.plotly_chart(fig)
    
            st.subheader("Jenis Customer yang Paling Banyak Melakukan Transaksi")
            B = df_Y["Customer_type"].value_counts()
            B = pd.DataFrame(B)
            B_label = list(B.index)
            fig = px.pie(B, values='Customer_type', names=B_label, color=B_label,
                         color_discrete_map={'Member':'green',
                                             'Normal':'yellow'})
            st.plotly_chart(fig)
    
        with col2:
            st.subheader("Produk yang Paling Banyak Terjual")
            D = df_Y.groupby("Product_line")["Quantity"].sum()
            D = pd.DataFrame(D)
            D_label = list(D.index)
            fig = px.pie(D, values='Quantity', names=D_label)
            st.plotly_chart(fig)
        
            st.subheader("Jenis Pembayaran yang Paling Banyak di pakai")
            CC = df_Y["Payment"].value_counts()
            CC = pd.DataFrame(CC)
            CC_label = list(CC.index)
            fig = go.Figure(data=[go.Pie(labels=CC_label, values=CC["Payment"], hole=.3)])
            st.plotly_chart(fig)
        
        st.subheader("Jumlah Penjualan per Hari")
        Qual = df_Y.groupby("Date")["Quantity"].sum()
        Qual=pd.DataFrame(Qual)
        fig = px.line(Qual, x=Qual.index, y="Quantity")
        st.plotly_chart(fig, use_container_width=True)
              
        
        st.subheader("Produk yang Paling Banyak Memberikan Gross Income")
        GIP = df_Y.groupby("Product_line")["gross_income"].sum()
        GIP = pd.DataFrame(GIP)
        GIP_label = list(GIP.index)
        fig = px.pie(GIP, values='gross_income', names=GIP_label)
        st.plotly_chart(fig)
        
        st.subheader("Jenis Customer yang Paling Banyak Memberikan Gross Income")
        Mem = df_Y.groupby("Customer_type")["gross_income"].sum()
        Mem = pd.DataFrame(Mem)
        Mem_label=list(Mem.index)
        fig = px.pie(Mem, values='gross_income', names=Mem_label)
        st.plotly_chart(fig)
        
        st.subheader("Gross Income per Hari")
        GID = df_Y.groupby("Date")["gross_income"].sum()
        GID=pd.DataFrame(GID)
        fig = px.line(GID, x=GID.index, y="gross_income")
        st.plotly_chart(fig, use_container_width=True)
            
    if select_page=="Naypyitaw" and select_month=="February":
        df_Z = df[df["City"]=="Naypyitaw"]
        df_Y = df_Z[(df_Z['Date']< "2019-03-32") & (df_Z['Date'] > "2019-01-32")]
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Jumlah Customer")
            A = df_Y["Customer_type"].value_counts()
            A = pd.DataFrame(A)
            fig = px.bar(A, x=A.index, y='Customer_type')
            st.plotly_chart(fig)
    
            st.subheader("Jenis Customer yang Paling Banyak Melakukan Transaksi")
            B = df_Y["Customer_type"].value_counts()
            B = pd.DataFrame(B)
            B_label = list(B.index)
            fig = px.pie(B, values='Customer_type', names=B_label, color=B_label,
                        color_discrete_map={'Member':'green',
                                            'Normal':'yellow'})
            st.plotly_chart(fig)
    
        with col2:
            st.subheader("Produk yang Paling Banyak Terjual")
            D = df_Y.groupby("Product_line")["Quantity"].sum()
            D = pd.DataFrame(D)
            D_label = list(D.index)
            fig = px.pie(D, values='Quantity', names=D_label)
            st.plotly_chart(fig)
        
            st.subheader("Jenis Pembayaran yang Paling Banyak di pakai")
            CC = df_Y["Payment"].value_counts()
            CC = pd.DataFrame(CC)
            CC_label = list(CC.index)
            fig = go.Figure(data=[go.Pie(labels=CC_label, values=CC["Payment"], hole=.3)])
            st.plotly_chart(fig)
        
        st.subheader("Jumlah Penjualan per Hari")
        Qual = df_Y.groupby("Date")["Quantity"].sum()
        Qual=pd.DataFrame(Qual)
        fig = px.line(Qual, x=Qual.index, y="Quantity")
        st.plotly_chart(fig, use_container_width=True)
        
        
        st.subheader("Produk yang Paling Banyak Memberikan Gross Income")
        GIP = df_Y.groupby("Product_line")["gross_income"].sum()
        GIP = pd.DataFrame(GIP)
        GIP_label = list(GIP.index)
        fig = px.pie(GIP, values='gross_income', names=GIP_label)
        st.plotly_chart(fig)
        
        st.subheader("Jenis Customer yang Paling Banyak Memberikan Gross Income")
        Mem = df_Y.groupby("Customer_type")["gross_income"].sum()
        Mem = pd.DataFrame(Mem)
        Mem_label=list(Mem.index)
        fig = px.pie(Mem, values='gross_income', names=Mem_label)
        st.plotly_chart(fig)
        
        st.subheader("Gross Income per Hari")
        GID = df_Y.groupby("Date")["gross_income"].sum()
        GID=pd.DataFrame(GID)
        fig = px.line(GID, x=GID.index, y="gross_income")
        st.plotly_chart(fig, use_container_width=True)
        

    if select_page=="Naypyitaw" and select_month=="March":
        df_Z = df[df["City"]=="Naypyitaw"]
        df_Y = df_Z[(df_Z['Date']< "2019-03-32") & (df_Z['Date'] > "2019-02-32")]
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Jumlah Customer di Naypyitaw Bulan Maret")
            A = df_Y["Customer_type"].value_counts()
            A = pd.DataFrame(A)
            fig = px.bar(A, x=A.index, y='Customer_type')
            st.plotly_chart(fig)
    
            st.subheader("Jenis Customer yang Paling Banyak Melakukan Transaksi")
            B = df_Y["Customer_type"].value_counts()
            B = pd.DataFrame(B)
            B_label = list(B.index)
            fig = px.pie(B, values='Customer_type', names=B_label, color=B_label,
                         color_discrete_map={'Member':'green',
                                             'Normal':'yellow'})
            st.plotly_chart(fig)
    
        with col2:
            st.subheader("Produk yang Paling Banyak Terjual")
            D = df_Y.groupby("Product_line")["Quantity"].sum()
            D = pd.DataFrame(D)
            D_label = list(D.index)
            fig = px.pie(D, values='Quantity', names=D_label)
            st.plotly_chart(fig)
            
            st.subheader("Jenis Pembayaran yang Paling Banyak di pakai")
            CC = df_Y["Payment"].value_counts()
            CC = pd.DataFrame(CC)
            CC_label = list(CC.index)
            fig = go.Figure(data=[go.Pie(labels=CC_label, values=CC["Payment"], hole=.3)])
            st.plotly_chart(fig)
            
        st.subheader("Jumlah Penjualan per Hari")
        Qual = df_Y.groupby("Date")["Quantity"].sum()
        Qual=pd.DataFrame(Qual)
        fig = px.line(Qual, x=Qual.index, y="Quantity")
        st.plotly_chart(fig, use_container_width=True)
            
            
        
        st.subheader("Produk yang Paling Banyak Memberikan Gross Income")
        GIP = df_Y.groupby("Product_line")["gross_income"].sum()
        GIP = pd.DataFrame(GIP)
        GIP_label = list(GIP.index)
        fig = px.pie(GIP, values='gross_income', names=GIP_label)
        st.plotly_chart(fig)
        
        st.subheader("Jenis Customer yang Paling Banyak Memberikan Gross Income")
        Mem = df_Y.groupby("Customer_type")["gross_income"].sum()
        Mem = pd.DataFrame(Mem)
        Mem_label=list(Mem.index)
        fig = px.pie(Mem, values='gross_income', names=Mem_label)
        st.plotly_chart(fig)
        
        st.subheader("Gross Income per Hari")
        GID = df_Y.groupby("Date")["gross_income"].sum()
        GID=pd.DataFrame(GID)
        fig = px.line(GID, x=GID.index, y="gross_income")
        st.plotly_chart(fig, use_container_width=True)
        
    

else:
    
    st.title("Hypotesis Testing")

    st.write("""Hipotesis testing ini bertunjuan untuk menentukan
             apakah rata rata dari gross income dari tiap branch 
             memiliki perbedaan yang signifikan apa tidak dengan 
             menggunakan One Way Anova dengan membandingkan 3 variable

    """)
    
    st.title("Parameter")

    st.write("""Parameter dari pengujian hipotesis ini adalah 
         
             H0: μ_yangon = μ_mandalay = μ_naypyitaw
             H1: μ_yangon != μ_mandalay != μ_naypyitaw

    """)

    st.write("""Distribusi data dari gross income tiap branch adalah
             seperti berikut

    """)
    fig = plt.figure()
    df = pd.read_csv("sales_clean.csv")
    sns.histplot(df[df['City'] == 'Yangon']['gross_income'], color='red', kde=True, label='Gross Income Yangon')
    sns.histplot(df[df['City'] == 'Mandalay']['gross_income'], color='green', kde=True, label='Gross Income Mandalay')
    sns.histplot(df[df['City'] == 'Naypyitaw']['gross_income'], color='blue', kde=True, label='Gross Income Naypyitaw')
    plt.legend()
    plt.show()

    st.pyplot(fig)

    Yan = df[df["City"]=="Yangon"][["City","gross_income"]]
    Man = df[df["City"]=="Mandalay"][["City","gross_income"]]
    Nay = df[df["City"]=="Naypyitaw"][["City","gross_income"]]
    
    f_stat,p_value = stats.f_oneway(Yan["gross_income"], Man["gross_income"], Nay["gross_income"])
    
    st.title("Hasil Hipotesis")
    st.write("""Hasil p value dari testing One Way ANOVA ini berkisar 0.413210174367147
             yang berarti nilai p value lebih besar dari nilai Confidence intervalnya yaitu 0.05
             ini menandakan H0 diterima yang berarti rata rata penjualan tiap branch Supermarket
             ini tidak mempunyai perbedaan yang signifikan atau cenderung sama, ini dapat dilihat dari nilai rata2 gross income
             dari tiap branch dimana yangon 14.87400147058824, Mandalay 15.232024096385551 dan Naypyitaw 16.05236737804879
             """)
    