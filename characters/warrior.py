from characters.character import Character
class Warrior(Character):
    def __init__(self, name, level, health, attack_power):
        super().__init__(name, level, health, attack_power)
        self.max_health = 100
        self.attack_power = 15

    def attack(self, target):
        damage = self.attack_power
        target.take_damage(damage)
        return f'{self.name}이(가) 공격했습니다 데미지:{damage}'

    def power_strike(self, target):
        damage = 2*self.attack_power
        self.health -= 5
        target.take_damage(damage)
        return f'{self.name}이(가) powerstrike를 사용했습니다! {target.get_name()}에게 {damage}의 피해를 주고 본인 체력 5 감소'
    def special_attack(self, target):
        return self.power_strike(target)
    
