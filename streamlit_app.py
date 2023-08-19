import altair as alt
import pandas as pd
import plotly.express as px
import streamlit as st
import hierarchical_review_plots as hrp


larga = pd.read_csv("static/larga_player.csv")
data = pd.read_csv("static/played_minutes.csv")
# ----------------- game start --------
radar_player = "J. Musiala"

fig = hrp.make_bar_plot_player(larga, radar_player)

team, player = st.tabs(["Team", "Player"])

with team:
    st.subheader("Mapa de calor")
    teams = ["Cimarrones", "Cancún", "Mineros de Zacatecas"]
    colours = {"Cimarrones": "oranges", "Cancún": "blues", "Mineros de Zacatecas": "reds"}
    team = st.selectbox("Selecciona un equipo:", teams)
    color = colours[team]
    played_minutes = data[data.team == team]

    # Crear el gráfico de Altair
    hm_consistent = hrp.make_heat_map_of_sonsistent(data, team, color)
    st.altair_chart(hm_consistent)

with player:
    st.subheader("Gráficas de desempeño")
    fig = hrp.add_nies_logo(fig)
    st.plotly_chart(fig)


st.markdown("Made with 💖 by [nies.futbol](https://nies.futbol)")
