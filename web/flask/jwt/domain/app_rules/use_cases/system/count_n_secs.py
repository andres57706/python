class CountNSecods(object):
    """
    Count N Seconds use case
    """

    def __init__(self, sleep):
        self._sleep = sleep

    def execute(self, seconds: float = 10):
        """
        execute use case count to n seconds

        Parameters:
            seconds [seconds]: seconds to count
        """
        c = 0
        while c < seconds:
            self._sleep(1)
            c += 1
            print(f'{seconds - c} remainig')
        print(f'seconds elapsed: {seconds}')
