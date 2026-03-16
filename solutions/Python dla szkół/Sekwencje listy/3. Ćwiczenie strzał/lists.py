def saveScore( scores, hit ):
    scores[hit - 1] += 1
    return scores