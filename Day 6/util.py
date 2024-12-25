import os


def get_input_path(path: str) -> str:
    # base = os.path.dirname(__file__)
    # return os.path.join(base, "../../input", path)
    return path


def input_single(path: str, strip: bool = True) -> str:
    path = get_input_path(path)
    with open(path, "r") as f:
        contents: str = f.read()
        if strip:
            return contents.strip()

        return contents


def input_lines(path: str) -> list[str]:
    path = get_input_path(path)
    with open(path, "r") as f:
        lines = []
        for line in f.readlines():
            lines.append(line.strip())

        return lines