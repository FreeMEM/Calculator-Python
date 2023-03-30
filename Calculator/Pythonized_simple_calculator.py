import argparse
import operator


def check_operator(value):
    valid_operator = ["-", "+", "/", "*"]
    if (True, False)[value in valid_operator and len(value) == 1]:
        raise argparse.ArgumentTypeError("debe ser un +, -, * ó / simple carácter")
    return value


if __name__ == "__main__":
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-x",
        "--num_x",
        required=True,
        help="integer number for the operation",
        type=int,
    )
    parser.add_argument(
        "-y",
        "--num_y",
        required=True,
        help="integer number for the operation",
        type=int,
    )
    parser.add_argument("-o", "--operator", required=True, help="", type=check_operator)
    args = parser.parse_args()

    calculator = lambda args: operators[args.operator](args.num_x, args.num_y)
    print(calculator(args))
