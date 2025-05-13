📌 Project Overview
This project analyzes global COVID-19 trends including cases, deaths, recoveries, and vaccination progress across different countries. The analysis is performed using Python data tools and visualized through interactive charts and maps.

🎯 Objectives
Import and clean COVID-19 global dataset

Analyze time trends (cases, deaths, vaccinations)

Compare metrics across countries/regions

Visualize trends with charts and maps

Generate insights and create a comprehensive report

📂 Project Structure
covid19-tracker/
│
├── data/
│   └── owid-covid-data.csv         # Raw dataset
│
├── notebooks/
│   └── COVID-19_Analysis.ipynb     # Jupyter notebook with analysis
│
├── outputs/
│   ├── charts/                     # Saved visualizations
│   └── reports/                    # Exported reports
│
├── README.md                       # This file
└── requirements.txt                # Python dependencies
🛠️ Installation
Clone the repository:

bash
git clone [https://github.com/Brayodelight/Covid-19-Tracker.git]
cd covid19-tracker
Install dependencies:

bash
pip install -r requirements.txt
📊 Data Sources
Primary dataset from Our World in Data:

owid-covid-data.csv

🔍 Analysis Workflow
Data Collection: Download the dataset

Data Loading: Import into pandas DataFrame

Data Cleaning: Handle missing values, filter countries

Exploratory Analysis: Calculate statistics, identify trends

Visualization: Create charts and maps

Reporting: Document findings and insights

📈 Key Visualizations
Time series of cases/deaths by country

Comparative bar charts of metrics

Vaccination progress charts

Choropleth world map of cases/vaccinations

💡 Key Insights
Comparison of case growth rates between countries

Analysis of death rates and vaccination impact

Identification of pandemic waves and peaks

Regional differences in vaccination rollout

🚀 Running the Analysis
Launch Jupyter Notebook:

bash
jupyter notebook
Open notebooks/COVID-19_Analysis.ipynb

Run cells sequentially

📝 Output Options
Jupyter Notebook with interactive visualizations

Exported PDF report (File → Download as → PDF)

HTML version of the notebook

PowerPoint presentation (screenshots + commentary)

🤝 Contributing
Contributions are welcome! Please fork the repository and create a pull request with your improvements.

Note: The dataset is updated regularly. For the most current analysis, download the latest data from Our World in Data before running the notebook.
