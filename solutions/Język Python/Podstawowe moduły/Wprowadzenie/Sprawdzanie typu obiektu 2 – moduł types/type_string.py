import types


def type_string(obj):
    if type(obj) == types.FunctionType or type(obj) == types.BuiltinFunctionType:
        return "Function"
    elif type(obj) == types.GeneratorType:
        return "Generator"
    elif type(obj) == int:
        return "Integer"
    else:
        return "UnknownType"