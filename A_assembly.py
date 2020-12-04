
def compile_error(text, line):
    print("Compile error at line " + str(line) + ": " + text)


def runtime_error(text, code_runner):
    print("Error at line " + str(get_file_line(code_runner)) + ": " + text)
    return mk_obj("", None)


def get_file_line(code_runner):
    line = get_line(code_runner)
    return stack[code_runner]["to_file"][line]


def assign(a, b):
    a["value"] = b["value"]
    return mk_obj(a["type"], a["value"])


def add_number(a, b):
    return mk_obj(a["type"], a["value"] + float(b["value"]))


def sub_number(a, b):
    return mk_obj(a["type"], a["value"] - float(b["value"]))


def mul_number(a, b):
    return mk_obj(a["type"], a["value"] * float(b["value"]))


def div_number(a, b):
    return mk_obj(a["type"], a["value"] / float(b["value"]))


def negate_number(n):
    return mk_number(-n["value"])


def equals(a, b):
    if a["value"] == b["value"] and a["type"] == b["type"]:
        return mk_number(1.0)
    return mk_number(0.0)


def less_than(a, b):
    if a["value"] < b["value"] and a["type"] == b["type"]:
        return mk_number(1.0)
    return mk_number(0.0)


def lesseq_than(a, b):
    if a["value"] <= b["value"] and a["type"] == b["type"]:
        return mk_number(1.0)
    return mk_number(0.0)


def greater_than(a, b):
    if a["value"] > b["value"] and a["type"] == b["type"]:
        return mk_number(1.0)
    return mk_number(0.0)


def greatereq_than(a, b):
    if a["value"] >= b["value"] and a["type"] == b["type"]:
        return mk_number(1.0)
    return mk_number(0.0)


def add_str(a, b):
    return mk_obj(a["type"], a["value"] + str(b["value"]))


def mul_str(a, b):
    return mk_obj(a["type"], a["value"] * int(b["value"]))


def mk_number(v):
    if type(v) == dict:
        val = v["value"]
        if type(val) == str:
            try:
                return mk_obj("a", float(val))
            except:
                runtime_error(
                    "Could not convert string to number: " + val, RUNNER)
        else:
            try:
                return mk_obj("a", float(val))
            except:
                runtime_error("Could to number: " + str(val), RUNNER)
    else:
        return mk_obj("a", float(v))


def mk_string(v):
    if type(v) == dict:
        return mk_obj("aA", str(v["value"]))
    else:
        return mk_obj("aA", str(v))


def mk_obj(typ, value):
    return {"value": value, "type": typ}


def str_print(v):
    if v["type"] == "aaa":
        return "[" + ", ".join([str_print(x) for x in v["value"]]) + "]"
    else:
        return str(v["value"])


def print_object(v):
    print(str_print(v))
    return mk_obj("", None)


def mk_function(id):
    return mk_obj("aa", id)


def input_object():
    return mk_string(input())


def number_and(a, b):
    return mk_number(1.0 if a["value"] != 0.0 and b["value"] != 0.0 else 0.0)


def number_or(a, b):
    return mk_number(1.0 if a["value"] != 0.0 or b["value"] != 0.0 else 0.0)


def number_not(n):
    return mk_number(1.0 if n["value"] == 0.0 else 0.0)


def bitwise_and(a, b):
    x = int(a["value"])
    y = int(b["value"])
    return mk_number(x & y)


def bitwise_or(a, b):
    x = int(a["value"])
    y = int(b["value"])
    return mk_number(x | y)


def bitwise_xor(a, b):
    x = int(a["value"])
    y = int(b["value"])
    return mk_number(x ^ y)


def bitwise_not(a):
    x = int(a["value"])
    return mk_number(~x)


def size_of(s):
    return mk_number(len(s["value"]))


def call_single(func, arg):
    return call_function(func, {"value": [arg]})


def mk_list(lst):
    return mk_obj("aaa", lst)


def call_function(func, args={"value": []}):
    if func["value"] in functions:
        func = functions[func["value"]]
        if callable(func):
            var = func(*args["value"])
            return var
        else:
            s = {"variables": {}, "to_file": func["to_file"], "functions": func["functions"], "labels": func["labels"],
                 "line": 0, "program": func["program"], "indent": func["indent"]}
            for i in range(len(func["arguments"])):
                if i < len(args["value"]):
                    s["variables"][func["arguments"][i]] = args["value"][i]
                else:
                    s["variables"][func["arguments"][i]] = mk_obj("", None)
            stack.append(s)
            var = run_stack()
            return var
    else:
        runtime_error("That function does not exist!", 0)


