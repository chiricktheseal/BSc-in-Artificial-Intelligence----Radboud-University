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
    test = ""

    # TODO: Generate a random test case
    # For example,
    # obj_0 = Stone(False, (1.75..., -8.63...), 4, True, False) # Stone constructor   # 1. СОЗДАЕМ ОБЪЕКТ
    
    # var_1 = obj_0.move((-1.50..., -2.50...), 8, True)         # Random method 1     # 2. ВЫЗЫВАЕМ МЕТОДЫ
    # var_2 = obj_0.distance_to_center()                        # Random method 2
    # var_3 = obj_0.is_passed_hogline()                         # Random method 3
    # var_4 = obj_0.is_in_house()                               # Random method 4
    
    # self.assertEqual(var1, 2.76)                                                    # 3. ПРОВЕРЯЕМ РЕЗУЛЬТАТЫ
    # self.assertEqual(var2, True)
    
    choice = random.choices(['Stone', 'End', 'Game'], weights=[50, 25, 25])[0]
    class_name = choice
    if class_name not in classes:
        return ""  
    
    all_methods = classes[class_name] 
    
    constructor = next((m for m in all_methods if m[0] == '__init__'), None)
    if not constructor:
        return "" 
    
    # arguments for constructor   
    constr_args = []
    for arg_type in constructor[1]:
        value = generate_value_for_type(arg_type)
        # if it's not a string (bool, int, float), convert to string
        # if it's a string, keep it as is (e.g., "None", "True", "False", or a tuple represented as a string)
        if isinstance(value, bool) or isinstance(value, int) or isinstance(value, float):
            constr_args.append(str(value))
        else:
            constr_args.append(value)
        
    #create object + use generetaed arguemtns    
    test_lines = []
    obj_id = random.randint(0, 999)
    obj_name = f"obj_{obj_id}"
    
    test_lines.append(f"{obj_name} = {class_name}({', '.join(constr_args)})")
    
    other_methods = [m for m in all_methods if m[0] != '__init__']
 
    #separetely for each class
    variables_to_check = []
    
    
    if class_name == 'Stone':
        stone_methods = [m for m in all_methods if m[0] != '__init__']
        
        # use move() more often --> complex method with more edge cases
        move_method = next((m for m in stone_methods if m[0] == 'move'), None)
        selected_methods = []
        
        if move_method and random.random() < 0.5:  # 50^ chance to include move in the test
            selected_methods.append(move_method)
            other = [m for m in stone_methods if m[0] != 'move']
            if other:
                selected_methods.extend( random.sample(other, min(2, len(other))))
        else:
            # without move - just randomly select some methods to test
            num = min(3, len(stone_methods))
            selected_methods = random.sample(stone_methods, num)
        
        for i, (method, arg_types, return_type) in enumerate(selected_methods):
            # generate args for method
            method_args = []
            for arg_type in arg_types:
                method_args.append(str(generate_value_for_type(arg_type)))
            
            var_name = f"var_{obj_id}_{i}_{method}"
            
            test_lines.append(f"{var_name} = {obj_name}.{method}({', '.join(method_args)})")
            if return_type != 'None':
                variables_to_check.append((var_name, return_type))
    
    elif class_name == 'End':
        # add_stone, score - more complex methods, test them more often
        end_methods = [m for m in all_methods if m[0] != '__init__']
        
        num_stones = random.randint(1, 2)
        stones_created = [] 
        for s in range(num_stones):
            stone_id = random.randint(0, 999)
            stone_name = f"stone_{stone_id}_{s}"
            stones_created.append(stone_name) 
                
            # generate random stone args
            stone_is_red = random.choice([True, False])
            stone_xy = f"({generate_value_for_type('float')}, {generate_value_for_type('float')})"
            stone_round = random.randint(1, 10)
            stone_hammer = constr_args[0] if constr_args else random.choice([True, False])
            stone_burned = random.choice([True, False])
            
            test_lines.append(
                f"{stone_name} = Stone({stone_is_red}, {stone_xy}, {stone_round}, {stone_hammer}, {stone_burned})"
            )
            # try to add stone
            add_var = f"add_{obj_id}_{s}"
            test_lines.append(f"{add_var} = {obj_name}.add_stone({stone_name})")
            variables_to_check.append((add_var, 'None'))
        
        
        num = min(2, len(end_methods))
        if end_methods:
            selected_methods = random.sample(end_methods, num)
            
            for i, (method, arg_types, return_type) in enumerate(selected_methods):
                # generate args for method
                method_args = []
                for arg_type in arg_types:
                    # if stone object is needed
                    if arg_type == 'Stone' and stones_created:
                        method_args.append(random.choice(stones_created))
                    else:
                        method_args.append(str(generate_value_for_type(arg_type)))
                
                var_name = f"var_{obj_id}_{i}_{method}"
                test_lines.append(f"{var_name} = {obj_name}.{method}({', '.join(method_args)})")
                if return_type != 'None':
                    variables_to_check.append((var_name, return_type))
                    
                    
    
    elif class_name == 'Game':
        # add_end, score `- more complex methods, test them more often`
        game_methods = [m for m in all_methods if m[0] != '__init__']
        
        # create some ends to add to the game
        num_ends = random.randint(1, 2)
        ends_created = []
        
        for e in range(num_ends):
            end_id = random.randint(0, 999)
            end_name = f"end_{end_id}"
            end_hammer = random.choice([True, False])
            
            test_lines.append(f"{end_name} = End({end_hammer})")
            ends_created.append(end_name)
            
            # add some stones to the end
            num_stones = random.randint(1, 2)
            stones_in_end = []  #
            
            for s in range(num_stones):
                stone_id = random.randint(0, 999)
                stone_name = f"stone_{stone_id}"
                stones_in_end.append(stone_name)
                
                stone_is_red = random.choice([True, False])
                stone_xy = f"({generate_value_for_type('float')}, {generate_value_for_type('float')})"
                stone_round = random.randint(1, 10)
                stone_burned = random.choice([True, False])
                
                test_lines.append(
                    f"{stone_name} = Stone({stone_is_red}, {stone_xy}, {stone_round}, {end_hammer}, {stone_burned})"
                )
                # Add stone to end
                add_stone_var = f"add_stone_{obj_id}_{e}_{s}"
                test_lines.append(f"{add_stone_var} = {end_name}.add_stone({stone_name})")
                variables_to_check.append((add_stone_var, 'None'))  
            
            #  add end to the game
            add_end_var = f"add_end_{obj_id}_{e}"
            test_lines.append(f"{add_end_var} = {obj_name}.add_end({end_name})")
            variables_to_check.append((add_end_var, 'None'))   
            
        
        num = min(2, len(game_methods))
        if game_methods:
            selected_methods = random.sample(game_methods, num)
            
            for i, (method, arg_types, return_type) in enumerate(selected_methods):
                # generate args for method
                method_args = []
                for arg_type in arg_types:
                    if arg_type == 'End' and ends_created:
                        method_args.append(random.choice(ends_created))
                    else:
                        method_args.append(str(generate_value_for_type(arg_type)))
                
                var_name = f"var_{obj_id}_{i}_{method}"
                test_lines.append(f"{var_name} = {obj_name}.{method}({', '.join(method_args)})")
                if return_type != 'None':
                    variables_to_check.append((var_name, return_type))
    
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
   
def generate_value_for_type(type_str):
    """ 
    Generates a random value for a given type string. For example:
    - 'bool' -> True or False
    - 'int' -> a random integer between -2 and 12
    - 'float' -> a random float between -8 and 8 rounded to 2 decimal places
    - 'tuple[float, float]' -> a tuple of two random floats between -8 and 8 rounded to 2 decimal places
    """
    if type_str == 'bool':
        return random.choice([True, False])
    
    elif type_str == 'int':
        if random.random() < 0.3:
            return random.choice([-2, -1, 0, 1, 10, 11, 12])
        return random.randint(-2, 12)
    
    elif 'float' in type_str:
        if random.random() < 0.3:
            return round(random.choice([-8.0, -6.401, 0.0, 1.83, 5.49, 8.0]), 2)
        return round(random.uniform(-8, 8), 2)
    
    elif 'tuple' in type_str:
        # tuple[float, float]  tuple[int, int]
        if 'int' in type_str:
            return f"({random.randint(-2, 12)}, {random.randint(-2, 12)})"
        else:
            return f"({round(random.uniform(-8, 8), 2)}, {round(random.uniform(-8, 8), 2)})"
    else:
        return 'None'
    

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
