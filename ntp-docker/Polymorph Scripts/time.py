def time(packet):
        try:
            if packet["UDP"]["srcport"]==123:
                packet["NTP"]["xmt"]=b'hola'.hex()
                return  packet
        except:
            return None


