class ChordsContent:
    CATEGORY_LAYOUT = [
        {
            "title": "Beginner Chords",
            "groups": [
                {
                    "label": "Open chords",
                    "items": [
                        "C Major", "G Major", "D Major", "A Major", "E Major", "A Minor", "E Minor", "D Minor"
                    ],
                    "item_type": "chord",
                },
                {
                    "label": "Simple 2–3 chord progressions",
                    "items": ["C - G - Am", "G - D - Em", "D - A - Bm"],
                    "item_type": "text",
                },
            ],
        },
        {
            "title": "Intermediate Chords",
            "groups": [
                {"label": "Barre chords", "items": ["F Major", "B Minor"], "item_type": "chord"},
                {"label": "Power chords", "items": ["E5", "A5", "D5"], "item_type": "chord"},
                {"label": "7th chords", "items": ["A7", "E7", "D7", "G7"], "item_type": "chord"},
            ],
        },
        {
            "title": "Advanced Chords",
            "groups": [
                {"label": "Major 7", "items": ["Cmaj7", "Gmaj7"], "item_type": "chord"},
                {"label": "Minor 7", "items": ["Am7", "Dm7", "Em7"], "item_type": "chord"},
                {"label": "Suspended", "items": ["Dsus2", "Dsus4", "Asus2"], "item_type": "chord"},
                {"label": "Diminished", "items": ["Bdim"], "item_type": "chord"},
                {"label": "Augmented", "items": ["Caug"], "item_type": "chord"},
                {
                    "label": "Extended chords (9ths, 11ths, 13ths)",
                    "items": ["C9", "D11", "G13"],
                    "item_type": "chord",
                },
            ],
        },
    ]

    CHORD_DATA = {
        "C Major": {"label": "Beginner - Open Chord", "strings": ["X", 3, 2, 0, 1, 0], "fret_count": 5},
        "G Major": {"label": "Beginner - Open Chord", "strings": [3, 2, 0, 0, 0, 3], "fret_count": 5},
        "D Major": {"label": "Beginner - Open Chord", "strings": ["X", "X", 0, 1, 3, 2], "fret_count": 5},
        "A Major": {"label": "Beginner - Open Chord", "strings": ["X", 0, 2, 2, 2, 0], "fret_count": 5},
        "E Major": {"label": "Beginner - Open Chord", "strings": [0, 2, 2, 1, 0, 0], "fret_count": 5},
        "A Minor": {"label": "Beginner - Open Chord", "strings": ["X", 0, 2, 2, 1, 0], "fret_count": 5},
        "E Minor": {"label": "Beginner - Open Chord", "strings": [0, 2, 2, 0, 0, 0], "fret_count": 5},
        "D Minor": {"label": "Beginner - Open Chord", "strings": ["X", "X", 0, 2, 3, 1], "fret_count": 5},
        "F Major": {"label": "Intermediate - Barre Chord", "strings": [1, 3, 3, 2, 1, 1], "fret_count": 5},
        "B Minor": {"label": "Intermediate - Barre Chord", "strings": ["X", 2, 4, 4, 3, 2], "fret_count": 5},
        "E5": {"label": "Intermediate - Power Chord", "strings": [0, 2, 2, "X", "X", "X"], "fret_count": 5},
        "A5": {"label": "Intermediate - Power Chord", "strings": ["X", 0, 2, 2, "X", "X"], "fret_count": 5},
        "D5": {"label": "Intermediate - Power Chord", "strings": ["X", "X", 0, 2, 3, "X"], "fret_count": 5},
        "A7": {"label": "Intermediate - 7th Chord", "strings": ["X", 0, 2, 0, 2, 0], "fret_count": 5},
        "E7": {"label": "Intermediate - 7th Chord", "strings": [0, 2, 0, 1, 0, 0], "fret_count": 5},
        "D7": {"label": "Intermediate - 7th Chord", "strings": ["X", "X", 0, 2, 1, 2], "fret_count": 5},
        "G7": {"label": "Intermediate - 7th Chord", "strings": [3, 2, 0, 0, 0, 1], "fret_count": 5},
        "Cmaj7": {"label": "Advanced - Major 7", "strings": ["X", 3, 2, 0, 0, 0], "fret_count": 5},
        "Gmaj7": {"label": "Advanced - Major 7", "strings": [3, 2, 0, 0, 0, 2], "fret_count": 5},
        "Am7": {"label": "Advanced - Minor 7", "strings": ["X", 0, 2, 0, 1, 0], "fret_count": 5},
        "Dm7": {"label": "Advanced - Minor 7", "strings": ["X", "X", 0, 2, 1, 1], "fret_count": 5},
        "Em7": {"label": "Advanced - Minor 7", "strings": [0, 2, 2, 0, 3, 0], "fret_count": 5},
        "Dsus2": {"label": "Advanced - Suspended", "strings": ["X", "X", 0, 2, 3, 0], "fret_count": 5},
        "Dsus4": {"label": "Advanced - Suspended", "strings": ["X", "X", 0, 2, 3, 3], "fret_count": 5},
        "Asus2": {"label": "Advanced - Suspended", "strings": ["X", 0, 2, 2, 0, 0], "fret_count": 5},
        "Bdim": {"label": "Advanced - Diminished", "strings": ["X", 2, 3, 1, 3, "X"], "fret_count": 5},
        "Caug": {"label": "Advanced - Augmented", "strings": ["X", 3, 2, 1, 1, "X"], "fret_count": 5},
        "C9": {"label": "Advanced - Extended Chord", "strings": ["X", 3, 2, 3, 3, "X"], "fret_count": 5},
        "D11": {"label": "Advanced - Extended Chord", "strings": ["X", 5, 5, 5, 5, "X"], "fret_count": 5},
        "G13": {"label": "Advanced - Extended Chord", "strings": [3, "X", 3, 4, 5, 5], "fret_count": 5},
    }

    FINGERINGS = {
        "C Major": [None, 3, 2, None, 1, None],
        "G Major": [2, 1, None, None, None, 3],
        "D Major": [None, None, None, 1, 3, 2],
        "A Major": [None, None, 1, 2, 3, None],
        "E Major": [None, 2, 3, 1, None, None],
        "A Minor": [None, None, 2, 3, 1, None],
        "E Minor": [None, 2, 3, None, None, None],
        "D Minor": [None, None, None, 2, 3, 1],
        "F Major": [1, 3, 4, 2, 1, 1],
        "B Minor": [None, 1, 3, 4, 2, 1],
        "E5": [None, 1, 3, None, None, None],
        "A5": [None, None, 1, 3, None, None],
        "D5": [None, None, None, 1, 3, None],
        "A7": [None, None, 2, None, 3, None],
        "E7": [None, 2, None, 1, None, None],
        "D7": [None, None, None, 2, 1, 3],
        "G7": [2, 1, None, None, None, 3],
        "Cmaj7": [None, 3, 2, None, None, None],
        "Gmaj7": [2, 1, None, None, None, 3],
        "Am7": [None, None, 2, None, 1, None],
        "Dm7": [None, None, None, 2, 1, 1],
        "Em7": [None, 2, 3, None, 4, None],
        "Dsus2": [None, None, None, 1, 2, None],
        "Dsus4": [None, None, None, 1, 2, 3],
        "Asus2": [None, None, 2, 3, None, None],
        "Bdim": [None, 2, 3, 1, 4, None],
        "Caug": [None, 3, 2, 1, 1, None],
        "C9": [None, 2, 1, 3, 4, None],
        "D11": [None, 1, 1, 1, 1, None],
        "G13": [1, None, 2, 3, 4, 4],
    }

    DEFAULT_CHORD = "C Major"

    CHORD_NAMES = (
        "C Major", "G Major", "D Major", "A Major", "E Major", "A Minor", "E Minor", "D Minor",
        "F Major", "B Minor", "E5", "A5", "D5", "A7", "E7", "D7", "G7",
        "Cmaj7", "Gmaj7", "Am7", "Dm7", "Em7", "Dsus2", "Dsus4", "Asus2",
        "Bdim", "Caug", "C9", "D11", "G13",
    )
