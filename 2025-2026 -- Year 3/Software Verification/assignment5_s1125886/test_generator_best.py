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


#-------------------------------------------------------------------------
# New written functions for test generation  
def generate_value_for_type(type_str):
    """ 
    Generates a random value for a given type string. For example:
    - 'bool' -> True or False
    - 'int' -> a random integer between -2 and 12
    - 'float' -> a random float between -8 and 8 rounded to 2 decimal places
    - 'tuple[float, float]' -> a tuple of two random floats between -8 and 8 rounded to 2 decimal places
    """
    if 'tuple' in type_str:
        # tuple[int, int]
        if 'int' in type_str:
            return f"({random.randint(-2, 12)}, {random.randint(-2, 12)})"
        else: # tuple[float, float]
            return f"({round(random.uniform(-3, 3), 2)}, {round(random.uniform(-7, 6), 2)})"    
    elif 'float' in type_str:
        if random.random() < 0.35:
            return round(random.choice([-8.0, -6.401, -2.5, 0.0, 1.83, 2.5, 5.49, 8.0]), 2)        
        return round(random.uniform(-8, 8), 2)
    elif type_str == 'int':
        if random.random() < 0.15:
            return random.choice([-2, -1, 0, 1, 10, 11, 12])
        return random.randint(-2, 12)
    elif type_str == 'bool':
        return random.choice([True, False])
    else:
        return 'None'
 

RADIUS = 0.15 #coppied from curling.py
min_distance_between_stones = 2 * RADIUS
  
