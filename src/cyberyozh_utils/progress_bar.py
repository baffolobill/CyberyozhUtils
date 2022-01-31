# progress_bar.py
#
# For printing iterations progress in a ternimal
class ProgressBar:
    """
    Create command-line-style ProgressBar
    """
    def __init__(self, total, prefix='', suffix='', length=100, fill='*'):
        """
        Init ProgressBar
        Start position is always 0, end position is total.
        Usage example:
        progress_bar = ProgressBar(0, l, prefix='Progress:', suffix='Complete', length=50)
        while some():
            progress_bar.iterate(i + 1)
        :param total: Required, total iterations (Int)
        :param prefix: Optional, prefix string (Str)
        :param suffix: Optional, suffix string (Str)
        :param length: Optional, character length of bar (Int)
        :param fill: Optional, bar fill character (Str)
        """
        self.counter = 0
        self.prev_counter = 0
        self.total = total
        self.percent_size = total/100
        self.prefix = prefix
        self.suffix = suffix
        self.length = length
        self.fill = fill

    def iterate(self, iteration):
        """
        Call in a loop to create terminal progress bar
        @param: iteration: Required, current iteration (Int)
        """
        self.prev_counter = int(iteration/self.percent_size)
        filled_length = int((self.prev_counter/100) * self.length)
        bar = self.fill * filled_length + '-' * (self.length - filled_length)
        if self.prev_counter != self.counter:
            print('\r%s |%s| %s%% %s' % (self.prefix, bar, self.prev_counter, self.suffix), end='\r')
        self.counter = self.prev_counter
        # Print New Line on Complete
        if iteration == self.total:
            print()
