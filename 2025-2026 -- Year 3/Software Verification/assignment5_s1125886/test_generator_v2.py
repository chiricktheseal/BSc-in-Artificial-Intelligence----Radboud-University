import argparse
import ast
from pathlib import Path
import random


def indent(code: str, level: int = 1) -> str:
    """Indent code by a given number of levels."""
    indentation = "    " * level
    return "\n".join(indentation + line for line in code.splitlines())


def get_classes_and_methods(
    file_path: str,
) -> dict[str, list[tuple[str, list[str], str]]]:
    """
    Finds all classes and their methods with types in the given Python file.
    It returns a dictionary where the keys are class names and the values are lists of methods, argument types and return types.

    For example:
    {
        "Stone": [
            ("__init__", ["bool", "tuple[float, float]", "int", "bool", "bool"], "None"),
            ("move", ["tuple[float, float]", "int", "bool"], "None"),
            ("distance_to_center", [], "float"),
            ("is_passed_hogline", [], "bool"),
            ("is_in_house", [], "bool")
        ]
    """
    with open(file_path, "r") as file:
        tree = ast.parse(file.read())

    classes = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            class_name = node.name
            methods = []
            for item in node.body:
                if isinstance(item, ast.FunctionDef):
                    method_name = item.name
                    args = []
                    for arg in item.args.args[1:]:  # Skip 'self'
                        arg_type = (
                            ast.unparse(arg.annotation) if arg.annotation else "Any"
                        )
                        args.append(arg_type)
                    return_type = ast.unparse(item.returns) if item.returns else "Any"
                    methods.append((method_name, args, return_type))
            classes[class_name] = methods

    return classes


def generate_test(
    classes: dict[str, list[tuple[str, list[str], str]]],
    file: str,
) -> str:
    """
    Generates a random test case for the given classes and methods.
    For example, it might generate a test case like:

    "
    obj_0 = Stone(False, (1.75..., -8.63...), 4, True, False) # Stone constructor
    var_1 = obj_0.move((-1.50..., -2.50...), 8, True)         # Random method 1
    var_2 = obj_0.distance_to_center()                        # Random method 2
    var_3 = obj_0.is_passed_hogline()                         # Random method 3
    var_4 = obj_0.is_in_house()                               # Random method 4
    self.assertEqual(var_1, True)
    self.assertEqual(var_2, 11.144049259545154)
    self.assertEqual(var_3, True)
    self.assertEqual(var_4, False)
    "
    or
    "
    with self.assertRaisesRegex(ValueError, "Cannot calculate distance to center for a burned stone."):
        obj_0 = Stone(True, (-0.22946106058599242, 3.6645716997143154), 10, True, False)
        var_1 = obj_0.move_out_of_play()
        var_2 = obj_0.distance_to_center()
    "
    """
    # TODO: Generate a random test case
    # For example,
    # obj_0 = Stone(False, (1.75..., -8.63...), 4, True, False) # Stone constructor   # 1. СОЗДАЕМ ОБЪЕКТ
    
    # var_1 = obj_0.move((-1.50..., -2.50...), 8, True)         # Random method 1     # 2. ВЫЗЫВАЕМ МЕТОДЫ
    # var_2 = obj_0.distance_to_center()                        # Random method 2
    # var_3 = obj_0.is_passed_hogline()                         # Random method 3
    # var_4 = obj_0.is_in_house()                               # Random method 4
    
    # self.assertEqual(var1, 2.76)                                                    # 3. ПРОВЕРЯЕМ РЕЗУЛЬТАТЫ
    # self.assertEqual(var2, True)
    
    class_name = 'Stone'
    if class_name not in classes:
        return ""  
    
    all_methods = classes[class_name] 
    
    constructor = None
    for method in all_methods:
        if method[0] == '__init__':
            constructor = method
            break
    if not constructor:
        return ""    
    
    # is_red: bool, xy: tuple, round: int, red_hammer: bool, burned: bool
    is_red = random.choice([True, False])
    x = round(random.uniform(-2.5, 2.5), 2)
    y = round(random.uniform(-6.401, 5.49), 2)
    round_num = random.randint(1, 10)
    red_hammer = random.choice([True, False])
    burned = random.choice([True, False])
    
    
    test_lines = []
    test_lines.append(f"stone = Stone({is_red}, ({x}, {y}), {round_num}, {red_hammer}, {burned})")
    
    other_methods = [m for m in all_methods if m[0] != '__init__']
    num_methods = min(6, len(other_methods))  
    selected_methods = random.sample(other_methods, num_methods)

    variables_to_check = [] 
    for i, (method, arg_types, return_type) in enumerate(selected_methods):
        if method == "move":
            dx = round(random.uniform(-0.5, 0.5), 2)
            dy = round(random.uniform(-0.5, 0.5), 2)
            in_round = random.randint(1, 10)
            by_red = random.choice([True, False])
            test_lines.append(f"var{i} = stone.{method}(({dx}, {dy}), {in_round}, {by_red})")
        else:
            test_lines.append(f"var{i} = stone.{method}()")
        variables_to_check.append((f"var{i}", return_type))
           
    test = "\n".join(test_lines).strip()
    
    result = evaluate(test, variables_to_check, file)
    if result[0] == "result":
        # IF SUCCECFUL TEST - add asserts to the test with real vals
        test_with_asserts = test + "\n"
        for var_name, var_type, var_value in result[1]:
            test_with_asserts += f"self.assertEqual({var_name}, {var_value})\n"
        return test_with_asserts
    else:
        # if error - return test with  assertRaises
        error_type, error_msg = result[1]
        return f"""with self.assertRaisesRegex({error_type}, "{error_msg}"):\n{indent(test, 2)}"""
    
   # return test

