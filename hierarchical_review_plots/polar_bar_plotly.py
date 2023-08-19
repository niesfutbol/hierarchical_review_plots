import plotly.express as px
from PIL import Image


def make_bar_plot_player(larga, radar_player, minutes_played, team, league_logo, team_logo):
    fig = _set_up_bar_polar(larga, radar_player, minutes_played, team)
    fig = _update_bar_polar(fig)
    return add_nies_logo(fig, league_logo, team_logo)


def add_nies_logo(fig, league_logo: str, team_logo: str):
    fig.add_layout_image(
        dict(
            source=Image.open(f"static/logos/{league_logo}.png"),
            xref="paper",
            yref="paper",
            x=0.9,
            y=1.05,
            sizex=0.2,
            sizey=0.2,
            xanchor="right",
            yanchor="bottom",
        )
    ).add_layout_image(
        dict(
            source=Image.open("static/logos/logo_nies.png"),
            xref="paper",
            yref="paper",
            x=0.05,
            y=0.05,
            sizex=0.2,
            sizey=0.2,
        )
    ).add_layout_image(
        dict(
            source=Image.open(f"static/logos/{team_logo}.png"),
            xref="paper",
            yref="paper",
            x=0.9,
            y=0.1,
            sizex=0.2,
            sizey=0.2,
            xanchor="right",
        )
    )
    return fig


def _set_up_bar_polar(larga, radar_player, minutes_played, team):
    player_t = larga[larga.Player == radar_player]
    fig = px.bar_polar(
        player_t,
        r="deciles",
        theta="variable",
        color="type_variable",
        title=f"{radar_player}, {team} ({minutes_played} minutes played)",
    )
    return fig


def _update_bar_polar(fig):
    fig.update_traces(showlegend=True)
    fig.update_polars(radialaxis_showticklabels=True)
    fig.update_layout(
        legend_title_text="Game phase",
        polar_radialaxis_ticksuffix="",
        polar_angularaxis_rotation=90,
        polar_angularaxis_direction="clockwise",
        polar_radialaxis_dtick=10,
        polar_hole=0.10,
    )
    return fig
