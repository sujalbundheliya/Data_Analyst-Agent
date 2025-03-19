import matplotlib.pyplot as plt
import seaborn as sns

def plot_data(df, x_col, y_col, plot_type="bar"):
    plt.figure(figsize=(8,6))

    if plot_type == "bar":
        sns.barplot(x=df[x_col], y=df[y_col], data=df)
    elif plot_type == "scatter":
        sns.scatterplot(x=df[x_col], y=df[y_col], data=df)

    plt.xticks(rotation=45)
    plt.title(f"{plot_type.capitalize()} Plot of {x_col} vs {y_col}")
    plt.show()
