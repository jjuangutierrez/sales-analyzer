import calendar
import pandas as pd
import streamlit as st
import altair as alt

def summary_statics(df: pd.DataFrame):
    mean_values = df.mean(numeric_only=True)
    median_values = df.median(numeric_only=True)
    mode_values = df.mode(numeric_only=True).iloc[0]
    min_values = df.min(numeric_only=True)
    max_values = df.max(numeric_only=True)

    st.subheader("📈 Resumen Estadístico")

    summary_text = "Media:\n"
    summary_text += mean_values.to_string() + "\n\n"

    summary_text += "Mediana:\n"
    summary_text += median_values.to_string() + "\n\n"

    summary_text += "Moda:\n"
    summary_text += mode_values.to_string() + "\n\n"

    summary_text += "Mínimos:\n"
    summary_text += min_values.to_string() + "\n\n"

    summary_text += "Máximos:\n"
    summary_text += max_values.to_string()

    st.markdown(f"```text\n{summary_text}\n```")

def top_sales(df: pd.DataFrame, product_column: str, sales_column: str):
    resumen = df.groupby(product_column)[sales_column].sum().reset_index()

    resumen = resumen.sort_values(by=sales_column, ascending=False)

    chart = alt.Chart(resumen).mark_bar().encode(
        x=alt.X(product_column, sort='-y'),
        y=alt.Y(sales_column),
        tooltip=[product_column, sales_column]
    ).properties(width=700)

    st.altair_chart(chart)

import pandas as pd
import altair as alt
import streamlit as st

def sales_month(df: pd.DataFrame, product_column: str, sales_column: str, month_column: str):
    df[month_column] = pd.to_datetime(df[month_column], errors='coerce')

    df["Mes"] = df[month_column].dt.month
    df["Mes_nombre"] = df[month_column].dt.month_name()

    resumen = (
        df.groupby(["Mes", "Mes_nombre", product_column])[sales_column]
        .sum()
        .reset_index()
    )

    resumen = resumen.sort_values(by="Mes")

    chart = (
        alt.Chart(resumen)
        .mark_bar()
        .encode(
            x=alt.X("Mes_nombre", sort=list(calendar.month_name)[1:]),
            y=alt.Y(sales_column),
            color=product_column,
            tooltip=[product_column, sales_column, "Mes_nombre"]
        )
        .properties(width=800)
    )

    st.altair_chart(chart, use_container_width=True)
