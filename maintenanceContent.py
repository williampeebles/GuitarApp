class MaintenanceContent:
    MAINTENANCE_LESSONS = (
        "Lesson 1: Daily Cleaning Basics",
        "Lesson 2: Safe Storage and Humidity",
        "Lesson 3: Fingerboard Conditioning",
        "Lesson 4: Hardware Check Routine",
        "Lesson 1: Wiping Strings After Practice",
        "Lesson 2: Knowing When to Change Strings",
        "Lesson 3: Proper String Changing Steps",
        "Lesson 4: Extending String Life",
        "Lesson 1: Standard Tuning Process",
        "Lesson 2: Intonation Basics",
        "Lesson 3: Action Height and Comfort",
        "Lesson 4: Quick Pre-Practice Setup Check",
    )

    LESSON_ITEMS_BY_TOPIC = {
        "Guitar Care": [
            "Lesson 1: Daily Cleaning Basics",
            "Lesson 2: Safe Storage and Humidity",
            "Lesson 3: Fingerboard Conditioning",
            "Lesson 4: Hardware Check Routine",
        ],
        "String Care": [
            "Lesson 1: Wiping Strings After Practice",
            "Lesson 2: Knowing When to Change Strings",
            "Lesson 3: Proper String Changing Steps",
            "Lesson 4: Extending String Life",
        ],
        "Tuning & Setup": [
            "Lesson 1: Standard Tuning Process",
            "Lesson 2: Intonation Basics",
            "Lesson 3: Action Height and Comfort",
            "Lesson 4: Quick Pre-Practice Setup Check",
        ],
    }

    LESSON_CONTENT = {
        "Lesson 1: Daily Cleaning Basics": (
            "Wipe down your guitar after every session.\n\n"
            "Use a clean, dry microfiber cloth to remove sweat and dust from the body, neck, and strings. "
            "This simple routine helps protect the finish and keeps grime from building up over time.\n\n"
            "Tips:\n"
            "• Keep one microfiber cloth in your case so cleanup becomes automatic.\n"
            "• Wipe from bridge to headstock with light pressure.\n"
            "• Spend 30–60 seconds after each practice rather than doing deep cleanups rarely.\n\n"
            "What not to do:\n"
            "• Don’t use household cleaners, glass spray, or alcohol on the guitar finish.\n"
            "• Don’t use rough towels or paper products that can scratch.\n"
            "• Don’t leave sweat on strings/body overnight."
        ),
        "Lesson 2: Safe Storage and Humidity": (
            "Store your guitar in a stable environment.\n\n"
            "Avoid direct sunlight, heaters, and damp areas. Keep humidity around 45%–55% when possible. "
            "Using a case can help protect against rapid temperature and humidity changes.\n\n"
            "Tips:\n"
            "• Use a small room hygrometer to track humidity.\n"
            "• Keep your guitar away from vents, windows, and radiators.\n"
            "• If your climate is extreme, use case humidification/dehumidification packs.\n\n"
            "What not to do:\n"
            "• Don’t store your guitar in a car trunk for long periods.\n"
            "• Don’t place it right beside heaters or AC units.\n"
            "• Don’t ignore seasonal humidity changes."
        ),
        "Lesson 3: Fingerboard Conditioning": (
            "Condition the fingerboard occasionally.\n\n"
            "For unfinished fingerboards, apply a small amount of appropriate fretboard conditioner during string changes. "
            "Do not over-apply—light treatment a few times a year is usually enough.\n\n"
            "Tips:\n"
            "• Apply conditioner to a cloth first, then wipe onto the board.\n"
            "• Let it sit briefly, then buff off all excess.\n"
            "• Conditioning is best done when strings are already off for replacement.\n\n"
            "What not to do:\n"
            "• Don’t soak the fingerboard with oil.\n"
            "• Don’t condition finished maple boards unless product guidance says it is safe.\n"
            "• Don’t leave residue around frets."
        ),
        "Lesson 4: Hardware Check Routine": (
            "Check hardware monthly.\n\n"
            "Inspect tuning pegs, strap buttons, bridge parts, and screws for looseness. "
            "Tighten gently as needed to avoid rattles and long-term wear.\n\n"
            "Tips:\n"
            "• Do a quick 2-minute check before longer practice sessions.\n"
            "• Use the right screwdriver size to avoid stripping screw heads.\n"
            "• Tighten just until snug—small adjustments are enough.\n\n"
            "What not to do:\n"
            "• Don’t overtighten screws or tuner nuts.\n"
            "• Don’t use power tools on small guitar hardware.\n"
            "• Don’t ignore strap button looseness (drop risk)."
        ),
        "Lesson 1: Wiping Strings After Practice": (
            "String wiping slows corrosion.\n\n"
            "After playing, run a soft cloth under and over each string to remove oils and moisture. "
            "This improves tone consistency and can increase string lifespan.\n\n"
            "Tips:\n"
            "• Pinch each string lightly with cloth and slide the length of the string.\n"
            "• Include the area near the bridge where sweat often accumulates.\n"
            "• Wash and dry hands before practice for even better string life.\n\n"
            "What not to do:\n"
            "• Don’t use abrasive pads or sharp tools on strings.\n"
            "• Don’t scrub aggressively near pickups.\n"
            "• Don’t leave strings damp after playing."
        ),
        "Lesson 2: Knowing When to Change Strings": (
            "Replace strings when tone and feel decline.\n\n"
            "Common signs include dull tone, tuning instability, rough feel, and visible discoloration. "
            "Frequent players may change every few weeks; occasional players can go longer.\n\n"
            "Tips:\n"
            "• Keep a simple log of string change dates.\n"
            "• Change before important performances or recordings.\n"
            "• Replace sooner if you notice intonation drift and frequent retuning.\n\n"
            "What not to do:\n"
            "• Don’t wait until a string snaps to replace all strings.\n"
            "• Don’t keep rusty strings because they still 'work'.\n"
            "• Don’t ignore rough string feel that causes finger discomfort."
        ),
        "Lesson 3: Proper String Changing Steps": (
            "Change strings with control and consistency.\n\n"
            "Replace one string at a time if you want to keep neck tension stable. "
            "Stretch new strings gently, retune several times, and trim excess string ends safely.\n\n"
            "Tips:\n"
            "• Leave enough wraps at the tuner for stable tuning (usually 2–3 wraps).\n"
            "• Wind neatly downward on tuning posts to improve break angle.\n"
            "• Tune up slowly to pitch and recheck after a few minutes.\n\n"
            "What not to do:\n"
            "• Don’t yank strings hard when stretching.\n"
            "• Don’t leave long untrimmed ends that can poke hands.\n"
            "• Don’t rush winding; crossed wraps can slip."
        ),
        "Lesson 4: Extending String Life": (
            "Build habits that preserve strings.\n\n"
            "Wash your hands before playing, keep your guitar clean, and store it in a case when not in use. "
            "These habits reduce oxidation and grime buildup.\n\n"
            "Tips:\n"
            "• Keep a cloth and spare strings in your gig bag at all times.\n"
            "• Use coated strings if your hands are naturally acidic.\n"
            "• Control humidity to reduce corrosion and fret wear.\n\n"
            "What not to do:\n"
            "• Don’t touch strings with dirty or greasy hands.\n"
            "• Don’t leave the guitar uncovered in dusty rooms.\n"
            "• Don’t ignore early rust spots."
        ),
        "Lesson 1: Standard Tuning Process": (
            "Tune from low E to high E with a reliable tuner.\n\n"
            "Tune up to pitch rather than down to pitch for better stability. "
            "Recheck all strings after one pass because string tension interacts across the neck.\n\n"
            "Tips:\n"
            "• Mute other strings while tuning for cleaner tuner readings.\n"
            "• Use consistent picking force when checking pitch.\n"
            "• Do two full passes across all strings for stability.\n\n"
            "What not to do:\n"
            "• Don’t crank tuning pegs quickly past target pitch.\n"
            "• Don’t tune by ear alone if your ear is still developing.\n"
            "• Don’t skip retuning after string changes."
        ),
        "Lesson 2: Intonation Basics": (
            "Intonation keeps notes in tune up the neck.\n\n"
            "Compare the 12th-fret harmonic and fretted note. If they differ, saddle position may need adjustment. "
            "Small changes matter, and retuning is required after each adjustment.\n\n"
            "Tips:\n"
            "• Use fresh strings before judging intonation accuracy.\n"
            "• Make tiny saddle adjustments and retune each time.\n"
            "• Check multiple frets after adjustment, not only the 12th fret.\n\n"
            "What not to do:\n"
            "• Don’t make large adjustment jumps.\n"
            "• Don’t evaluate intonation with old dead strings.\n"
            "• Don’t skip retuning between checks."
        ),
        "Lesson 3: Action Height and Comfort": (
            "Action affects playability and buzzing.\n\n"
            "Higher action can reduce fret buzz but feels stiffer. Lower action feels easier but may buzz if too low. "
            "Find a balanced setup based on your style.\n\n"
            "Tips:\n"
            "• Test action changes with your real playing dynamics.\n"
            "• Adjust in small increments and play for a day before changing again.\n"
            "• Balance comfort, tone, and clean fretting across the neck.\n\n"
            "What not to do:\n"
            "• Don’t chase ultra-low action if it causes constant buzz.\n"
            "• Don’t adjust truss rod aggressively without understanding the process.\n"
            "• Don’t compare setups directly across very different guitar types."
        ),
        "Lesson 4: Quick Pre-Practice Setup Check": (
            "Use a one-minute setup check before practice.\n\n"
            "Confirm tuning, inspect string condition, and look for obvious hardware issues. "
            "A quick check helps keep practice focused and avoids interruptions.\n\n"
            "Tips:\n"
            "• Follow the same checklist each session: tune, strings, hardware, posture.\n"
            "• Keep tuner, picks, and cloth in one consistent spot.\n"
            "• Address tiny issues immediately before they become bigger problems.\n\n"
            "What not to do:\n"
            "• Don’t skip checks when you are in a hurry.\n"
            "• Don’t start intense practice on an unstable setup.\n"
            "• Don’t ignore strange buzzes or sudden tuning drift."
        ),
    }

    QUIZ_BANK_BY_TOPIC = {
        "Guitar Care": [
            {
                "question": "What should you use for routine guitar wipe-downs?",
                "choices": ["A clean microfiber cloth", "Paper towels with water", "A rough brush", "Steel wool"],
                "answer": 0,
            },
            {
                "question": "What humidity range is generally safe for guitars?",
                "choices": ["45%–55%", "10%–20%", "70%–85%", "0%–10%"],
                "answer": 0,
            },
            {
                "question": "Where should you avoid storing your guitar?",
                "choices": ["Direct sunlight", "A stable room", "A hard case", "A guitar stand in mild conditions"],
                "answer": 0,
            },
            {
                "question": "How often should you check hardware for looseness?",
                "choices": ["About monthly", "Once every 5 years", "Never", "Only after string breaks"],
                "answer": 0,
            },
            {
                "question": "Fretboard conditioner should generally be applied:",
                "choices": ["Lightly and occasionally", "Daily in heavy amounts", "Only on strings", "Never under any condition"],
                "answer": 0,
            },
        ],
        "String Care": [
            {
                "question": "Why wipe strings after practice?",
                "choices": ["To remove oils and moisture", "To change tuning", "To increase scale length", "To lower action"],
                "answer": 0,
            },
            {
                "question": "A common sign strings need replacing is:",
                "choices": ["Dull tone and instability", "The guitar feels heavy", "Frets look shiny", "Pick feels loose"],
                "answer": 0,
            },
            {
                "question": "When changing strings, a stable approach is to:",
                "choices": ["Replace one string at a time", "Remove all and leave overnight", "Tune randomly first", "Skip stretching new strings"],
                "answer": 0,
            },
            {
                "question": "Which habit helps extend string life?",
                "choices": ["Washing hands before playing", "Leaving guitar in damp rooms", "Using dirty cloths", "Never storing in a case"],
                "answer": 0,
            },
            {
                "question": "New strings usually need:",
                "choices": ["Gentle stretching and retuning", "No tuning at all", "Immediate bridge adjustment", "Permanent detuning"],
                "answer": 0,
            },
        ],
        "Tuning & Setup": [
            {
                "question": "A good tuning habit is to tune:",
                "choices": ["Up to pitch", "Down past pitch only", "Without a tuner", "Only one string"],
                "answer": 0,
            },
            {
                "question": "Intonation checks often compare:",
                "choices": ["12th-fret harmonic vs fretted note", "Nut color vs bridge color", "String brand vs pick brand", "Open chord vs barre chord"],
                "answer": 0,
            },
            {
                "question": "Action height affects:",
                "choices": ["Playability and fret buzz", "Wood grain pattern", "Pickup wiring", "Case size"],
                "answer": 0,
            },
            {
                "question": "Before practice, a quick setup check should include:",
                "choices": ["Tuning and string condition", "Changing all strings", "Removing hardware", "Polishing frets every time"],
                "answer": 0,
            },
            {
                "question": "After making setup adjustments, you should usually:",
                "choices": ["Retune and recheck", "Ignore tuning", "Lower all strings at once", "Stop playing for a week"],
                "answer": 0,
            },
        ],
    }

    QUIZ_BANK_BY_LESSON = {}

    EXTRA_QUIZ_QUESTIONS = [
        {
            "question": "What is the best maintenance mindset for guitar care?",
            "choices": ["Consistent small habits", "Only react to problems", "Avoid all checks", "Use random adjustments"],
            "answer": 0,
        },
        {
            "question": "What does regular maintenance help prevent?",
            "choices": ["Performance and reliability issues", "Learning chord names", "Music theory mistakes", "Metronome usage"],
            "answer": 0,
        },
        {
            "question": "How should you approach hardware tightening?",
            "choices": ["Gently and carefully", "Forcefully", "With glue", "Never inspect hardware"],
            "answer": 0,
        },
        {
            "question": "What is a good reason to keep your guitar clean?",
            "choices": ["Longer component life", "Bigger frets", "Higher tuning pegs", "Automatic intonation"],
            "answer": 0,
        },
        {
            "question": "Routine checks are most effective when they are:",
            "choices": ["Short and consistent", "Rare and extreme", "Only yearly", "Skipped when busy"],
            "answer": 0,
        },
    ]
