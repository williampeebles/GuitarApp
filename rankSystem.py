class RankSystem:
    """Pure rank/XP logic with no database or UI dependencies."""

    RANKS = [
        "Copper 3",
        "Copper 2",
        "Copper 1",
        "Bronze 3",
        "Bronze 2",
        "Bronze 1",
        "Silver 3",
        "Silver 2",
        "Silver 1",
        "Gold 3",
        "Gold 2",
        "Gold 1",
        "Platinum 3",
        "Platinum 2",
        "Platinum 1",
        "Emerald 3",
        "Emerald 2",
        "Emerald 1",
        "Diamond 3",
        "Diamond 2",
        "Diamond 1",
        "Virtuoso",
    ]

    LESSON_XP = 100
    CHORD_XP = 50
    XP_PER_RANK = 250

    @classmethod
    def get_total_xp(cls, completed_lessons, mastered_chords):
        return (completed_lessons * cls.LESSON_XP) + (mastered_chords * cls.CHORD_XP)

    @classmethod
    def get_rank_progress_from_xp(cls, total_xp):
        max_rank_index = len(cls.RANKS) - 1
        rank_index = min(total_xp // cls.XP_PER_RANK, max_rank_index)
        current_rank = cls.RANKS[rank_index]

        if rank_index >= max_rank_index:
            progress_percent = 100
            next_rank = cls.RANKS[max_rank_index]
            xp_to_next = 0
        else:
            xp_in_rank = total_xp % cls.XP_PER_RANK
            progress_percent = int((xp_in_rank / cls.XP_PER_RANK) * 100)
            next_rank = cls.RANKS[rank_index + 1]
            xp_to_next = cls.XP_PER_RANK - xp_in_rank

        return {
            "current_rank": current_rank,
            "next_rank": next_rank,
            "progress_percent": progress_percent,
            "total_xp": total_xp,
            "xp_to_next": xp_to_next,
        }
