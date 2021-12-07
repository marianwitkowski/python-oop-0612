"""
 Dataclasses
"""
from dataclasses import dataclass, field
from enum import Enum

class Organization(Enum):
    UEFA = 1
    FIFA = 2

@dataclass(frozen=False, order=True)
class FootballTeam:
    sort_index : int = field(init=False, repr=False, compare=False) #nazwa wbudowana sort_index
    country: str
    continent: str = field(repr=False)
    rank: int = field(compare=False)
    federation: Organization = field(repr=True, compare=False)
    players: list = field(repr=True, compare=False)
    word_champion: bool = field(default=False, repr=False, compare=False)

    custom_field : int = field(init=False, repr=True, compare=False)

    def __post_init__(self):
        self.sort_index = -1*self.rank # ustawienie indeksu
        if self.players is None:
            self.players = []
        self.custom_field = -1

####################################################
ft1 = FootballTeam("Poland","Europe",88, Organization.UEFA ,None)
print(ft1)
# for k,v in ft1.__dict__.items():
#     print(f"{k}={v}")

ft2 = FootballTeam(continent="Europe", country="Germany",
                   players=["Muller"], rank=5, word_champion=True,
                   federation=Organization.UEFA)
ft2.custom_field = 2
print(ft2)

ft3 = FootballTeam(continent="Europe", country="France",
                   players=["Mbappe"], rank=3, word_champion=True,
                   federation=None)
ft3.custom_field = 22
print(ft3)

#print(ft2 == ft3)
items = [ft3, ft1, ft2]
print(sorted(items))
