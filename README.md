# 🇸🇦 Saudi Digital Talent Insights

An interactive dashboard analyzing the growth of Saudi Arabia's **Information & Communication (ICT)** workforce and women's participation in tech, using official GASTAT labour market data (Q2 2022 – Q2 2026).

🔗 **Live Dashboard:** [saudi-digital-talent.streamlit.app](https://saudi-digital-talent.streamlit.app)

---

## ❓ Key Questions
1. How has the ICT workforce grown over recent years?
2. What is the participation rate of women in ICT?
3. How does ICT participation differ between Saudis and non-Saudis?
4. Where are the gaps, and what can be done to close them?

## 📊 Key Findings
- The ICT sector's share of total employment grew from **1.14% (2022)** to **1.31% (2026)**.
- Saudi women make up **~31%** of Saudi ICT workers, close to MCIT's reported 35%.
- Across *all* ICT workers (including non-Saudis), women are only **~10%**.
- Saudi women's share in ICT fell from **37.7% (2022)** to **27.7% (2025)**, then recovered to **31.2% (2026)**, even as women's share of total Saudi employment rose from 31% to 34%.
- Recent ICT growth was led mainly by **non-Saudi** workers.

## 🔍 The Problem: a matching gap
- **16.5%** unemployment among Saudi women with an ICT specialization (vs 7.8% for Saudi men)
- **60%** of unemployed Saudi women hold a bachelor's degree
- **96%** of unemployed Saudi women are willing to work in the private sector

Qualified talent exists, but recent ICT growth went mainly to non-Saudis. This is a matching gap, not a talent gap.

**Proposed solution, "Rabt" (Connect):** match ICT-qualified Saudi women with MCIT partner companies, prioritize qualified Saudi candidates for entry-level tech roles, offer short employer-defined training tied to job offers, and track progress quarterly. No new government payroll required.

## 💡 Recommendations
1. Convert women's workforce growth into tech careers through targeted reskilling and placement programs.
2. Report women's share among all ICT workers alongside the Saudi-only figure.
3. Ask training partners to commit to hiring a share of Saudi trainees in private-sector ICT roles.
4. Scale the digital talent pipeline in line with Vision 2030 goals.

## 📂 Data Source
**General Authority for Statistics (GASTAT)** – Labour Market Statistics, Q2 of each year (2022–2026):
- Table 3-1: Percentage distribution of employed by nationality and sex
- Table 3-5: Percentage distribution of employed by nationality, sex and main economic activity
- Tables 2-3, 2-7 and 2-11 (Q2 2026): unemployment by specialization, education, and willingness to work in the private sector

> Note: Figures are survey-based estimates (percentages), not headcounts. Women's share of the ICT workforce is derived by combining tables 3-1 and 3-5.

## 🛠 Tools
Python · Pandas · Plotly · Streamlit · Google Colab

## 🗂 Project Files
| File | Description |
|---|---|
| `analysis.ipynb` | Data collection, cleaning, merging and EDA |
| `app.py` | Interactive Streamlit dashboard |
| `ict_dashboard.csv` | Final cleaned dataset |
| `requirements.txt` | Python libraries needed to run the app |

## ▶️ Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

---

**Rimas Alshahrani** · Data Analyst · https://www.linkedin.com/in/rimas-abdulrhman-a0018a3b6?utm_source=share_via&utm_content=profile&utm_medium=member_ios
