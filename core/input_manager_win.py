from algorithms import DesignPattern

class PygameButton(DesignPattern.SingletonInstance):
    """
    Get user-input by pygame
    """
    def __init__(self):
        import pygame
        self._pygame = pygame

    def get_button_state(self, button=None):
        """
        Get button state(up, left, right, down, etc...) by pygame
        """
        keystate = self._pygame.key.get_pressed()

        is_right = keystate[self._pygame.K_RIGHT]
        is_left = keystate[self._pygame.K_LEFT]
        is_jump = keystate[self._pygame.K_UP] or keystate[self._pygame.K_SPACE]
        is_setup = keystate[self._pygame.K_LCTRL]

        buttonstate = dict(right=is_right, left=is_left, jump=is_jump, setup=is_setup)

        if button == None:
            return buttonstate
        elif button in buttonstate.keys():
            return buttonstate[button]
        else:
            return None
        
def Keyboard(keyboard_type=1):
    """
    keyboard_type 1: curse keyboard
    keyboard_type 2: system keyboard
    keyboard_type 3: GPIO Buttons
    """
    if keyboard_type == 1:
        return PygameButton.instance()