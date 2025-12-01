import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "--practice",
    action="store_true",
    help="Run in practice mode"
)

def get_input(day: int, is_practice: bool = False) -> list[str]:
    fp = f"input/day{day}_input{'_prac' if is_practice else ''}.txt"
    with open(fp, 'r') as f:
        return f.read().splitlines()

def get_args() -> argparse.Namespace:
    return parser.parse_args()

