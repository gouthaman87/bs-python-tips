# Youtbe Link: https://www.youtube.com/watch?v=A2zlm3NkeDk

# Libraries ----
import pandas as pd
import numpy as np
from plotnine.mapping.aes import aes

from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

import plotnine as pn

# Dataset ----
mpg_df = pd.read_csv("https://gist.githubusercontent.com/omarish/5687264/raw/7e5c814ce6ef33e25d5259c1fe79463c190800d9/mpg.csv")
mpg_df

# Linear Regression: ----
df = mpg_df[["mpg", "weight"]]

y = mpg_df.mpg
X = mpg_df[["weight"]]

mod_lr = LinearRegression().fit(X, y)

mod_lr

# Results ----
mod_lr.coef_
mod_lr.intercept_

# Predictions ----
mod_lr.predict(X)

# Variance Explained ----
r2_score(
    y_true=y,
    y_pred=mod_lr.predict(X)
)

# Visualizations

df["fitted"] = mod_lr.predict(X)
df

pn.ggplot(
    pn.aes(
        "weight", "mpg",
    ),
    data=df
) + \
    pn.geom_point(alpha=0.5, color="#2c3e50") + \
    pn.geom_line(pn.aes(y="fitted"), color = "blue") + \
    pn.theme_minimal()
