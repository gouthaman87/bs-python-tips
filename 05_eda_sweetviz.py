# Blog Link: https://www.youtube.com/watch?v=CCy0JAB_fbo
# Blog Link: https://www.business-science.io/python/2021/08/03/sweetviz-eda.html

# Libraries ----
import pandas as pd
import sweetviz as sv
import plotnine as pn

# Dataset ----
mpg_df = pd.read_csv("https://gist.githubusercontent.com/omarish/5687264/raw/7e5c814ce6ef33e25d5259c1fe79463c190800d9/mpg.csv")
mpg_df

# SweetViz ----
report = sv.analyze(
    mpg_df,
    target_feat="mpg"
)

report.show_html(
    filepath="report.html"
)

# Plotnine ----
pn.ggplot(
    pn.aes(
        "horsepower", "acceleration",
        color = "mpg",
        size = "mpg"
    ),
    data = mpg_df
) + \
    pn.geom_point(alpha = 0.5) + \
    pn.geom_smooth(
        method = "lowess",
        span = 0.3,
        color = "blue"
    ) + \
    pn.guides(size = False) + \
    pn.theme_classic()
