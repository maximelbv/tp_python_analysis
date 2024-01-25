from data import centersPopulations, centers

def sameInterest():
    sameInterest = []
    for c in centers:
        if c[1] not in [interest["interest"] for interest in sameInterest]:
            sameInterest.append({"interest": c[1], "users": []})

    
    for interest in sameInterest:
        for center in centers:
            if interest["interest"] == center[1]:
                interest["users"].append(center[0])
    print(sameInterest)

sameInterest()