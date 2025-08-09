import streamlit as st
import pandas as pd
from components.uploader import  upload_csv
from analyzer.summary import top_sales, sales_month, summary_statics

def main():
    st.set_page_config(page_title="Sales Analyzer", page_icon="💹")
    st.title("Sales Analyzer")

    uploaded_file = upload_csv()

    if uploaded_file:
        st.success("✅ Archivo cargado correctamente")
        df = pd.read_csv(uploaded_file)

        columns = df.columns.tolist()

        st.dataframe(df)

        selected_product = st.selectbox("Selecciona la columna de producto", options=columns)
        selected_sales = st.selectbox("Selecciona la columna de ventas", options=columns)
        selected_date = st.selectbox("selecciona la columna fecha", options=columns)

        if st.button("Analizar"):
            summary_statics(df)
            top_sales(df, selected_product, selected_sales)
            sales_month(df, selected_product, selected_sales, selected_date)

            

if __name__ == "__main__":
    main()