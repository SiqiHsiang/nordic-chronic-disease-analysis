import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

NORDIC_COLORS = {
    'Sweden': '#006AA7',
    'Norway': '#EF2B2D',
    'Denmark': '#C60C30',
    'Finland': '#003580',
    'Iceland': '#003897',
    'Netherlands': '#FF6600'
}

def plot_diabetes_trend(df, save_path=None):
    fig, ax = plt.subplots(figsize=(10, 6))
    for country, group in df.groupby('country'):
        ax.plot(group['year'], group['diabetes_prevalence'] * 100,
                label=country, color=NORDIC_COLORS[country], linewidth=2)
    ax.set_title('Diabetes Prevalence in Nordic Countries (1990–2022)',
                 fontsize=14, fontweight='bold')
    ax.set_xlabel('Year')
    ax.set_ylabel('Prevalence (%)')
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(decimals=1))
    ax.legend(title='Country')
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150)
    plt.show()