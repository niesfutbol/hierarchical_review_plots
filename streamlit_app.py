import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
import hierarchical_review_plots as hrp


data = pd.read_csv("static/played_minutes.csv")
# ----------------- game start --------

team, player, groups = st.tabs(["Team", "Player", "Groups"])

with team:
    st.subheader("Mapa de calor")
    teams = ["Cimarrones", "Cancún", "Mineros de Zacatecas"]
    colours = {"Cimarrones": "oranges", "Cancún": "blues", "Mineros de Zacatecas": "reds"}
    team = st.selectbox("Selecciona un equipo:", teams)
    color = colours[team]
    played_minutes = data[data.team == team]

    # Consistency heat map with Altair
    hm_consistent = hrp.make_heat_map_of_consistent(data, team, color)
    st.altair_chart(hm_consistent)
    # Weighted xG with Plotly
    weighted = pd.read_csv("static/weighted_g_and_xg_94.csv")
    weight_plot = hrp.make_weighted(weighted)
    st.plotly_chart(weight_plot, use_container_width=True)
    # Tilt, PPDA, and Build-up Disruption with Altair
    tilt_ppda = pd.read_csv("static/xG_build-up_ppda_tilt_94.csv")
    options = hrp.select_pression_index()
    ppda_plot = hrp.make_tilt_ppda_build_up_disruption(tilt_ppda, options)
    st.altair_chart(ppda_plot)

with player:
    st.subheader("Gráficas de desempeño")
    radar_player = "J. Musiala"
    larga = pd.read_csv("static/larga_player.csv")
    minutes_played = 123
    scotland_logo = "logo_cinch_premiership"
    ac_milan_logo = "logo_489"
    fig = hrp.make_bar_plot_player(
        larga,
        radar_player,
        minutes_played,
        team,
        league_logo=scotland_logo,
        team_logo=ac_milan_logo,
    )
    st.plotly_chart(fig)

    player_t = larga[larga.Player == radar_player]
    fig_2 = hrp.make_bar_plot_player_2(
        player_t,
        radar_player,
        minutes_played,
        team,
        league_logo=scotland_logo,
        team_logo=ac_milan_logo,
    )
    st.plotly_chart(fig_2)


df = pd.read_csv("static/champions_team_values.csv")
with groups:
    fig = px.treemap(df, path=[px.Constant("Champions"), 'group', 'Team'], values='market_value',
                  color_continuous_scale='RdBu',
                  color_continuous_midpoint=np.average(df['market_value'], weights=df['market_value']))
    fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    st.plotly_chart(fig)
    
    fig_is = px.treemap(df, path=[px.Constant("Paridad en la Champions"), 'group', 'Team'], values='p2',
                  color='market_value',
                  color_continuous_scale='RdBu',
                  color_continuous_midpoint=np.average(df['market_value'], weights=df['market_value']))
    fig_is.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    st.plotly_chart(fig_is)


st.markdown("Made with 💖 by [nies.futbol](https://nies.futbol)")
