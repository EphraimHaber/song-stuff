import streamlit as st

from my_data import fetch_artist_data, fetch_available_track_names

st.set_page_config(layout="wide")
st.title("Artist Albums and Tracks")


if "artist_data" not in st.session_state:
    st.session_state.artist_data = fetch_artist_data()

if "available_track_names" not in st.session_state:
    st.session_state.available_track_names = fetch_available_track_names()


albums_data = st.session_state.artist_data["albums"]
available_track_names = st.session_state.available_track_names


st.markdown(
    """
    <style>
    [data-baseweb="tag"] {
        width: 90%;
    }
    .st-de {
        max-width: 90%;
    }
    .row-widget.stRadio {
        justify-content: center;
    }
    </style>
""",
    unsafe_allow_html=True,
)


def update_album_state(index, field, field_type: str):
    albums_data[index][field] = st.session_state[f"{field}_{field_type}_{index}"]


def checkbox_builder(label: str, index: int, value: bool, key: str, field: str):
    st.checkbox(
        label=label,
        value=value,
        key=key,
        on_change=lambda: update_album_state(index, field, "checkbox"),
    )


def multiselect_builder(label: str, index: int, value: list, key: str, field: str):
    st.multiselect(
        label=label,
        options=available_track_names,
        default=value,
        key=key,
        on_change=lambda: update_album_state(index, field, "multiselect"),
        label_visibility="collapsed",
    )


def main():
    for index, row in enumerate(albums_data):
        st.divider()
        st.subheader(row["name"])
        _, col2, col3, col4 = st.columns(
            [1, 1, 1, 1], vertical_alignment="center", gap="small"
        )
        with col2:
            checkbox_builder(
                label="CP",
                index=index,
                value=row["isReleased"],
                key=f"isReleased_checkbox_{index}",
                field="isReleased",
            )
        with col3:
            checkbox_builder(
                label="DP",
                index=index,
                value=row["isPlatinum"],
                key=f"isPlatinum_checkbox_{index}",
                field="isPlatinum",
            )
        with col4:
            checkbox_builder(
                label="CF",
                index=index,
                value=row["isExplicit"],
                key=f"isExplicit_checkbox_{index}",
                field="isExplicit",
            )

        with st.columns([1])[0]:
            with st.expander("Permissions", expanded=True):
                multiselect_builder(
                    label="Tracks",
                    index=index,
                    value=row["tracks"],
                    key=f"tracks_multiselect_{index}",
                    field="tracks",
                )
    if st.button("Print All Data 2"):
        st.json(albums_data)


if __name__ == "__main__":
    main()
