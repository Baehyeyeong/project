from characters.character import Character
class Mage(Character):
    class ManaError(Exception):
        pass

    def __init__(self, name, level, health, attack_power):
        super().__init__(name, level, health, attack_power)
        self.max_health = 80
        self.attack_power = 18
        self.mana = 100

    def attack(self, target):
        damage = self.attack_power
        target.take_damage(damage)
        return f'{self.name}이(가) 공격했습니다 데미지:{damage}'

    def fireball(self, target):
        """파이어볼: 마나 20 소모, 1.5배 공격력"""
        if self.mana < 20:
            raise Mage.ManaError(f'{self.name}의 마나가 부족합니다. 현재 마나:{self.mana}')
        damage = 1.5*self.attack_power
        self.mana -= 20
        target.take_damage(damage)
        return f'{self.name}이(가) fireball을 사용했습니다! {target.get_name()}에게 {damage}의 피해를 주고 마나 20 감소'

    def special_attack(self, target):
        return self.fireball(target)