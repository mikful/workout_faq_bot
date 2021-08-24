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
            ' '.join('''  # If you're just playing amateur level sports, and make it your goal to have a massive vertical jump,
     you'll more than make up for your lack of height.'''.split()),

        #     - Can weight lost be sustained through exercise influenced metabolism changes?
        "ask_metabol_q2":
            ' '.join('''  # So now we've got people who've lost fat as well as useful lean body mass, have a lowered metabolic 
    rate and are then released from their harsh crash diet.'''.split()),

        #     - Is it true that you can eat anything you want within 15 minutes of working out without putting on weight?
        "ask_metabol_q3":
            ' '.join('''  # Your body will process the food that you ingest, and if the caloric intake of the food is greater 
    than the amount of calories burned during the ensuing exercise, you will gain weight.'''.split()),

        #           - Does working a diverse set of muscles increase metabolism?
        "ask_metabol_q4":
            ' '.join('''    # Anaerobic workouts are basically intense workouts that push your body beyond the ability 
    to provide energy just through normal aerobic metabolism.'''.split()),

        # - How does one train for sports when the three metabolic pathways interact?
        "ask_metabol_q5":
            ' '.join('''  # The oxidative pathways run fairly continuously to maintain life and replenish tissues 
    that have made use of anaerobic energy conversion.'''.split()),

        #     - Does exercise REALLY increase the basal metabolism rate for any significant length of time after the exercise is over?
        "ask_metabol_q6":
            ' '.join('''  # In this study :  http://www.mendeley.com/research/postexercise-energy-expenditure-response-acute-aerobic-resistive-exercise/  
    they used 90 minute, high intensity strength workouts, and still after 15 hours, the metabolic rate was elevated.'''.split()),

        #     - How much cardio is advisable for an overweight person who is new to bodybuilding?
        "ask_metabol_q7":
            ' '.join('''    # Vice versa, with higher peaks and stronger contractions you will get a glycolitic type of 
    muscle; and this type of muscle is the one you want to get if you are trying to aim at power/strenght 
    sports and/or hypertrophy ( composed mostly of IIa and IIx fibers ).'''.split()),

        #         - Naturally increasing my Metabolism
        "ask_metabol_q8":
            ' '.join('''        # Eating large portions spaced far apart will make the body believe there is a "famine" 
    and will store the food as fat to prepare for hard times.'''.split()),

        #         - What is the best way to bring one's metabolism out of starvation mode following a diet?
        "ask_metabol_q9":
            ' '.join('''        # Progress can be measured by trying to determine her basal temperature; it's probably 
    quite low now (almost nobody on the planet actually has a 98.6 deg.'''.split()),

        #         - why do we need more rest when lifting heavy?
        "ask_metabol_q10":
            ' '.join('''      # "They need a break to be ready for the next lifting. In that break time, they undergo 
    repair and get nourished and grow stronger."'''.split()),

        # ------------------------- ends metabolism questions --------------------------

        # ------------------------- start weight-gain -----------------------------------

        #         - How can I gain weight and muscle weight?
        "ask_weight_gain_q1":
            ' '.join('''    # If you want upper-body mass you need to do activities that engage
             and exercise those muscle groups.'''.split()),

        #         - Can weight lost be sustained through exercise influenced metabolism changes?
        "ask_weight_gain_q2":
            ' '.join('''    # So now we've got people who've lost fat as well as useful lean body 
            mass, have a lowered metabolic rate and are then released from their harsh crash diet.'''.split()),

        #         - Is it true that you can eat anything you want within 15 minutes of working out without putting on weight?
        "ask_weight_gain_q3":
            ' '.join('''   # Your body will process the food that you ingest,
             and if the caloric intake of the food is greater than the amount of calories 
             burned during the ensuing exercise, you will gain weight.'''.split()),

        #              - Weight gained using GOMAD strategy
        "ask_weight_gain_q4":
            ' '.join('''      # If you lift heavy three times a week and do GOMAD, 
            a little less than half of the weight you gain will be fat.'''.split()),

        #  - How to gain weight for a naturally thin person?
        "ask_weight_gain_q5":
            ' '.join(''' "My general suggestion for people are new to exercise is to start with aiming for balance of their intake of carbs and protein.
      #How many calories depends a lot on your weight/height/age."'''.split()),

        #         - Mom Losing Her Mobility Because of her Weight Gain
        "ask_weight_gain_q6":
            ' '.join('''    # She's very likely a clear candidate for  weight loss surgery , and a physician 
            friend of mine has told me of cases of extreme obesity (which your mother has) where removing the 
            weight needs to be carefully tracked.'''.split()),

        #        - Milk+honey helps gain weight?
        "ask_weight_gain_q7":
            ' '.join('''# It might help you gain weight, but you would have to drink a lot of it.
      #You're in a position where you have the opportunity to eat lots of nutritious foods which 
      # will benefit more then you know but you've chosen milk and honey.'''.split()),

        #          - Gaining weight without gaining fat
        "ask_weight_gain_q8":
            ' '.join('''        # I'm not saying be a body builder, but you want to increase your lean mass to keep 
            your body fat low as you gain weight.
            # At least 1g of protein per pound of lean body mass while you want to gain muscle.'''.split()),

        # -------------------------  weight-gain questions end ------------------------------

        # -------------------------  reduce body-fat qs start -----------------------------------

    }

    return qa_mem_db[question]
