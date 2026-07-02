<div align="center">

# 🎬 Netflix Data Analysis Dashboard

### An interactive, Netflix-themed analytics dashboard built with Streamlit, Pandas & Plotly

<p>
  <img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
</p>

<p>
  <img src="https://img.shields.io/badge/License-MIT-brightgreen?style=flat-square" />
  <img src="https://img.shields.io/badge/Status-Active-success?style=flat-square" />
  <img src="https://img.shields.io/badge/PRs-Welcome-orange?style=flat-square" />
  <img src="https://img.shields.io/github/last-commit/your-username/netflix-data-analysis?style=flat-square&color=red" />
  <img src="https://img.shields.io/github/stars/your-username/netflix-data-analysis?style=flat-square&color=yellow" />
</p>

**[View Demo](#-screenshots) · [Report Bug](../../issues) · [Request Feature](../../issues)**

</div>

<br/>

---

## 📚 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Screenshots](#-screenshots)
- [Tech Stack](#️-tech-stack)
- [Project Structure](#-project-structure)
- [Dataset](#️-dataset)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [Roadmap](#️-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgements](#-acknowledgements)

---

## 📖 Overview

This project turns the classic **Netflix Titles dataset** (8,800+ Movies & TV Shows) into a clean, filterable analytics dashboard. It's built with **Streamlit** for the app layer, **Pandas** for data wrangling, and **Plotly** for interactive charts — finished off with a hand-rolled CSS theme that mimics Netflix's own dark, red-accented aesthetic.

> 💡 Built as a data analysis / dashboarding portfolio project to demonstrate end-to-end skills: data cleaning, interactive filtering, visualization, and UI polish.

<br/>

## ✨ Features

<table>
<tr>
<td width="50%" valign="top">

**🎛️ Dynamic Filtering**
Filter by content type (Movie / TV Show) and release year range in real time

**📊 Live KPI Metrics**
Total titles, movie count, and TV show count update instantly with your filters

**📈 Content Type Distribution**
Clean bar chart comparing Movies vs. TV Shows

</td>
<td width="50%" valign="top">

**🌍 Top Producing Countries**
Bar chart of the top 10 countries by content volume

**📉 Release Trend Analysis**
Line chart tracking title releases year over year

**🗂️ Raw Data Explorer**
Interactive, sortable table of the filtered dataset

</td>
</tr>
</table>

🎨 **Custom Netflix-Style Theme** — dark background, red accent color, styled metric cards with hover effects, and themed tables/charts
⚡ **Cached Data Loading** — `@st.cache_data` for instant reloads

<br/>

## 📸 Screenshots

<table>
  <tr>
    <td align="center" width="25%">
      <img src="Screenshot%202026-07-02%20101843.png" width="220"/><br/>
      <sub><b>Dashboard Overview & KPIs</b></sub>
    </td>
    <td align="center" width="25%">
      <img src="Screenshot%202026-07-02%20101858.png" width="220"/><br/>
      <sub><b>Top Countries</b></sub>
    </td>
    <td align="center" width="25%">
      <img src="Screenshot%202026-07-02%20101918.png" width="220"/><br/>
      <sub><b>Content Release Trend</b></sub>
    </td>
    <td align="center" width="25%">
      <img src="Screenshot%202026-07-02%20101941.png" width="220"/><br/>
      <sub><b>Raw Data Explorer</b></sub>
    </td>
  </tr>
</table>

<br/>

## 🖥️ Tech Stack

<p>
  <img src="https://img.shields.io/badge/Streamlit-App%20Framework-FF4B4B?style=flat-square&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-Data%20Wrangling-150458?style=flat-square&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/Plotly-Visualization-3F4F75?style=flat-square&logo=plotly&logoColor=white" />
  <img src="https://img.shields.io/badge/CSS3-Custom%20Theme-1572B6?style=flat-square&logo=css3&logoColor=white" />
</p>

| Layer | Technology |
|---|---|
| App Framework | [Streamlit](https://streamlit.io/) |
| Data Handling | [Pandas](https://pandas.pydata.org/) |
| Visualization | [Plotly Express](https://plotly.com/python/plotly-express/) |
| Styling | Custom CSS (`style.css`) |
| Data Source | [Netflix Movies and TV Shows (Kaggle)](https://www.kaggle.com/datasets/shivamb/netflix-shows) |

<br/>

## 📁 Project Structure

```
netflix-data-analysis/
├── app.py                              # Main Streamlit application
├── style.css                           # Custom Netflix-themed styling
├── netflix_titles.csv                  # Dataset (Movies & TV Shows metadata)
├── requirements.txt                    # Python dependencies
├── README.md
├── Screenshot 2026-07-02 101843.png    # Dashboard overview screenshot
├── Screenshot 2026-07-02 101858.png    # Top countries screenshot
├── Screenshot 2026-07-02 101918.png    # Release trend screenshot
└── Screenshot 2026-07-02 101941.png    # Raw data screenshot
```

<br/>

## 🗃️ Dataset

<table>
<tr>
<td width="33%" align="center"><b>8,807</b><br/><sub>Total Titles</sub></td>
<td width="33%" align="center"><b>6,131</b><br/><sub>Movies</sub></td>
<td width="34%" align="center"><b>2,676</b><br/><sub>TV Shows</sub></td>
</tr>
</table>

The dashboard uses the Netflix Titles dataset, spanning titles released between **1925 and 2021**, with the following key fields:

`show_id` · `type` · `title` · `director` · `cast` · `country` · `date_added` · `release_year` · `rating` · `duration` · `listed_in` · `description`

> Rows missing `type`, `country`, `release_year`, or `listed_in` are dropped during preprocessing to ensure clean, reliable visualizations.

<br/>

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/netflix-data-analysis.git
cd netflix-data-analysis

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### `requirements.txt`

```
streamlit
pandas
plotly
```

### Run the App

```bash
streamlit run app.py
```

The app will open automatically at `http://localhost:8501` 🚀

<br/>

## 🎯 Usage

| Step | Action |
|---|---|
| 1️⃣ | Use the **sidebar** to select content type(s) — Movie, TV Show, or both |
| 2️⃣ | Adjust the **release year slider** to focus on a specific time period |
| 3️⃣ | View live-updating **KPI cards**, **charts**, and the **raw data table** below |

<br/>

## 🛣️ Roadmap

- [ ] Add genre-level (`listed_in`) breakdown chart
- [ ] Add rating (TV-MA, PG-13, etc.) distribution chart
- [ ] Deploy to Streamlit Community Cloud
- [ ] Add search/filter by title, director, or cast
- [ ] Add dark/light theme toggle

<br/>

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](../../issues) or open a pull request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<br/>

## 🙏 Acknowledgements

- Dataset by [Shivam Bansal on Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows)
- Built with [Streamlit](https://streamlit.io/) and [Plotly](https://plotly.com/)

---

<div align="center">

### If you found this project useful, consider giving it a ⭐

<sub>Made with ❤️ by [Mohammad Shahnawaz](https://github.com/your-username)</sub>

</div>
