def mid( input ):
    if ( (len(input) % 2) != 0):
        middleNumber = int((len(input) / 2))
        return input[middleNumber]
    else:
        return ""