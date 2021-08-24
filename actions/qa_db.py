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
    }

    return qa_mem_db[question]
