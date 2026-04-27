from fundamentalsController import FundamentalsController
from maintenanceController import MaintenanceController
from chordsController import ChordsController


class ProgressBreakdown:
    """Builds section/subsection progress percentages from completed items."""

    @staticmethod
    def _percentage(completed, total):
        if total <= 0:
            return 0.0
        return round((completed * 100.0) / total, 1)

    @classmethod
    def build(cls, fundamentals_completed, chords_completed, maintenance_completed):
        breakdown = []
        fundamentals_lessons_by_topic = FundamentalsController.get_lesson_items_by_topic()
        maintenance_lessons_by_topic = MaintenanceController.get_lesson_items_by_topic()
        chord_layout = ChordsController.get_category_layout_data()
        chord_names = ChordsController.get_chord_names()

        fundamentals_total = sum(len(items) for items in fundamentals_lessons_by_topic.values())
        fundamentals_subsections = []
        for topic_name, lessons in fundamentals_lessons_by_topic.items():
            completed = sum(1 for lesson in lessons if lesson in fundamentals_completed)
            fundamentals_subsections.append({
                "name": topic_name,
                "percent": cls._percentage(completed, len(lessons)),
            })
        breakdown.append({
            "name": "Fundamentals",
            "percent": cls._percentage(len(fundamentals_completed), fundamentals_total),
            "subsections": fundamentals_subsections,
        })

        chords_subsections = []
        for section in chord_layout:
            section_chords = []
            for group in section.get("groups", []):
                if group.get("item_type") == "chord":
                    section_chords.extend(group.get("items", []))
            unique_chords = list(dict.fromkeys(section_chords))
            completed = sum(1 for chord in unique_chords if chord in chords_completed)
            chords_subsections.append({
                "name": section.get("title", "Section"),
                "percent": cls._percentage(completed, len(unique_chords)),
            })
        breakdown.append({
            "name": "Chords",
            "percent": cls._percentage(len(chords_completed), len(chord_names)),
            "subsections": chords_subsections,
        })

        maintenance_total = sum(len(items) for items in maintenance_lessons_by_topic.values())
        maintenance_subsections = []
        for topic_name, lessons in maintenance_lessons_by_topic.items():
            completed = sum(1 for lesson in lessons if lesson in maintenance_completed)
            maintenance_subsections.append({
                "name": topic_name,
                "percent": cls._percentage(completed, len(lessons)),
            })
        breakdown.append({
            "name": "Maintenance",
            "percent": cls._percentage(len(maintenance_completed), maintenance_total),
            "subsections": maintenance_subsections,
        })

        return breakdown
