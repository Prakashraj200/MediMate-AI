"""
Physiotherapy and Post-Accident Pain Management Knowledge Base
100+ Clinical Questions, Answers, and Categorized Recommendations for Preethi AI.
"""

PAIN_QNA_DATABASE = [
    # =========================================================================
    # CATEGORY 1: POST-ACCIDENT & POST-SURGERY RECOVERY (1 - 25)
    # =========================================================================
    {
        "id": 1,
        "category": "post_accident_recovery",
        "keywords": ["cast removed", "stiffness", "plaster off", "cannot bend", "joint tight"],
        "question": "Why is my joint so stiff and painful after my plaster cast was removed?",
        "answer": "After weeks of immobilization in a cast, muscles naturally atrophy and joint capsules tighten. This stiffness and mild aching are completely normal. Begin with gentle active-assisted range of motion (ROM) in warm water. Avoid sudden forceful bending.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 2,
        "category": "post_accident_recovery",
        "keywords": ["walk after surgery", "weight bearing", "crutches", "start walking"],
        "question": "When can I start putting weight on my leg after fracture surgery?",
        "answer": "Weight-bearing must strictly follow your orthopedic surgeon's timeline: typically Non-Weight Bearing (NWB) for 0-4 weeks, Partial Weight Bearing (PWB) with crutches at 4-8 weeks, and Full Weight Bearing (FWB) once callus formation is confirmed on X-ray.",
        "severity": "moderate",
        "red_flag": False
    },
    {
        "id": 3,
        "category": "post_accident_recovery",
        "keywords": ["whiplash", "neck pain", "car accident", "rear end", "neck stiffness"],
        "question": "I had a car accident and my neck hurts when turning. Is this whiplash?",
        "answer": "Yes, rapid acceleration-deceleration forces in vehicular collisions cause cervical strain (whiplash). Apply cold compresses for the first 48 hours, perform gentle chin tucks and isometric neck contractions. Avoid soft collars for extended periods as they weaken muscles.",
        "severity": "moderate",
        "red_flag": False
    },
    {
        "id": 4,
        "category": "post_accident_recovery",
        "keywords": ["scar pain", "surgical incision", "scar tight", "incision pulling"],
        "question": "My surgical incision scar feels tight and pulls when I move. How can I relieve it?",
        "answer": "Once the surgical wound is fully healed and sutures are removed, perform gentle scar tissue mobilization (cross-friction massage) with vitamin E oil or plain moisturizer for 5 minutes twice daily to break up collagen adhesions.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 5,
        "category": "post_accident_recovery",
        "keywords": ["knee click", "knee pop", "acl surgery", "meniscus surgery", "cracking sound"],
        "question": "My knee clicks or pops after ligament/meniscus surgery when doing rehab exercises. Is it torn again?",
        "answer": "Painless clicking (crepitus) is very common after knee surgery due to minor scar tissue, fluid shifts, or quadriceps muscle imbalance. As long as there is no acute swelling, sudden buckling, or sharp pain, it is benign.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 6,
        "category": "post_accident_recovery",
        "keywords": ["swollen ankle", "fracture swelling", "puffy foot", "ankle enlarged"],
        "question": "Why does my ankle still swell at the end of the day 2 months after an accident?",
        "answer": "Gravity causes dependent edema as venous return and lymphatic drainage take 3 to 6 months to fully normalize after bone fracture. Elevate your leg above heart level when resting, perform active ankle pumps, and consider a graduated compression sock.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 7,
        "category": "post_accident_recovery",
        "keywords": ["hardware pain", "implant", "plate and screws", "rod cold", "metal pain"],
        "question": "I can feel the metal plate/screws in my bone and it aches in cold weather. Is this normal?",
        "answer": "Yes, orthopedic implants conduct thermal changes faster than surrounding bone and soft tissue, causing a cold ache. Unless the skin over the implant becomes red, hot, or painful to touch (infection signs), implant aching is harmless.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 8,
        "category": "post_accident_recovery",
        "keywords": ["shoulder frozen", "cannot lift arm", "post accident shoulder", "shoulder stuck"],
        "question": "I immobilized my shoulder after a collarbone/arm fracture, and now I cannot raise my arm. What happened?",
        "answer": "You are developing secondary adhesive capsulitis (frozen shoulder) due to prolonged disuse. Immediate physiotherapy with Codman's pendulum exercises, passive forward elevation, and finger-wall ladder walks is vital to restore glenohumeral mobility.",
        "severity": "moderate",
        "red_flag": False
    },
    {
        "id": 9,
        "category": "post_accident_recovery",
        "keywords": ["back spasm", "lumbar spine", "bike accident", "lower back catch"],
        "question": "My lower back seized up after a bike fall. How can I manage the acute muscle spasm?",
        "answer": "Acute lumbar spasms protect the injured spine. Lie supine on a firm surface with pillows under your knees (90-90 resting position). Apply cold packs for 15 minutes, perform gentle pelvic tilts and knee-to-chest stretches. Avoid prolonged bed rest beyond 24-48 hours.",
        "severity": "moderate",
        "red_flag": False
    },
    {
        "id": 10,
        "category": "post_accident_recovery",
        "keywords": ["drive after accident", "driving car", "brake pedal", "driving clearance"],
        "question": "When is it safe to drive again after a right leg fracture or surgery?",
        "answer": "You should not drive until you have full emergency braking reaction time (usually 6 to 9 weeks post-op), are fully off all narcotic pain medications, and your physiotherapist verifies normal right leg quadriceps control.",
        "severity": "moderate",
        "red_flag": False
    },
    {
        "id": 11,
        "category": "post_accident_recovery",
        "keywords": ["muscle twitch", "muscle spasm", "fasciculation", "quivering"],
        "question": "My thigh muscle twitches continuously when doing physical therapy exercises. Is it damaged?",
        "answer": "Muscle fasciculations are benign signs of neuromuscular fatigue and re-innervation during recovery. Ensure adequate hydration and magnesium/potassium intake. Rest between exercise sets and avoid overtraining.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 12,
        "category": "post_accident_recovery",
        "keywords": ["rib fracture", "broken rib", "breathing hurts", "coughing hurts"],
        "question": "I fractured 2 ribs in a road crash. Breathing and coughing hurt terribly. How do I recover safely?",
        "answer": "Hold a soft pillow against your chest (splinting) when coughing. Practice hourly gentle diaphragmatic deep breathing or use an incentive spirometer to prevent atelectasis and pneumonia. Avoid binding the chest tightly as it restricts lung expansion.",
        "severity": "moderate",
        "red_flag": False
    },
    {
        "id": 13,
        "category": "post_accident_recovery",
        "keywords": ["sleeping position", "sleep with broken leg", "sleep post surgery", "how to sleep"],
        "question": "What is the best sleeping position while recovering from leg surgery or fracture?",
        "answer": "Sleep on your back with 2 pillows lengthwise supporting your injured leg in slight elevation. If side sleeping, lie on the uninjured side with a thick pillow between your knees to maintain pelvic alignment and avoid lateral rotation.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 14,
        "category": "post_accident_recovery",
        "keywords": ["weakness", "muscle loss", "skinny leg", "atrophy"],
        "question": "My injured leg is visibly thinner than my healthy leg. Will the muscle mass return?",
        "answer": "Yes, disuse atrophy can reduce quadriceps/calf circumference by 20-30% within 3 weeks. Progressive resistance exercises (isometric quad sets, straight leg raises, mini-squats) combined with 1.2g/kg protein daily will rebuild muscle bulk over 3 to 6 months.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 15,
        "category": "post_accident_recovery",
        "keywords": ["shower", "bath with cast", "waterproof cast", "wet incision"],
        "question": "When can I take a shower after orthopedic trauma surgery?",
        "answer": "Never submerge an unhealed incision in water. Showering is typically allowed 48-72 hours post-op if protected by a waterproof dressing, or once sutures/staples are removed and the skin is fully closed without drainage.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 16,
        "category": "post_accident_recovery",
        "keywords": ["wrist fracture", "colles fracture", "stiff fingers", "fist cannot close"],
        "question": "I had a wrist fracture and now my fingers are stiff and I cannot make a fist. What exercises help?",
        "answer": "Finger stiffness after wrist trauma is common. Perform composite fist exercises: hook fist, straight fist, and full fist. Do tendon gliding exercises and soak the hand in warm water for 5 minutes before active gripping exercises with a soft sponge.",
        "severity": "moderate",
        "red_flag": False
    },
    {
        "id": 17,
        "category": "post_accident_recovery",
        "keywords": ["limping", "antalgic gait", "cannot walk straight", "limp"],
        "question": "I limp when walking without crutches even though the bone has healed. How do I stop limping?",
        "answer": "A persistent limp (Trendelenburg gait) is caused by gluteus medius hip abductor weakness and subconscious pain guarding. Use one crutch or cane in the OPPOSITE hand, and do side-lying leg lifts and pelvic bridge exercises.",
        "severity": "moderate",
        "red_flag": False
    },
    {
        "id": 18,
        "category": "post_accident_recovery",
        "keywords": ["nerve tingling", "pins and needles", "foot numb", "hand numb"],
        "question": "I feel pins and needles in my toes after leg cast removal. Is my nerve damaged?",
        "answer": "Mild paresthesia can occur from localized pressure of swelling against peripheral nerves (peroneal nerve). If sensation is improving with movement, it is neuropraxia which resolves in 4-8 weeks. If foot drop or complete numbness occurs, notify your surgeon.",
        "severity": "moderate",
        "red_flag": False
    },
    {
        "id": 19,
        "category": "post_accident_recovery",
        "keywords": ["bone healing food", "diet for fracture", "supplements", "calcium"],
        "question": "What diet speeds up bone fracture healing and ligament repair?",
        "answer": "Eat high-quality protein (1.2-1.5g/kg), calcium-rich foods (milk, yogurt, ragi, sesame seeds, dark greens), vitamin D3 (1000-2000 IU daily), vitamin C (500mg for collagen synthesis), and zinc. Avoid smoking and alcohol as they delay osteoblast bone formation.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 20,
        "category": "post_accident_recovery",
        "keywords": ["sports return", "gym after accident", "running again", "sports clearance"],
        "question": "When can I return to jogging, gym, or cricket after an accident injury?",
        "answer": "Return to high-impact activities requires: 1) 100% full pain-free ROM, 2) Injured limb strength at least 85-90% of uninjured limb on dynamometer testing, and 3) Passing functional hop and agility tests certified by your physiotherapist.",
        "severity": "moderate",
        "red_flag": False
    },
    {
        "id": 21,
        "category": "post_accident_recovery",
        "keywords": ["morning stiffness", "stiff morning", "waking up stiff"],
        "question": "Why is my injured joint much stiffer and more painful in the morning?",
        "answer": "During sleep, synovial fluid thickens and lack of muscle pump causes micro-edema. Spend 5 minutes doing active gentle bed stretches before standing, and take a warm shower to increase joint lubrication.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 22,
        "category": "post_accident_recovery",
        "keywords": ["crutch height", "how to use crutches", "underarm crutches", "crutch pain"],
        "question": "My armpits hurt when using axillary crutches. Am I using them wrong?",
        "answer": "Yes! Never rest your body weight on your armpits, as this compresses the brachial plexus nerves causing crutch palsy. The top of the crutch should be 2 finger-widths below your armpit, and your hands must bear 100% of the weight through the hand grips.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 23,
        "category": "post_accident_recovery",
        "keywords": ["stairs with crutches", "climbing stairs", "stairs fracture"],
        "question": "How do I safely go up and down stairs using crutches or a cane?",
        "answer": "Remember the clinical rule: 'UP with the GOOD, DOWN with the BAD'. When going up: step up with your uninjured leg first, then bring crutches and injured leg up. When going down: put crutches down first, step down with injured leg, then uninjured leg.",
        "severity": "moderate",
        "red_flag": False
    },
    {
        "id": 24,
        "category": "post_accident_recovery",
        "keywords": ["bruise spreading", "skin black and blue", "hematoma", "skin color"],
        "question": "The dark bruise on my injured leg is moving downward toward my ankle and turning yellow. Is that dangerous?",
        "answer": "No, this is completely normal. Gravity causes pooled subcutaneous blood (ecchymosis) to migrate downward, and enzymatic breakdown of hemoglobin turns the color from purple to green and yellow as your body reabsorbs it.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 25,
        "category": "post_accident_recovery",
        "keywords": ["fear of movement", "afraid to walk", "kinesiophobia", "scared of re-injury"],
        "question": "I am terrified of putting weight on my leg because I fear re-breaking the bone. How do I overcome this?",
        "answer": "Fear of movement (kinesiophobia) is a well-known psychological response after trauma. Gradual graded exposure—starting with seated heel-slides, then parallel bar standing, then partial weight bearing in front of a mirror—retrains your brain's threat alarm system.",
        "severity": "mild",
        "red_flag": False
    },

    # =========================================================================
    # CATEGORY 2: ICE VS. HEAT THERAPY & SWELLING MANAGEMENT (26 - 45)
    # =========================================================================
    {
        "id": 26,
        "category": "ice_vs_heat",
        "keywords": ["ice or heat", "cold or hot", "when to use ice", "when to use heat"],
        "question": "Should I use ice or heat for pain after an accident or exercise?",
        "answer": "Use ICE for acute injuries (first 48-72 hours) and sudden flare-ups with swelling/warmth to constrict blood vessels and numb pain. Use MOIST HEAT for subacute/chronic muscle stiffness, tightness, and before stretching to increase blood flow.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 27,
        "category": "ice_vs_heat",
        "keywords": ["ice pack duration", "how long ice", "frostbite", "ice time"],
        "question": "How long should I leave an ice pack on my injured joint?",
        "answer": "Apply ice for 15 to 20 minutes per session, at least 2 hours apart. Never apply ice directly onto bare skin; always wrap it in a damp towel. Applying ice longer than 20 minutes causes reflex vasodilation (Hunting reaction) and risks tissue frostbite.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 28,
        "category": "ice_vs_heat",
        "keywords": ["heat pack burn", "heat on swollen knee", "hot water bag"],
        "question": "Can I put a hot water bag on a freshly swollen knee?",
        "answer": "NO! Never apply heat to an acutely inflamed, swollen, or warm joint. Heat causes vasodilation, increasing blood flow and worsening inflammation and internal edema. Stick strictly to cold compression.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 29,
        "category": "ice_vs_heat",
        "keywords": ["contrast bath", "hot and cold therapy", "alternate hot cold"],
        "question": "What is contrast bath therapy and how does it help persistent hand/foot swelling?",
        "answer": "Contrast therapy alternates hot and cold immersion (3 minutes in warm water 38°C followed by 1 minute in cold water 15°C for 4 cycles, ending on cold). This creates a 'vascular pump' that dramatically reduces stubborn edema in subacute recovery.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 30,
        "category": "ice_vs_heat",
        "keywords": ["rice protocol", "rest ice compression elevation", "rice method"],
        "question": "How do I correctly apply the R.I.C.E protocol after a joint sprain or contusion?",
        "answer": "R = Rest (avoid aggravating movements); I = Ice (15-20 mins with towel barrier); C = Compression (wrap elastic bandage from distal to proximal without cutting circulation); E = Elevation (keep injured limb supported above heart level).",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 31,
        "category": "ice_vs_heat",
        "keywords": ["tight bandage", "crepe bandage tight", "toes cold", "bandage blue"],
        "question": "How do I know if my compression bandage or crepe wrap is too tight?",
        "answer": "If your toes or fingers feel cold, tingle, turn pale or bluish, or if throbbing pain intensifies, the bandage is too tight and impairing venous circulation. Remove the wrap immediately, wait 10 minutes, and re-wrap with gentle, even tension.",
        "severity": "moderate",
        "red_flag": True
    },
    {
        "id": 32,
        "category": "ice_vs_heat",
        "keywords": ["ice before exercise", "heat before exercise", "warm up therapy"],
        "question": "Should I apply heat or ice before doing my physiotherapy exercise routine?",
        "answer": "Apply MOIST HEAT for 10-15 minutes BEFORE exercises to warm up collagen tissues, improve muscle elasticity, and reduce stiffness. Apply ICE for 15 minutes AFTER exercises to prevent post-workout inflammatory soreness.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 33,
        "category": "ice_vs_heat",
        "keywords": ["epsom salt", "magnesium bath", "salt soak"],
        "question": "Does soaking my injured foot/hand in warm Epsom salt water help pain?",
        "answer": "Yes, once surgical wounds are completely healed, soaking in warm water with Epsom salt (magnesium sulfate) for 15 minutes relaxes hypertonic muscles, reduces minor edema, and soothes joint stiffness.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 34,
        "category": "ice_vs_heat",
        "keywords": ["gel pack", "frozen peas", "diy ice pack"],
        "question": "What is the best household alternative if I do not have an ice gel pack?",
        "answer": "A bag of frozen peas or corn wrapped in a damp kitchen towel is ideal because it molds perfectly to the anatomical contours of knees, ankles, or shoulders. Alternatively, mix 1 part rubbing alcohol with 3 parts water in a Ziploc bag and freeze for a slushy gel pack.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 35,
        "category": "ice_vs_heat",
        "keywords": ["tens machine", "electrical stimulation", "tens unit pain"],
        "question": "How does a TENS unit work for post-accident musculoskeletal pain?",
        "answer": "Transcutaneous Electrical Nerve Stimulation (TENS) works on the Pain Gate Theory (Melzack & Wall): harmless tingling electrical pulses travel along fast A-beta fibers, closing the nerve gate in the spinal cord and stimulating natural endorphin release.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 36,
        "category": "ice_vs_heat",
        "keywords": ["tens placement", "where to put tens pads", "tens electrode"],
        "question": "Where should I place TENS electrodes for knee or lower back pain?",
        "answer": "Place pads on clean, dry skin surrounding the painful area (at least 2 inches apart), never directly over bony prominences. NEVER place pads over the front of the neck (carotid sinus), over the heart, over open wounds, or if you have a cardiac pacemaker.",
        "severity": "moderate",
        "red_flag": False
    },
    {
        "id": 37,
        "category": "ice_vs_heat",
        "keywords": ["elevation height", "how high elevate", "leg elevation pillows"],
        "question": "How high should I elevate my injured limb to reduce post-traumatic swelling?",
        "answer": "For elevation to be physiologically effective, the injured joint must be elevated ABOVE THE LEVEL OF YOUR HEART. Placing your foot on a low footstool while sitting upright in a chair does not aid venous return.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 38,
        "category": "ice_vs_heat",
        "keywords": ["topical spray", "volini", "moov", "pain relief spray", "menthol spray"],
        "question": "Can I use over-the-counter pain relief sprays/gels (Diclofenac/Menthol) on my injured muscle?",
        "answer": "Topical NSAID gels (such as Diclofenac) and counter-irritants (menthol) can provide targeted relief for superficial muscle strains with fewer systemic GI side effects than oral tablets. Never apply to broken skin, open wounds, or under tight heat wraps.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 39,
        "category": "ice_vs_heat",
        "keywords": ["hot tub", "sauna post fracture", "steam bath"],
        "question": "Can I sit in a hot tub, jacuzzi, or sauna while recovering from bone trauma?",
        "answer": "Avoid hot tubs and saunas until your orthopedic surgeon confirms complete bone union and surgical incision maturation. Excessive systemic heat causes peripheral vasodilation which can precipitate systemic hypotension or exacerbate localized joint effusion.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 40,
        "category": "ice_vs_heat",
        "keywords": ["ice burn", "skin red after ice", "cold allergy"],
        "question": "My skin turned bright red and itchy after applying an ice pack. Did I get an ice burn?",
        "answer": "Reactive hyperemia (temporary red skin) is normal, but if skin blisters, turns white/waxy, or remains numb 30 minutes after ice removal, it indicates superficial frostbite or cold urticaria. Discontinue ice and warm gently with room-temperature water.",
        "severity": "moderate",
        "red_flag": False
    },
    {
        "id": 41,
        "category": "ice_vs_heat",
        "keywords": ["kinesiology tape", "k tape for pain", "physio tape"],
        "question": "Does kinesiology taping (K-tape) help reduce swelling and muscle pain?",
        "answer": "Yes, properly applied K-tape microscopically lifts the epidermis, creating subtle decompressive space that facilitates lymphatic drainage and provides gentle proprioceptive feedback to stabilize fatigued muscles.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 42,
        "category": "ice_vs_heat",
        "keywords": ["heating pad in bed", "sleep with heating pad", "overnight heat"],
        "question": "Can I sleep with an electric heating pad turned on my painful back?",
        "answer": "NO! Never fall asleep with an electric heating pad. Sensory receptors become habituated, leading to severe second-degree thermal burns and erythema ab igne. Always use pads with an automatic 20-minute shutoff timer.",
        "severity": "moderate",
        "red_flag": False
    },
    {
        "id": 43,
        "category": "ice_vs_heat",
        "keywords": ["massage after accident", "deep tissue massage", "massage swelling"],
        "question": "Can I get a vigorous deep tissue massage immediately after an accident injury?",
        "answer": "No. Vigorous deep massage within the first 1-2 weeks can re-rupture healing capillary beds, increase internal hematoma, and risk myositis ossificans (calcification within muscle). Only gentle retrograde lymphatic effleurage is safe early on.",
        "severity": "moderate",
        "red_flag": False
    },
    {
        "id": 44,
        "category": "ice_vs_heat",
        "keywords": ["painkiller addiction", "paracetamol vs tramadol", "stop painkillers"],
        "question": "I am worried about becoming dependent on prescribed painkiller tablets. How do I taper off?",
        "answer": "Switch to a multimodal non-opioid strategy: combine scheduled Paracetamol with physical modalities (ice, TENS, gentle ROM). Taper narcotic painkillers (like Tramadol) by reducing dose every 2-3 days under your physician's guidance.",
        "severity": "moderate",
        "red_flag": False
    },
    {
        "id": 45,
        "category": "ice_vs_heat",
        "keywords": ["swelling won't go down", "persistent edema", "chronic swelling"],
        "question": "Why has the swelling in my knee not resolved even 6 weeks after my bike fall?",
        "answer": "Persistent joint effusion indicates active low-grade synovitis or occult internal derangement (such as a chondral flap or occult micro-fracture). You require a formal physiotherapist ultrasound or MRI re-evaluation.",
        "severity": "moderate",
        "red_flag": False
    },

    # =========================================================================
    # CATEGORY 3: SAFE PHYSIOTHERAPY EXERCISES & MOBILITY (46 - 70)
    # =========================================================================
    {
        "id": 46,
        "category": "rehab_exercises",
        "keywords": ["isometric", "isometric exercises", "quad sets", "static exercise"],
        "question": "What are isometric exercises and why do physiotherapists prescribe them first?",
        "answer": "Isometric exercises contract muscles without moving the joint (e.g., quad sets pressing your knee flat into the bed). They maintain muscle tone and stimulate blood circulation without placing mechanical stress on healing bones or ligaments.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 47,
        "category": "rehab_exercises",
        "keywords": ["good pain vs bad pain", "exercise hurts", "should it hurt", "pain threshold"],
        "question": "How do I distinguish between 'good rehab pain' and 'bad injury pain' during exercise?",
        "answer": "'Good rehab pain' is a mild muscular burn, stretch, or dull ache (VAS 1-3/10) that settles within 30 minutes post-exercise. 'Bad pain' is sharp, stabbing, pinching (VAS 5+/10), causes joint swelling within 2 hours, or causes limping the next morning.",
        "severity": "moderate",
        "red_flag": False
    },
    {
        "id": 48,
        "category": "rehab_exercises",
        "keywords": ["heel slides", "bend knee after surgery", "knee flexion exercise"],
        "question": "How do I perform heel slides safely to increase knee flexion after surgery?",
        "answer": "Lie on your back on a smooth surface wearing a sock. Slowly slide your heel toward your buttocks until you feel a firm, mild stretch (not sharp pain). Hold for 5 seconds, then slowly slide back. Perform 10-15 repetitions, 3 times daily.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 49,
        "category": "rehab_exercises",
        "keywords": ["straight leg raise", "slr exercise", "quad strengthening", "lift leg"],
        "question": "I cannot lift my leg straight up (quad lag) after knee surgery. How do I fix this?",
        "answer": "Quad lag is caused by arthrogenic muscle inhibition. First, tighten your thigh muscle firmly, lock the knee completely straight, and only then lift the leg 6-8 inches off the bed. If unable, start with active-assisted lifts using a towel loop.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 50,
        "category": "rehab_exercises",
        "keywords": ["ankle pumps", "blood clot prevention", "calf pump"],
        "question": "Why do doctors insist on doing ankle pumps 100 times a day after trauma?",
        "answer": "Ankle pumps activate the calf muscle venous pump (often called the 'peripheral heart'), increasing deep venous blood velocity by over 200%. This is the single most effective natural prevention against life-threatening Deep Vein Thrombosis (DVT).",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 51,
        "category": "rehab_exercises",
        "keywords": ["pendulum exercise", "codman pendulum", "shoulder swing"],
        "question": "How do I do Codman's pendulum exercises for a painful injured shoulder?",
        "answer": "Bend forward at your waist 90 degrees, supporting your healthy arm on a table. Let your injured arm dangle completely relaxed like a pendulum. Use your torso to gently sway the arm in small circles (clockwise, counterclockwise, forwards/backwards) without actively using shoulder muscles.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 52,
        "category": "rehab_exercises",
        "keywords": ["resistance band", "theraband", "elastic band exercises"],
        "question": "When is it safe to advance from bodyweight stretches to resistance bands (Therabands)?",
        "answer": "Transition to light resistance bands (Yellow or Red) only when you can complete 3 sets of 15 bodyweight repetitions with full active ROM and zero next-day inflammatory pain.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 53,
        "category": "rehab_exercises",
        "keywords": ["bridge exercise", "glute bridge", "pelvic bridge"],
        "question": "Why is the pelvic bridge exercise essential for post-accident lower body recovery?",
        "answer": "The glute bridge strengthens gluteus maximus and hamstrings without loading the spine or anterior knee joint. It restores lumbopelvic core stability necessary for walking without a pelvic tilt or limp.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 54,
        "category": "rehab_exercises",
        "keywords": ["chin tuck", "neck posture", "cervical retraction"],
        "question": "How do chin tuck exercises relieve whiplash neck pain and tension headaches?",
        "answer": "Chin tucks strengthen deep cervical flexor muscles (longus colli/capitis) and stretch tight suboccipital muscles. Sit upright, look straight ahead, and gently glide your chin backwards like making a double chin. Hold 5 seconds; repeat 10 times.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 55,
        "category": "rehab_exercises",
        "keywords": ["how many reps", "exercise frequency", "sets and reps", "overtraining"],
        "question": "How many times a day should I perform my physiotherapy home exercises?",
        "answer": "For ROM and gentle mobility: 2-3 times daily in short 10-minute bouts. For muscle strengthening: once daily or every alternate day (3 sets of 10-12 reps) to allow 24-48 hours of muscular recovery and protein synthesis.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 56,
        "category": "rehab_exercises",
        "keywords": ["wall slides", "shoulder wall slide", "shoulder mobility"],
        "question": "How do wall slides help restore overhead shoulder reach after a collarbone injury?",
        "answer": "Stand facing a wall with forearms resting against it on a towel. Slide your arms upward in a 'V' shape, maintaining contact, while focusing on serratus anterior upward scapular rotation. Slide back down with control.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 57,
        "category": "rehab_exercises",
        "keywords": ["stationary bike", "cycling rehab", "bicycle after knee"],
        "question": "When can I begin riding a stationary upright bicycle after knee injury?",
        "answer": "You need at least 95-100 degrees of passive knee flexion to complete a full pedal revolution without rocking your pelvis. Set the seat high initially, pedal with zero resistance, and start with gentle backward pedaling.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 58,
        "category": "rehab_exercises",
        "keywords": ["balance exercise", "single leg stand", "proprioception"],
        "question": "Why do I need balance training after an ankle sprain or leg fracture?",
        "answer": "Trauma tears microscopic proprioceptors (nerve mechanoreceptors) in joint capsules and ligaments, leaving the brain blind to joint position. Balance exercises (standing on 1 foot for 30s) re-wire neuromuscular pathways to prevent re-sprains.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 59,
        "category": "rehab_exercises",
        "keywords": ["calf stretch", "achilles stretch", "wall calf stretch"],
        "question": "How do I stretch tight calf muscles safely after removing a walking boot?",
        "answer": "Stand facing a wall. Step your injured leg back with heel flat on the floor and knee straight. Lean hips forward until you feel a comfortable stretch in the calf. Hold 30 seconds; do not bounce. Repeat with knee slightly bent to stretch the deeper soleus.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 60,
        "category": "rehab_exercises",
        "keywords": ["exercise ball", "swiss ball", "stability ball"],
        "question": "Are stability gym balls safe for post-accident core and back rehab?",
        "answer": "Yes, seated pelvic rocks and gentle bridge rollouts on an exercise ball stimulate deep multifidus and transversus abdominis stabilizers with minimal compressive axial spinal loading.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 61,
        "category": "rehab_exercises",
        "keywords": ["breathing during exercise", "hold breath", "valsalva"],
        "question": "Should I hold my breath when doing difficult rehab exercises?",
        "answer": "NO! Holding your breath (Valsalva maneuver) spikes blood pressure and intra-thoracic pressure, restricting cerebral venous return. Always EXHALE on the effort/exertion phase and INHALE on the return/relaxation phase.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 62,
        "category": "rehab_exercises",
        "keywords": ["clam shell", "clamshell exercise", "hip strength"],
        "question": "What is the purpose of the clamshell exercise in leg rehabilitation?",
        "answer": "Clamshells specifically isolate the gluteus medius and external hip rotators. Strengthening this muscle prevents valgus knee collapse during walking, directly protecting the knee joint and patella tracking.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 63,
        "category": "rehab_exercises",
        "keywords": ["towel scrunch", "intrinsic foot muscles", "foot arch exercise"],
        "question": "How do towel scrunches help after foot fracture or ankle trauma?",
        "answer": "Sit with bare feet on a towel and use your toes to scrunch the towel toward you. This activates plantar intrinsic foot muscles, rebuilding the longitudinal arch and restoring push-off power in your gait.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 64,
        "category": "rehab_exercises",
        "keywords": ["cat cow stretch", "spinal mobility", "back stiffness stretch"],
        "question": "Is the Cat-Cow yoga stretch safe for post-accident spine stiffness?",
        "answer": "Yes, on hands and knees, gently arching the spine upward (cat) and dipping downward (cow) provides segmental spinal articulation, promotes disc nutrition via imbibition, and relieves muscular guarding.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 65,
        "category": "rehab_exercises",
        "keywords": ["missed a day", "skipped exercises", "behind schedule"],
        "question": "I missed 2 days of physiotherapy exercises because of pain. Will my recovery be ruined?",
        "answer": "Not at all! Muscle and bone remodeling occur during recovery and rest. Never try to double the exercises on the next day; simply resume your normal prescribed routine at a comfortable pace.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 66,
        "category": "rehab_exercises",
        "keywords": ["hydrotherapy", "swimming after injury", "pool therapy"],
        "question": "When can I do aquatic therapy or swimming after bone fracture healing?",
        "answer": "Hydrotherapy is fantastic once surgical incisions are 100% healed. Water buoyancy offsets 80-90% of body weight, allowing early pain-free normal gait practice and progressive hydrodynamic resistance.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 67,
        "category": "rehab_exercises",
        "keywords": ["quadriceps stretch", "thigh stretch", "heel to buttock"],
        "question": "How do I stretch tight quadriceps safely without twisting the knee?",
        "answer": "Lie prone on your stomach. Wrap a strap or belt around your ankle and gently pull your heel toward your buttocks until you feel a stretch along the front of your thigh. Keep your pelvis pressed flat to avoid hyper-extending the lumbar spine.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 68,
        "category": "rehab_exercises",
        "keywords": ["hamstring stretch", "back of thigh tight", "seated hamstring"],
        "question": "What is the safest way to stretch tight hamstrings after a knee injury?",
        "answer": "Do a seated single-leg hamstring stretch on a firm chair: extend the injured leg straight with heel on floor and toes pointing up. Keep your spine straight and hinge forward from the hips until a stretch is felt in the back of the thigh.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 69,
        "category": "rehab_exercises",
        "keywords": ["grip strengthener", "stress ball", "hand grip exercise"],
        "question": "How often should I squeeze a stress ball after arm fracture recovery?",
        "answer": "Perform 15-20 repetitions, 3 times a day. Do not squeeze continuously for minutes, as excessive isometric gripping can trigger flexor tendonitis or carpal tunnel irritation.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 70,
        "category": "rehab_exercises",
        "keywords": ["squat rehab", "mini squat", "wall squat"],
        "question": "When can I start doing squats after leg surgery?",
        "answer": "Start with shallow mini-squats (0 to 45 degrees) against a wall with an exercise ball behind your lower back. Never squat past 90 degrees in early recovery, as patellofemoral joint contact forces peak dramatically.",
        "severity": "moderate",
        "red_flag": False
    },

    # =========================================================================
    # CATEGORY 4: PAIN ASSESSMENT & NERVE VS MUSCLE PAIN (71 - 85)
    # =========================================================================
    {
        "id": 71,
        "category": "pain_assessment",
        "keywords": ["vas scale", "pain score 1 to 10", "rate pain", "pain scale"],
        "question": "How does the 1 to 10 Visual Analogue Scale (VAS) categorize my recovery pain?",
        "answer": "VAS 1-3 = Mild Pain (noticeable but doesn't disrupt rehab; continue exercises). VAS 4-6 = Moderate Pain (interferes with movement; reduce intensity, apply ice). VAS 7-10 = Severe/Critical Pain (unbearable, halts movement; stop exercises immediately and contact physiotherapist).",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 72,
        "category": "pain_assessment",
        "keywords": ["nerve pain vs muscle pain", "burning pain", "electric shock", "shooting pain"],
        "question": "How do I tell if my pain is nerve pain or ordinary muscle soreness?",
        "answer": "Muscle soreness feels like a dull, heavy, stiff ache that peaks 24-48 hours post-exercise (DOMS). Nerve pain feels like burning, electric shocks, lightning-bolt shooting, tingling, or extreme sensitivity to light touch.",
        "severity": "moderate",
        "red_flag": False
    },
    {
        "id": 73,
        "category": "pain_assessment",
        "keywords": ["doms", "delayed onset muscle soreness", "pain next day"],
        "question": "Why do my muscles hurt more 2 days after therapy than on the day of exercise?",
        "answer": "This is Delayed Onset Muscle Soreness (DOMS), caused by microscopic tears in muscle Z-disc fibers during eccentric contractions. It is a normal physiological trigger for muscle remodeling and resolves spontaneously within 72 hours.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 74,
        "category": "pain_assessment",
        "keywords": ["phantom pain", "amputation pain", "limb hurts not there"],
        "question": "What is phantom limb pain and how does mirror therapy help?",
        "answer": "Phantom pain occurs when cortical sensory maps in the brain continue firing despite limb loss. Mirror Therapy tricks the brain's neuroplastic visual cortex by reflecting the healthy limb, suppressing abnormal nociceptive signals.",
        "severity": "moderate",
        "red_flag": False
    },
    {
        "id": 75,
        "category": "pain_assessment",
        "keywords": ["weather changes pain", "rain pain", "barometric pressure"],
        "question": "Does cloudy or rainy weather actually increase joint pain after bone fractures?",
        "answer": "Yes! Falling atmospheric barometric pressure allows injured articular tissues and micro-fibrous scars to slightly expand, irritating sensitizing mechanoreceptors inside bone periosteum and joints.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 76,
        "category": "pain_assessment",
        "keywords": ["pain diary", "tracking pain", "pain log"],
        "question": "Why does my physiotherapist ask me to keep a daily pain tracking diary?",
        "answer": "Tracking daily pain scores (VAS 1-10), morning stiffness duration, and post-exercise recovery time enables the physiotherapist to objectively measure tissue adaptation and prevent overtraining plateaus.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 77,
        "category": "pain_assessment",
        "keywords": ["sciatica", "pain shooting down leg", "pinched nerve", "buttock pain"],
        "question": "I have pain shooting from my buttock down to my calf after a fall. What is this?",
        "answer": "This is lumbar radiculopathy (sciatica), caused by disc protrusion or piriformis muscle spasm compressing the L4-S1 nerve roots. Avoid forward bending, perform gentle McKenzie prone press-ups, and avoid lifting objects.",
        "severity": "moderate",
        "red_flag": False
    },
    {
        "id": 78,
        "category": "pain_assessment",
        "keywords": ["radiating arm pain", "cervical radiculopathy", "neck to fingers"],
        "question": "My neck injury causes pain radiating down my arm into my index finger. What causes this?",
        "answer": "This indicates C6 cervical nerve root irritation. Perform nerve flossing (median nerve neurodynamic glides) and gentle cervical retraction. Avoid overhead heavy lifting.",
        "severity": "moderate",
        "red_flag": False
    },
    {
        "id": 79,
        "category": "pain_assessment",
        "keywords": ["hypersensitivity", "shirt hurts", "allodynia", "skin burning"],
        "question": "Even light bedsheets brushing against my recovering limb cause burning pain. Is this normal?",
        "answer": "This is allodynia (cutaneous hypersensitivity). Desensitize the skin by gently stroking the limb with graduated textures (silk $\\rightarrow$ cotton $\\rightarrow$ velvet $\\rightarrow$ terrycloth towel) for 5 minutes 3 times daily to recalibrate nerve threshold.",
        "severity": "moderate",
        "red_flag": False
    },
    {
        "id": 80,
        "category": "pain_assessment",
        "keywords": ["night pain", "pain wakes me up", "throbbing at night"],
        "question": "Why does my injured shoulder ache and throb much worse at night when lying down?",
        "answer": "In horizontal recumbent sleep, gravity no longer pulls the arm down to decompress the subacromial space, and lower cortisol levels at night lower pain thresholds. Sleep semi-reclined or prop a pillow under your elbow.",
        "severity": "moderate",
        "red_flag": False
    },
    {
        "id": 81,
        "category": "pain_assessment",
        "keywords": ["bone ache", "deep ache", "fracture site dull ache"],
        "question": "My fracture site has a constant deep dull ache. How do I know if the bone is failing to heal?",
        "answer": "A mild, deep bone ache during loading is normal osteoblastic remodeling. However, if sharp, acute focal pain persists at the fracture line after 12 weeks with gross motion, a non-union must be checked via repeat X-ray.",
        "severity": "moderate",
        "red_flag": False
    },
    {
        "id": 82,
        "category": "pain_assessment",
        "keywords": ["tendonitis", "tendon pain", "burning tendon"],
        "question": "What is the difference between muscle pain and tendonitis?",
        "answer": "Muscle pain occurs across the broad muscle belly and resolves with rest. Tendonitis occurs at the localized point where tendon anchors into bone (e.g., patellar tendon, Achilles) and hurts sharply at the start of exercise.",
        "severity": "moderate",
        "red_flag": False
    },
    {
        "id": 83,
        "category": "pain_assessment",
        "keywords": ["chronic pain cycle", "central sensitization", "brain pain"],
        "question": "What is central sensitization in long-term post-accident pain?",
        "answer": "When acute pain persists for months, the central nervous system becomes hyper-excitable, amplifying pain signals even after structural tissue healing. Mindful breathing, aerobic walking, and pacing therapy re-tune brain pathways.",
        "severity": "moderate",
        "red_flag": False
    },
    {
        "id": 84,
        "category": "pain_assessment",
        "keywords": ["posture pain", "desk posture", "slouching hurts"],
        "question": "Why does sitting at my office desk trigger pain in my accident-injured back?",
        "answer": "Slouched sitting increases intra-discal pressure by 140% compared to standing. Maintain a lumbar roll curve, ensure your feet are flat on the floor with knees at 90 degrees, and take a 2-minute standing break every 45 minutes.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 85,
        "category": "pain_assessment",
        "keywords": ["hydration pain", "drinking water and cramps", "water recovery"],
        "question": "Does drinking enough water really make a difference in muscle recovery and pain?",
        "answer": "Yes! Fascia and cartilage are over 70% water. Dehydration causes fascial micro-stickiness, reduces synovial joint lubrication, and triggers painful nocturnal muscle cramps.",
        "severity": "mild",
        "red_flag": False
    },

    # =========================================================================
    # CATEGORY 5: RED-FLAGS, COMPLICATIONS & EMERGENCY ESCALATION (86 - 105)
    # =========================================================================
    {
        "id": 86,
        "category": "red_flags",
        "keywords": ["dvt", "calf swelling", "calf warm", "pain in calf", "blood clot"],
        "question": "One of my calves is red, swollen, warm to touch, and aches when I flex my foot. What should I do?",
        "answer": "EMERGENCY: These are classic signs of Deep Vein Thrombosis (DVT / blood clot). Do NOT massage your calf. Seek immediate emergency room evaluation for a venous Doppler ultrasound to prevent pulmonary embolism.",
        "severity": "critical",
        "red_flag": True
    },
    {
        "id": 87,
        "category": "red_flags",
        "keywords": ["compartment syndrome", "severe pain cast", "fingers pale and cold", "pain out of proportion"],
        "question": "My cast feels excruciatingly tight, my fingers/toes are pale and cold, and pain medication is not helping at all. What is happening?",
        "answer": "CRITICAL SURGICAL EMERGENCY: This suggests Acute Compartment Syndrome (dangerous pressure buildup inside muscle fascial compartments). Report to the nearest emergency department immediately for cast split or emergency fasciotomy.",
        "severity": "critical",
        "red_flag": True
    },
    {
        "id": 88,
        "category": "red_flags",
        "keywords": ["wound infection", "pus", "fever after surgery", "yellow discharge", "wound red and hot"],
        "question": "My surgical wound is leaking yellow pus, surrounding skin is red and burning, and I have a fever of 101°F. What is this?",
        "answer": "CRITICAL EMERGENCY: These are definitive signs of a deep surgical site infection (SSI) or osteomyelitis. Contact your orthopedic surgeon immediately. Do NOT self-prescribe antibiotics without a wound culture.",
        "severity": "critical",
        "red_flag": True
    },
    {
        "id": 89,
        "category": "red_flags",
        "keywords": ["cauda equina", "cannot pass urine", "loss of bowel", "saddle numbness", "groin numb"],
        "question": "After my back injury, I cannot pass urine, and my inner groin/saddle area has gone completely numb. What should I do?",
        "answer": "CRITICAL NEUROLOGICAL EMERGENCY: This is Cauda Equina Syndrome (severe compression of spinal nerve roots). You require emergency spinal decompression surgery within 24-48 hours to prevent permanent paralysis and incontinence. Go to the ER immediately.",
        "severity": "critical",
        "red_flag": True
    },
    {
        "id": 90,
        "category": "red_flags",
        "keywords": ["foot drop", "toes drag", "cannot lift foot", "trip on foot"],
        "question": "I cannot lift my toes or foot upward, and it drags when I walk after my knee injury. What does this mean?",
        "answer": "This is Foot Drop, caused by injury to the Common Peroneal Nerve near the fibular head. Consult your orthopedic specialist or neurologist for an EMG/NCS nerve conduction study and a temporary Ankle-Foot Orthosis (AFO) brace.",
        "severity": "high",
        "red_flag": True
    },
    {
        "id": 91,
        "category": "red_flags",
        "keywords": ["bone deformity", "crooked bone", "popped out", "unnatural angle"],
        "question": "My recovering arm/leg suddenly looks crooked or has an unnatural bend after a minor stumble. What happened?",
        "answer": "EMERGENCY: This suggests a re-fracture or failure/displacement of orthopedic hardware (plates/screws). Immobilize the limb immediately with a splint, apply no weight, and seek urgent orthopedic radiological assessment.",
        "severity": "critical",
        "red_flag": True
    },
    {
        "id": 92,
        "category": "red_flags",
        "keywords": ["shortness of breath", "chest pain after fracture", "coughing blood", "pulmonary embolism"],
        "question": "I am recovering from a femur fracture and suddenly have sharp chest pain, shortness of breath, and rapid heartbeat. What is this?",
        "answer": "LIFE-THREATENING EMERGENCY: This suggests a Pulmonary Embolism (blood clot migrated to the lungs) or Fat Embolism Syndrome. Call emergency medical services (108 / 911) IMMEDIATELY.",
        "severity": "critical",
        "red_flag": True
    },
    {
        "id": 93,
        "category": "red_flags",
        "keywords": ["crps", "burning skin", "sweating foot", "color change limb", "reflex sympathetic"],
        "question": "My injured hand is burning relentlessly, skin is shiny and sweaty, and changes color between pale, red, and purple. What is this?",
        "answer": "This indicates Complex Regional Pain Syndrome (CRPS / Sudeck's atrophy), a severe sympathetic nervous system dysfunction. Early intervention by a specialized physiotherapist and pain management specialist is essential.",
        "severity": "high",
        "red_flag": True
    },
    {
        "id": 94,
        "category": "red_flags",
        "keywords": ["giving way", "knee buckle", "sudden collapse", "unstable joint"],
        "question": "My knee suddenly gave way and buckled under me while walking across the room. Did my ligament fail?",
        "answer": "Giving way indicates either mechanical joint instability (graft failure/meniscal tear) or sudden reflex quadriceps shutoff. Use crutches immediately, apply a stabilizing knee brace, and visit your physiotherapist for Lachman/Pivot-shift testing.",
        "severity": "high",
        "red_flag": False
    },
    {
        "id": 95,
        "category": "red_flags",
        "keywords": ["septic arthritis", "hot joint", "cannot move joint at all", "shivering joint"],
        "question": "My injured joint has become scorching hot, severely swollen, and I cannot tolerate even 1 millimeter of movement. What could it be?",
        "answer": "CRITICAL EMERGENCY: This indicates Septic Arthritis (bacterial infection of the synovial joint space). It can permanently destroy articular cartilage within 24 hours. Immediate emergency arthrocentesis (joint aspiration) is required.",
        "severity": "critical",
        "red_flag": True
    },
    {
        "id": 96,
        "category": "red_flags",
        "keywords": ["severe headache accident", "dizziness vomiting", "concussion", "head strike"],
        "question": "I was in an accident and now have a worsening throbbing headache, blurred vision, and nausea/vomiting. What should I do?",
        "answer": "EMERGENCY: These are red-flag signs of Traumatic Brain Injury (TBI), concussion, or intracranial hemorrhage. Report immediately to an emergency department for an urgent non-contrast CT brain scan.",
        "severity": "critical",
        "red_flag": True
    },
    {
        "id": 97,
        "category": "red_flags",
        "keywords": ["pop sound during exercise", "loud snap", "sudden sharp tear"],
        "question": "I heard a loud audible 'POP' sound in my healing tendon during exercise followed by immediate weakness. Did it tear?",
        "answer": "EMERGENCY: A loud audible pop followed by immediate loss of active movement indicates acute tendon or ligament rupture (e.g., Achilles or Patellar tendon rupture). Stop exercise, ice, and get immediate orthopedic evaluation.",
        "severity": "critical",
        "red_flag": True
    },
    {
        "id": 98,
        "category": "red_flags",
        "keywords": ["uncontrolled bleeding", "blood soaking bandage", "incision opening"],
        "question": "Blood is continuously soaking through my surgical dressing and dripping. What should I do?",
        "answer": "EMERGENCY: Apply firm, continuous direct pressure over the dressing using a clean sterile gauze or towel for 10 full minutes without peeking. If bleeding continues soaking through, report to emergency care immediately.",
        "severity": "critical",
        "red_flag": True
    },
    {
        "id": 99,
        "category": "red_flags",
        "keywords": ["cast broken", "wet plaster", "soft cast", "cracked cast"],
        "question": "My plaster cast got soaked in water and is soft and cracked. Can I wait until my next appointment?",
        "answer": "NO. A wet or cracked cast loses structural rigidity, permitting bone fracture displacement, and wet padding causes rapid skin maceration and ulcers. You must visit the clinic within 24 hours for a cast change.",
        "severity": "moderate",
        "red_flag": False
    },
    {
        "id": 100,
        "category": "red_flags",
        "keywords": ["allergic rash dressing", "tape blister", "skin peeling under tape"],
        "question": "The skin around my surgical adhesive tape is breaking out in painful itchy blisters. What should I do?",
        "answer": "This is adhesive contact dermatitis. Gently remove the irritating tape using baby oil or an adhesive remover wipe. Switch to hypoallergenic paper tape (Micropore) or tubular stockinette, and apply calamine lotion to intact skin.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 101,
        "category": "red_flags",
        "keywords": ["sudden vision blur", "dizzy standing", "orthostatic hypotension"],
        "question": "I feel blackouts and dizziness every time I stand up with crutches after being in bed for days. Is this normal?",
        "answer": "This is Orthostatic Hypotension due to bed-rest deconditioning. Sit on the edge of the bed for 2 minutes and pump your ankles 15 times before standing up. Stay hydrated with electrolyte fluids.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 102,
        "category": "red_flags",
        "keywords": ["nail turn black", "subungual hematoma", "blood under nail"],
        "question": "A heavy object fell on my toe/finger in an accident and blood pooled under the nail. How is it relieved?",
        "answer": "A subungual hematoma creates intense throbbing pressure. If covering more than 50% of the nail, a physician can perform micro-trephination (painless cautery hole) to release the blood and relieve pain instantly.",
        "severity": "mild",
        "red_flag": False
    },
    {
        "id": 103,
        "category": "red_flags",
        "keywords": ["pain scale 10", "unbearable pain", "crying with pain"],
        "question": "My pain is rated 10 out of 10 and none of my prescribed medications are touching it. What should I do?",
        "answer": "EMERGENCY: Breakthrough pain at 10/10 requires immediate clinical escalation. Contact your treating hospital or on-call orthopedic team for IV analgesic titration and rule out ischemic complications.",
        "severity": "critical",
        "red_flag": True
    },
    {
        "id": 104,
        "category": "red_flags",
        "keywords": ["pins loosening", "external fixator loose", "ex fix pin drainage"],
        "question": "The metal pins sticking out of my leg (external fixator) are wiggling and oozing clear fluid. Is this safe?",
        "answer": "WARNING: External fixator pin-site loosening or persistent discharge indicates pin-tract infection or loss of mechanical bone stability. Clean with chlorhexidine and contact your orthopedic surgeon promptly.",
        "severity": "high",
        "red_flag": True
    },
    {
        "id": 105,
        "category": "red_flags",
        "keywords": ["emergency triage", "red flag criteria", "when to go to hospital"],
        "question": "What are the universal RED-FLAG warning signs that require immediate hospital admission during recovery?",
        "answer": "🚨 RED-FLAG CRITERIA: 1) One-sided hot swollen calf (DVT), 2) Sudden chest pain or shortness of breath (PE), 3) Fever >101°F with wound pus, 4) Progressive loss of bowel/bladder control, 5) Cold, pale, pulseless extremity with severe pain out of proportion.",
        "severity": "critical",
        "red_flag": True
    }
]