def generate_non_overlapping_xy(existing_xy, max_attempts=100):
    """ 
    Generates a random (x, y) coordinate that does not overlap with existing coordinates in existing_xy.
    existing_xy is a list of tuples [(x1, y1), (x2, y2), ...] representing the coordinates of existing stones.
    """
    for _ in range(max_attempts):
        x = round(random.uniform(-2.5, 2.5), 2)
        y = round(random.uniform(-6.401, 5.49), 2)
        overlap = False             # check if the generated (x, y) overlaps with any existing coordinates
        for (ex, ey) in existing_xy:
            distance_squared =  (x - ex)**2 + (y - ey)**2 
            if distance_squared < min_distance_between_stones**2:   # if the distance is less than the minimum required, it's an overlap
                overlap = True
                break
        if not overlap:
            return (x, y)
    # if we fail to generate a non-overlapping coordinate after max_attempts, we can return a random coordinate (or raise an exception)
    return (round(random.uniform(-2.5, 2.5), 2), round(random.uniform(-6.401, 5.49), 2))


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
    
    class_names = list(classes.keys())
    known_classes = ['Stone', 'End', 'Game']
    
    known_present = [c for c in class_names if c in known_classes]
    unknown_present = [c for c in class_names if c not in known_classes] #for hidden class
    
    if unknown_present and random.random() < 0.3:  # 30% for hidden class if it exists
        class_name = random.choice(unknown_present)
        use_known_strategy = False
    else:
        if known_present:
            class_name = random.choice(known_present)
            use_known_strategy = True
            
            
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
    
    
    if use_known_strategy and class_name == 'Stone':
        # not burned and inside the fiel --> test more methods without getting errors
        if len(constr_args) >= 5 and constr_args[4] == 'False':
            x = round(random.uniform(-2.5, 2.5), 2)
            y = round(random.uniform(-6.401, 5.49), 2)
            constr_args[1] = f"({x}, {y})"
            # update the test line with the new args
            test_lines[-1] = f"{obj_name} = {class_name}({', '.join(constr_args)})"
            
        stone_methods = [m for m in all_methods if m[0] != '__init__']
        
        # use move() more often --> complex method with more edge cases
        move_method = next((m for m in stone_methods if m[0] == 'move'), None)
        selected_methods = []
        
        if move_method and random.random() < 0.5:  # 50^ chance to include move in the test
            selected_methods.append(move_method)
            other = [m for m in stone_methods if m[0] != 'move']
            if other:
                selected_methods.extend( random.sample(other, min(4, len(other))))
        else:
            # without move - just randomly select some methods to test
            selected_methods = random.sample(stone_methods, min(5, len(stone_methods)))
        
        #to cover is_out_of_bands --> generate outside coords
        if random.random() < 0.1:
            if len(constr_args) >= 5 and constr_args[4] == 'False':  # only if the stone is not burned
                x = round(random.choice([-5.0, -3.0, 3.0, 5.0]), 2)  
                y = round(random.choice([-8.0, -7.0, 6.0, 7.0]), 2)  
                constr_args[1] = f"({x}, {y})"
                test_lines[-1] = f"{obj_name} = {class_name}({', '.join(constr_args)})"
                
        for i, (method, arg_types, return_type) in enumerate(selected_methods):
            # generate args for method
            method_args = []
            for j, arg_type in enumerate(arg_types):        
                # if it's move -> generate args to cover more edges
                if method == 'move':
                    if j == 0:  # dxy - tuple[float, float]
                        # choose between small move (stays in the field) and large move (goes out of bounds) to cover more cases
                        move_type = random.choice(['small', 'large'])
                        if move_type == 'small':
                            dx = round(random.uniform(-0.5, 0.5), 2)
                            dy = round(random.uniform(-0.5, 0.5), 2)
                        else:
                            dx = round(random.choice([-5.0, 5.0]), 2)
                            dy = round(random.choice([-5.0, 5.0]), 2)
                        method_args.append(f"({dx}, {dy})")
                    elif j == 1:  # in_round
                        # val to cover Free Guard Zone
                        method_args.append(str(random.choice([1, 2, 3, 4, 8])))
                    elif j == 2:  # by_red
                        method_args.append(str(random.choice([True, False])))
                else:
                    method_args.append(str(generate_value_for_type(arg_type)))
            
            var_name = f"var_{obj_id}_{i}_{method}"
            
            test_lines.append(f"{var_name} = {obj_name}.{method}({', '.join(method_args)})")
            if return_type != 'None':
                variables_to_check.append((var_name, return_type))
    
    
    elif use_known_strategy and class_name == 'End':
        # add_stone, score - more complex methods, test them more often
        end_methods = [m for m in all_methods if m[0] != '__init__']
        end_hammer = constr_args[0] == 'True' # st to bool
        
        num_stones = random.randint(1, 3)
        stones_created = [] 
        coordinates = [] 
        
        for s in range(num_stones):
            stone_name = f"stone_{obj_id}_{s}"
            stones_created.append(stone_name) 
              
            # first stone= any color, but if = first stone --> set its color to be opposite of hammer to test 2 cases (red and yellow)
            if s == 0:
                stone_is_red = not end_hammer
            else:
                # for subsequent stones, we can randomly choose color, but let's make sure we test both colors in the generated tests
                stone_is_red = (s % 2 == 0) != end_hammer
            
            # Round of the stone = (round of the end // 2) + 1 
            stone_round = (s // 2) + 1
            # hammer of the stone = hammer of the end
            stone_hammer = end_hammer
            
            x, y = generate_non_overlapping_xy(coordinates)
            coordinates.append((x, y))
            stone_xy = f"({x}, {y})"
            
            # is not burned to be able to test more methods without getting errors --> higher coverage
            stone_burned = False
            
            test_lines.append(
                f"{stone_name} = Stone({stone_is_red}, {stone_xy}, {stone_round}, {stone_hammer}, {stone_burned})"
            )
            add_var = f"add_{obj_id}_{s}"
            test_lines.append(f"{add_var} = {obj_name}.add_stone({stone_name})")
            variables_to_check.append((add_var, 'None'))
        
        num = min(3, len(end_methods))
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
                    
                   
    elif use_known_strategy and class_name == 'Game':
        # add_end, score `- more complex methods, test them more often`
        game_methods = [m for m in all_methods if m[0] != '__init__']
        
        # create some ends to add to the game
        num_ends = random.randint(1, 3)
        ends_created = []
                
        for e in range(num_ends):
            end_name = f"end_{obj_id}_{e}"
            end_hammer = random.choice([True, False])
            
            ends_created.append(end_name)
            test_lines.append(f"{end_name} = End({end_hammer})")
                    
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
   
    else: #for hidden class -->randomly select some methods to test as we do not know how to weight different methods
        other_methods = [m for m in all_methods if m[0] != '__init__']
        
        if other_methods:
            num_methods = random.randint(2, min(4, len(other_methods)))
            selected_methods = random.sample(other_methods, num_methods)
            
            for i, (method, arg_types, return_type) in enumerate(selected_methods):
                method_args = []
                for arg_type in arg_types:
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
            if 'float' in var_type:
                test_with_asserts += f"self.assertAlmostEqual({var_name}, {var_value})\n" #friend suggested ti use this for floats
            else:
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
