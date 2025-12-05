class StringDeterminer:
    vowels = 'aeiou'
    forbidden_substrings = ['ab', 'cd', 'pq', 'xy']

    def is_nice_day_1(self, text):
        is_nice = True

        if sum(1 for char in text if char in self.vowels) < 3:
            is_nice = False

        if any(sub in text for sub in self.forbidden_substrings):
            is_nice = False

        if not any(text[i] == text[i + 1] for i in range(len(text) - 1)):
            is_nice = False

        return is_nice
    
    def is_nice_day_2(self, text):
        is_nice = True

        if not self._has_repeated_pair(text):
            is_nice = False

        if not self._has_sandwiched_letter(text):
            is_nice = False

        return is_nice
    
    def _has_repeated_pair(self, text):
        pairs = {}
        for i in range(len(text) - 1):
            pair = text[i:i + 2]
            if pair in pairs:
                if i - pairs[pair] > 1:
                    return True
            else:
                pairs[pair] = i
        return False
    
    def _has_sandwiched_letter(self, text):
        for i in range(len(text) - 2):
            if text[i] == text[i + 2]:
                return True
        return False