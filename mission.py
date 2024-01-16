class Mission:
    def __init__(self, name, date, device_type, device_status):
        self.name=name
        self.date=date
        self.device_type=device_type
        self.device_status=device_status


    def getHash(self):
        return hash(self)
        

        

