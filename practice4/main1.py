from class_generator import Generator
from practice4 import RabbitListBasic, RabbitListExtended, RabbitListBonus


def generate_rabbits(generator, count):
    return [generator.generate_single()[0] for _ in range(count)]


def test_rabbit_list_basic(rabbits):
    basic = RabbitListBasic()
    basic.extend(rabbits[:3])
    print(f"Length: {len(basic)}")
    basic.insert(1, rabbits[3])
    basic.insert(0, rabbits[4])
    print(f"List: {basic}")
    print(f"Length: {len(basic)}")
    print(f"Index of rabbits[2]: {basic.index(rabbits[2])}")
    basic.remove(rabbits[2])
    print(f"List after removal: {basic}")
    print(f"Length: {len(basic)}")


def test_rabbit_list_extended(rabbits):
    extended = RabbitListExtended()
    extended.extend(rabbits[:3])
    print(f"Length: {len(extended)}")
    extended.clear()
    print(f"Length after clear: {len(extended)}")
    extended.extend(rabbits[:3])
    rabbit_list_copy = extended.copy()
    print("Extended List:")
    for rabbit in extended:
        print(rabbit)
    del extended[1]
    print("List after element removal:")
    for rabbit in extended:
        print(rabbit)
    extended.extend([rabbit for rabbit in generate_rabbits(g, 1)])
    print("List after extension:")
    for rabbit in extended:
        print(rabbit)
    popped_rabbit = extended.pop(2)
    print(f"Popped item: {popped_rabbit}")
    extended.reverse()
    print("Reversed list:")
    for rabbit in extended:
        print(rabbit)
    count = extended.count(extended[0])
    print(f"Number of occurrences: {count}")


def test_rabbit_list_bonus(rabbits):
    bonus = RabbitListBonus()
    bonus.extend(rabbits[:3])
    print(f"List: {bonus}")
    print(f"Length: {len(bonus)}")
    bonus_copy = bonus.deepcopy()
    print(f"Copy: {bonus_copy}")
    rabbit_list_sum = bonus + bonus_copy
    print(f"Sum: {rabbit_list_sum}")
    rabbit_list_mul = bonus * 3
    print(f"Mul: {rabbit_list_mul}")


if __name__ == "__main__":
    g = Generator()
    rabbits = generate_rabbits(g, 5)

    for rabbit in rabbits:
        print(rabbit)

    print("Basic:")
    print("------------------------")
    test_rabbit_list_basic(rabbits)

    print("------------------------")
    print("Extended:")
    print("------------------------")
    test_rabbit_list_extended(rabbits)

    print("------------------------")
    print("Bonus:")
    print("------------------------")
    test_rabbit_list_bonus(rabbits)
