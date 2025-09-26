import random
from characters.character import Character
class Rogue(Character):
    def __init__(self, name, level, health, attack_power):
        super().__init__(name, level, health, attack_power)
        self.max_health = 90
        self.attack_power = 12

    def attack(self, target):
        damage = self.attack_power
        target.take_damage(damage)
        return f'{self.name}이(가) 공격했습니다 데미지:{damage}'

    def ambush(self, target):
        """ambush: 랜덤 모듈을 이용해서 70% 확률로 3배 데미지를 입힘 (랜덤 확률 시스템 활용)
• 실패 시 공격하지 않음"""
        chance = random.random()
        if chance <= 0.7:
            damage = self.attack_power*3
            target.take_damage(damage)
            return f'{self.name}이(가) ambush에 성공했습니다. {target.get_name()}에게 {damage}의 피해를 주었습니다'
        else:
            return f'{self.name}의 ambush에 실패했습니다.'
        
    def special_attack(self, target):
        return self.ambush(target)