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
    
    test_lines = []
    
    test_lines.append("obj0 = Stone(False, (1.75, -8.63), 4, True, False)")  # 1. ДОБАВЛЯЕМ КОНСТРУКТОР
    test_lines.append("var1 = obj0.move((-1.50, -2.50), 8, True)")           # 2. ДОБАВЛЯЕМ МЕТОДЫ
    test_lines.append("var2 = obj0.distance_to_center()")
    test_lines.append("var3 = obj0.is_passed_hogline()")
    test_lines.append("var4 = obj0.is_in_house()")
    test_lines.append("self.assertEqual(var1, True)")                        # 3. ДОБАВЛЯЕМ ПРОВЕРКИ
    test_lines.append("self.assertEqual(var2, 11.144049259545154)")
    test_lines.append("self.assertEqual(var3, True)")
    test_lines.append("self.assertEqual(var4, False)")
    
    test = "\n".join(test_lines).strip()
    return test


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
