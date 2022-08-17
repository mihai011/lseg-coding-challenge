"""
Resolving LSEG coding challenge.

"""

import numpy as np
from tqdm import tqdm

from utils import increase, init, zeros, ones, toogle, increase, decrease


TURN_ON = "turn on"
TURN_OFF = "turn off"
TOGGLE = "toggle"


def read_input(file):
    """
    Opens, read file and parse the contents.
    Args:
        file (str): path to the file
    Returns:
        list: list of parsed instructions
    """

    instructions = []

    action_instructions = {}
    action_instructions[TURN_ON] = TURN_ON
    action_instructions[TURN_OFF] = TURN_OFF
    action_instructions[TOGGLE] = TOGGLE

    with open(file, encoding="utf-8") as input_file:
        for line in input_file.readlines():

            instruction = {}
            words = line.split(" ")
            pos_2 = eval(words[-1])
            pos_1 = eval(words[-3])

            instruction["pos1"] = pos_1
            instruction["pos2"] = pos_2

            for pos_instruction in [TURN_ON, TURN_OFF, TOGGLE]:
                if line.startswith(pos_instruction):
                    instruction["action"] = action_instructions[pos_instruction]

            instructions.append(instruction)

    return instructions


def resolve(file_name, part_2=False):
    """
    Args:
        file_name
        part_2 (bool, optional): Bool values for switching on resolving part 2. Defaults to False.
    Returns:
        int: sum of all elements in the grid
    """

    instructions = read_input(file_name)
    grid = init((1000, 1000))

    action_functions = {TURN_ON: ones, TURN_OFF: zeros, TOGGLE: toogle}

    if part_2:
        action_functions[TURN_ON] = lambda area: increase(area, 1)
        action_functions[TURN_OFF] = lambda area: decrease(area, 1)
        action_functions[TOGGLE] = lambda area: increase(area, 2)

    for ins in tqdm(instructions):
        ins["pos2"] = ins["pos2"][0] + 1, ins["pos2"][1] + 1
        pos10, pos20, pos11, pos21 = (
            ins["pos1"][0],
            ins["pos2"][0],
            ins["pos1"][1],
            ins["pos2"][1],
        )
        array_slice = np.s_[pos10:pos20, pos11:pos21]
        work_area = grid[array_slice]
        grid[array_slice] = action_functions[ins["action"]](work_area)

    return np.sum(grid)


def test_read():
    """test read function"""

    instructions = read_input("test_input.txt")
    expected_instruction = [
        {"action": TURN_ON, "pos1": (0, 0), "pos2": (999, 999)},
        {"action": TURN_OFF, "pos1": (499, 499), "pos2": (500, 500)},
        {"action": TOGGLE, "pos1": (0, 499), "pos2": (999, 500)},
    ]

    assert instructions == expected_instruction


def test_resolve():
    """test resolve functions"""

    res_1 = resolve("test_input.txt")
    assert res_1 == 998004
    res_2 = resolve("test_input.txt", True)
    assert res_2 == 1003996


if __name__ == "__main__":

    res_1 = resolve("test_input.txt", False)
    print(res_1)
    res_2 = resolve("test_input.txt", True)
    print(res_2)
    real_res = resolve("real_input.txt", True)
    print(real_res)
