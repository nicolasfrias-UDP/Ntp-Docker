def stratum (packet):
    try:
        if packet["UDP"]["srcport"]==123:
             packet["NTP"]["stratum"]=1
            return packet
    except:
        return None
