import random

class Hero:
    "This will be the total hero class"

    #Example or generation: Alastricus=Hero()
    def __init__(self,myRace,myClass):
        self.myRace=myRace
        self.myClass=myClass
    
    #def attack():

class CharacterRace:
    "This will be the superclass of all classes of races"

class Human(CharacterRace):
    "Humans are ..."

class CaveHuman(Human):
    """
    Cave humans are humans that have ventured and habited into caves over millenia. 
    Their day-night cycle is absent, however since they aren't too far removed yet from surface-dwelling humans, the effect can still be called forward by confining to a day-night-
    structure of sleep. The natural absence makes cave humans well-fit for keeping sharp guard at night. 
    Cave humans have bad eyesight adapted to seeing at most shapes in the dark. In light, their eyes will slowly adjust, but still aren't that functional. Their skin is pale and weak
    against direct sunlight, which will cause it to flake and hurt after even short amounts of time (hours). 
    """

class GreaterHuman(Human):
    """
    Greater human is a name this subrace has given itself. Most other races find them foolish for their narcissism, and other human subraces tend to, if at all, get along very
    harshly with them. A name most other races use for greater humans is the 'Seil', after the place where their development began to take shape: Seilith.
    The Seil are an aggressive people. Their economy is largely based on mass production of everything. Most other (sub)races are afraid to start any conflict with them, as the Seil
    fight viciously and furiously, and take any opportunity to start a war. 
    """

class CentralHuman(Human):
    """
    The central humans are a subrace of humans both wise and intelligent. They tend to be at the centre of almost all unified human action, but even they have trouble with the Seil.
    Central humans 
    """

class Dwarf(CharacterRace):
    "Dwarves are sturdy, "

class MountainDwarf(Dwarf):
    "Mountain dwarves are ..."

class LowDwarf(Dwarf):
    "Low dwarves are from flat, low ground"

class Elf(CharacterRace):
    "Elves are ..."

class ForestElf(Elf):
    "Forest elves are ... [inclined to druidry]"

class ArcaneElf(Elf):
    "Forest elves are ... [inclined to magic general]"

class AquaticElf(Elf):
    """
    Aquatic elves live under water. They can breathe water perfectly and air reasonably. When not in rest on land, they tend to use spells to breathe above water. 
    They are inclined to aquatic spellcasting, but also have affinities for ...
    """

class CharacterClass:
    "This will be the superclass of all classes of classes characters can have"

class Barbarian(CharacterClass):
    "Barbarians are ..."

class Wizard(CharacterClass):
    "Wizards are ..."

class Thief(CharacterClass):
    "Thieves are ..."

class Healer(CharacterClass):
    "Healers are a support class that can do many things, a most prominent of that restoring ally health"

class Tinkerer(CharacterClass):
    "Tinkerers are characters that are quite exclusive from other systems. The tinkerer can help upgrade team gear, set up quick barricades, and invent (unlock) new items"

class Alchemist(Tinkerer):
    "Alchemists ..."