def index_list(lst, index):
    return lst["value"][int(index["value"])]


def index_dict(dict, key):
    return dict["value"][key["value"]]


def mk_copy(obj):
    return mk_obj(obj["type"], obj["value"])


def mk_null():
    return mk_obj("", None)


def add_to_list(lst, value):
    lst["value"].append(mk_copy(value))
    return mk_null()


def remove_from_list(lst, value):
    if value in lst["value"]:
        lst["value"].remove(value)
        return mk_number(1.0)
    return mk_number(0.0)


def concat_list(a, b):
    return mk_list(a["value"] + b["value"])


def file_in(str_obj):
    file = open(str_obj["value"], "r")
    t = file.read()
    file.close()
    return mk_string(t)


def file_out(path, str_obj):
    file = open(path["value"], "w")
    file.write(str_obj["value"])
    file.close()


def split_string(string, split_at):
    return mk_string(string["value"].split(split_at["value"]))


def call_member_single(func, val):
    return call_member_function(func, {"value": [val]})


def fits_call(arg_types, compare_to):
    if len(arg_types) != len(compare_to):
        return False
    for i in range(len(compare_to)):
        if compare_to[i] == "any":
            continue
        if arg_types[i] != compare_to[i]:
            return False
    return True


def call_member_function(func, args={"value": []}):
    calls = assembly[func["value"]["var"]["type"]
                     ]["functions"][func["value"]["func"]]
    arg_types = [x["type"] for x in args["value"]]
    for call in calls:
        if fits_call(arg_types, call["args"]):
            return call["func"](func["value"]["var"], *args["value"])
    runtime_error("There is no matching argument list!", 0)
    return mk_null()


def get_self(func):
    return func["var"]


def index_string(string, number):
    if int(number["value"]) >= len(string["value"]):
        runtime_error("String index out of range.", RUNNER)
        return mk_null()
    return mk_string(string["value"][int(number["value"])])


functions = {"Aaa": print_object, "AaA": input_object,
             "Aaaa": file_in, "AaaA": file_out}

labels = {"A": 0}

stack = [{"indent": 0, "line": 0, "variables": {},
          "functions": functions, "labels": labels}]

operator_order = {"a": -99, "AaAa": -10, "AaAaa": -10, "AaAaA": -10, "AaAaaa": -10, "AaAaAa": -10, "A": 10, "Aa": 10,
                  "AA": 15, "AAa": 15, "AAA": 20, "AAAa": 20, "AaAA": 999, "AaA": 1000}

assembly = {"a": {"operators": {"A": {"a": add_number}, "Aa": {"a": sub_number, "solo": negate_number}, "AA": {"a": mul_number}, "AAa": {"a": div_number},
                                "Aaa": {"solo": number_not}, "Aaaa": {"a": number_and}, "AaaA": {"a": number_or},
                                "AAaa": {"solo": bitwise_not}, "AAaaa": {"a": bitwise_and}, "AAaaA": {"a": bitwise_or}, "AAaaAa": {"a": bitwise_xor},
                                "AaAa": {"a": equals}, "AaAaa": {"a": less_than}, "AaAaaa": {"a": lesseq_than}, "AaAaA": {"a": greater_than}, "AaAaAa": {"a": greatereq_than}},
                  "constructors": {("a",): mk_number, ("aA",): mk_number}},
            "aA": {"operators": {"AaAa": {"aA": equals}, "AaAA": {"a": index_string}, "a": {"aA": assign}, "A": {"aA": add_str}, "AA": {"a": mul_str}},
                   "constructors": {("a",): mk_string, ("aA",): mk_string}, "functions": {"a": [{"args": (), "func": size_of}], "AAa": [{"args": ("aA"), "func": split_string}]}},
            "aa": {"operators": {"AaA": {"aaa": call_function, "solo": call_function, "a": call_single, "aA": call_single, "aa": call_single, "aaaA": call_single, "": call_single}}},
            "aaaA": {"operators": {"AaA": {"aaa": call_member_function, "solo": call_member_function, "a": call_member_single, "aA": call_member_single, "aa": call_member_single, "aaaA": call_member_single, "": call_member_single}},
                     "functions": {"aa": [{"args": (), "func": get_self}]}},
            "aaa": {"operators": {"AaAA": {"a": index_list}, "A": {"aaa": concat_list}}, "functions": {"a": [{"args": (), "func": size_of}], "A": [{"args": ("any",), "func": add_to_list}]}},
            "aaA": {"operators": {"AaAA": {"a": index_dict, "aA": index_dict}}}}


