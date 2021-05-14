def determineWordCount(str):
    if(" " not in str):
        return "Not a valid sentence"
    counter = 0
    for x in range(0, int(len(str))):
        if(str[x] == ' '):
            counter+=1
    return counter+1
