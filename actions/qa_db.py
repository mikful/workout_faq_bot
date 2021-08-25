def question_answer_pair(question: str) -> str:
    qa_mem_db = {
        # What is the best exercise agains belly fat ?
        "fitness_q1":
            ' '.join('''There is no 'best' exercise to lose belly fat.
    For many people, cutting out most of the sugar in 
    their diet (obviously not sugar from fruit and other 
    healthy sources) is an excellent way to lose the weight.'''.split()),
        # Optimal exercises for an abdominal workout
        "fitness_q2":
            ' '.join('''The crunch flexes the trunk and primarily targets the 
    rectus abdominis, not the transversus abdominis or 
    the obliques.'''.split()),
        # How old should children be to train with weights?
        "fitness_q3":
            ' '.join('''Taking Eric and Dave's answers into consideration, we must understand 
    that children's bodies are still developing. I believe a structured lifting program 
    for children can be a fantastic introduction to controlled multiplanar movement.'''.split()),

        # ------------------------- start metabolism -------------------------
        #     - How to Increase height naturally? Are those ads gimmicks?
        "ask_metabol_q1":
            ' '.join('''If you're just playing amateur level sports, and make it your goal to have a massive vertical jump,
     you'll more than make up for your lack of height.'''.split()),

        #     - Can weight lost be sustained through exercise influenced metabolism changes?
        "ask_metabol_q2":
            ' '.join('''So now we've got people who've lost fat as well as useful lean body mass, have a lowered metabolic 
    rate and are then released from their harsh crash diet.'''.split()),

        #     - Is it true that you can eat anything you want within 15 minutes of working out without putting on weight?
        "ask_metabol_q3":
            ' '.join('''Your body will process the food that you ingest, and if the caloric intake of the food is greater 
    than the amount of calories burned during the ensuing exercise, you will gain weight.'''.split()),

        #           - Does working a diverse set of muscles increase metabolism?
        "ask_metabol_q4":
            ' '.join('''Anaerobic workouts are basically intense workouts that push your body beyond the ability 
    to provide energy just through normal aerobic metabolism.'''.split()),

        # - How does one train for sports when the three metabolic pathways interact?
        "ask_metabol_q5":
            ' '.join('''The oxidative pathways run fairly continuously to maintain life and replenish tissues 
    that have made use of anaerobic energy conversion.'''.split()),

        #     - Does exercise REALLY increase the basal metabolism rate for any significant length of time after the exercise is over?
        "ask_metabol_q6":
            ' '.join('''In this study :  http://www.mendeley.com/research/postexercise-energy-expenditure-response-acute-aerobic-resistive-exercise/  
    they used 90 minute, high intensity strength workouts, and still after 15 hours, the metabolic rate was elevated.'''.split()),

        #     - How much cardio is advisable for an overweight person who is new to bodybuilding?
        "ask_metabol_q7":
            ' '.join('''Vice versa, with higher peaks and stronger contractions you will get a glycolitic type of 
    muscle; and this type of muscle is the one you want to get if you are trying to aim at power/strenght 
    sports and/or hypertrophy ( composed mostly of IIa and IIx fibers ).'''.split()),

        #         - Naturally increasing my Metabolism
        "ask_metabol_q8":
            ' '.join('''Eating large portions spaced far apart will make the body believe there is a "famine" 
    and will store the food as fat to prepare for hard times.'''.split()),

        #         - What is the best way to bring one's metabolism out of starvation mode following a diet?
        "ask_metabol_q9":
            ' '.join('''Progress can be measured by trying to determine her basal temperature; it's probably 
    quite low now (almost nobody on the planet actually has a 98.6 deg.'''.split()),

        #         - why do we need more rest when lifting heavy?
        "ask_metabol_q10":
            ' '.join('''They need a break to be ready for the next lifting. In that break time, they undergo 
    repair and get nourished and grow stronger."'''.split()),

        # ------------------------- ends metabolism questions --------------------------

        # ------------------------- start weight-gain -----------------------------------

        #         - How can I gain weight and muscle weight?
        "ask_weight_gain_q1":
            ' '.join('''If you want upper-body mass you need to do activities that engage
                    and exercise those muscle groups.'''.split()),

        #         - Can weight lost be sustained through exercise influenced metabolism changes?
        "ask_weight_gain_q2":
            ' '.join('''So now we've got people who've lost fat as well as useful lean body 
                   mass, have a lowered metabolic rate and are then released from their harsh crash diet.'''.split()),

        #         - Is it true that you can eat anything you want within 15 minutes of working out without putting on weight?
        "ask_weight_gain_q3":
            ' '.join('''Your body will process the food that you ingest,
                    and if the caloric intake of the food is greater than the amount of calories 
                    burned during the ensuing exercise, you will gain weight.'''.split()),

        #              - Weight gained using GOMAD strategy
        "ask_weight_gain_q4":
            ' '.join('''If you lift heavy three times a week and do GOMAD, 
                   a little less than half of the weight you gain will be fat.'''.split()),

        #  - How to gain weight for a naturally thin person?
        "ask_weight_gain_q5":
            ' '.join('''My general suggestion for people are new to exercise is to start with aiming
             for balance of their intake of carbs and protein.
             #How many calories depends a lot on your weight/height/age."'''.split()),

        #         - Mom Losing Her Mobility Because of her Weight Gain
        "ask_weight_gain_q6":
            ' '.join('''She's very likely a clear candidate for  weight loss surgery , and a physician 
                   friend of mine has told me of cases of extreme obesity (which your mother has) where removing the 
                   weight needs to be carefully tracked.'''.split()),

        #        - Milk+honey helps gain weight?
        "ask_weight_gain_q7":
            ' '.join('''It might help you gain weight, but you would have to drink a lot of it.
             #You're in a position where you have the opportunity to eat lots of nutritious foods which 
             # will benefit more then you know but you've chosen milk and honey.'''.split()),

        #          - Gaining weight without gaining fat
        "ask_weight_gain_q8":
            ' '.join('''I'm not saying be a body builder, but you want to increase your lean mass to keep 
        your body fat low as you gain weight.
        At least 1g of protein per pound of lean body mass while you want to gain muscle.'''.split()),

        # -------------------------  weight-gain questions end ------------------------------

        # -------------------------  reduce body-fat qs start -----------------------------------

        #            - How accurate is the Navy Body Fat Calculator?
        "ask_body_fat_q1":
            ' '.join('''The second term probably corrects for height (so that tall people don't get 
        punished for have proportionate girths), and the last term is probably an 
        experimentally-justified constant that corrects the result of the equation to it's as close 
        as possible to actual body fat levels.'''.split()),

        #     - Why is body mass index so widely used to determine ideal body weight?
        "ask_body_fat_q2":
            ' '.join('''It's based on the idea that people who weigh significantly more or 
        less than the average person of their height are probably not a healthy weight.'''.split()),

        #                - Is it possible to lose weight on some special parts of body?
        "ask_body_fat_q3":
            ' '.join('''I'm assuming you mean according to the BMI measure.
        So, while you can't target where your body burns fat, what you can do is change the proportions of muscle and
        fat at your weight."'''.split()),

        #         - Body fat loss halted. Anyone have experience getting under 8% body fat?
        "ask_body_fat_q4":
            ' '.join('''A light amount of cardio in morning before breakfast (called fasted cardio) 
        targets the fat supplies and, for the most part, leaves your muscles intact.'''.split()),

        #    - How to maintain my body without fat and reduce belly?
        "ask_body_fat_q5":
            ' '.join('''I think rice and fish is a good meal, but maybe try to change it a bit.
        #If you fry your fish, try to use less fat.'''.split()),

        #      - Upper and lower body proportion, gaining muscle losing fat
        "ask_body_fat_q6":
            ' '.join('''It may be the case, that there is actually quite little fat 
        on your buttocks and legs, but it just looks a lot because of lack of muscle.'''.split()),

        #            - How much cardio is advisable for an overweight person who is new to bodybuilding?
        "ask_body_fat_q7":
            ' '.join('''Vice versa, with higher peaks and stronger contractions you 
        will get a glycolitic type of muscle; and this type of muscle is the one you want to get if you 
        are trying to aim at power/strenght sports and/or hypertrophy 
        ( composed mostly of IIa and IIx fibers ).'''.split()),

        #           - Naturally increasing my Metabolism
        "ask_body_fat_q8":
            ' '.join('''Eating large portions spaced far apart will make the body believe there is a 
        "famine" and will store the food as fat to prepare for hard times.'''.split()),

        #         - Chubbyness from the face and body
        "ask_body_fat_q9":
            ' '.join('''More specifically the sodium/carb intake within your diet and hydration.
        Cut back on the salts and increase you're hydration and see if that can't take off some of the water weight 
        in your face.'''.split()),

        #     - Lower body fat problem
        "ask_body_fat_q10":
            ' '.join('''It might not be to your choosing, but for your body's furnace fat burning 
        mechanism, it will get energy from fat based on it's most readily available source.'''.split()),

        #            - Is spot reduction necessarily a myth?
        "ask_body_fat_q11":
            ' '.join('''If we change the definition of spot reduction to be an optimal diet with a 
        core-focused high-intensity strength workout followed by high-intensity cardio to minimally 
        increase the efficiency of fat burn in the mid-section then yes, I think it has some merit.'''.split()),

        #              - How to accurately measure muscle mass versus body fat?
        "ask_body_fat_q12":
            ' '.join('''Intelamterix makes a product called  BodyMetrix  that can accurately scan 
        your body fat percentage and track your fat loss and muscle gain.
        The  software  itself tracks measurements and can generate reports.'''.split()),

        # -------------------------  reduce body-fat qs end ----------------------------------

        # -------------------------  muscle-mass qs start -----------------------------------

        #            - How can I gain weight and muscle weight?
        "ask_muscle_mass_q1":
            ' '.join('''If you want upper-body mass you need to do activities that engage and exercise 
        those muscle groups.'''.split()),

        #           - Why is muscle size not proportional to strength?
        "ask_muscle_mass_q2":
            ' '.join('''Two reasons why muscle mass and strength may not be completely 
        congruous are:     Muscle fiber density   Muscle utilization      
        Density:  Your muscles are composed of four different types of fibers
        (slow-twitch, and three forms of fast-twitch).'''.split()),

        #     - How long does it take for muscles to recover?
        "ask_muscle_mass_q3":
            ' '.join('''Probably the biggest reason folks use real training programs 
            (Starting Strength, Madcow, Texas, 5/3/1, etc) are because they attempt
             to thread the needle on lifting as much as possible while never 
             exceeding your recovery (basically).'''.split()),

        #          - Best timing and amount of protein intake for building mass
        "ask_muscle_mass_q4":
            ' '.join('''Testosterone and growth hormone are both known to cause muscle growth
             and make good use of the amino acids and proteins you have in your body at the time.'''.split()),

        #       - Is increasing resistance the only possibility to build more muscle mass?
        "ask_muscle_mass_q5":
            ' '.join('''Lack of change in intensity, volume or frequency : Muscles get used to
             your set and rep scheme with in 6 workouts if not changed or progressively loaded will 
             not super compensate.'''.split()),

        #          - Does muscle mass help or hurt for powerlifting and other strength sports?
        "ask_muscle_mass_q6":
            ' '.join('''I’m not saying you have to have a fat torso, but a light lifter like that 
            won’t have the torso support for leverage.”   Taking the 6’2”, 165 lb aspiring powerlifter 
            as an example, what’s the least he should weigh to avoid chasing his tail in the squat 
            and the sport in general?'''.split()),

        #              - How do I gain lean muscle mass as a vegetarian or vegan?
        "ask_muscle_mass_q7":
            ' '.join('''Gaining healthy weight is the same for vegetarians as it is for omnivores:  
        lift heavy, eat big, prioritize getting bigger .
        You'll still have to find a way to lift heavy, eat big, 
        and prioritize getting bigger.'''.split()),

        #           - Can you effectively put on mass while being highly active/fit?
        "ask_muscle_mass_q8":
            ' '.join(''' Here's an article from Greg Knuckols entitled "Avoiding Cardio
         Could Be Holding You Back " and another from Juggernaut Training 
         entitled "Conditioning: How To Do It Right"   Combined there's easily maybe 20 pages 
         of material to shift through, but the TLDR version is: Lifting weights requires energy.'''.split()),

        #              - Is it possible to effectively build muscle mass using resistance bands?
        "ask_muscle_mass_q9":
            ' '.join('''Free weights and resistance bands have in common that they produce a constant 
            force along the line of action. So using a resistance band the force increases during the 
            range of motion of the exercise.'''.split()),

        #         - If I can't get plenty of sleep, should I be doing anything different when trying to put on mass?
        "ask_muscle_mass_q10":
            ' '.join(''' Priorise getting at least 7 hours of sleep a night:  This is necessary for good health.
            Look at alternate times:  if you are at work, university or school, can you workout during lunch?'''.split()),

        #              - Why do compound exercises build more mass than isolation exercises?
        "ask_muscle_mass_q11":
            ' '.join(''' The compound exercises help build that base of strength, but they are 
        not going to shape the muscles the way you want.'''.split()),

        #         - Why do sprinters have muscular arms?
        "ask_muscle_mass_q12":
            ' '.join('''  The main role of the arms in sprinting is to stabilize the torso and provide
             drive forward, especially in the start (Which is critical in 100/200m races).'''.split()),

        #        - List of muscles by volume in average man
        "ask_muscle_mass_q13":
            ' '.join('''    # Despite the erector spinae being 843cm^3 in one study, and possibly more, 
            I only found individual data on longissimus thoracis and 2 other of the 9 muscles involved.'''.split()),

        #     - Training your forearms with weights?
        "ask_muscle_mass_q14":
            ' '.join('''A good beginner routine to build a base for more advanced grip training:  
            http://www.davidhorne-gripmaster.com/basics.html    Since the program doesn't include 
            any pics/videos  here's a video  demonstrating the first two exercises, the two hands 
            pinch (you can use loose plates or make a pinch block but the idea is the same) 
            and barbell finger rolls.'''.split()),

        #        - How much muscle gain can be expected within 1 month of training on average (m/w) [closed]
        "ask_muscle_mass_q15":
            ' '.join('''If you are really strict with your diet (Bulking) you can expect to get like half
             a kilo of muscle per week after that.'''.split()),

        #     - Full body workout for strength with minimal size
        "ask_muscle_mass_q16":
            ' '.join('''If you have zero equipment and you do not want to buy any I suggest 
            that you accept that it is practically impossible to do bodyweight exercises and seriously 
            gain strength without gaining any muscle.'''.split()),

        #            - What are you views on progress between rep range vs. fixed reps?
        "ask_muscle_mass_q17":
            ' '.join('''The next week is for a transition, and the sets/reps are higher intensity but lower 
            volume. He saw good results with that (all this fits within the increasing work capacity 
            framework mind you),until he started stagnating and feeling beat up with that."'''.split()),

        #       - Is it okay to take a one week break from the gym after the first one and a half months of training?
        "ask_muscle_mass_q18":
            ' '.join('''Anecdotally, I'll take a week off every couple of months (by choice or chance),
             and if anything I get a bit more flexible and can get back into the weight room with
              less nagging inflammation.'''.split()),

        #             - Can I gain muscle mass doing push ups?
        "ask_muscle_mass_q19":
            ' '.join('''It definitely helps you gain muscle mass as long as you keep challenging 
            yourself and altering your workout to target different areas of your chest as well as to 
            prevent your body from adapting to the routine.'''.split()),

        #        - How to accurately measure muscle mass versus body fat?
        "ask_muscle_mass_q20":
            ' '.join(''' Intelamterix makes a product called  BodyMetrix  that can accurately 
            scan your body fat percentage and track your fat loss and muscle gain.
            The  software  itself tracks measurements and can generate reports.'''.split()),

        #         - How can I increase ab depth and size?
        "ask_muscle_mass_q21":
            ' '.join('''Because your abs will get a ton of work from squats and deadlifts.
            Personally, deadlifting heavy grew my obliques/lower abs/v(whatever that's called) more than anything else.
            Good luck man '''.split()),

        # -------------------------  muscle-mass qs end -----------------------------------
        # -------------------------  strength qs start -----------------------------------
        # What are the trade-offs of weight versus repetition?
        "ask_strength_q1":
            ' '.join('''Possible Goals: Training for strength, power, endurance and hypertrophy all require
             a different number of sets and reps, e.g.: Strength (how much weight your muscle can move) is best 
             developed by lifting as much weight as possible.'''.split()),

        "ask_strength_q2":
        # Is it normal when starting squats to not have flexible enough ankles?
            ' '.join('''When I started squatting, I had trouble with balance, hip mobility, and ankle mobility.
            I recommend warming the ankles up with lots of joint rotations (e.g. 20 in both directions) 
            and more squatting.'''.split()),

        "ask_strength_q3":
        # Are these Workout Routines right for Body Building?
            ' '.join('''Reg Park's program includes a lot of compound lifts (squats, deadlifts, dips, bench 
            and overhead presses), but also a good deal of bodybuilding-oriented accessory work (calves, wrists).'''.split()),

        "ask_strength_q4":
        # Why is muscle size not proportional to strength?
            ' '.join('''Two reasons why muscle mass and strength may not be completely congruous are:     
            1. Muscle fiber density, 2. Muscle utilization. Density: Your muscles are composed of four different 
            types of fibers (slow-twitch, and three forms of fast-twitch).'''.split()),

        "ask_strength_q5":
        # How does muscle size relate to strength?
            ' '.join('''Strength training will increase the size and quantity of myofibrils, 
            and subsequently increase the size of the respective muscle fibers; 
            this process is called  hypertrophy, and it results in larger and stronger muscles.'''.split()),

        "ask_strength_q6":
        # Should one generally avoid machines in favor of free weights?
            ' '.join('''The advantage with free weights, of course, is we're all built differently.
            #Testosterone production is not similarly increased by isolation free-weight exercises
             - or training on machines.'''.split()),

        "ask_strength_q7":
        # Do you need to “feel the burn” to become stronger?
            ' '.join('''Training for powerlifting (completely strength-oriented) involves avoiding failure, 
            keeping the number of reps low, and resting a lot between sets, none of which are really conducive 
            to "burn" during a workout or soreness afterwards.'''.split()),        
        
        "ask_strength_q8":
        # Where do I start when finding/creating a fitness program for myself?
            ' '.join('''Let me recommend a couple books to you, as they can help you a long way towards your goals:
            Starting Strength: Basic Barbell Training, Practical Programming for Strength Training. 
            Both of these are by Dr. Kilgore and Mark Rippetoe.'''.split()),    

        "ask_strength_q9":
        # Neural Adaptation Training vs. Hypertrophy Training?
            ' '.join('''By doing hypertrophy-type training, the neural output is fairly low (as compared to power training)
             and is not sufficient to simulate the motor neurons to "bud" 
             (increase the number of muscle fibers in the motor unit they innervate).'''.split()),   

        "ask_strength_q10":
        # Resuming workouts after 2 months. Any beginner workout suggestions?
            ' '.join('''My own rule of thumb for strength training is to start 2 months earlier - that is, in your example,  
            the break period - in the workout routines and to proceed from there with a 1-2 week reboot period.'''.split()),   
     
        "ask_strength_q11":
        # Why aren't stiff legged deadlifts bad for your back?
            ' '.join('''Despite its name, proper form in this exercise requires a slight bend of the knees and 
            when you bend down you need to be letting the middle of your body lean 
            backwards over your center of gravity.'''.split()),   

        "ask_strength_q12":
        # How can I increase the number of push-ups I can do?
            ' '.join('''The variations in resistance, targeting different muscle groups, and working towards a burn-out all 
            contributed to breaking the muscle down to the point where it would grow back stronger 
            during the recovery period.'''.split()),

        "ask_strength_q13":
        # Smoking and its effects on muscle building
            ' '.join('''In my experience, the most detrimental aspect of smoking while bodybuilding is the lack of energy.
            From a medical standpoint, probably the most detrimental aspect of smoking is lack of oxygen.'''.split()),
        
        "ask_strength_q14":
        # What's the time threshold for a drop in performance when taking a break from training?
            ' '.join('''In most strength programs, novices have a very quick recovery/supercompensation period--one to two days.
            Intermediate strength programming is generally designed around one week supercompensation periods.'''.split()),
        
        
        "ask_strength_q15":
        #            - Diet Plan for Building Lean Muscle
            ' '.join('''To ensure that you're getting the maximum muscle building benefits of protein, 
            you'll want to consume about 0.8 grams of protein per pound of body weight.'''.split()),

        "ask_strength_q16":
        # Upper and lower body proportion, gaining muscle losing fat
            ' '.join('''It may be the case, that there is actually quite little fat on your buttocks and legs, 
            but it just looks a lot because of lack of muscle.'''.split()),

        "ask_strength_q17":
        #            - How can the conventional deadlift be harder at the top than the bottom?
            ' '.join('''Answering your question showed me that at (or around) that point, 
            the quads become less dominant and the load is transferred to the hamstrings and glutes.'''.split()),

        "ask_strength_q18":
        #            - bodyweight leg exercises for strength/hypertrophy
            ' '.join('''Kettlebell Swings: You can make your own improvised Kettlebell to save money, 
            you should do these with pretty heavy weight if you want to build any size with these.
            Hindu Squats: are great for building lung power and and endurance.'''.split()),

        "ask_strength_q19":
        #            - How do I naturally boost my Testosterone levels?
            ' '.join('''Kraemer et al, 1991; Kraemer et al 1990: High volume, multiple set programs are  
            more effective at increasing the body's production of testosterone and growth hormone. 
            Soy increases estrogen, a female hormone, which lowers testosterone.'''.split()),

        "ask_strength_q20":
        #            - how to correct forward neck posture?
            ' '.join('''In addition to these neck exercises, you should consider adding some deadlifts
            to your routine to balance the muscles of the upper back.'''.split()),

        "ask_strength_q21":
        #            - The value of strength training vs. the time/effort it takes
            ' '.join('''1.To live long and with a high quality of life (includes cognitive benefits, 
            ability to use my body effectively long term, avoiding medical problems, etc.).
            The extra time for strength training is definitely worth it for all of your goals.'''.split()),

        "ask_strength_q22":
        #            - How can I increase the number of push-ups I can do?
            ' '.join('''The variations in resistance, targeting different muscle groups, and working towards 
            a burn-out all contributed to breaking the muscle down to the point where it 
            would grow back stronger during the recovery period.'''.split()),

        "ask_strength_q23":
        #            - Losing weight without losing muscle
            ' '.join('''You could increase the number of sets to keep volume constant, or you could just do three 
            very heavy sets of 3 and call it a day for your strength maintenance work.'''.split()),

        "ask_strength_q24":
        #            - Good form with little weight or bad form with a lot of weight?
            ' '.join('''It's possible that the people you watch have different goals than you, 
            like hypertrophy rather than strength, or bragging rights about the weight they curl 
            instead of actually improving their curl.'''.split()),

        - "ask_strength_q25":
        #            - How can I improve my vertical?
            ' '.join('''The focus is on an isolated jump, per the combine, but perhaps with some practice to drive 
            these techniques into muscle memory you could work them into real-world usage i.e. basketball.'''.split()),

        "ask_strength_q26":
        #            - Exercise for shoulders strength with no special equipment
            ' '.join('''Some videos I recently bookmarked: Best Bodyweight Shoulder Exercise 
            - shows that you can do pike push ups even with a cat in the way.'''.split()),

        "ask_strength_q27":
        #           - How to overcome grip strength as sticking point for deadlifts?
            ' '.join('''There are three main ways to grip the bar for deadlifts that are competition legal: 
            overhand (weakest), hook grip (rough on the thumbs), and mixed grip (one hand suppinated, strongest).'''.split()),

        "ask_strength_q28":
        #           - What is the simplest way to measure strength?
            ' '.join('''It tests strength with one-repetition maximum lifts in the squat, deadlift, and bench press.
            #The squat/bench/deadlift is well balanced for overall strength--though it omits a pulling motion - 
            but a one-repetition maximum in many lifts can test strength.'''.split()),

        "ask_strength_q29":
        #            - Can I increase flexibility by strengthening muscles?
            ' '.join('''You could check out the following link as a starting point: https://www.precisionmovement.coach/front-splits-mobility-technique/.
            I have gone from a very stiff left hip to a much more flexible and mobile state.'''.split()),

        "ask_strength_q30":
        #            - what's the reality that keeps progressive strength training from being constant?
            ' '.join('''All you need at that point is a different way to manage your training volume and intensity.
            The most assured way to build strength is to increase the volume of work.'''.split()),

        "ask_strength_q31":
        #                - How to exercise for kyphosis?
            ' '.join('''I recommend the olympic style front squat: http://www.exrx.net/WeightExercises/OlympicLifts/FrontSquat.html. 
            The front squat is the king of exercises for the thoracic spine. 
            It will give you perfect posture, and will get you strengthening and extending your upper back like nothing else.'''.split()),

        "ask_strength_q32":
        #            - How does one lift a heavy box up from the ground?
            ' '.join('''https://doi.org/10.1136/bmj.39463.418380.be. "There is no evidence to support use of advice 
            or training in working techniques with or without lifting equipment 
            for preventing back pain or consequent disability.'''.split()),

        "ask_strength_q33":
        #            - Full body workout for strength with minimal size
            ' '.join('''If you have zero equipment and you do not want to buy any I suggest that you
             accept that it is practically impossible to do bodyweight exercises and seriously gain 
             strength without gaining any muscle.'''.split()),

        "ask_strength_q34":
        #            - Which muscles would I need to train for ambulance work?
            ' '.join('''Look at all the different components to each task as you have described: 
            squatting, lifting, carrying, walking forwards and backwards, climbing up and down stairs 
            forwards and backwards, pushing, pulling, gripping etc.'''.split()),

        "ask_strength_q35":
        #            - What credibility or scientific backing does 1g protein per 1lb of body weight have for its applications?
            ' '.join('''A study examined nitrogen balance and lean body mass preservation related
             to protein intake, and found that when not training, bodybuilders needed little more than
              sedentary to maintain mass, while protein needs did increase during training, 
              and endurance athletes needed more than bodybuilders, being 1.12 x sedentary control 
              levels for bodybuilders, and 1.67 x sedentary control for endurance training.'''.split()),

        "ask_strength_q36":
        #            - How can I best recover for a second strength workout on the same day?
            ' '.join('''I'd focus on nailing my first post-workout meal and making sure I have 
            enough energy for the second workout. I'd try to eat a meal or snack about two hours 
            before the second workout.'''.split()),

        "ask_strength_q37":
        #            - Are multiple sets with decreasing weight and no rest between them a good idea?
            ' '.join('''This process of lifting a heavy weight several times, then immediately doing 
            the same exercise with lower weight for many reps, is called strip or drop sets. That's why 
            bodybuilders prefer drop sets - because they're decidedly geared towards 
            increasing muscle size (hypertrophy).'''.split()),

        "ask_strength_q38":
        #            - Does “Greasing the groove” work and if so why?
            ' '.join('''However, what Thibaudeau is probably describing is neural fatigue, 
            and this is why commentators (Bompa and others) recommend periodising strength training 
            to allow the nervous system time to recover.'''.split()),

        "ask_strength_q39":
        #            - To count or not to count?
            ' '.join('''If you could only do 10 pushups for years, then tried a new exercise and all 
            the sudden you can do 50 pushups, you might want to example that and see why there was a change. 
            For weight lifting, you don't want to do too many reps.'''.split()),

        "ask_strength_q40":
        #            - Do isometric exercises decrease flexibility?
            ' '.join('''I'll try to answer this another way, and state that full range of motion (ROM) 
            exercises do indeed increase flexibility. But provided you are stretching your body in other ways, 
            I believe the range of motion will stay.'''.split()),
        
        "ask_strength_q41":
        #            - Abdominal role in squats
            ' '.join('''Squats train all of the supporting muscles of the torso -- 
            including the anterior/abdominal muscles -- if you use a  Valsalva maneuver.'''.split()),

        "ask_strength_q42":
        #            - What is a low-impact exercise routine that slowly progresses towards more normal exercises?
            ' '.join('''You can get a good cardio workout, run in water, swim, stretch, do martial arts and 
            strengthen with water exercises. For example, if you strengthen your hip muscles they can lessen 
            the stress on your knee joints.'''.split()),

        "ask_strength_q43":
        #            - What are the target muscles of kettlebell swings
            ' '.join('''Performing a proper two-hand kettlebell swing is a whole-body workout as 
            opposed to isolating single muscles.'''.split()),

        "ask_strength_q44":
        #            - Are partial reps okay?
            ' '.join('''The pros of partial reps include the fact that you can carry on with an 
            exercise when you can no longer do full ROM with good form, and you still want to 
            push it a bit further to exert a smaller subset of the muscle group more.'''.split()),

        "ask_strength_q45":
        #            - why do we need more rest when lifting heavy?
            ' '.join('''They need a break to be ready for the next lifting.
            #In that break time, they undergo repair and get nourished and grow stronger.'''.split()),

        "ask_strength_q46":
        #            - Are the basic barbell lifts not enough for the “core”?
            ' '.join('''In most of the academic literature, the core is understood to be comprised 
            of three muscle groups: the  diaphragm  at the top, the  pelvic floor  complex at the 
            bottom, and the deep  multifidus  and superficial  transversus abdominis  in the middle.'''.split()),

        "ask_strength_q47":
        #            - Will calcium supplements affect my strength gain?
            ' '.join('''One of the side effects of higher protein content in your meals is that your 
            body can start leeching calcium from your bones.'''.split()),

        "ask_strength_q48":
        #            - Can I add in some core exercises to SL 5x5 and what do you suggest if so?
            ' '.join('''The squat, deadlift, and overhead press are all core exercises, and quite good ones.
            If you're not getting enough work now, you will soon, because you're adding weight each workout.'''.split()),

        - "ask_strength_q49":
        #            - Pinky finger movement affected by lifting weights?
            ' '.join('''It’s the result of an inflammation of the tendon that moves the finger.'''.split()),

        # -------------------------  strength qs end -----------------------------------


    }

    return qa_mem_db[question]