def parse_num(string, code_runner):
    num = 0
    decimals = 0.0
    point = 1
    has_point = False
    for c in string:
        if c == " ":
            continue
        if c == "a":
            if not has_point:
                num <<= 1
            else:
                point += 1
        elif c == "A":
            if not has_point:
                num <<= 1
                num += 1
            else:
                decimals += 1 / (2 ** point)
                point += 1
        elif c == "Â":
            if has_point:
                runtime_error(
                    "Two points in the same number definition.", code_runner)
            else:
                has_point = True
        else:
            runtime_error(
                "Error non aA-character in number definition.", code_runner)
    return num + decimals


def parse_string(string, code_runner):
    result = ""
    current = ""
    for c in string:
        if c.isspace():
            continue
        current += c
        if len(current) == 8:
            num = parse_num(current, code_runner)
            result += chr(int(num))
            current = ""
    return result


def get_number(code, i, code_runner):
    string = ""
    while i < len(code) and is_a(code[i]):
        string += code[i]
        i += 1
    if i < len(code) and code[i] == "Â":
        string += "Â"
        i += 1
        while i < len(code) and is_a(code[i]):
            string += code[i]
            i += 1

    return i, parse_num(string, code_runner)


def do_operation(a, b, operator):
    ta = assembly[a["type"]]

    if operator in ta["operators"]:
        if b["type"] in ta["operators"][operator]:
            ta["operators"][operator][b["type"]](a, b)
        else:
            return "The type " + a["type"] + " does not implement " + operator + " for type " + b["type"] + "."
    else:
        return "The type " + a["type"] + " does not implement " + operator + "."


def get_line_indent(line):
    indent = 0
    for c in line:
        if c == "\t":
            indent += 1
        else:
            break
    return indent


def is_a(char):
    return char == "a" or char == "A"


def get_var(var):
    for s in stack[::-1]:
        if var in s["variables"]:
            return s["variables"][var]


def get_function(function, code_runner):
    for s in stack[code_runner::-1]:
        if "functions" in s:
            if function in s["functions"]:
                return s["functions"][function]


def get_label(label, code_runner):
    for s in stack[code_runner::-1]:
        if "labels" in s:
            if label in s["labels"]:
                return s["labels"][label]


def get_order(operator):
    order = 0
    if operator in operator_order:
        order = operator_order[operator]
    return order


def get_next_char(code, i, ignore=False, ignore_white_space=False):
    new_lines = 0
    while i < len(code) and code[i].isspace():
        if code[i] == "\n":
            new_lines += 1
            if not ignore:
                return i, "\n", new_lines
        i += 1
        if not ignore_white_space and not code[i].isspace():
            return i - 1, " ", new_lines
    if i < len(code) and code[i] == "ⓐ":
        while i < len(code) and code[i] != "\n":
            i += 1
        new_lines += 1
        if ignore:
            index, char, n = get_next_char(code, i, True)
            new_lines += n
            return index, char, new_lines
        else:
            return i, "\n", new_lines
    if i < len(code) and code[i] == "Ⓐ":
        newline = False
        while i < len(code) and code[i] != "Ⓐ":
            i += 1
            if code[i] == "\n":
                newline = True
                new_lines += 1
        if newline and ignore:
            index, char, n = get_next_char(code, i, True)
            new_lines += n
            return index, char, new_lines
        elif newline and not ignore:
            return i, "\n"
        else:
            return get_next_char(code, i, ignore)
    if i < len(code):
        return i, code[i], new_lines
    return i, None, new_lines


def indentation(s, tabsize=4):
    sx = s.expandtabs(tabsize)
    return 0 if sx.isspace() else len(sx) - len(sx.lstrip())


RUNNER = 0


