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

    QUIZ_BANK_BY_LESSON.update({
        "Lesson 4: Guitar Angle": [
            {
                "question": "What guitar neck angle is recommended in this lesson?",
                "choices": ["Slightly upward", "Flat to the floor", "Pointing straight up", "Pointing down"],
                "answer": 0,
            },
            {
                "question": "Why does guitar angle matter?",
                "choices": ["It helps both hands move comfortably", "It changes string gauge", "It retunes the guitar", "It increases fret count"],
                "answer": 0,
            },
            {
                "question": "What should you avoid while setting angle?",
                "choices": ["Extreme tilt that bends the wrist", "Keeping the body stable", "Small adjustments", "Testing comfort"],
                "answer": 0,
            },
            {
                "question": "When should you re-check your guitar angle?",
                "choices": ["When you change chairs or position", "Only once a month", "Only during tuning", "Never during practice"],
                "answer": 0,
            },
            {
                "question": "What is the mini drill goal for this lesson?",
                "choices": ["Find the angle where notes feel cleanest", "Play as loudly as possible", "Use random neck positions", "Lock your wrist"],
                "answer": 0,
            },
        ],
        "Lesson 5: Shoulder Alignment": [
            {
                "question": "What shoulder position is the target?",
                "choices": ["Level and relaxed", "Raised to the ears", "Twisted hard", "Pinned back forcefully"],
                "answer": 0,
            },
            {
                "question": "Proper shoulder alignment mainly improves what?",
                "choices": ["Endurance and freedom of movement", "String brightness", "Amp volume", "Capo placement"],
                "answer": 0,
            },
            {
                "question": "What should you avoid to reach the neck?",
                "choices": ["Twisting your torso", "Small arm adjustments", "Relaxed breathing", "Neutral posture"],
                "answer": 0,
            },
            {
                "question": "What reset tip is given between exercises?",
                "choices": ["Inhale then drop shoulders on exhale", "Hold your breath", "Tighten shoulder muscles", "Lift both shoulders"],
                "answer": 0,
            },
            {
                "question": "Hidden shoulder tension most often causes what?",
                "choices": ["Faster fatigue", "Automatic tuning", "Cleaner intonation", "Lower action"],
                "answer": 0,
            },
        ],
        "Lesson 6: Neck Position": [
            {
                "question": "How should your neck and head be aligned?",
                "choices": ["Head centered over spine", "Chin dropped constantly", "Neck twisted left", "Head leaned far forward"],
                "answer": 0,
            },
            {
                "question": "What should move first when checking the fretboard?",
                "choices": ["Your eyes first", "Your shoulders first", "Your whole torso", "Your knees"],
                "answer": 0,
            },
            {
                "question": "If visibility is poor, what does the lesson suggest?",
                "choices": ["Raise the guitar slightly", "Drop your head more", "Twist your neck", "Ignore discomfort"],
                "answer": 0,
            },
            {
                "question": "How often are short posture breaks suggested?",
                "choices": ["About every 10 minutes", "Every hour", "Only after practice", "Never"],
                "answer": 0,
            },
            {
                "question": "What is a warning sign your neck angle is off?",
                "choices": ["Tightness after one song", "Strings sounding bright", "Pick wear", "Warm fingertips"],
                "answer": 0,
            },
        ],
        "Lesson 7: Wrist Alignment": [
            {
                "question": "What kind of wrist bend is preferred?",
                "choices": ["Small and natural bends", "Deep forced bends", "Locked straight wrists", "No movement at all"],
                "answer": 0,
            },
            {
                "question": "What should you avoid in the fretting wrist?",
                "choices": ["Collapsing inward", "Light flexibility", "Neutral shape", "Short breaks"],
                "answer": 0,
            },
            {
                "question": "What should you avoid in strumming motion?",
                "choices": ["Stiff straight-line motions", "Relaxed motion", "Consistent tempo", "Smooth transitions"],
                "answer": 0,
            },
            {
                "question": "If stiffness appears, what should you do?",
                "choices": ["Pause and shake out your hands", "Grip harder", "Play faster", "Ignore it"],
                "answer": 0,
            },
            {
                "question": "The practice idea in this lesson focuses on what?",
                "choices": ["Resetting whenever wrists harden", "Holding tension continuously", "Maximizing speed first", "Avoiding slow scales"],
                "answer": 0,
            },
        ],
        "Lesson 8: Common Posture Mistakes": [
            {
                "question": "Why is early posture error detection important?",
                "choices": ["It saves time and discomfort", "It changes tuning quickly", "It replaces warmups", "It increases gain"],
                "answer": 0,
            },
            {
                "question": "Which is listed as a frequent posture issue?",
                "choices": ["Rounded back and slouched shoulders", "Relaxed neutral spine", "Balanced feet", "Steady breathing"],
                "answer": 0,
            },
            {
                "question": "What breathing mistake is mentioned?",
                "choices": ["Holding breath in difficult sections", "Breathing calmly", "Breathing through your nose", "Exhaling between drills"],
                "answer": 0,
            },
            {
                "question": "What correction method is recommended?",
                "choices": ["Fix one mistake per session for 5 minutes", "Fix everything at once", "Ignore posture and play longer", "Only adjust weekly"],
                "answer": 0,
            },
            {
                "question": "Pressing the guitar too tightly usually causes what?",
                "choices": ["Unnecessary tension", "Perfect rhythm", "Lower fret buzz", "Automatic muting"],
                "answer": 0,
            },
        ],
        "Lesson 9: Preventing Back Pain": [
            {
                "question": "Back pain in practice is commonly caused by what?",
                "choices": ["Long sessions without movement", "Using a metronome", "Changing picks", "Slow practice"],
                "answer": 0,
            },
            {
                "question": "What chair type is recommended?",
                "choices": ["A firm chair with support", "A deep soft couch", "A bean bag", "A recliner"],
                "answer": 0,
            },
            {
                "question": "How should your weight and feet be managed?",
                "choices": ["Feet planted with balanced weight", "Weight shifted to one side", "Feet tucked under chair", "One foot lifted"],
                "answer": 0,
            },
            {
                "question": "How often should you stand and stretch?",
                "choices": ["Every 15 to 20 minutes", "Every 2 hours", "Only when pain starts", "Only after sessions"],
                "answer": 0,
            },
            {
                "question": "What end-of-session tip is given?",
                "choices": ["Do a gentle back stretch for one minute", "Do heavy lifting", "Skip cooldown", "Lock your back straight"],
                "answer": 0,
            },
        ],
        "Lesson 10: Daily Posture Practice": [
            {
                "question": "How does posture improve fastest in this lesson?",
                "choices": ["Short, consistent routines", "Rare long sessions", "Random practice lengths", "Only weekend practice"],
                "answer": 0,
            },
            {
                "question": "How long is the suggested daily routine?",
                "choices": ["About 10 minutes", "About 45 minutes", "About 1 minute", "About 2 hours"],
                "answer": 0,
            },
            {
                "question": "What is included in the routine?",
                "choices": ["Slow chord changes with relaxed shoulders", "Fast solos only", "Skipping setup checks", "No breaks"],
                "answer": 0,
            },
            {
                "question": "What should you do for 2 minutes in the routine?",
                "choices": ["Neck and wrist reset breaks", "Maximum speed drills", "Palm-muted power chords", "String changes"],
                "answer": 0,
            },
            {
                "question": "What is the end goal of this routine?",
                "choices": ["Finish feeling controlled and relaxed", "Finish exhausted and tense", "Play louder each day", "Use more force"],
                "answer": 0,
            },
        ],
        "Lesson 2: Fretting Hand Position": [
            {
                "question": "Where should the thumb be in this lesson?",
                "choices": ["Behind the neck", "Over every fret", "On the strings", "Under the neck"],
                "answer": 0,
            },
            {
                "question": "How should fingers approach the strings?",
                "choices": ["From above with curved joints", "Flat from the side", "With straight locked fingers", "With palm pressure"],
                "answer": 0,
            },
            {
                "question": "Where should fretting pressure be placed?",
                "choices": ["Close to the fret wire", "Middle of fret space only", "On top of the metal fret", "On the fingerboard edge"],
                "answer": 0,
            },
            {
                "question": "What should the palm avoid doing?",
                "choices": ["Collapsing into the neck", "Staying relaxed", "Remaining light", "Allowing finger reach"],
                "answer": 0,
            },
            {
                "question": "What does the drill in this lesson train?",
                "choices": ["Consistent clean tone per note", "Maximum hand force", "Fast random jumps", "Open-string muting only"],
                "answer": 0,
            },
        ],
        "Lesson 3: Finger Strength Training": [
            {
                "question": "Finger strength should come from what?",
                "choices": ["Control, not force", "Force only", "Shoulder tension", "Locked wrists"],
                "answer": 0,
            },
            {
                "question": "Which pattern is recommended for training?",
                "choices": ["Slow chromatic patterns", "Random fast strums", "Only open chords", "Palm-muted tremolo"],
                "answer": 0,
            },
            {
                "question": "What is a core pressure habit in this lesson?",
                "choices": ["Light squeeze then immediate relaxation", "Maximum squeeze at all times", "No pressure changes", "Grip until forearm burns"],
                "answer": 0,
            },
            {
                "question": "Where should unused fingers stay?",
                "choices": ["Close to the fretboard", "Fully extended away", "Curled into palm tightly", "Pressed on other strings"],
                "answer": 0,
            },
            {
                "question": "If your forearm burns quickly, what should you do?",
                "choices": ["Reduce pressure and tempo", "Increase pressure", "Ignore the burn", "Stop using a metronome"],
                "answer": 0,
            },
        ],
        "Lesson 4: String Muting Basics": [
            {
                "question": "What is the purpose of muting?",
                "choices": ["Control unwanted string noise", "Make notes louder", "Lower tuning", "Change scale length"],
                "answer": 0,
            },
            {
                "question": "Which hand can help with muting in this lesson?",
                "choices": ["Both hands", "Only fretting hand", "Only strumming hand", "Neither hand"],
                "answer": 0,
            },
            {
                "question": "What can the strumming hand do for low strings?",
                "choices": ["Use palm muting", "Press harder with pick", "Avoid contact completely", "Mute with thumb nail"],
                "answer": 0,
            },
            {
                "question": "After a note or chord, what muting habit is suggested?",
                "choices": ["Lift pressure slightly", "Increase pressure", "Hold full sustain always", "Move hand away"],
                "answer": 0,
            },
            {
                "question": "What does the exercise focus on?",
                "choices": ["Stopping sound right after each strum", "Long continuous ring", "Only speed changes", "Ignoring transitions"],
                "answer": 0,
            },
        ],
        "Lesson 5: Fretting Near the Fret": [
            {
                "question": "Where should your fingertip be placed for best clarity?",
                "choices": ["Just behind the fret wire", "Middle of the fret space", "On top of the fret wire", "Far from the fret"],
                "answer": 0,
            },
            {
                "question": "How much pressure should you use?",
                "choices": ["Minimum needed for clean sound", "Maximum force", "No pressure", "Variable pressure with noise"],
                "answer": 0,
            },
            {
                "question": "What should you avoid when placing the finger?",
                "choices": ["Directly pressing on the metal fret", "Being near the fret wire", "Listening for buzz", "Adjusting position"],
                "answer": 0,
            },
            {
                "question": "If the note buzzes, what should you do?",
                "choices": ["Reposition the finger", "Press harder forever", "Ignore it", "Mute all strings"],
                "answer": 0,
            },
            {
                "question": "What is the key feedback signal in this lesson?",
                "choices": ["Clean tone", "Loudest volume", "Fastest speed", "Strongest grip"],
                "answer": 0,
            },
        ],
        "Lesson 6: Thumb Position Behind Neck": [
            {
                "question": "Where should the thumb often sit for control?",
                "choices": ["Roughly opposite the middle finger", "Wrapped over the neck always", "On top of strings", "At neck heel only"],
                "answer": 0,
            },
            {
                "question": "How much counter-pressure is recommended?",
                "choices": ["Light counter-pressure when needed", "Constant heavy pressure", "No pressure ever", "Alternating maximum pressure"],
                "answer": 0,
            },
            {
                "question": "What thumb habit should beginners avoid?",
                "choices": ["Wrapping over neck for every exercise", "Moving with hand shifts", "Re-centering for stretches", "Keeping grip relaxed"],
                "answer": 0,
            },
            {
                "question": "How should thumb movement relate to hand shifts?",
                "choices": ["Move with the hand, do not lock it", "Lock it in one place", "Move independently and randomly", "Lift it off the neck entirely"],
                "answer": 0,
            },
            {
                "question": "If fingers cannot stretch, what should you check first?",
                "choices": ["Re-center your thumb", "Increase shoulder tension", "Lower tuning", "Switch picks"],
                "answer": 0,
            },
        ],
        "Lesson 7: Finger Independence Exercises": [
            {
                "question": "What is the goal of finger independence work?",
                "choices": ["Move one finger without disturbing others", "Use all fingers together always", "Increase hand tension", "Play louder chords"],
                "answer": 0,
            },
            {
                "question": "Which pattern is included in this lesson?",
                "choices": ["1-2-3-4 and 4-3-2-1", "Only 1-3-4", "Random skips only", "Open-string tremolo"],
                "answer": 0,
            },
            {
                "question": "Where should each finger stay between notes?",
                "choices": ["Close to the fretboard", "Lifted very high", "Pressed into palm", "Resting on pickguard"],
                "answer": 0,
            },
            {
                "question": "How should tempo progression be handled?",
                "choices": ["Start slow with metronome, increase only when clean", "Start fast immediately", "Ignore timing", "Increase speed despite mistakes"],
                "answer": 0,
            },
            {
                "question": "This lesson says independence grows from what?",
                "choices": ["Consistency", "Rushing", "Grip tension", "Long breaks"],
                "answer": 0,
            },
        ],
        "Lesson 8: Building Calluses": [
            {
                "question": "How should calluses be developed?",
                "choices": ["Gradually with safe daily practice", "As fast as possible with force", "By over-gripping", "By avoiding practice"],
                "answer": 0,
            },
            {
                "question": "What session style is recommended?",
                "choices": ["Shorter sessions practiced daily", "One very long weekly session", "Only monthly sessions", "Continuous no-break sessions"],
                "answer": 0,
            },
            {
                "question": "When should you stop during early callus building?",
                "choices": ["Before skin becomes overly irritated", "Only when string breaks", "Never stop", "After sharp pain starts"],
                "answer": 0,
            },
            {
                "question": "What fingertip care is suggested?",
                "choices": ["Keep fingertips clean and dry", "Keep fingers wet", "Use rough sandpaper", "Apply heavy oils before playing"],
                "answer": 0,
            },
            {
                "question": "Which discomfort is normal according to this lesson?",
                "choices": ["Mild tenderness", "Sharp pain", "Finger numbness", "Joint locking"],
                "answer": 0,
            },
        ],
        "Lesson 9: Stretching and Flexibility": [
            {
                "question": "Why does this lesson include stretching?",
                "choices": ["To reduce stiffness and prepare hands", "To replace technique practice", "To increase string tension", "To tune faster"],
                "answer": 0,
            },
            {
                "question": "Which movement is part of the routine?",
                "choices": ["Wrist circles both directions", "Neck locking", "Finger clenching for minutes", "Shoulder shrug holds"],
                "answer": 0,
            },
            {
                "question": "Which finger movement is suggested?",
                "choices": ["Light extension and flexion holds", "Forced hyperextension", "No finger movement", "Fast tapping only"],
                "answer": 0,
            },
            {
                "question": "What upper-body movement appears in the routine?",
                "choices": ["Shoulder rolls and neck release", "Chest presses", "Heavy shrugs", "Backbends"],
                "answer": 0,
            },
            {
                "question": "What is the key safety rule for stretching?",
                "choices": ["Never force through pain", "Stretch as hard as possible", "Ignore discomfort", "Only stretch after pain"],
                "answer": 0,
            },
        ],
        "Lesson 10: Advanced Hand Positioning": [
            {
                "question": "As pieces get harder, hand positioning should be what?",
                "choices": ["Adaptive, efficient, and relaxed", "Fixed and rigid", "Forceful and tense", "Random per measure"],
                "answer": 0,
            },
            {
                "question": "What should be minimized in advanced positioning?",
                "choices": ["Unnecessary motion", "Planning transitions", "Thumb-finger coordination", "Small loop practice"],
                "answer": 0,
            },
            {
                "question": "How should thumb and fingers move in this lesson?",
                "choices": ["As one coordinated unit", "In opposite random directions", "With thumb locked", "With fingers fully lifted"],
                "answer": 0,
            },
            {
                "question": "When should you prepare the next shape?",
                "choices": ["Early during transitions", "After missing the chord", "Only at the last moment", "Never in advance"],
                "answer": 0,
            },
            {
                "question": "How should difficult transitions be practiced?",
                "choices": ["In small loops before full playthroughs", "Only in full-speed songs", "With no repetition", "By skipping weak spots"],
                "answer": 0,
            },
        ],
        "Lesson 2: Basic Downstrokes": [
            {
                "question": "What matters more than speed in this lesson?",
                "choices": ["Consistency and timing", "Maximum force", "Random accents", "Arm size"],
                "answer": 0,
            },
            {
                "question": "Downstrokes should come primarily from what?",
                "choices": ["Relaxed wrist with light forearm support", "Locked elbow", "Finger-only flicks", "Shoulder swings"],
                "answer": 0,
            },
            {
                "question": "How should stroke depth be managed?",
                "choices": ["Controlled and even", "As deep as possible", "Different every stroke", "Ignored"],
                "answer": 0,
            },
            {
                "question": "What does the drill use for timing?",
                "choices": ["Quarter-note downstrokes with metronome", "No click at all", "Triplets at max tempo", "Only muted strums"],
                "answer": 0,
            },
            {
                "question": "What should happen after each stroke?",
                "choices": ["Smooth return to start position", "Sudden arm lock", "Pause for a full beat", "Reset grip each time"],
                "answer": 0,
            },
        ],
        "Lesson 3: Basic Upstrokes": [
            {
                "question": "Upstrokes are essential for what?",
                "choices": ["Balanced strumming patterns", "Lowering action", "Changing tuning", "Increasing fret size"],
                "answer": 0,
            },
            {
                "question": "How should upstrokes feel?",
                "choices": ["Light and controlled", "Aggressive and tense", "Heavy and slow", "Random"],
                "answer": 0,
            },
            {
                "question": "What force should be avoided in upstrokes?",
                "choices": ["Aggressive upward force", "Relaxed return motion", "Even timing", "Consistent angle"],
                "answer": 0,
            },
            {
                "question": "Upstroke timing should match what?",
                "choices": ["The downstrokes", "Only the beat 1 accent", "Random accents", "String changes only"],
                "answer": 0,
            },
            {
                "question": "What exercise is suggested?",
                "choices": ["Alternate one downstroke and one upstroke slowly", "Only upstrokes fast", "Only downstrokes", "Silent right-hand motion only"],
                "answer": 0,
            },
        ],
        "Lesson 4: Down-Up Strumming Pattern": [
            {
                "question": "What count pattern is taught?",
                "choices": ["1-and-2-and-3-and-4-and", "1-2-3 only", "Triplet swing only", "No counting"],
                "answer": 0,
            },
            {
                "question": "Where do downstrokes land in this lesson?",
                "choices": ["On the numbers", "On every and", "Only beat 4", "Randomly"],
                "answer": 0,
            },
            {
                "question": "Where do upstrokes land in this lesson?",
                "choices": ["On the ands", "On numbers only", "On rests only", "Not used"],
                "answer": 0,
            },
            {
                "question": "What hand-motion rule is emphasized?",
                "choices": ["Keep the hand moving continuously", "Stop between every stroke", "Lock wrist after each beat", "Use only elbow"],
                "answer": 0,
            },
            {
                "question": "What practice loop is recommended first?",
                "choices": ["One simple chord with timing locked in", "Fast chord changes immediately", "No metronome counting", "Complex syncopation first"],
                "answer": 0,
            },
        ],
        "Lesson 5: Wrist Rotation Technique": [
            {
                "question": "What does controlled wrist rotation improve?",
                "choices": ["Smooth and efficient strumming", "String lifespan", "Pickup output", "Neck relief"],
                "answer": 0,
            },
            {
                "question": "What usually reduces consistency?",
                "choices": ["Large arm swings", "Small circular motion", "Loose forearm", "Consistent contact"],
                "answer": 0,
            },
            {
                "question": "What kind of wrist motion is preferred?",
                "choices": ["Small circular motion", "Rigid linear motion", "No wrist movement", "Shoulder-only motion"],
                "answer": 0,
            },
            {
                "question": "How should pick contact be across strings?",
                "choices": ["Consistent", "Random and uneven", "As hard as possible", "Avoiding middle strings only"],
                "answer": 0,
            },
            {
                "question": "What outcome does this lesson target?",
                "choices": ["Better tone with less fatigue", "More tension for volume", "Longer arm travel", "Faster without control"],
                "answer": 0,
            },
        ],
        "Lesson 6: Maintaining Rhythm": [
            {
                "question": "What should be prioritized under pressure?",
                "choices": ["Steady pulse", "Perfect chord shape first", "Fast tempo", "Complex fills"],
                "answer": 0,
            },
            {
                "question": "What right-hand habit is emphasized?",
                "choices": ["Keep movement constant", "Pause during hard changes", "Stop on mistakes", "Only move on downbeats"],
                "answer": 0,
            },
            {
                "question": "What tool setting is recommended?",
                "choices": ["Metronome on slow settings", "No click ever", "Max tempo only", "Random BPM"],
                "answer": 0,
            },
            {
                "question": "What should you simplify if timing breaks down?",
                "choices": ["Chord changes", "Counting", "Hand motion", "Practice frequency"],
                "answer": 0,
            },
            {
                "question": "If timing collapses, what is the correct response?",
                "choices": ["Slow down and rebuild consistency", "Push faster", "Ignore the click", "Stop using rhythm drills"],
                "answer": 0,
            },
        ],
        "Lesson 7: String Muting Between Chords": [
            {
                "question": "Why is muting between chords important?",
                "choices": ["It keeps transitions clean", "It increases sustain always", "It lowers pitch", "It replaces fretting"],
                "answer": 0,
            },
            {
                "question": "What should fretting pressure do after a strum?",
                "choices": ["Release to stop unwanted ring", "Increase immediately", "Stay fully pressed", "Move to open strings"],
                "answer": 0,
            },
            {
                "question": "What can help shorten sustain?",
                "choices": ["Palm muting", "Bending strings", "Harder picking", "Raising action"],
                "answer": 0,
            },
            {
                "question": "Mute timing should be coordinated with what?",
                "choices": ["The beat", "Only visual cues", "Chord names", "String numbers"],
                "answer": 0,
            },
            {
                "question": "What is the core goal of this lesson?",
                "choices": ["Intentional, separated chord sound", "Continuous blurry ringing", "Faster muting only", "No dynamic contrast"],
                "answer": 0,
            },
        ],
        "Lesson 8: Different Strumming Patterns": [
            {
                "question": "Why learn different strumming patterns?",
                "choices": ["To expand rhythmic vocabulary", "To avoid metronome work", "To remove groove", "To reduce chord knowledge"],
                "answer": 0,
            },
            {
                "question": "Which option is one pattern type listed?",
                "choices": ["Straight eighth-note pattern", "Only quarter rests", "Single upstroke per bar", "Silence on every beat"],
                "answer": 0,
            },
            {
                "question": "What does syncopation add?",
                "choices": ["Rhythmic variation and feel", "Lower string tension", "Automatic speed", "Different tuning"],
                "answer": 0,
            },
            {
                "question": "What dynamics idea is mentioned?",
                "choices": ["Soft verse vs stronger chorus", "Same volume always", "Mute all choruses", "Only loud verses"],
                "answer": 0,
            },
            {
                "question": "How should you approach learning patterns?",
                "choices": ["Master one pattern at a time", "Mix all patterns immediately", "Skip groove practice", "Avoid repetition"],
                "answer": 0,
            },
        ],
        "Lesson 9: Playing with a Metronome": [
            {
                "question": "What does metronome practice primarily build?",
                "choices": ["Reliable time", "Faster tuning", "Stronger grip", "Higher string action"],
                "answer": 0,
            },
            {
                "question": "What tempo should you start with?",
                "choices": ["A comfortable tempo", "The fastest possible tempo", "A random tempo", "No tempo marking"],
                "answer": 0,
            },
            {
                "question": "What should you do while strumming to the click?",
                "choices": ["Count beats aloud", "Hold your breath", "Ignore beat numbers", "Only watch your fretting hand"],
                "answer": 0,
            },
            {
                "question": "How should tempo increases be made?",
                "choices": ["In small steps", "In large jumps", "Only after mistakes", "Every 5 seconds"],
                "answer": 0,
            },
            {
                "question": "When should you move up in tempo?",
                "choices": ["After 60 seconds of clean, steady playing", "After one clean measure", "Immediately after tuning", "Whenever it feels hard"],
                "answer": 0,
            },
        ],
        "Lesson 10: Building Speed and Accuracy": [
            {
                "question": "Speed in this lesson should come from what?",
                "choices": ["Efficient technique and stable timing", "Extra tension", "Harder picking only", "Skipping slow work"],
                "answer": 0,
            },
            {
                "question": "What is the first step in the method?",
                "choices": ["Clean slow repetitions", "Maximum tempo runs", "No metronome", "Heavy forearm tension"],
                "answer": 0,
            },
            {
                "question": "How should tempo increases be handled?",
                "choices": ["By small increments", "By doubling instantly", "By random changes", "Only after errors"],
                "answer": 0,
            },
            {
                "question": "What should you do when errors cluster?",
                "choices": ["Stop and reset", "Push through at same speed", "Ignore the errors", "Grip tighter"],
                "answer": 0,
            },
            {
                "question": "If tone quality drops, what is the rule?",
                "choices": ["Reduce tempo and rebuild precision", "Increase speed more", "Skip technique", "Switch strings immediately"],
                "answer": 0,
            },
        ],
    })

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

