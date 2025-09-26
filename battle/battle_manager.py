import random
import time


# 1. 전투 흐름:
# • 랜덤 모듈을 이용해서 전투의 선공(첫 번째 공격자)을 랜덤으로 결정한다.
# • 첫 번째 캐릭터가 공격
# • 두 번째 캐릭터가 살아있으면 반격
# • 한 캐릭터의 체력이 0이 되면 전투 종료
# • 타임 모듈을 이용해서, 전투 진행시 딜레이를 추가하여 더 자연스러운 전투를 연출한다.
# 2. 기본 공격 vs 특수 공격 선택:
# • 랜덤 모듈을 통해 70% 확률로 기본 공격, 30% 확률로 특수 공격 (예외 발생 가능)
# 3. 예외 처리
# • 마나 부족 시 공격 불가
class BattleManager:
    def __init__(self,char1,char2):
        self.char1=char1
        self.char2=char2
       
    def start_battle(self):
        
        print(f'전투 시작: {self.char1.get_name()} vs {self.char2.get_name()}')
        time.sleep(1)
        attacker, defender =(self.char1, self.char2) if random.random() <0.5 else (self.char2, self.char1)
        print(f'{attacker.get_name()}이(가) 먼저 공격합니다!\n')
        time.sleep(1)
        round_num=1
        while attacker.is_alive() and defender.is_alive():
            print(f'---라운드 {round_num} ---')
            attack_type="special" if random.random() <0.3 else "basic"
            
            try:
                if attack_type =="basic":
                    print(attacker.attack(defender))    
                else:
                    if hasattr(attacker,"power_strike"): #hasattr는 이 객체가 이 이름의 속성을 갖고 있는지
                        print(attacker.power_strike(defender))
                    elif hasattr(attacker,"fireball"):
                        print(attacker.fireball(defender))
                    elif hasattr(attacker, "ambush"):
                        print(attacker.ambush(defender))
                    else:
                        print(attacker.attack(defender))
            except getattr(attacker.__class__, "ManaError", Exception ) as e:
                print(f"마나 부족: {e}")
                print(attacker.attack(defender))
            except Exception as e:
                print(f"{attacker.get_name()}의 공격이 실패했습니다: {e}")

            time.sleep(1)

            if defender.is_alive():
                attacker,defender=defender, attacker
                round_num+=1
            else:
                print(f"\n{defender.get_name()}이(가) 패배했습니다.")
                print(f"\n{attacker.get_name()}이(가) 승리했습니다.")
                break
        return attacker if attacker.is_alive() else defender