def eval(expr, code_runner):
    global RUNNER
    RUNNER = code_runner
    if len(expr) == 0:
        return mk_obj("", None)
    elements = []
    op_ord = []
    i = 0
    while i < len(expr):
        if expr[i] == "ä":
            string = ""
            i += 1
            while i < len(expr) and is_a(expr[i]):
                string += expr[i]
                i += 1
            var = get_var(string)
            if var == None:
                var = mk_obj("", None)
                stack[-1]["variables"][string] = var

            if i < len(expr) and expr[i] == "Â":
                i += 1
                member = ""
                while i < len(expr) and is_a(expr[i]):
                    member += expr[i]
                    i += 1
                if member in assembly[var["type"]]["functions"]:
                    elements.append(
                        mk_obj("aaaA", {"func": member, "var": var}))
                else:
                    runtime_error(
                        "That member function does not exist!", code_runner)
            else:
                elements.append(var)
        elif expr[i] == "å":
            string = ""
            i += 1
            while i < len(expr) and is_a(expr[i]):
                string += expr[i]
                i += 1
            order = get_order(string)
            if not order in op_ord:
                op_ord.append(order)
            elements.append(string)
        elif expr[i] == "ã":
            string = ""
            i += 1
            from_var = False
            if expr[i] == "ä":
                from_var = True
                i += 1
            while is_a(expr[i]):
                string += expr[i]
                i += 1
            if from_var:
                elements.append(mk_obj("A", get_var(string)["type"]))
            else:
                while expr[i] != "Á":
                    i += 1
                i += 1
                depth = 1
                args = []
                current = ""
                while True:
                    if expr[i] == "Á":
                        depth += 1
                    elif expr[i] == "À":
                        depth -= 1
                    if depth == 0:
                        break
                    if depth == 1 and expr[i] == "â":
                        args.append(eval(current, code_runner))
                        current = ""
                    else:
                        current += expr[i]
                    i += 1

                if len(current) > 0:
                    args.append(eval(current, code_runner))
                t = tuple([x["type"] for x in args])
                elements.append(assembly[string]["constructors"][t](*args))
                i += 1
        elif expr[i] == "Å":
            i += 1
            string = ""
            while i < len(expr) and is_a(expr[i]):
                string += expr[i]
                i += 1
            elements.append(mk_function(string))
        elif expr[i] == "Ä":
            i += 1
            string = ""
            while expr[i] != "Ä":
                string += expr[i]
                i += 1
            i += 1
            elements.append(mk_obj("aA", parse_string(string, code_runner)))
        elif expr[i] == "Á":
            i += 1
            depth = 1
            elems = []
            string = ""
            while i << len(expr):
                if depth == 1 and expr[i] == "â":

                    elems.append(eval(string, code_runner))
                    string = ""
                    i += 1
                    continue
                if expr[i] == "Á":
                    depth += 1
                elif expr[i] == "À":
                    depth -= 1
                if depth == 0:
                    break
                string += expr[i]
                i += 1
            i += 1
            if len(elems) > 0:
                if len(string) > 0:
                    elems.append(eval(string, code_runner))
                elements.append(mk_list(elems))
            else:
                if len(string) == 0:
                    elements.append(mk_list([]))
                else:
                    elements.append(eval(string, code_runner))
        elif is_a(expr[i]) or expr[i] == "Â":
            i, num = get_number(expr, i, code_runner)
            elements.append(mk_number(num))
        if i < len(expr) and expr[i] == " ":
            i += 1

    op_ord.sort()
    while len(elements) > 1:
        if len(op_ord) == 0:
            print(elements)
        order = op_ord.pop()
        i = 0

        def single(index):
            operator = elements[index[0]]
            index[0] += 1
            obj = None
            if index[0] < len(elements):
                if type(elements[index[0]]) == str:
                    obj = single(index)
                else:
                    obj = elements[index[0]]
                return assembly[obj["type"]]["operators"][operator]["solo"](obj)
            else:
                print(elements)
                runtime_error(
                    "Expected an object after an operator but found nothing.", code_runner)
                return mk_null()
        while i < len(elements):
            if type(elements[i]) == dict:
                a = elements[i]
                start = i
                i += 1
                if i >= len(elements):
                    break
                if type(elements[i]) == str:
                    if get_order(elements[i]) == order:
                        operator = elements[i]
                        i += 1
                        b = None
                        assign = False
                        if (elements[i] == "a"):
                            assign = True
                            i += 1
                        if type(elements[i]) == str:
                            index = [i]
                            b = single(index)
                            i = index[0]
                        else:
                            b = elements[i]
                        del elements[start: i + 1]
                        c = None
                        if operator == "a":
                            c = b
                            assign = True
                        else:
                            if a["type"] in assembly:
                                if operator in assembly[a["type"]]["operators"]:
                                    if b["type"] in assembly[a["type"]]["operators"][operator]:
                                        c = assembly[a["type"]]["operators"][operator][b["type"]](
                                            a, b)

                                        RUNNER = code_runner
                                    else:
                                        return runtime_error(
                                            "There is no operator " + operator + " for types " + a["type"] + " and " + b["type"] + ".", code_runner)
                                else:
                                    return runtime_error(
                                        "No operator " + operator + " found for type " + a["type"] + ".", code_runner)
                            else:
                                return runtime_error(
                                    "No type " + a["type"] + " found.", code_runner)
                        if assign:
                            a["type"] = c["type"]
                            a["value"] = c["value"]
                        elements.insert(start, c)
                        i = start
                    else:
                        i += 1
                else:
                    return runtime_error("Expected an operation.", code_runner)
            else:
                start = i
                index = [i]
                obj = single(index)
                RUNNER = code_runner
                i = index[0]
                del elements[start:i + 1]
                elements.insert(start, obj)
                i = start + 1
    return elements[0]


