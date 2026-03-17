from databaseController import DatabaseController
from rankSystem import RankSystem
from progressBreakdown import ProgressBreakdown


class DashboardController:
    """Computes rank and XP progress for the dashboard."""

    def __init__(self):
        self.db = DatabaseController()

    def _get_completed_count(self, category_name):
        category = self.db.get_category_by_name(category_name)
        if not category:
            return 0

        elements = self.db.get_elements_by_category(category["category_id"])
        return sum(1 for element in elements if element.get("completed"))

    def _get_completed_set(self, category_name):
        category = self.db.get_category_by_name(category_name)
        if not category:
            return set()

        elements = self.db.get_elements_by_category(category["category_id"])
        return {
            element["element_type"]
            for element in elements
            if element.get("completed")
        }

    def get_rank_progress(self):
        completed_fundamentals = self._get_completed_count("Fundamentals")
        completed_maintenance = self._get_completed_count("Maintenance")
        mastered_chords = self._get_completed_count("Chords")

        total_lessons = completed_fundamentals + completed_maintenance
        total_xp = RankSystem.get_total_xp(total_lessons, mastered_chords)
        rank_progress = RankSystem.get_rank_progress_from_xp(total_xp)

        return {
            **rank_progress,
            "completed_fundamentals": completed_fundamentals,
            "completed_maintenance": completed_maintenance,
            "mastered_chords": mastered_chords,
        }

    def get_progress_breakdown(self):
        fundamentals_completed = self._get_completed_set("Fundamentals")
        chords_completed = self._get_completed_set("Chords")
        maintenance_completed = self._get_completed_set("Maintenance")
        songs_category = self.db.get_category_by_name("Songs")
        songs_percent = songs_category.get("completion_percentage", 0.0) if songs_category else 0.0

        return ProgressBreakdown.build(
            fundamentals_completed=fundamentals_completed,
            chords_completed=chords_completed,
            maintenance_completed=maintenance_completed,
            songs_percent=songs_percent,
        )

    def get_suggested_sections(self, limit=8):
        """Return prioritized sections/subsections to work on, lowest completion first."""
        breakdown = self.get_progress_breakdown()
        suggestions = []
        chord_difficulty_order = {
            "Beginner Chords": 0,
            "Intermediate Chords": 1,
            "Advanced Chords": 2,
        }

        for section in breakdown:
            section_name = section.get("name", "Section")
            section_percent = float(section.get("percent", 0.0))

            for subsection in section.get("subsections", []):
                subsection_name = subsection.get("name", "Subsection")
                subsection_percent = float(subsection.get("percent", 0.0))
                if subsection_percent < 100.0:
                    difficulty_rank = 99
                    if section_name == "Chords":
                        difficulty_rank = chord_difficulty_order.get(subsection_name, 99)
                    suggestions.append({
                        "name": f"{section_name} • {subsection_name}",
                        "percent": subsection_percent,
                        "difficulty_rank": difficulty_rank,
                    })

            if not section.get("subsections") and section_percent < 100.0:
                suggestions.append({
                    "name": section_name,
                    "percent": section_percent,
                    "difficulty_rank": 99,
                })

        suggestions.sort(key=lambda item: (item["percent"], item["difficulty_rank"], item["name"]))
        return suggestions[:limit]

    def close(self):
        if self.db:
            self.db.close()
