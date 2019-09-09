from algorithms import DesignPattern

class SysKeyboard(DesignPattern.SingletonInstance):
    def __init__(self):
        import termios, os, sys, fcntl
	
        self.fd = sys.stdin.fileno()
        # save old state
        self.flags_save = fcntl.fcntl(self.fd, fcntl.F_GETFL)
        self.attrs_save = termios.tcgetattr(self.fd)
        # make raw - the way to do this comes from the termios(3) man page.
        attrs = list(self.attrs_save) # copy the stored version to update
        # iflag
        attrs[0] &= ~(termios.IGNBRK | termios.BRKINT | termios.PARMRK
                | termios.ISTRIP | termios.INLCR | termios. IGNCR
                | termios.ICRNL | termios.IXON )
        # oflag
        attrs[1] &= ~termios.OPOST
        # cflag
        attrs[2] &= ~(termios.CSIZE | termios. PARENB)
        attrs[2] |= termios.CS8
        # lflag
        attrs[3] &= ~(termios.ECHONL | termios.ECHO | termios.ICANON 
                | termios.ISIG | termios.IEXTEN)
        termios.tcsetattr(self.fd, termios.TCSANOW, attrs)
        # turn off non-blocking
        fcntl.fcntl(self.fd, fcntl.F_SETFL, self.flags_save & ~os.O_NONBLOCK)
        
    def get(self):
        import sys

        try:
            return ord(sys.stdin.read())
        except KeyboardInterrupt:
            return 0

    def getToChr(self):
        import sys

        return sys.stdin.read()

    def close(self):
        import termios, fcntl

        termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.attrs_save)
        fcntl.fcntl(self.fd, fcntl.F_SETFL, self.flags_save)

    def __del__(self):
        try:
            self.close()
        except:
            pass
	
    
    """
    def __call__(self, keyboard_type):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            if keyboard_type == 1:
                ch = sys.stdin.read(1)
            elif keyboard_type == 2:
                ch = sys.stdin.read(3)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    """

    """
    def get(self, keyboard_type):
        
    """
        # arrow_type 1 : for ASDF (common type)
        # arrow_type 2 : for Arrow key

    """
        inkey = self
        result = []
        
        print("Asdf")
        k = inkey(keyboard_type)
        
        if keyboard_type == 1:
            result.append(k)
        
        elif keyboard_type == 2:
            if k=='\x1b[A':
                result.append("up")
            
            if k=='\x1b[B':
                result.append("down")
            
            if k=='\x1b[C':
                result.append("right")
            
            if k=='\x1b[D':
                result.append("left")
        
        return result
    """

class CurseKeyboard(DesignPattern.SingletonInstance):
    def __init__(self):
        import curses

        self.screen = curses.initscr()

        curses.noecho()
        curses.cbreak()
        self.screen.nodelay(True)
        self.screen.keypad(True)
        self.button_id = ['d', 'a', 'w', 'q']

    def get(self):
        return self.screen.getch()

    def getToChr(self):
        char = self.screen.getch()

        if char > -1:
            return chr(char)
        else:
            return ""
        
    def get_button_state(self, button=None):
        b = self.getToChr()

        isRight = (b == self.button_id[0])
        isLeft = (b == self.button_id[1])
        isJump = (b == self.button_id[2])
        isSetup = (b == self.button_id[3])

        buttonState = dict(right = isRight, left = isLeft, jump = isJump, setup = isSetup)

        if button == None:
            return buttonState
        elif button in buttonState.keys():
            return buttonState[button]
        else:
            return None

    def close(self):
        import curses

        curses.nocbreak()
        self.screen.keypad(0)
        curses.echo()
        curses.endwin()

    def __del__(self):
        try:
            self.close()
        except:
            pass


class GPIOButton(DesignPattern.SingletonInstance):
    def __init__(self):
        import RPi.GPIO as GPIO
        
        GPIO.setmode(GPIO.BCM)

        # GPIO.BCM
        self.rightButton = 17
        self.leftButton = 22
        self.jumpButton = 27
        self.setupButton = 4

        self.buttonPins = [self.rightButton, self.leftButton, self.jumpButton, self.setupButton]
        
        for i in self.buttonPins:
            GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def get_button_state(self, button=None):
        import RPi.GPIO as GPIO

        isRight = not GPIO.input(self.rightButton)
        isLeft = not GPIO.input(self.leftButton)
        isJump = not GPIO.input(self.jumpButton)
        isSetup = not GPIO.input(self.setupButton)

        buttonState = dict(right = isRight, left = isLeft, jump = isJump, setup = isSetup)

        if button == None:
            return buttonState
        elif button in buttonState.keys():
            return buttonState[button]
        else:
            return None


def Keyboard(keyboard_type=3):
    """
    keyboard_type 1: curse keyboard
    keyboard_type 2: system keyboard
    keyboard_type 3: GPIO Buttons
    """
    if keyboard_type == 1:
        return CurseKeyboard.instance()

    elif keyboard_type == 2:
        return SysKeyboard.instance()

    elif keyboard_type == 3:
        return GPIOButton.instance()

def main():
    keyboard = Keyboard()
    
    t = 0
    while True:
        char = keyboard.getToChr()
        if char == 'q':
            break
        elif char != '':
            keyboard.screen.addstr(t, 0, char)
            t += 1
        
if __name__=='__main__':
    main()