def compile(code, min_indent=0, i=0, fns=functions, lbls=labels, current_line=0):
    program = []
    program_to_file_line = []
    while i < len(code):
        while i < len(code) and code[i] == "\n":
            i += 1
        start = i
        indent = indentation(code[start:])
        if indent < min_indent:
            break
        while i < len(code) and code[i].isspace():
            i += 1
        line = ""
        end = None
        start_line = current_line
        i, char, newlines = get_next_char(code, i)
        current_line += newlines

        if i + 2 < len(code) and code[i:i+3] == "ÃA ":
            i += 3
            if i < len(code):
                i, char, newlines = get_next_char(code, i, False, True)
                current_line += newlines
                if char == "Å":
                    i += 1
                    name = ""
                    while i < len(code) and is_a(code[i]):
                        name += code[i]
                        i += 1

                    parameter = None
                    parameters = []

                    def add_parameter():
                        if parameter != None and len(parameter) > 0:
                            if not parameter in parameters:
                                parameters.append(parameter)
                            else:
                                compile_error(
                                    "There are two or more arguments named " + parameter + " in the funciton " + name + ".", -1)

                    i, char, newlines = get_next_char(
                        code, i, end != None, True)
                    current_line += newlines
                    while char != "\n" and char != None:
                        if end == None:
                            if char == "Á":
                                end = "À"
                        elif char == end:
                            end = None
                        if char == "ä":
                            add_parameter()
                            parameter = ""
                        elif is_a(char):
                            if parameter != None:
                                parameter += char
                            else:
                                compile_error(
                                    "You cannot have numeric constants in function arguments.", -1)
                        else:
                            compile_error("Unnexpected symbol '" +
                                          char + "' in function " + name, -1)
                        i += 1
                        i, char, newlines = get_next_char(
                            code, i, end != None, True)
                        current_line += newlines
                    add_parameter()
                    inner_functions = {}
                    inner_labels = {}
                    prog, to_file, i, current_line = compile(
                        code, indent + 1, i + 1, inner_functions, inner_labels, current_line)
                    fns[name] = {"value": name, "functions": inner_functions,
                                 "labels": inner_labels, "program": prog, "to_file": to_file, "arguments": parameters, "indent": indent + 1}

                else:
                    compile_error("Expected 'Å' but got '" + char + "'.", -1)
            else:
                compile_error("Missing function name.", -1)

        else:
            if i + 3 < len(code) and code[i:i+4] == "ÃaA ":
                i += 4
                if i < len(code):
                    i, char, newlines = get_next_char(code, i, False, True)
                    current_line += newlines
                    if char == "Ä":
                        i += 1
                        i, char, newlines = get_next_char(code, i, True, True)
                        current_line += newlines
                        string = ""
                        while char != "Ä" or char != None:
                            if is_a(char):
                                string += char
                            else:
                                compile_error(
                                    "Expected 'A' or 'a' but got '" + char + "'", -1)
                            i += 1
                            i, char, newlines = get_next_char(
                                code, i, True, True)
                            current_line += newlines
                        if char == "Ä":
                            if not string in lbls:
                                lbls[string] = len(program)
                            else:
                                compile_error("That label already exists.", -1)
                        else:
                            compile_error(
                                "The file ended before the string was completed.", -1)
                    elif is_a(char):
                        i, num = get_number(code, i, -1)
                        if not num in lbls:
                            lbls[num] = len(program)
                        else:
                            compile_error("That label already exists.", -1)
                    else:
                        compile_error(
                            "Only constant string and numbers are allowed for label keys.", -1)
            else:
                while char != "\n" and char != None:
                    if end == None:
                        if char == "Á":
                            end = "À"
                        elif char == "á":
                            end = "à"
                        elif char == "Ä":
                            end = "Ä"
                    elif char == end:
                        end = None
                    line += char

                    i += 1
                    i, char, new_lines = get_next_char(code, i, end != None)
                    current_line += new_lines
                current_line += 1
                line = line.strip()
                if len(line) > 0:
                    program.append((line, indent))
                    program_to_file_line.append(start_line)

    return program, program_to_file_line, i, current_line


