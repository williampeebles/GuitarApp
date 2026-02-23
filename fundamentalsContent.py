class FundamentalsContent:
    FUNDAMENTALS_LESSONS = (
        "Lesson 1: Body Posture",
        "Lesson 2: Sitting Position",
        "Lesson 3: Foot Placement",
        "Lesson 4: Guitar Angle",
        "Lesson 5: Shoulder Alignment",
        "Lesson 6: Neck Position",
        "Lesson 7: Wrist Alignment",
        "Lesson 8: Common Posture Mistakes",
        "Lesson 9: Preventing Back Pain",
        "Lesson 10: Daily Posture Practice",
        "Lesson 1: Finger Curve Technique",
        "Lesson 2: Fretting Hand Position",
        "Lesson 3: Finger Strength Training",
        "Lesson 4: String Muting Basics",
        "Lesson 5: Fretting Near the Fret",
        "Lesson 6: Thumb Position Behind Neck",
        "Lesson 7: Finger Independence Exercises",
        "Lesson 8: Building Calluses",
        "Lesson 9: Stretching and Flexibility",
        "Lesson 10: Advanced Hand Positioning",
        "Lesson 1: Holding the Pick",
        "Lesson 2: Basic Downstrokes",
        "Lesson 3: Basic Upstrokes",
        "Lesson 4: Down-Up Strumming Pattern",
        "Lesson 5: Wrist Rotation Technique",
        "Lesson 6: Maintaining Rhythm",
        "Lesson 7: String Muting Between Chords",
        "Lesson 8: Different Strumming Patterns",
        "Lesson 9: Playing with a Metronome",
        "Lesson 10: Building Speed and Accuracy",
    )

    LESSON_ITEMS_BY_TOPIC = {
        "Posture": [
            "Lesson 1: Body Posture",
            "Lesson 2: Sitting Position",
            "Lesson 3: Foot Placement",
            "Lesson 4: Guitar Angle",
            "Lesson 5: Shoulder Alignment",
            "Lesson 6: Neck Position",
            "Lesson 7: Wrist Alignment",
            "Lesson 8: Common Posture Mistakes",
            "Lesson 9: Preventing Back Pain",
            "Lesson 10: Daily Posture Practice",
        ],
        "Hand Positioning": [
            "Lesson 1: Finger Curve Technique",
            "Lesson 2: Fretting Hand Position",
            "Lesson 3: Finger Strength Training",
            "Lesson 4: String Muting Basics",
            "Lesson 5: Fretting Near the Fret",
            "Lesson 6: Thumb Position Behind Neck",
            "Lesson 7: Finger Independence Exercises",
            "Lesson 8: Building Calluses",
            "Lesson 9: Stretching and Flexibility",
            "Lesson 10: Advanced Hand Positioning",
        ],
        "Strumming": [
            "Lesson 1: Holding the Pick",
            "Lesson 2: Basic Downstrokes",
            "Lesson 3: Basic Upstrokes",
            "Lesson 4: Down-Up Strumming Pattern",
            "Lesson 5: Wrist Rotation Technique",
            "Lesson 6: Maintaining Rhythm",
            "Lesson 7: String Muting Between Chords",
            "Lesson 8: Different Strumming Patterns",
            "Lesson 9: Playing with a Metronome",
            "Lesson 10: Building Speed and Accuracy",
        ],
    }

    QUIZ_BANK_BY_TOPIC = {
        "Posture": [
            {
                "question": "Which posture cue helps reduce strain while playing?",
                "choices": ["Back straight but relaxed", "Shoulders raised", "Lean forward", "Neck bent"],
                "answer": 0,
            },
            {
                "question": "What is the best sitting position for guitar practice?",
                "choices": ["Feet flat on the floor", "Legs crossed", "Slouched on a couch", "Chair with armrests"],
                "answer": 0,
            },
            {
                "question": "How should your shoulders feel while playing?",
                "choices": ["Relaxed", "Tense", "Raised", "Locked back"],
                "answer": 0,
            },
            {
                "question": "Why is proper foot placement important?",
                "choices": ["Provides balance and stability", "Looks stylish", "Makes the guitar louder", "Reduces string tension"],
                "answer": 0,
            },
            {
                "question": "If your feet do not reach the floor, what should you use?",
                "choices": ["A footrest", "A pillow behind your back", "A taller chair", "A guitar strap only"],
                "answer": 0,
            },
        ],
        "Hand Positioning": [
            {
                "question": "Where should the fingertips press the strings?",
                "choices": ["On the tips", "On the flats", "On the nails", "With the palm"],
                "answer": 0,
            },
            {
                "question": "What is the benefit of proper finger curve?",
                "choices": ["Cleaner notes and less muting", "Higher volume", "Faster string changes", "Longer guitar life"],
                "answer": 0,
            },
            {
                "question": "Which thumb position helps fretting accuracy?",
                "choices": ["Behind the neck", "Over the fretboard", "Under the neck", "Pressed on strings"],
                "answer": 0,
            },
            {
                "question": "What should you avoid when fretting a note?",
                "choices": ["Muting adjacent strings", "Curving fingers", "Light pressure", "Relaxed wrist"],
                "answer": 0,
            },
            {
                "question": "What helps build finger independence?",
                "choices": ["Targeted exercises", "Tight wrist", "Heavy grip", "Skipping warmups"],
                "answer": 0,
            },
        ],
        "Strumming": [
            {
                "question": "What angle should the pick be to the strings?",
                "choices": ["About 45 degrees", "Perpendicular", "Flat to the strings", "Any angle is fine"],
                "answer": 0,
            },
            {
                "question": "Which motion keeps strumming smooth?",
                "choices": ["Relaxed wrist rotation", "Stiff elbow motion", "Locked wrist", "Only finger movement"],
                "answer": 0,
            },
            {
                "question": "What is a basic strumming pattern?",
                "choices": ["Down-up", "Up-up-up", "Down-down-down only", "Random strokes"],
                "answer": 0,
            },
            {
                "question": "What tool helps you maintain rhythm?",
                "choices": ["Metronome", "Capo", "Slide", "Tuner"],
                "answer": 0,
            },
            {
                "question": "How should your pick grip feel?",
                "choices": ["Firm but not tense", "Very tight", "Very loose", "Pinched with nails"],
                "answer": 0,
            },
        ],
    }

    EXTRA_QUIZ_QUESTIONS = [
        {
            "question": "What should you do before playing to avoid tension?",
            "choices": ["Relax your shoulders", "Hold your breath", "Grip harder", "Hunch forward"],
            "answer": 0,
        },
        {
            "question": "What helps build good habits over time?",
            "choices": ["Consistent practice", "Ignoring posture", "Skipping warmups", "Rushing"],
            "answer": 0,
        },
    ]

    LESSON_CONTENT = {
        "Lesson 1: Body Posture": """Body Posture Fundamentals

Proper body posture is the foundation of comfortable and effective guitar playing. When you maintain good posture, you reduce strain on your back, neck, and shoulders, allowing you to play for longer periods without discomfort.

Key Points:
• Keep your back straight but not rigid
• Relax your shoulders and let them hang naturally
• Avoid hunching or leaning forward
• Make sure your spine is aligned vertically
• Sit on a chair with proper support

Benefits of Good Posture:
✓ Reduces fatigue during practice
✓ Prevents long-term back and neck problems
✓ Improves finger dexterity and speed
✓ Enhances your ability to reach all frets comfortably

Tip: Practice sitting with a straight back for 5 minutes daily before picking up your guitar. This helps build muscle memory.""",
    "Lesson 2: Sitting Position": """The Correct Sitting Position

Your sitting position affects your comfort and technique. A proper sitting position allows your arms to move freely and reduces unnecessary tension in your body.

Step-by-Step Guide:
1. Sit upright on a sturdy chair without armrests
2. Place both feet flat on the floor
3. The chair height should allow your thighs to be parallel to the ground
4. Keep your chest open and shoulders relaxed
5. Avoid crossing your legs

Common Mistakes:
✗ Slouching or rounding your back
✗ Sitting too low or too high
✗ Leaning to one side
✗ Tensing your shoulders

Exercise: Sit in the correct position for 10 minutes daily and notice how it feels natural over time.""",
    "Lesson 3: Foot Placement": """Proper Foot Placement

Your feet provide stability and allow you to shift your body position as needed. Proper foot placement ensures balance and comfort during extended practice sessions.

Correct Foot Position:
• Both feet should be flat on the floor
• Feet should be shoulder-width apart
• Knees should form approximately 90-degree angles
• Neither foot should be in mid-air or twisted
• You should feel stable and grounded

Why It Matters:
- Provides a solid foundation for your entire body
- Reduces strain on your back and hips
- Allows you to adjust your body position smoothly
- Prevents discomfort during long practice sessions

Tip: If your feet don't reach the floor comfortably, use a footrest to maintain proper leg positioning.""",
    "Lesson 1: Finger Curve Technique": """Finger Curve Technique Explained

Curving your fingers properly is essential for clean note production and efficient finger movement on the fretboard.

How to Curve Your Fingers:
1. Place your hand in front of you with fingers relaxed
2. Slowly curl your fingers as if holding a small ball
3. Your fingertips should touch the strings, not the flat of your fingers
4. Maintain this curve when fretting notes
5. Practice keeping the curve even when moving between strings

Benefits of Proper Finger Curving:
✓ Prevents accidentally muting adjacent strings
✓ Improves speed and accuracy
✓ Reduces finger fatigue
✓ Creates clearer, more articulate notes

Exercise: Hold the curved position for 30 seconds, rest, and repeat 5 times. Do this daily.""",
    "Lesson 1: Holding the Pick": """Essential Pick-Holding Technique

How you hold your pick dramatically affects your strumming accuracy, speed, and tone quality. A proper grip provides control and stability.

Correct Pick Hold Steps:
1. Hold the pick between your thumb and index finger
2. The pick should be at a 45-degree angle to the strings
3. Only a small portion of the pick should be exposed
4. Your grip should be firm but not tense
5. Keep your wrist relaxed and loose

Common Grip Mistakes:
✗ Gripping the pick too tightly (causes tension and fatigue)
✗ Exposing too much of the pick (reduces control)
✗ Holding the pick perpendicular to strings (creates scratching sound)
✗ Tensing your entire forearm and hand

Practice Tip: Hold the pick in position and practice moving your hand without the guitar for 1-2 minutes. This builds muscle memory.""",
    }
