import pathlib
import typing as tp
import random
    
T = tp.TypeVar("T")

def display(grid: tp.List[tp.List[str]]) -> None:
    """Вывод Судоку """
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print(
            "".join(
                grid[row][col].center(width) + ("|" if str(col) in "25" else "") for col in range(9)
            )
        )
        if str(row) in "25":
            print(line)
    print()


def group(values: tp.List[T], n: int) -> tp.List[tp.List[T]]:
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов

    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    fullList = []
    subList = 0
    numberOfStringStart = 0
    for i in range(int(len(values) / n)):
        subList = values[numberOfStringStart + i:numberOfStringStart + i + n]
        print(subList)
        fullList.append(subList)
        numberOfStringStart += n - 1
    return fullList


def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера строки, указанной в pos

    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """

    return grid[pos[0]]


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера столбца, указанного в pos

    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """

    return [i[pos[1]] for i in grid]


def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения из квадрата, в который попадает позиция pos

    >>> grid = read_sudoku('puzzle1.txt')
    >>> get_block(grid, (0, 1))
    ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    >>> get_block(grid, (4, 7))
    ['.', '.', '3', '.', '.', '1', '.', '.', '6']
    >>> get_block(grid, (8, 8))
    ['2', '8', '.', '.', '.', '5', '.', '7', '9']
    """
    block = []
    startRow = int(pos[0] / 3) * 3
    startColumn = int(pos[1] / 3) * 3
    # for i in range(3):
    for i in range(3):
        string = grid[startRow + i]
        string = string[startColumn: startColumn + 3]
        block.append(string[0])
        block.append(string[1])
        block.append(string[2])
    return block


def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    """Найти первую свободную позицию в пазле

    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j] == '.'):
                return (i, j)
    return None

def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    """Вернуть множество возможных значения для указанной позиции

    >>> grid = read_sudoku('puzzle1.txt')
    >>> values = find_possible_values(grid, (0,2))
    >>> values == {'1', '2', '4'}
    True
    >>> values = find_possible_values(grid, (4,7))
    >>> values == {'2', '5', '9'}
    True
    """
    possibleValues = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
    row = get_row(grid, pos)
    column = get_col(grid, pos)
    block = get_block(grid, pos)
    for i in range(len(row)):
        if row[i] != ".":
            possibleValues.remove(row[i])
    for i in range(len(column)):
        if (column[i] != "."):
            if (possibleValues.__contains__(column[i])):
                possibleValues.remove(column[i])
    for i in range(len(block)):
        if (block[i] != "."):
            if (possibleValues.__contains__(block[i])):
                possibleValues.remove(block[i])

    return possibleValues

def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    """Вернуть множество возможных значения для указанной позиции

    >>> grid = read_sudoku('puzzle1.txt')
    >>> values = find_possible_values(grid, (0,2))
    >>> values == {'1', '2', '4'}
    True
    >>> values = find_possible_values(grid, (4,7))
    >>> values == {'2', '5', '9'}
    True
    """
    possibleValues = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
    row = get_row(grid, pos)
    column = get_col(grid, pos)
    block = get_block(grid, pos)
    for i in range(len(row)):
        if row[i] != ".":
            possibleValues.remove(row[i])
    for i in range(len(column)):
        if (column[i] != "."):
            if (possibleValues.__contains__(column[i])):
                possibleValues.remove(column[i])
    for i in range(len(block)):
        if (block[i] != "."):
            if (possibleValues.__contains__(block[i])):
                possibleValues.remove(block[i])

    return possibleValues


def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    """ Решение пазла, заданного в grid """
    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла

    >>> grid = read_sudoku('puzzle1.txt')
    >>> solve(grid)
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """

    def checking(grid: tp.List[tp.List[str]]):
        position = find_empty_positions(grid)
        if not position:
            return True
        else:
            posValues = find_possible_values(grid, (position[0], position[1]))
            if (len(posValues)) == 0:
                return False
            else:
                for i in posValues:
                    grid[position[0]][position[1]] = i
                    if checking(grid) == True:
                        return True
                    else:
                        grid[position[0]][position[1]] = '.'

    checking(grid)
    return grid


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """ Если решение solution верно, то вернуть True, в противном случае False """
    # TODO: Add doctests with bad puzzles
    for i in range(len(solution)):
        for j in range(len(solution)):
            row = set(get_row(solution, (i, j)))
            col = set(get_col(solution, (i, j)))
            block = set(get_block(solution, (i, j)))
            if (len(row) < 9) or (len(col) < 9) or (len(block) < 9) or (row.__contains__(".")) or (
                    col.__contains__(".")) or (block.__contains__(".")):
                return False
    return True


def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
    """Генерация судоку заполненного на N элементов

    >>> grid = generate_sudoku(40)
    >>> sum(1 for row in grid for e in row if e == '.')
    41
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(1000)
    >>> sum(1 for row in grid for e in row if e == '.')
    0
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(0)
    >>> sum(1 for row in grid for e in row if e == '.')
    81
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    """
    N = 81 - N
    blankSudoku = [["." for i in range(9)] for j in range(9)]
    grid = solve(blankSudoku)
    while (N > 0):
        display(grid)
        rowNumber = random.randint(0, 8)
        columnNumber = random.randint(0, 8)
        if (grid[rowNumber][columnNumber] != "."):
            grid[rowNumber][columnNumber] = "."
            N -= 1
    return (grid)


if __name__ == "__main__":
    # print(find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']]))

    print(solve([["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
