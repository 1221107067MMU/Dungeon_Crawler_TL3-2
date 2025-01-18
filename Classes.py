


class character:
    def __init__(self, name: str, ATK: int, HP: int, MAGIC: int):
        self.name = name
        self.HP = HP
        self.MAXHP = HP
        self.ATK = ATK
        self.MAGIC = MAGIC
    
    def attack(self, target) -> None:
        target.HP -= self.ATK
        target.HP = max(target.HP, 0)

    def heal(self, target) -> None:
        target.HP += self.MAGIC
        target.HP = min(target.HP, target.MAXHP)

class player(character):
    def __init__(self,
                name = str,
                ATK = int,
                HP= int,
                MAGIC= int) -> None:
        super().__init__(name=name, ATK=ATK, HP= HP, MAGIC=MAGIC)

class goblin(character):
    def __init__(self,
                name =str,
                ATK= int,
                HP= int,
                MAGIC= int) -> None:
        super().__init__(name=name, ATK=ATK, HP= HP, MAGIC=MAGIC)

class wolf(character):
    def __init__(self,
                name =str,
                ATK= int,
                HP= int,
                MAGIC= int) -> None:
        super().__init__(name=name, ATK=ATK, HP= HP, MAGIC=MAGIC)

class bandit(character):
    def __init__(self,
                name =str,
                ATK= int,
                HP= int,
                MAGIC= int) -> None:
        super().__init__(name=name, ATK=ATK, HP= HP, MAGIC=MAGIC)


#sources:
# https://www.youtube.com/watch?v=cM_ocyOrs_k&t=677s