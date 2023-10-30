import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import numpy as np

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.set_index('date')

# Clean data
df = df[(df['value']>df['value'].quantile(0.025)) &
        (df['value']<df['value'].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    sns.lineplot(data=df)


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    
    # Copy and modify data for monthly bar plot
    months = ["January", "February", "March", "April", "May", "June", "July", "August",
    "September", "October", "November", "December"]
    df_bar = df.copy(deep=True)
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()
    df_bar['month'] = pd.Categorical(df_bar['month'], categories=months)
    df_bar_pivot = pd.pivot_table(df_bar, values="value", index="year", columns="month", aggfunc=np.mean)
  
    # Draw bar plot
    fig = df_bar_pivot.plot(kind='bar').get_figure()
    fig.set_figheight(6)
    fig.set_figwidth(8)
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')
  
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box.date = pd.to_datetime(df_box.date)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1,2,figsize=(18,6))

    # Years
    sns.boxplot(data=df_box, x="year", y="value", ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")
  
    # Months
    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    sns.boxplot(data=df_box, x="month", y="value", order=month_order, ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
