import pandas as pd

# Load the dataset (replace path if needed)
url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
df = pd.read_csv(url)

# Save a local copy (optional)
df.to_csv("owid-covid-data.csv", index=False)
print("Columns:", df.columns.tolist())
print("\nFirst 5 rows:")
display(df.head())

print("\nMissing values per column:")
print(df.isnull().sum())# Select key countries
countries = ["Kenya", "United States", "India", "Brazil", "Germany"]
df_filtered = df[df["location"].isin(countries)].copy()

# Convert date to datetime
df_filtered["date"] = pd.to_datetime(df_filtered["date"])

# Fill missing numerical values with 0 (or interpolate)
cols_to_fill = ["total_cases", "total_deaths", "new_cases", "people_vaccinated"]
df_filtered[cols_to_fill] = df_filtered[cols_to_fill].fillna(0)

print("Cleaned data sample:")
display(df_filtered.head())
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12, 6))
sns.lineplot(
    data=df_filtered,
    x="date",
    y="total_cases",
    hue="location",
    linewidth=2
)
plt.title("Total COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Cases (Millions)")
plt.grid(True)
plt.show()
df_filtered["death_rate"] = (df_filtered["total_deaths"] / df_filtered["total_cases"]) * 100

plt.figure(figsize=(10, 5))
sns.barplot(
    data=df_filtered.groupby("location")["death_rate"].max().reset_index(),
    x="location",
    y="death_rate",
    palette="viridis"
)
plt.title("Highest Recorded Death Rate by Country")
plt.xlabel("Country")
plt.ylabel("Death Rate (%)")
plt.xticks(rotation=45)
plt.show()
plt.figure(figsize=(12, 6))
sns.lineplot(
    data=df_filtered,
    x="date",
    y="people_vaccinated",
    hue="location",
    style="location",
    markers=True
)
plt.title("Vaccination Progress by Country")
plt.xlabel("Date")
plt.ylabel("People Vaccinated (Millions)")
plt.grid(True)
plt.show()
import plotly.express as px

# Get latest data per country
latest_data = df.dropna(subset=["iso_code"]).sort_values("date").groupby("iso_code").last().reset_index()

fig = px.choropleth(
    latest_data,
    locations="iso_code",
    color="total_cases",
    hover_name="location",
    title="Global COVID-19 Cases (Latest Data)",
    color_continuous_scale="Viridis"
)
fig.show()