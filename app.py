
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(
    page_title="Delivery Delay Analytics",
    page_icon="📦",
    layout="wide"
)

st.title("Delivery Delay & Operations Analytics")
st.write(
    "An interactive dashboard to explore shipping performance "
    "and identify potential operational hotspots."
)

DATA_DIR = Path(__file__).parent


@st.cache_data
def load_data():
    mode = pd.read_csv(DATA_DIR / "shipping_mode_summary.csv")
    region = pd.read_csv(DATA_DIR / "region_summary.csv")
    category = pd.read_csv(DATA_DIR / "category_summary.csv")
    monthly = pd.read_csv(DATA_DIR / "monthly_summary.csv")
    hotspots = pd.read_csv(DATA_DIR / "operational_hotspots.csv")
    importance = pd.read_csv(
        DATA_DIR / "model_feature_importance.csv"
    )

    return mode, region, category, monthly, hotspots, importance


try:
    mode, region, category, monthly, hotspots, importance = load_data()

    total_rows = int(mode["total_rows"].sum())
    late_rows = int(mode["late_rows"].sum())

    late_rate = (
        late_rows / total_rows * 100 if total_rows else 0
    )

    on_time_rate = 100 - late_rate

    st.sidebar.header("Dashboard Filters")

    modes = sorted(mode["Shipping Mode"].dropna().unique())
    selected_modes = st.sidebar.multiselect(
        "Shipping Mode",
        modes,
        default=modes
    )

    filtered_mode = mode[
        mode["Shipping Mode"].isin(selected_modes)
    ]

    st.subheader("Overall Shipping Performance")

    col1, col2, col3 = st.columns(3)

    col1.metric("Non-cancelled Rows", f"{total_rows:,}")
    col2.metric("Late-shipping Rate", f"{late_rate:.2f}%")
    col3.metric("On-time / Early Rate", f"{on_time_rate:.2f}%")

    st.caption(
        "Rates are based on the saved shipping-mode summaries. "
        "Cancelled rows are excluded."
    )

    st.divider()

    left, right = st.columns(2)

    with left:
        st.subheader("Late Rate by Shipping Mode")

        if not filtered_mode.empty:
            fig = px.bar(
                filtered_mode,
                x="Shipping Mode",
                y="late_rate_percent",
                color="Shipping Mode",
                labels={
                    "late_rate_percent": "Late Rate (%)"
                }
            )
            st.plotly_chart(fig, use_container_width=True)

    with right:
        st.subheader("Regional Performance")

        region_sorted = region.sort_values(
            "late_rate_percent", ascending=False
        ).head(10).sort_values("late_rate_percent")

        fig = px.bar(
            region_sorted,
            x="late_rate_percent",
            y="Order Region",
            orientation="h",
            labels={
                "late_rate_percent": "Late Rate (%)"
            }
        )
        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    st.subheader("Monthly Late-Shipping Trend")

    month_column = monthly.columns[0]

    monthly["month_label"] = monthly[month_column].astype(str)

    fig = px.line(
        monthly,
        x="month_label",
        y="late_rate_percent",
        markers=True,
        labels={
            "month_label": "Order Month",
            "late_rate_percent": "Late Rate (%)"
        }
    )

    st.plotly_chart(fig, use_container_width=True)

    left, right = st.columns(2)

    with left:
        st.subheader("Product Category Performance")

        category_sorted = category.sort_values(
            "late_rate_percent", ascending=False
        ).head(10)

        st.dataframe(
            category_sorted,
            use_container_width=True,
            hide_index=True
        )

    with right:
        st.subheader("Potential Operational Hotspots")

        st.dataframe(
            hotspots.head(15),
            use_container_width=True,
            hide_index=True
        )

    st.subheader("Decision Tree: Feature Importance")

    importance_sorted = importance.sort_values(
        "Importance", ascending=False
    ).head(15)

    fig = px.bar(
        importance_sorted.sort_values("Importance"),
        x="Importance",
        y="Feature",
        orientation="h",
        labels={"Importance": "Importance Score"}
    )

    st.plotly_chart(fig, use_container_width=True)

    st.success("Dashboard loaded successfully.")

except FileNotFoundError as error:
    st.error(
        f"Missing file: {error.filename}. "
        "Upload all six summary CSV files to the repository."
    )

except Exception as error:
    st.error(f"Dashboard could not load: {error}")
