from chordsContent import ChordsContent
from databaseController import DatabaseController


class ChordsController:
    """Provides chord data for the chords GUI."""

    def __init__(self):
        self.db = DatabaseController()
        self.category_layout = ChordsContent.CATEGORY_LAYOUT
        self.chord_data = ChordsContent.CHORD_DATA
        self.fingerings = ChordsContent.FINGERINGS
        self.default_chord = ChordsContent.DEFAULT_CHORD
        self.chord_names = ChordsContent.CHORD_NAMES
        self.category_id = None
        self.mastered_chords = set()
        self._load_mastered_chords()

    def _load_mastered_chords(self):
        category = self.db.get_category_by_name("Chords")
        if not category:
            return

        self.category_id = category["category_id"]
        elements = self.db.get_elements_by_category(self.category_id)
        self.mastered_chords = {
            element["element_type"]
            for element in elements
            if element.get("completed")
        }

    def get_category_layout(self):
        return self.category_layout

    def get_default_chord(self):
        return self.default_chord

    def is_chord_mastered(self, chord_name):
        return chord_name in self.mastered_chords

    def set_chord_mastered(self, chord_name, mastered=True):
        if self.category_id is None:
            return

        completed_value = 1 if mastered else 0
        self.db.mark_element_completed(self.category_id, chord_name, completed=completed_value)
        if mastered:
            self.mastered_chords.add(chord_name)
        else:
            self.mastered_chords.discard(chord_name)

    def get_chord_details(self, chord_name):
        chord_data = self.chord_data.get(chord_name)
        if not chord_data:
            return None

        return {
            "name": chord_name,
            "label": chord_data["label"],
            "strings": chord_data["strings"],
            "fingers": self.fingerings.get(chord_name, [None] * 6),
            "fret_count": chord_data["fret_count"],
            "mastered": self.is_chord_mastered(chord_name),
        }

    def get_chord_info_text(self, chord_details):
        string_names = ["Low E", "A", "D", "G", "B", "High E"]
        string_values = chord_details["strings"]
        fingers = chord_details["fingers"]

        representation_lines = [
            f"{name} = {value}"
            for name, value in zip(string_names, string_values)
        ]

        finger_placements = []
        for name, fret, finger in zip(string_names, string_values, fingers):
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

    def close(self):
        if self.db:
            self.db.close()
