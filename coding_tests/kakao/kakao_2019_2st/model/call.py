class Call:
    def __init__(self, res_calls):  # id, ts, st, end
        self.calls = sorted([list(calls.values()) + [True] for calls in res_calls], key=lambda e: (e[2], e[3]))
        self.separate_calls()

    def __repr__(self):
        return f'{[[call[0], call[2]] for call in self.calls]}'

    def separate_calls(self):
        self.up_calls = []
        self.down_calls = []
        for call in self.calls:
            if call[2] < call[3]: self.up_calls.append(call)
            else: self.down_calls.append(call)

    def get_calls_by_floor(self, floor):
        return [call for call in self.calls if call[-1] and call[2] == floor]

    def upcalls_more_than_downcalls(self, floor):
        up = [call for call in self.calls if call[-1] and call[2] > floor]
        down = [call for call in self.calls if call[-1] and call[2] < floor]
        if len(up) == len(down) == 0: return 0
        return 1 if len(up) >= len(down) else -1

    def upcalls_more_than_downcalls_by_floor(self, floor):
        up = [call for call in self.up_calls if call[-1] and call[2] > floor]
        down = [call for call in self.down_calls if call[-1] and call[2] < floor]
        if len(up) == len(down) == 0: return 0
        return 1 if len(up) >= len(down) else -1

    def remove_calls(self, ids):
        for i in range(len(self.calls)):
            if self.calls[i][0] in ids: self.calls[i][-1] = False
        for i in range(len(self.up_calls)):
            if self.up_calls[i][0] in ids: self.up_calls[i][-1] = False
        for i in range(len(self.down_calls)):
            if self.down_calls[i][0] in ids: self.down_calls[i][-1] = False