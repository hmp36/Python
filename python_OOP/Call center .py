
class Call(object):
    def __init__(self, idnum, name, number, time, reason):
        self.idnum = idnum
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason

    def display(self):
        print "Call ID: {}".format(self.idnum)
        print "Caller name: {}".format(self.name)
        print "Phone number: {}".format(self.number)
        print "Time of call: {}".format(self.time)
        print "Reason for call: {}".format(self.reason)


class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.total_calls = 0

    def add_call(self, name, number, time, reason):
        self.total_calls += 1
        new_call = Call(self.total_calls, name, number, time, reason)
        self.calls.append(new_call)
        return self

    def end_call(self):
        del self.calls[:1]

    def info(self):
        for record in self.calls:
            print "Call ID: {}".format(record.idnum)
            print "Caller name: {}".format(record.name)
            print "Phone number: {}".format(record.number)
            print "Time of call: {}".format(record.time)
            print "Reason for call: {}".format(record.reason)
        print len(self.calls)

    def remove_call(self, query_number):
        for record in range(len(self.calls)):
            if self.calls[record].number == query_number:
                del self.calls[record]
                break
        return self

    def sort_calls(self):
        for val in range(len(self.calls)):
            end = len(self.calls) - 1
            while end > val:
                if self.calls[end].time > self.calls[val].time:
                    temp = self.calls[end]
                    self.calls[end] = self.calls[val]
                    self.calls[val] = temp
                end -= 1
        return self


center = CallCenter()
center.add_call("Gary", "444-4444", 1950, "He's a wuss").add_call("Naomi", "555-5555",
                                                                  1055, "Annual checkup").add_call("Octavian", "666-6666", 1659, "Lost a toe")
center.info()
# center.remove_call("555-5555").info()
center.sort_calls().info()
# center.info()


