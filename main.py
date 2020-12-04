import random

knight_hp = 10
knight_attack = 10
victory_list = []


def plus(a: int, b: int) -> int:
    c = a + b
    return c


def minus(a: int, b: int) -> int:
    c = a - b
    return c


def exception():
    while True:
        try:
            number = int(input())
            if number < 1 or number > 2:
                raise Exception
        except ValueError:
            return "Вы ввели неверное значение , надо ввести 1 или 2"
        except Exception:

            return "Вы ввели неверное значение , надо ввести 1 или 2"
        return number


while True:
    devil_hp = random.randint(5, 10)
    devil_attack = random.randint(5, 10)
    new_hp_knight = random.randint(5, 10)
    new_attack_knight = random.randint(5, 10)
    rand = random.choice(['1', '2', '3'])
    if rand == '1':
        print(f"Вы встретили чудовище: Здоровье чудовища {devil_hp} Сила атаки чудовища {devil_attack} Нажмите 1 - "
              f"сражаться, 2 - убежать, чтобы набраться сил, ваше здоровье сейчас: {knight_hp}")
        nm = exception()
        print(nm)
        if nm == 1:
            if devil_attack >= knight_hp:
                print("Вы умерли")
                break
            if knight_attack > devil_hp:
                knight_hp = minus(knight_hp, devil_attack)
                print(f"Вы выбрали сражаться с монстром, ваше здоровье {knight_hp}")
                victory_list.append(knight_hp)
                print(f"Убито монстров: {len(victory_list)}")
                if len(victory_list) == 10:
                    print("Победа!")
                    break
        if nm == 2:
            print(" Вы убежали ")

    if rand == '2':
        knight_hp = plus(knight_hp, new_hp_knight)
        print(f"Вы нашли яблоко. Новое здоровье рыцаря:  {knight_hp}")

    if rand == '3':
        print("Вы нашли меч, Введите: 1 что бы взять меч себе выбросив старый, 2 что бы пройти мимо меча")
        nm = exception()
        if nm == 1:
            knight_attack = plus(knight_attack, new_attack_knight)
            print(f" Вы взяли меч -> Новая атака рыцаря:   {knight_attack}")
        if nm == 2:
            print("Вы прошли мимо меча")
