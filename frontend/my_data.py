def fetch_artist_data():
    return {
        "name": "Global Beats",
        "albums": [
            {
                "name": "World Tour Vol. 1",
                "isReleased": True,
                "isPlatinum": True,
                "isExplicit": False,
                "tracks": ["Rhythm of the World", "Echoes of Eternity"],
            },
            {
                "name": "Festival Anthems",
                "isReleased": True,
                "isPlatinum": True,
                "isExplicit": True,
                "tracks": [
                    "Fire in the Sky",
                    "Electric Pulse",
                ],
            },
        ],
    }


def fetch_available_track_names():
    return [
        "Rhythm of the World",
        "Echoes of Eternity",
        "Fire in the Sky",
        "Electric Pulse",
        "track 1",
        "track 2",
        "track 3",
        "track 4",
        "track 5",
    ]