import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Initialize Sublinear TF-IDF Engine over 105 Clinical Q&As
_corpus = []
for _item in PAIN_QNA_DATABASE:
    _text = (
        _item["question"] + " " +
        " ".join(_item["keywords"]) + " " +
        _item["category"].replace("_", " ")
    )
    _corpus.append(_text)

_tfidf_vectorizer = TfidfVectorizer(
    stop_words="english",
    sublinear_tf=True,
    ngram_range=(1, 2)
)
_tfidf_matrix = _tfidf_vectorizer.fit_transform(_corpus)


def query_pain_knowledge_base(query_text):
    """
    Sublinear TF-IDF + Cosine Similarity NLP Search over 105 Physiotherapy Q&As.
    Returns best matching clinical recommendation and red flag status.
    """
    clean_query = (query_text or "").strip().lower()
    if not clean_query:
        return {"found": False, "message": "Empty query."}

    # 1. TF-IDF Cosine Similarity Search
    q_clean = re.sub(r"[^a-zA-Z0-9\s]", " ", clean_query).strip()
    q_vec = _tfidf_vectorizer.transform([q_clean])
    sims = cosine_similarity(q_vec, _tfidf_matrix)[0]
    best_idx = int(sims.argmax())
    best_tfidf_score = float(sims[best_idx])
    best_match = PAIN_QNA_DATABASE[best_idx]

    # 2. Exact keyword / phrase matching bonus
    keyword_boost = 0
    words_in_query = set(q_clean.split())
    for kw in best_match["keywords"]:
        kw_clean = kw.lower()
        if " " in kw_clean and kw_clean in clean_query:
            keyword_boost += 0.35
        elif kw_clean in words_in_query:
            keyword_boost += 0.20

    combined_confidence = best_tfidf_score + keyword_boost

    # Acceptance threshold (avoids false-positive Red Flags or random triggers)
    if combined_confidence >= 0.18:
        return {
            "found": True,
            "match_id": best_match["id"],
            "category": best_match["category"],
            "question": best_match["question"],
            "answer": best_match["answer"],
            "severity": best_match["severity"],
            "red_flag": best_match["red_flag"],
            "confidence": round(combined_confidence, 3)
        }

    return {
        "found": False,
        "message": "Please consult your physiotherapist for an individual rehabilitation assessment. Maintain gentle range of motion within your pain-free zone."
    }


# Alias for external service imports
PHYSIO_PAIN_KNOWLEDGE_BASE = PAIN_QNA_DATABASE
