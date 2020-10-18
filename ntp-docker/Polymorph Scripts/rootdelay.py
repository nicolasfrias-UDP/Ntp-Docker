def rootdelay(packet):
        try:
            if packet["UDP"]["srcport"]==123:
                packet["NTP"]["rootdelay"]=10000000
                return  packet
        except:
            return None
