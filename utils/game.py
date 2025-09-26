# 1. 캐릭터 선택 함수 구현: choose_character(prompt)
# 1) 사용자가 자신의 캐릭터 선택
# 2) 사용자가 상대 캐릭터 선택
# ※ while문 이용
# 2. BattleManger클래스의 start_battle로 전투 실행
# 3. 플레이어가 승리하면 새로운 적을 선택하여 전투 진행 가능 (y/n 입력으로 선택 가능)
# ※ while문 이용
# 4. 패배 시 게임 종료

from characters.mage import Mage
from characters.warrior import Warrior
from characters.rogue import Rogue
from battle.battle_manager import BattleManager
def choose_character(prompt,characters):
    while True:
        print(prompt)
        for i,char in enumerate(characters, start=1): #enumerate 리스트를 순회하면서 인덱스와 값을 동시에 가져옴
            print(f"{i}. {char.show_status()}")
        choice= input("번호를 선택하세요:")
        if choice.isdigit() and 1<=int(choice) <= len(characters):# isdigit() choice에 숫자로만 이루어져있는지
            return characters[int(choice)-1]
        print("잘못된 선택입니다. 다시 입력해주세요\n")
def game_loop():
    
    characters=[
        Warrior("세트",5,100,15),
        Mage("유미", 5, 80, 18),
        Rogue("카이로", 5, 90, 12)

    ]
    while True:
        player=choose_character("플레이어 캐릭터를 선택하세요:", characters)
        opponent=choose_character("상대 캐릭터를 선택하세요:",[c for c in characters if c !=player])
        
        battle= BattleManager(player,opponent)
        winner= battle.start_battle()

        if winner== player:
            again= input("\n 승리했습니다 새로운 적과 적투하시겠습니까? (y/n):").lower()
            if again != "y":
                print("게임을 종료")
                break
        else:
            print("\n 패배했습니다. 게임 종료")
            break
if __name__ == "__main__":
    game_loop()
                