def should_run(code_runner):
    return get_line(code_runner) < len(stack[code_runner]["program"])


def get_code(code_runner):
    return stack[code_runner]["program"][get_line(code_runner)][0]


def get_line(code_runner):
    return stack[code_runner]["line"]


def get_indent(code_runner):
    return stack[code_runner]["program"][get_line(code_runner)][1]


def next_line(code_runner):
    stack[code_runner]["line"] += 1


def new_scope(indent):
    stack.append({"indent": indent, "variables": {}})


def skip_scope(code_runner, indent):
    while should_run(code_runner) and get_indent(code_runner) > indent:
        next_line(code_runner)


def run_stack():
    code_runner = len(stack) - 1
    while should_run(code_runner):
        code = get_code(code_runner)
        indent = get_indent(code_runner)
        while indent < stack[-1]["indent"]:
            stack.pop()
        if indent > stack[-1]["indent"]:
            new_scope(indent)
        if code[0] == "Ã":
            if code[1] == "a":
                if code[2] == " ":
                    var = eval(code[3:], code_runner)
                    if (var["value"] != 0):
                        stack[-1]["skip_else"] = True
                        new_scope(indent + 1)
                        next_line(code_runner)
                    else:
                        stack[-1]["skip_else"] = False
                        next_line(code_runner)
                        skip_scope(code_runner, indent)
                elif code[2] == "a":
                    if code[3] == " ":
                        if stack[-1]["skip_else"]:
                            next_line(code_runner)
                            skip_scope(code_runner, indent)
                        else:
                            var = eval(code[4:], code_runner)
                            if (var["value"] != 0):
                                stack[-1]["skip_else"] = True
                                new_scope(indent + 1)
                                next_line(code_runner)
                            else:
                                next_line(code_runner)
                                skip_scope(code_runner, indent)
                    elif code[3] == "a" and (len(code) == 4 or code[4] == " "):
                        if stack[-1]["skip_else"]:
                            next_line(code_runner)
                            skip_scope(code_runner, indent)
                        else:
                            stack[-1]["skip_else"] = True
                            new_scope(indent + 1)
                            next_line(code_runner)
                    elif code[3] == "A" and (len(code) == 4 or code[4] == " "):
                        val = eval(code[5:], code_runner)
                        del stack[code_runner:]
                        return val
                    else:
                        runtime_error("Unnexpected keyword.", code_runner)
                elif code[2] == "A":
                    if code[3] == "a" and code[4] == " ":
                        key = eval(code[5:], code_runner)
                        if key["type"] == "a" or key["type"] == "aA":
                            if key["value"] in stack[code_runner]["labels"]:
                                stack[code_runner]["line"] = stack[code_runner]["labels"][key["value"]]
                            else:
                                runtime_error(
                                    "That label does not exist.", code_runner)
                        else:
                            runtime_error(
                                "The only valid types for labels are ãa and ãaA.", code_runner)
                    else:
                        runtime_error("Unnexpected keyword.", code_runner)
                else:
                    runtime_error("Unnexpected keyword.", code_runner)
            else:
                runtime_error("Unnexpected keyword.", code_runner)
        else:
            eval(code, code_runner)
            next_line(code_runner)
    stack.pop()
    return mk_obj("", None)
