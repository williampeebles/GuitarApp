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

    def _get_completed_xp(self, category_name):
        """Return total XP from completed elements in a category."""
        category = self.db.get_category_by_name(category_name)
        if not category:
            return 0

        elements = self.db.get_elements_by_category(category["category_id"])
        return sum(
            int(element.get("experience_points") or 0)
            for element in elements
            if element.get("completed")
        )

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

        total_xp = (
            self._get_completed_xp("Fundamentals")
            + self._get_completed_xp("Maintenance")
            + self._get_completed_xp("Chords")
        )
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
        """Return prioritized section suggestions using fixed per-section quotas.

        Quotas:
        - Chords: 1 subsection (Beginner -> Intermediate -> Advanced priority)
        - Fundamentals: up to 3 subsections (lowest completion first)
        - Maintenance: up to 3 subsections (lowest completion first)
        """
        breakdown = self.get_progress_breakdown()
        quotas = {
            "Chords": 1,
            "Fundamentals": 3,
            "Maintenance": 3,
        }
        selected_suggestions = []
        chord_difficulty_order = {
            "Beginner Chords": 0,
            "Intermediate Chords": 1,
            "Advanced Chords": 2,
        }

        section_candidates = {
            "Chords": [],
            "Fundamentals": [],
            "Maintenance": [],
        }

        for section in breakdown:
            section_name = section.get("name", "Section")
            if section_name not in section_candidates:
                continue

            for subsection in section.get("subsections", []):
                subsection_name = subsection.get("name", "Subsection")
                subsection_percent = float(subsection.get("percent", 0.0))
                if subsection_percent >= 100.0:
                    continue

                difficulty_rank = 99
                if section_name == "Chords":
                    difficulty_rank = chord_difficulty_order.get(subsection_name, 99)

                section_candidates[section_name].append({
                    "name": f"{section_name} • {subsection_name}",
                    "percent": subsection_percent,
                    "difficulty_rank": difficulty_rank,
                })

        section_candidates["Chords"].sort(
            key=lambda item: (item["difficulty_rank"], item["percent"], item["name"])
        )
        section_candidates["Fundamentals"].sort(
            key=lambda item: (item["percent"], item["name"])
        )
        section_candidates["Maintenance"].sort(
            key=lambda item: (item["percent"], item["name"])
        )

        for section_name in ("Chords", "Fundamentals", "Maintenance"):
            take_count = quotas[section_name]
            selected_suggestions.extend(section_candidates[section_name][:take_count])

        return selected_suggestions[:limit]

    def close(self):
        if self.db:
            self.db.close()
