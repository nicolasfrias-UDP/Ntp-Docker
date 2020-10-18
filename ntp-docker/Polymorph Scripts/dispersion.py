def rootdispersion(packet):
    try:
        if packet["UDP"]["srcport"]==123:
            packet["NTP"]["rootdispersion"]=1000000000
            return packet
    except:
        return None
