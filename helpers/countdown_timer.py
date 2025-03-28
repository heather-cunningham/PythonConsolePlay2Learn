import threading
import time


## BEGIN
class CountdownTimer():
    """ A countdown clock or timer """
    

    def __init__(self, seconds=60, running=False):
        """ Creates countdown clock or timer 

        Keyword arguments: `seconds` (int) - The number of seconds form which the clock should count down.
                                            Defaults to 60.
                            `running` (bool) - Whether the timer is running or not. Defaults to False.
        """
        self.seconds = seconds
        self.running = running
        self._thread = None
        return


    @property
    def seconds(self):
        return self._seconds


    @seconds.setter
    def seconds(self, seconds):
        self._seconds = seconds
        return


    @property
    def running(self):
        return self._running


    @running.setter
    def running(self, running):
        self._running = running
        return


    def _run_timer(self):
        while (self.seconds >= 0 and self.running):
            time.sleep(1)
            self.seconds -= 1   
        return


    def start_timer(self):
        if(not self.running):
            self.running = True
            self._thread = threading.Thread(target=self._run_timer)
            self._thread.start()
        return


    def stop_timer(self):
        if(self.running and self._thread is not None):
            self.running = False
            self._thread.join()
        return


    def reset_timer(self, seconds=60):
        self.stop_timer()
        self.seconds = seconds
        return
## END Class


def main():
    timer = CountdownTimer(3)
    timer.start_timer()
    while(timer.running and timer.seconds >= 0):
        print("Time left:", timer.seconds)
    else:
        timer.stop_timer()
        print("Time's up!!!")


if(__name__ == "__main__"):
    main()
            