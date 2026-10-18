# 🇸🇦 Saudi Digital Talent Insights

An interactive dashboard analyzing the growth of Saudi Arabia's **Information & Communication (ICT)** workforce and women's participation in tech, using official GASTAT labour market data (Q2 2022 – Q2 2026).

🔗 **Live Dashboard:** [add Streamlit link]

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

## 💡 Recommendations
1. Convert women's workforce growth into tech careers through targeted reskilling and placement programs.
2. Report women's share among all ICT workers alongside the Saudi-only figure.
3. Link training programs to direct hiring to accelerate localization in ICT roles.
4. Scale the digital talent pipeline in line with Vision 2030 goals.

## 📂 Data Source
**General Authority for Statistics (GASTAT)** – Labour Market Statistics, Q2 of each year (2022–2026):
- Table 3-1: Percentage distribution of employed by nationality and sex
- Table 3-5: Percentage distribution of employed by nationality, sex and main economic activity

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

**Rimas Alshahrani** · Data Analyst · [LinkedIn](add your link)
