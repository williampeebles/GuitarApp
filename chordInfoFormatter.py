class ChordInfoFormatter:
    """Formats chord detail dictionaries into display text for the UI."""

    STRING_NAMES = ["Low E", "A", "D", "G", "B", "High E"]

    @classmethod
    def build_info_text(cls, chord_details):
        string_values = chord_details["strings"]
        fingers = chord_details["fingers"]

        representation_lines = [
            f"{name} = {value}"
            for name, value in zip(cls.STRING_NAMES, string_values)
        ]

        finger_placements = []
        for name, fret, finger in zip(cls.STRING_NAMES, string_values, fingers):
            if isinstance(fret, int) and fret > 0 and finger in (1, 2, 3, 4):
                suffix = "th"
                if fret % 10 == 1 and fret % 100 != 11:
                    suffix = "st"
                elif fret % 10 == 2 and fret % 100 != 12:
                    suffix = "nd"
                elif fret % 10 == 3 and fret % 100 != 13:
                    suffix = "rd"
                finger_placements.append(f"{finger} on {name} string, {fret}{suffix} fret")

        if not finger_placements:
            finger_placements.append("No finger placement data")

        info_lines = [
            "String Representation:",
            *representation_lines,
            "",
            "Finger numbering:",
            "1 = Index",
            "2 = Middle",
            "3 = Ring",
            "4 = Pinky",
            "",
            "Finger placement:",
            *finger_placements,
            "",
            "O = Open string (play it)",
            "X = Do not play (mute)",
        ]
        return "\n".join(info_lines)
