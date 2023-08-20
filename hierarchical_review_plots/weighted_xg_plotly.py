import plotly.express as px
from PIL import Image


def make_weighted(weighted):
    weight_plot = setup_weighted(weighted)
    weight_plot = add_team_logo(weighted, weight_plot)
    return weight_plot


def setup_weighted(weighted):
    min_x = weighted.weighted_attack.min()
    max_x = weighted.weighted_attack.max()
    diff = (max_x - min_x) / 5
    weight_plot = (
        px.scatter(
            weighted,
            x="weighted_attack",
            y="weighted_deffense",
            labels={
                "weighted_attack": "Weighted xG and G For",
                "weighted_deffense": "Weighted xG and G Against",
            },
        )
        .update_layout(yaxis=dict(autorange="reversed"), xaxis_range=[min_x - diff, max_x + diff])
        .add_layout_image(
            dict(
                source=Image.open("static/logos/logo_nies.png"),
                xref="paper",
                yref="paper",
                x=0.7,
                y=0.2,
                sizex=0.2,
                sizey=0.2,
            )
        )
    )
    return weight_plot


def add_team_logo(weighted, weight_plot):
    for x, y, id_t in zip(weighted.weighted_attack, weighted.weighted_deffense, weighted.team_id):
        weight_plot.add_layout_image(
            x=x,
            y=y,
            source=Image.open(f"static/logos/logo_{id_t}.png"),
            xref="x",
            yref="y",
            sizex=0.07,
            sizey=0.07,
            xanchor="center",
            yanchor="middle",
        )
        weight_plot.layout.xaxis.fixedrange = True
        weight_plot.layout.yaxis.fixedrange = True
    return weight_plot
