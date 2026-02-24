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

    QUIZ_BANK_BY_LESSON = {
        "Lesson 1: Body Posture": [
            {
                "question": "For body posture, how should your back be while playing?",
                "choices": ["Straight but relaxed", "Rounded forward", "Twisted sideways", "Rigid and locked"],
                "answer": 0,
            },
            {
                "question": "Which shoulder position is recommended in this lesson?",
                "choices": ["Relaxed and natural", "Raised toward ears", "Pulled hard backward", "Tensed forward"],
                "answer": 0,
            },
            {
                "question": "What should you avoid according to body posture basics?",
                "choices": ["Hunching forward", "Neutral spine", "Balanced seating", "Relaxed upper body"],
                "answer": 0,
            },
            {
                "question": "Why is aligned posture important in this lesson?",
                "choices": ["It reduces strain and fatigue", "It makes strings brighter", "It changes tuning", "It increases guitar weight"],
                "answer": 0,
            },
            {
                "question": "What short daily habit is suggested for posture practice?",
                "choices": ["Sit with proper posture for a few minutes", "Practice only while standing", "Skip warm-up posture", "Keep shoulders tense"],
                "answer": 0,
            },
        ],
        "Lesson 2: Sitting Position": [
            {
                "question": "What kind of chair is best for this sitting-position lesson?",
                "choices": ["A sturdy chair without armrests", "A soft couch", "A stool with no support", "Any recliner"],
                "answer": 0,
            },
            {
                "question": "How should your feet be placed while seated?",
                "choices": ["Flat on the floor", "Crossed under chair", "One on toes only", "Hanging freely"],
                "answer": 0,
            },
            {
                "question": "What is the recommended thigh position?",
                "choices": ["Parallel to the ground", "Pointing sharply down", "Pointing sharply up", "Any angle works equally"],
                "answer": 0,
            },
            {
                "question": "Which habit should be avoided when seated?",
                "choices": ["Crossing your legs", "Relaxing shoulders", "Keeping chest open", "Sitting upright"],
                "answer": 0,
            },
            {
                "question": "What is a key goal of good sitting position?",
                "choices": ["Allow free arm movement with less tension", "Increase volume automatically", "Shorten guitar neck reach", "Eliminate need for rhythm practice"],
                "answer": 0,
            },
        ],
        "Lesson 3: Foot Placement": [
            {
                "question": "Why does this lesson emphasize foot placement?",
                "choices": ["It creates balance and stability", "It changes string gauge", "It tunes the guitar", "It improves pickups"],
                "answer": 0,
            },
            {
                "question": "How should both feet be positioned?",
                "choices": ["Flat on the floor", "Both on chair legs", "One lifted constantly", "Crossed at ankles"],
                "answer": 0,
            },
            {
                "question": "What spacing is recommended for feet?",
                "choices": ["About shoulder-width apart", "As close as possible", "Very wide split", "One in front of the other"],
                "answer": 0,
            },
            {
                "question": "What is suggested if feet do not reach the floor comfortably?",
                "choices": ["Use a footrest", "Raise your shoulders", "Lean forward", "Use only a guitar strap"],
                "answer": 0,
            },
            {
                "question": "Proper foot placement helps prevent which issue?",
                "choices": ["Discomfort during long practice", "Low battery in tuner", "Broken strings", "Wrong capo position"],
                "answer": 0,
            },
        ],
        "Lesson 1: Finger Curve Technique": [
            {
                "question": "In finger-curve technique, where should pressure be applied?",
                "choices": ["On fingertips", "On finger flats", "With palm", "With fingernails"],
                "answer": 0,
            },
            {
                "question": "What shape should your fingers mimic in this lesson?",
                "choices": ["Holding a small ball", "Completely straight", "Locked backward", "Pressed together flat"],
                "answer": 0,
            },
            {
                "question": "A good finger curve helps avoid what?",
                "choices": ["Muting nearby strings", "Using a metronome", "Changing pick angle", "Tuning pegs"],
                "answer": 0,
            },
            {
                "question": "What is the main result of proper finger curvature?",
                "choices": ["Cleaner notes and accuracy", "Louder guitar body", "Lower string tension", "Fewer frets to use"],
                "answer": 0,
            },
            {
                "question": "This lesson suggests repeating short hold-and-rest drills to build what?",
                "choices": ["Muscle memory", "Amplifier gain", "Song tempo changes", "Chord names"],
                "answer": 0,
            },
        ],
        "Lesson 1: Holding the Pick": [
            {
                "question": "How should the pick be held in this lesson?",
                "choices": ["Between thumb and index finger", "Between ring and pinky", "In a full fist", "Pressed to palm"],
                "answer": 0,
            },
            {
                "question": "What pick angle is recommended to the strings?",
                "choices": ["Around 45 degrees", "90 degrees", "Flat and parallel", "Any random angle"],
                "answer": 0,
            },
            {
                "question": "How should your grip feel?",
                "choices": ["Firm but not tense", "Extremely tight", "Very loose", "Locked wrist and forearm"],
                "answer": 0,
            },
            {
                "question": "What should be exposed past your fingers?",
                "choices": ["Only a small part of the pick", "Most of the pick", "None of the pick", "The thumb only"],
                "answer": 0,
            },
            {
                "question": "Why does this lesson emphasize relaxed wrist movement?",
                "choices": ["For better control and smoother strumming", "To tune faster", "To reduce fret count", "To change string color"],
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
    "Lesson 4: Guitar Angle": """Finding the Right Guitar Angle

The angle of your guitar changes how easily both hands can move. A good angle keeps your fretting wrist neutral and gives your strumming hand a comfortable path.

Guidelines:
• Tilt the neck slightly upward, not flat to the floor
• Keep the guitar body stable against your torso
• Avoid extreme tilt that bends your wrist
• Re-check your angle whenever you change chairs

Mini Drill: Play a simple four-note pattern while adjusting the neck angle. Keep the position where notes feel easiest and cleanest.""",
    "Lesson 5: Shoulder Alignment": """Shoulder Alignment for Relaxed Playing

Shoulders often carry hidden tension. Proper shoulder alignment improves endurance and helps both hands move freely.

What to Aim For:
• Both shoulders level and relaxed
• No lifting toward your ears
• No twisting your torso to reach the neck
• Light breathing while playing

Reset Tip: Between exercises, inhale deeply and drop your shoulders on the exhale to release tension.""",
    "Lesson 6: Neck Position": """Healthy Neck Position

Your neck should stay neutral while reading the fretboard. Constantly bending forward can cause stiffness and pain.

Best Practices:
• Keep your head centered over your spine
• Look with your eyes first, then slight head movement
• Raise the guitar slightly instead of dropping your head too far
• Take short posture breaks every 10 minutes

Quick Check: If your neck feels tight after one song, your viewing angle needs adjustment.""",
    "Lesson 7: Wrist Alignment": """Wrist Alignment Basics

Neutral wrists improve control and reduce strain. Both fretting and strumming wrists should feel flexible, not locked.

Focus Points:
• Keep wrist bends small and natural
• Avoid collapsing the fretting wrist inward
• Avoid stiff, straight-line strumming motions
• Pause and shake out hands if stiffness appears

Practice Idea: Play a slow scale and stop whenever your wrist hardens. Reset and continue.""",
    "Lesson 8: Common Posture Mistakes": """Common Posture Mistakes to Avoid

Many beginners progress slower because posture errors create unnecessary tension. Spotting mistakes early saves time and discomfort.

Frequent Issues:
• Slouching shoulders and rounded back
• Holding breath during difficult sections
• Leaning to one side for fret reach
• Pressing the guitar too tightly into the body

Correction Method: Pick one mistake per session and consciously fix it for 5 minutes.""",
    "Lesson 9: Preventing Back Pain": """Preventing Back Pain During Practice

Back pain usually comes from long sessions without movement. Smart breaks and setup habits protect your body.

Prevention Checklist:
• Sit on a firm chair with support
• Keep feet planted and weight balanced
• Stand and stretch every 15–20 minutes
• Alternate seated and standing practice when possible

Recovery Tip: End each session with a gentle back stretch for one minute.""",
    "Lesson 10: Daily Posture Practice": """Daily Posture Routine

Posture improves fastest with short, consistent routines. A repeatable daily system builds automatic technique.

10-Minute Routine:
1. 2 minutes seated setup check
2. 4 minutes slow chord changes with relaxed shoulders
3. 2 minutes neck and wrist reset breaks
4. 2 minutes reflection on tension points

Goal: Finish each day feeling controlled and relaxed, not fatigued.""",
    "Lesson 2: Fretting Hand Position": """Correct Fretting Hand Position

Hand position determines note clarity and speed. Good placement reduces buzzing and accidental string muting.

Core Rules:
• Thumb rests behind the neck for support
• Fingers approach from above with curved joints
• Press close to the fret wire, not in the middle
• Keep palm from collapsing into the neck

Drill: Fret each note on one string and listen for consistent clean tone.""",
    "Lesson 3: Finger Strength Training": """Finger Strength Training

Strength should come from control, not force. Focus on precise pressure and relaxed movement.

Training Ideas:
• Slow chromatic patterns across four frets
• Hold-and-release exercises per finger
• Light squeeze, then immediate relaxation
• Keep unused fingers close to the fretboard

Reminder: If your forearm burns quickly, reduce pressure and tempo.""",
    "Lesson 4: String Muting Basics": """String Muting Fundamentals

Muting helps keep your playing clean by controlling unwanted string noise. Both hands can contribute to muting.

Techniques:
• Fretting hand lightly touches adjacent strings
• Strumming hand palm controls low-string ring
• Lift pressure slightly after each note/chord
• Practice muting transitions between shapes

Exercise: Play short chord stabs and stop sound immediately after each strum.""",
    "Lesson 5: Fretting Near the Fret": """Fretting Near the Fret Wire

Placing your finger near the fret wire gives cleaner notes with less effort than pressing in the middle of the fret space.

How to Do It:
• Place fingertip just behind the fret wire
• Use minimum pressure needed for clean sound
• Avoid placing directly on top of the metal fret
• Reposition if note buzzes

Goal: Make clean tone your feedback for good placement, not stronger force.""",
    "Lesson 6: Thumb Position Behind Neck": """Thumb Position Behind the Neck

Thumb placement supports reach, balance, and finger independence. A centered thumb often gives the best control for beginners.

Guidelines:
• Keep thumb roughly opposite middle finger
• Apply light counter-pressure only when needed
• Avoid wrapping thumb over neck for every exercise
• Move thumb with hand shifts rather than locking it

Check: If fingers cannot stretch, re-center your thumb first.""",
    "Lesson 7: Finger Independence Exercises": """Building Finger Independence

Independent finger movement improves speed and accuracy. The goal is moving one finger without disturbing the others.

Exercise Pattern:
• Play 1-2-3-4 then 4-3-2-1 across strings
• Keep each finger close to the fretboard
• Use metronome at slow tempo first
• Increase speed only when clean

Tip: Independence grows from consistency, not from rushing.""",
    "Lesson 8: Building Calluses": """Building Healthy Calluses

Calluses make fretting more comfortable over time, but they should develop gradually with safe practice habits.

Safe Approach:
• Practice in shorter sessions daily
• Stop before skin becomes overly irritated
• Keep fingertips clean and dry
• Avoid over-gripping to speed up callus growth

Expectation: Mild tenderness is normal early on, sharp pain is not.""",
    "Lesson 9: Stretching and Flexibility": """Stretching and Flexibility for Guitarists

Gentle stretching prepares your hands for practice and reduces stiffness afterward.

Simple Routine:
• Wrist circles in both directions
• Finger extension and light flexion holds
• Thumb stretch across palm
• Shoulder rolls and neck release

Rule: Stretch lightly; never force through pain.""",
    "Lesson 10: Advanced Hand Positioning": """Advanced Hand Positioning Concepts

As pieces become harder, hand position must adapt quickly while staying efficient and relaxed.

Advanced Focus:
• Shift hand position without lifting too far
• Keep thumb and fingers moving as one unit
• Prepare next shape early during transitions
• Minimize unnecessary motion

Practice Strategy: Work difficult transitions in small loops before full-song playthroughs.""",
    "Lesson 2: Basic Downstrokes": """Basic Downstrokes

Downstrokes are the foundation of rhythm guitar. Consistent motion and timing matter more than speed.

Technique:
• Move from relaxed wrist and small forearm support
• Keep stroke depth controlled
• Strike target strings evenly
• Return to starting position smoothly

Drill: Play steady quarter-note downstrokes with a metronome for one minute.""",
    "Lesson 3: Basic Upstrokes": """Basic Upstrokes

Upstrokes balance your strumming and are essential for most patterns. Keep them light and controlled.

Key Points:
• Use a relaxed return motion through strings
• Avoid aggressive upward force
• Match timing with downstrokes
• Keep pick angle consistent

Exercise: Alternate one downstroke and one upstroke at slow tempo.""",
    "Lesson 4: Down-Up Strumming Pattern": """Down-Up Strumming Pattern

Combining down and up strokes creates flowing rhythm. This lesson focuses on even spacing and groove.

Pattern Basics:
• Count 1-and-2-and-3-and-4-and
• Downstrokes on numbers, upstrokes on and
• Keep hand moving continuously
• Accent beats without tensing

Practice Loop: Use one simple chord and lock in timing before chord changes.""",
    "Lesson 5: Wrist Rotation Technique": """Wrist Rotation Technique

Controlled wrist rotation produces smooth, efficient strumming. Large arm swings usually reduce consistency.

What to Practice:
• Small circular wrist motion
• Loose grip and relaxed forearm
• Consistent pick contact across strings
• Reduced vertical hand travel

Result: Better tone and endurance with less fatigue.""",
    "Lesson 6: Maintaining Rhythm": """Maintaining Rhythm Under Pressure

Good rhythm means keeping steady time even when chord changes feel difficult.

Rhythm Habits:
• Prioritize pulse over perfect chord shape
• Keep right-hand movement constant
• Use metronome on slow settings
• Simplify chord changes until timing is stable

Tip: If timing collapses, slow down and rebuild consistency first.""",
    "Lesson 7: String Muting Between Chords": """Muting Between Chords

Clean transitions require stopping unwanted string ring between chord changes.

Methods:
• Release fretting pressure right after strum
• Use palm muting to shorten sustain
• Coordinate mute timing with the beat
• Practice mute-change-strum cycles slowly

Goal: Chords sound intentional and separated, not blurry.""",
    "Lesson 8: Different Strumming Patterns": """Exploring Different Strumming Patterns

Different songs need different rhythmic feels. Learning pattern variations expands your musical vocabulary.

Try These:
• Straight eighth-note pattern
• Syncopated accents
• Omitted strokes for groove space
• Soft verse vs stronger chorus dynamics

Approach: Master one pattern at a time before combining styles.""",
    "Lesson 9: Playing with a Metronome": """Playing with a Metronome

A metronome develops reliable time and exposes rhythm drift quickly.

How to Use It:
• Start at a comfortable tempo
• Count beats aloud while strumming
• Stay with click through chord changes
• Increase tempo in small steps

Benchmark: Move up only when you can play cleanly for 60 seconds straight.""",
    "Lesson 10: Building Speed and Accuracy": """Building Speed with Accuracy

Speed should be the result of efficient technique and stable timing, not tension.

Progress Method:
• Begin with clean slow repetitions
• Increase tempo by small increments
• Stop and reset when errors cluster
• Keep shoulders, wrists, and grip relaxed

Rule of Thumb: If tone quality drops, reduce tempo and rebuild precision.""",
    }
