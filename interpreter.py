import sys
import traceback
from A_assembly import compile, assembly, mk_obj, mk_number, mk_list, mk_string, mk_function, operator_order, stack, run_stack, functions, labels, runtime_error, compile_error
file = open


allowed = "Ⓐⓐ⒜AaẠạÅåÄäẢảḀḁẤấẦầẨẩȂȃẪẫẬậẮắẰằẲẳẴẵẶặĀāĄąȀȁǺǻȦȧÁáǞǟǍǎÀàÃãǠǡÂâȺⱥÆæǢǣǼǽⱯꜲꜳꜸꜹꜺꜻⱭ℀⅍℁ª"


def run_program(code):
    test_line = 1
    for c in code:
        if c == "\n":
            test_line += 1
        if not c in allowed and not c.isspace():
            compile_error("Non A or whitespace character found.", test_line)
            return 1
    code.expandtabs(4)
    program, _ptf_line, _i = compile(code)
    stack[-1]["program"] = program
    run_stack()
    return 0


run_stack_ref = run_stack
runtime_error_ref = runtime_error

if __name__ == "__main__" and len(sys.argv) > 1:
    path = sys.argv[1]
    file = open(path, "r", encoding="utf-8")
    code = file.read()
    file.close()
    sys.exit(run_program(code))
