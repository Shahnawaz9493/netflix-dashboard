# 🎬 Netflix Data Analysis Dashboard

An interactive **Streamlit** dashboard for exploring the Netflix titles catalog — content type distribution, top producing countries, and release trends over time, wrapped in a custom Netflix-themed dark UI.

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</div>

---

## 📖 Overview

This project turns the classic **Netflix Titles dataset** (8,800+ Movies & TV Shows) into a clean, filterable analytics dashboard. It's built with **Streamlit** for the app layer, **Pandas** for data wrangling, and **Plotly** for interactive charts — finished off with a hand-rolled CSS theme that mimics Netflix's own dark, red-accented aesthetic.

> Built as a data analysis / dashboarding portfolio project to demonstrate end-to-end skills: data cleaning, interactive filtering, visualization, and UI polish.

## ✨ Features

- 🎛️ **Dynamic Sidebar Filters** — filter by content type (Movie / TV Show) and release year range
- 📊 **KPI Metrics** — live counts of total titles, movies, and TV shows based on current filters
- 📈 **Content Type Distribution** — bar chart comparing Movies vs. TV Shows
- 🌍 **Top 10 Producing Countries** — bar chart of the most prolific content-producing countries
- 📉 **Release Trend Over Time** — line chart tracking title releases by year
- 🗂️ **Raw Data Explorer** — interactive, sortable table of the filtered dataset
- 🎨 **Custom Netflix-Style Theme** — dark background, red accent color, styled metric cards, hover effects, and themed tables/charts
- ⚡ **Cached Data Loading** — `@st.cache_data` for fast reloads

## 🖥️ Tech Stack

| Layer | Technology |
|---|---|
| App Framework | [Streamlit](https://streamlit.io/) |
| Data Handling | [Pandas](https://pandas.pydata.org/) |
| Visualization | [Plotly Express](https://plotly.com/python/plotly-express/) |
| Styling | Custom CSS (`style.css`) |
| Data Source | [Netflix Movies and TV Shows (Kaggle)](https://www.kaggle.com/datasets/shivamb/netflix-shows) |

## 📁 Project Structure

```
netflix-data-analysis/
├── app.py                # Main Streamlit application
├── style.css              # Custom Netflix-themed styling
├── netflix_titles.csv     # Dataset (Movies & TV Shows metadata)
├── requirements.txt       # Python dependencies
└── README.md
```

## 🗃️ Dataset

The dashboard uses the Netflix Titles dataset containing **8,807 titles** (6,131 Movies, 2,676 TV Shows) released between **1925 and 2021**, with the following key fields:

`show_id`, `type`, `title`, `director`, `cast`, `country`, `date_added`, `release_year`, `rating`, `duration`, `listed_in`, `description`

Rows missing `type`, `country`, `release_year`, or `listed_in` are dropped during preprocessing to ensure clean, reliable visualizations.

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

The app will open automatically at `http://localhost:8501`.

## 🎯 Usage

1. Use the **sidebar** to select content type(s) — Movie, TV Show, or both.
2. Adjust the **release year slider** to focus on a specific time period.
3. View live-updating **KPI cards**, **charts**, and the **raw data table** below.

## 📸 Screenshots

> _Add screenshots of the dashboard here, e.g.:_
> `![Dashboard Overview](screenshots/dashboard.png)`

## 🛣️ Roadmap

- [ ] Add genre-level (`listed_in`) breakdown chart
- [ ] Add rating (TV-MA, PG-13, etc.) distribution chart
- [ ] Deploy to Streamlit Community Cloud
- [ ] Add search/filter by title, director, or cast
- [ ] Add dark/light theme toggle

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](../../issues) or open a pull request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- Dataset by [Shivam Bansal on Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows)
- Built with [Streamlit](https://streamlit.io/) and [Plotly](https://plotly.com/)

---

<div align="center">

If you found this project useful, consider giving it a ⭐!

</div>