def evaluate(
    test: str, variables: list[tuple[str, str]], file: str
) -> tuple[str, list[tuple[str, str, str]] | tuple[str, str]]:
    """
    Given a test str such as:
    "
    obj_0 = Stone(False, (1.75..., -8.63...), 4, True, False) # Stone constructor
    var_1 = obj_0.move((-1.50..., -2.50...), 8, True)         # Random method 1
    var_2 = obj_0.distance_to_center()                        # Random method 2
    var_3 = obj_0.is_passed_hogline()                         # Random method 3
    var_4 = obj_0.is_in_house()                               # Random method 4
    ",
    and a list of variables to evualate such as: [("var_1", "int"), ("var_2", "float"), ("var_3", "bool"), ("var_4", "bool")]

    and the file to import from, it evaluates the test and returns a tuple of the form:
    ("result", [("var_1", "int", "8"), ("var_2", "float", "3.14"), ("var_3", "bool", "True"), ("var_4", "bool", "False")])
    or ("error", ("ValueError", "Invalid argument type: str"))
    """
    local_vars = {}
    file_path = Path(file)
    code = f"""
from {file_path.stem} import *
{test}
    """
    try:
        exec(code, {}, local_vars)
    except Exception as e:
        return "error", (str(type(e)).split("'")[1], str(e))

    return "result", [(var, ty, repr(local_vars[var])) for var, ty in variables]


def write_unittest_file(tests: list[str], src_file: str, out_file: str):
    """
    Writes the generated test to a unittest file.
    """
    file_path = Path(src_file)
    test_code = f"""import unittest
from {file_path.stem} import *
class TestGenerated(unittest.TestCase):
    """
    for i, test in enumerate(tests):
        test_func = f"""
    def test_{i}(self):
{indent(test, 2)}
        """
        test_code += test_func

    out_file_path = Path(out_file)
    out_file_path.write_text(test_code)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test Generator for Assignment 5")
    parser.add_argument(
        "input_file",
        type=str,
        help="Path to the input file containing test cases",
    )
    parser.add_argument(
        "num", type=int, default=10, help="Number of test cases to generate"
    )

    args = parser.parse_args()

    classes_and_methods = get_classes_and_methods(args.input_file)
    print("Classes and their methods with types:")
    for class_name, methods in classes_and_methods.items():
        print(f"Class: {class_name}")
        for method in methods:
            print(f"  Method: {method}")

    tests = []
    print("Generating tests:")
    for _ in range(args.num):
        tests.append(generate_test(classes_and_methods, args.input_file))

    write_unittest_file(tests, args.input_file, "tests.py")
