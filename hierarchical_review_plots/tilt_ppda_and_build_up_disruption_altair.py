import altair as alt


def select_pression_index():
    dropdown = alt.binding_select(
        options=["build_up_disruption", "ppda", "tilt"], name="Pressure indices "
    )
    return alt.param(value="tilt", bind=dropdown)


def make_tilt_ppda_build_up_disruption(tilt_ppda, xcol_param):
    tilt_plot = (
        alt.Chart(tilt_ppda)
        .mark_point()
        .encode(
            x=alt.X("x:Q").title(""),
            y="xG:Q",
            tooltip=["team", "xG", "tilt", "build_up_disruption", "ppda"],
        )
        .transform_calculate(x=f"datum[{xcol_param.name}]")
        .add_params(xcol_param)
    )
    return tilt_plot
