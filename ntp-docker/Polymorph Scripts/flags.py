def flags(packet):

    try:
        if packet["UDP"]["srcport"]==123:
            packet["NTP"]["flags"]='0x1b'
            return  packet
    except:
        return None

