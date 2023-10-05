from pynput import keyboard

cKeyboard = keyboard.Controller()

keys = ({
    "<": "⇒",
    "+": "±",
    "0": "⁰",
    "1": "⇔",
    "2": "²",
    "3": "³",
    "a": "α",
    "b": "β",
    "d": "Δ",
    "o": "Ø",
    "i": "∞",
    "p": "π",
    "r": "ℝ",
    "4": "√",
    "s": "Σ",
    "v": "∀",
    "-": "⁻",
    "w": "∄",
    "e": "∃",
    "{": "∈",
    "}": "∉",
    "´": "∴",

})


parsed_keybandings = ({})

class KeyBinding:

    def __init__(self,activation_character,result):
        self.activation_character = activation_character
        self.result = result
        self.parsedKeyBinding = f'<ctrl>+<alt>+<shift>+{activation_character}'
    
    def handlePress(self):
        cKeyboard.type(self.result)
        pass



for activation_key in keys:
    kb = KeyBinding(activation_key,keys[activation_key])
    parsed_keybandings[kb.parsedKeyBinding] = kb.handlePress

with keyboard.GlobalHotKeys(parsed_keybandings) as h:
    h.join()
