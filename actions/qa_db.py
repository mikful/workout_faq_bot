def question_answer_pair(question: str) -> str:
    qa_mem_db = {
        # What is the best exercise agains belly fat ?
        "fitness_q1": """ There is no 'best' exercise to lose belly fat.
                        For many people, cutting out most of the sugar in 
                        their diet (obviously not sugar from fruit and other 
                        healthy sources) is an excellent way to lose the weight.""",
        # Optimal exercises for an abdominal workout
        "fitness_q2": ' '.join('''The crunch flexes the trunk and primarily targets the 
                                rectus abdominis, not the transversus abdominis or 
                                the obliques.'''.split()),
        # How old should children be to train with weights?
        "fitness_q3": """ Taking Eric and Dave's answers into consideration, we must understand 
                        that children's bodies are still developing. I believe a structured lifting program 
                        for children can be a fantastic introduction to controlled multiplanar movement."""
    }

    return qa_mem_db[question]
