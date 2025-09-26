import random
from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, name, level, health, attack_power):
        self.name = name
        self.level = level
        self.max_health = health
        self.health = health
        self.attack_power = attack_power

    @abstractmethod
    def attack(self, target):
        pass

    @abstractmethod
    def special_attack(self, target):
        pass

    def take_damage(self, damage):
        """피해를 입으면 체력이 감소"""
        self.health -= damage
        if self.health < 0:
            self.health = 0
        return f'{self.name}이(가) {damage}의 피해를 입었습니다. 현재체력:{self.health}'

    def is_alive(self):
        """ 체력이 0 이하이면 false 반환"""
        return self.health >0

    def show_status(self):
        """캐릭터 정보를 출력"""
        return f'캐릭터 이름:{self.name}, 캐릭터 레벨:{self.level},체력:{self.health}/{self.max_health}, 공격력:{self.attack_power}'

    def reset_health(self):
        """캐릭터의 체력을 초기화"""
        self.health = self.max_health
        return f'{self.name}의 체력이 {self.max_health}로 회복되었습니다.'

    def get_name(self):
        """캐릭터의 이름을 가져옴"""
        return self.name






