# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 19:14:45 2026

@author: Clara
"""
# %% Librerias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %% WINE DATASET

# Import file
wine = pd.read_csv('wine.csv', sep=";")

# Display the first few rows of the DataFrame
print(wine.head())

# %% Correlation Matrix

# Only select numeric columns
numeric_df = wine.select_dtypes(include='number')

# Compute correlation matrix
corr = numeric_df.corr()

# Plot
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix")
plt.show()


# %% Pairplot (includes distribution plots along diagonals)
sns.pairplot(wine.select_dtypes(include='number'), kind='scatter', diag_kind='kde')
plt.suptitle("Pairplot with Distributions", y=1.02)
plt.show()


# %% Select target column and numeric features
target = 'pH'
numeric_cols = wine.select_dtypes(include='number').columns
cols_to_plot = [col for col in numeric_cols if col != target]

# Pairplot: each column vs 'C'
sns.pairplot(wine[cols_to_plot + [target]])
plt.suptitle(f"Pairwise Plots Compared to {target}", y=1.02)
plt.show()

# %% Foco en pH

import math

target = 'pH'
numeric_cols = wine.select_dtypes(include='number').columns
features = [col for col in numeric_cols if col != target]

# Layout parameters
n_plots = len(features)
cols = 3  # Number of columns in grid
rows = math.ceil(n_plots / cols)

fig, axes = plt.subplots(rows, cols, figsize=(cols * 5, rows * 4))
axes = axes.flatten()  # Flatten to 1D array for easy indexing

for i, feature in enumerate(features):
    sns.scatterplot(x=wine[feature], y=wine[target], ax=axes[i])
    axes[i].set_title(f"{feature} vs {target}")
    axes[i].set_xlabel(feature)
    axes[i].set_ylabel(target)

# Remove unused subplots
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()


# %% Foco en pH por Tipo

target = 'pH'
category_col = 'type'
numeric_cols = wine.select_dtypes(include='number').columns
features = [col for col in numeric_cols if col != target]

# Grid layout
n_plots = len(features)
cols = 2
rows = math.ceil(n_plots / cols)

fig, axes = plt.subplots(rows, cols, figsize=(cols * 5, rows * 4))
axes = axes.flatten()

for i, feature in enumerate(features):
    sns.scatterplot(data=wine, x=feature, y=target, hue=category_col, ax=axes[i])
    axes[i].set_title(f"{feature} vs {target} by {category_col}")
    axes[i].legend(title=category_col)

for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()


# %% Scatter Plot + Gráfico de líneas

target = 'pH'
category_col = 'type'
numeric_cols = wine.select_dtypes(include='number').columns
features = [col for col in numeric_cols if col != target]

# Layout settings
n_plots = len(features)
cols = 2
rows = math.ceil(n_plots / cols)

fig, axes = plt.subplots(rows, cols, figsize=(cols * 6, rows * 4))
axes = axes.flatten()

palette = sns.color_palette("Set2")
unique_categories = wine[category_col].unique()

for i, feature in enumerate(features):
    ax = axes[i]
    for j, cat in enumerate(unique_categories):
        subset = wine[wine[category_col] == cat]
        sns.regplot(
            data=subset,
            x=feature,
            y=target,
            scatter=True,
            label=str(cat),
            ax=ax,
            ci=None,
            color=palette[j],
        )
    ax.set_title(f"{feature} vs {target} by {category_col}")
    ax.set_xlabel(feature)
    ax.set_ylabel(target)
    ax.legend(title=category_col)

# Remove unused axes
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()