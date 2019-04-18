class wwb:
    def __init__(self,data):
        self.lenth = 0
        for i in range(len(data)):
            if i == 0:
                self.start_date = data[i]['time']
            elif i == (len(data) - 1):
                self.end_date = data[i]['time']

            self.lenth += 1