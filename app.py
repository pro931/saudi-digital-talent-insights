"""
Saudi Digital Talent Insights - Interactive Dashboard
Author : Rimas Alshahrani, Data Analyst
Data   : GASTAT Labour Market Statistics (Q2 2022 - Q2 2026)
Run    : streamlit run app.py
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# ----------------------------------------------------------
# Page setup
# ----------------------------------------------------------
st.set_page_config(page_title="Saudi Digital Talent Insights", page_icon="🇸🇦", layout="wide")


GREEN = "#0B7A55"
TEAL = "#4C8DF6"
GOLD = "#C9A227"
GREY = "#8A949E"
MCIT_BENCHMARK = 35  # MCIT reported women's share in the tech workforce (%)

st.markdown(
    """
    <style>
    .block-container {padding-top: 2rem;}
    [data-testid="stMetricValue"] {font-size: 2rem; color: #0B7A55;}
    .note {color: #6b7280; font-size: 0.85rem;}
    [data-testid="stSlider"] {direction: ltr;}
    </style>
    """,
    unsafe_allow_html=True,
)


# ----------------------------------------------------------
# Load data
# ----------------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("ict_dashboard.csv")


df = load_data()

# ----------------------------------------------------------
# Sidebar filters
# ----------------------------------------------------------
st.sidebar.title("Filters")

years = sorted(df["Year"].unique())
year_range = st.sidebar.select_slider(
    "Year range", options=years, value=(years[0], years[-1])
)

group = st.sidebar.radio("Nationality", ["Saudi", "Non-Saudi", "All"], index=0)
prefix = {"Saudi": "Saudi", "Non-Saudi": "NonSaudi", "All": "All"}[group]

st.sidebar.markdown("---")
st.sidebar.markdown(
    "**Source:** General Authority for Statistics (GASTAT), "
    "Labour Market Statistics, Q2 of each year."
)
st.sidebar.markdown("**Built by:** Rimas Alshahrani")

data = df[(df["Year"] >= year_range[0]) & (df["Year"] <= year_range[1])].copy()
data["Label"] = data["Year"].astype(str)
first, last = data.iloc[0], data.iloc[-1]

# ----------------------------------------------------------
# Header
# ----------------------------------------------------------
st.title("🇸🇦 Saudi Digital Talent Insights")
st.markdown(
    "How is the **Information & Communication (ICT)** workforce in Saudi Arabia evolving, "
    "and where do women stand in it?"
)

# ----------------------------------------------------------
# KPIs
# ----------------------------------------------------------
k1, k2, k3, k4 = st.columns(4)

ict_share = last[f"{prefix}_Total"]
ict_change = last[f"{prefix}_Total"] - first[f"{prefix}_Total"]
k1.metric(
    f"ICT share of employment ({group})",
    f"{ict_share:.2f}%",
    f"{ict_change:+.2f} pts since {int(first['Year'])}",
)

saudi_women = last["Saudi_Women_in_ICT"]
k2.metric(
    "Saudi women in Saudi ICT workforce",
    f"{saudi_women:.1f}%",
    f"{saudi_women - first['Saudi_Women_in_ICT']:+.1f} pts since {int(first['Year'])}",
)

all_women = last["All_Women_in_ICT"]
k3.metric(
    "Women in total ICT workforce",
    f"{all_women:.1f}%",
    f"{all_women - first['All_Women_in_ICT']:+.1f} pts since {int(first['Year'])}",
)

gap = MCIT_BENCHMARK - saudi_women
k4.metric("Gap to MCIT 35% benchmark", f"{gap:.1f} pts", delta_color="off")

st.markdown("")

# ----------------------------------------------------------
# Row 1: ICT share trend + group comparison
# ----------------------------------------------------------
c1, c2 = st.columns(2)

with c1:
    trend = data.melt(
        id_vars="Label",
        value_vars=[f"{prefix}_Male", f"{prefix}_Female", f"{prefix}_Total"],
        var_name="Gender",
        value_name="Share",
    )
    trend["Gender"] = trend["Gender"].str.replace(f"{prefix}_", "", regex=False)
    fig1 = px.line(
        trend,
        x="Label",
        y="Share",
        color="Gender",
        markers=True,
        color_discrete_map={"Male": TEAL, "Female": GOLD, "Total": GREEN},
        title=f"Share of {group} workers employed in ICT (%)",
    )
    fig1.update_layout(yaxis_title="% of employed", xaxis_title="Year (Q2 data)", legend_title="")
    fig1.update_xaxes(type="category", showgrid=False)
    st.plotly_chart(fig1, use_container_width=True)

with c2:
    comp = data.melt(
        id_vars="Label",
        value_vars=["Saudi_Male", "Saudi_Female", "NonSaudi_Total"],
        var_name="Group",
        value_name="Share",
    )
    comp["Group"] = comp["Group"].map(
        {"Saudi_Male": "Saudi men", "Saudi_Female": "Saudi women", "NonSaudi_Total": "Non-Saudis"}
    )
    fig2 = px.bar(
        comp,
        x="Label",
        y="Share",
        color="Group",
        barmode="group",
        color_discrete_map={"Saudi men": TEAL, "Saudi women": GOLD, "Non-Saudis": GREY},
        title="Who is moving into ICT? (% of each group)",
    )
    fig2.update_layout(yaxis_title="% of employed", xaxis_title="Year (Q2 data)", legend_title="")
    fig2.update_xaxes(type="category", showgrid=False)
    st.plotly_chart(fig2, use_container_width=True)

# ----------------------------------------------------------
# Row 2: Women in the ICT workforce vs benchmark
# ----------------------------------------------------------
fig3 = go.Figure()
fig3.add_trace(
    go.Scatter(
        x=data["Label"], y=data["Saudi_Women_in_ICT"], mode="lines+markers+text",
        name="Saudi women (of Saudi ICT workers)", line=dict(color=GOLD, width=3),
        text=data["Saudi_Women_in_ICT"].round(1), textposition="top center",
    )
)
fig3.add_trace(
    go.Scatter(
        x=data["Label"], y=data["All_Women_in_ICT"], mode="lines+markers+text",
        name="All women (of all ICT workers)", line=dict(color=GREEN, width=3),
        text=data["All_Women_in_ICT"].round(1), textposition="bottom center",
    )
)
fig3.add_trace(
    go.Scatter(
        x=data["Label"], y=data["Saudi_FemaleShare"], mode="lines",
        name="Saudi women (of all Saudi workers)", line=dict(color=GREY, dash="dot"),
    )
)
fig3.add_hline(
    y=MCIT_BENCHMARK, line_dash="dash", line_color="#B42318",
    annotation_text="MCIT reported: 35%", annotation_position="top left",
)
fig3.update_xaxes(type="category", showgrid=False)
fig3.update_layout(
    title="Women's share of the ICT workforce (%)",
    yaxis_title="%", xaxis_title="Year (Q2 data)", legend_title="",
    yaxis_range=[0, 45], legend=dict(orientation="h", y=-0.2),
)
st.plotly_chart(fig3, use_container_width=True)

st.markdown(
    '<p class="note">Women\'s share of the ICT workforce is estimated by combining GASTAT tables 3-1 '
    "(gender split of employed) and 3-5 (employed by economic activity). Figures are survey-based "
    "estimates, not headcounts.</p>",
    unsafe_allow_html=True,
)

# ----------------------------------------------------------
# The problem: a matching gap
# ----------------------------------------------------------
st.markdown("---")
st.subheader("🔍 The Problem: the talent exists, but it is not reaching ICT jobs")
p1, p2, p3 = st.columns(3)
p1.metric(
    "Unemployment: Saudi women with ICT specialization",
    "16.5%",
    "vs 7.8% for Saudi men",
    delta_color="off",
)
p2.metric("Unemployed Saudi women holding a bachelor's", "60%", delta_color="off")
p3.metric("Unemployed Saudi women willing to work in private sector", "96%", delta_color="off")
st.markdown(
    "Meanwhile, recent ICT growth went mainly to non-Saudi workers. "
    "**This is a matching gap, not a talent gap.**"
)
st.markdown(
    '<p class="note">Q2 2026 · Source: GASTAT Labour Market Statistics, Tables 2-3, 2-7 and 2-11.</p>',
    unsafe_allow_html=True,
)

st.subheader("💡 Proposed Solution: “Rabt” (Connect)")
s1, s2, s3, s4 = st.columns(4)
s1.markdown("**01 · Match**  \nOne pathway linking ICT-qualified Saudi women to MCIT partner companies")
s2.markdown("**02 · Prioritize**  \nQualified Saudi candidates first for entry-level tech roles")
s3.markdown("**03 · Upskill**  \nShort training on skills the employer names, tied to a job offer")
s4.markdown("**04 · Measure**  \nTrack ICT-graduate unemployment and women's ICT share every quarter")
st.success("No new government payroll: builds on existing partnerships and private-sector demand.")

# ----------------------------------------------------------
# Insights & Recommendations
# ----------------------------------------------------------
st.markdown("---")
i1, i2 = st.columns(2)

with i1:
    st.subheader("📊 Key Findings")
    st.markdown(
        """
1. **The ICT sector is growing, but is still small:** its share of total employment rose
   from **1.14% (2022)** to **1.31% (2026)**.
2. **Saudi women make up ~31% of Saudi ICT workers**, close to MCIT's reported 35%.
   Across *all* ICT workers, including non-Saudis, women are only **~10%**.
3. **Saudi women's share in ICT fell** from **37.7% (2022)** to **27.7% (2025)** before
   recovering to **31.2% (2026)**, even while women's share of total Saudi employment
   kept rising (31% → 34%).
4. **Recent ICT growth was led by non-Saudis:** their ICT share rose from 1.23% to 1.37%
   between 2025 and 2026, while the Saudi share stayed near 1.18%.
"""
    )

with i2:
    st.subheader("💡 Recommendations")
    st.markdown(
        """
1. **Convert women's workforce growth into tech careers:** more Saudi women are joining
   the labour market, but fewer of them are choosing ICT. Targeted reskilling and
   placement programs can redirect this growth.
2. **Track both indicators:** report women's share among *all* ICT workers next to the
   Saudi-only figure, to show the full picture (~10% vs ~31%).
3. **Link partner training to private-sector hiring:** recent sector growth is driven
   mainly by non-Saudi workers; asking training partners to commit to hiring a share of
   Saudi trainees can raise Saudi uptake without new government payroll.
4. **Scale the talent pipeline:** at ~1.3% of employment, ICT still has wide room to grow
   in line with Vision 2030 digital economy goals.
"""
    )

st.markdown("---")
st.caption("Saudi Digital Talent Insights · Built with Python, Pandas, Plotly & Streamlit · Rimas Alshahrani")
