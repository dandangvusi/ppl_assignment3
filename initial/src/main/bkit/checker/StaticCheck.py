
"""
 * @author Dang Vu Si Dan
"""
from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from AST import * 
from Visitor import *
from StaticError import *
from functools import *

class Type(ABC):
    __metaclass__ = ABCMeta
    pass
class Prim(Type):
    __metaclass__ = ABCMeta
    pass
class IntType(Prim):
    pass
class FloatType(Prim):
    pass
class StringType(Prim):
    pass
class BoolType(Prim):
    pass
class VoidType(Type):
    pass
class Unknown(Type):
    pass
class ArrayType():
    pass

@dataclass
class ArrayType(Type):
    dimen:List[int]
    eletype: Type

@dataclass
class MType:
    is_func: bool
    intype:List[Type]
    restype:Type

@dataclass
class Symbol:
    name: str
    mtype:Type

class StaticChecker(BaseVisitor):
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = [dict()]
        builtin_func = {
            "int_of_float": MType(True, [FloatType()], IntType()),
            "float_of_int": MType(True, [IntType()], FloatType()),
            "int_of_string": MType(True, [StringType()], IntType()),
            "string_of_int": MType(True, [IntType()], StringType()),
            "float_of_string": MType(True, [StringType()], FloatType()),
            "string_of_float": MType(True, [FloatType()], StringType()),
            "bool_of_string": MType(True, [StringType()], BoolType()),
            "string_of_bool": MType(True, [BoolType()], StringType()),
            "read": MType(True, [], StringType()),
            "printLn": MType(True, [], VoidType()),
            "printStr": MType(True, [StringType()], VoidType()),
            "printStrLn": MType(True, [StringType()], VoidType())}
        self.global_envi.append(builtin_func)
   
    def check(self):
        return self.visit(self.ast,self.global_envi)

    def visitProgram(self,ast, global_envi):
        # Check redeclared
        for decl in ast.decl:
            self.visit(decl, global_envi)
        # Check main function
        is_main_func_defined = False
        for decl in ast.decl:
            if isinstance(decl, FuncDecl) and decl.name.name == "main":
                is_main_func_defined = True
                break
        if not is_main_func_defined:
            raise NoEntryPoint()

    # Visit Function declaration
    def visitFuncDecl(self, ast, global_envi):
        # Check redeclared function name
        if ast.name.name in global_envi[0]:
            raise Redeclared(Function(), ast.name.name)
        local_decl = [dict()]
        param_list = [dict()]
        # Check redeclared param
        for param in ast.param:
            if param.variable.name in param_list:
                raise Redeclared(Parameter(), param.variable.name)
            else:
                param_type = Unknown()
                param_name = param.variable.name
                param_list[0][param_name] = MType(False, None, param_type)
                local_decl[0][param_name] = MType(False, None, param_type)
        # Check redeclared local variable
        for decl in ast.body[0]:
            if decl.variable.name in local_decl[0]:
                raise Redeclared(Variable(), decl.variable.name)
            else:
                var_type = self.visit(decl.varInit)
                var_name = decl.variable.name
                local_decl[0][var_name] = MType(False, None, var_type)
        rtn_type = Unknown()
        new_envi = local_decl + global_envi
        # Visit statements
        for stmt in ast.body[1]:
            if isinstance(stmt, Return):
                rtn_type = self.visit(stmt.expr)
            else:
                self.visit(stmt, new_envi)
        # Add function to environment
        intype = []
        for param in ast.param:
            intype.append(Unknown)
        global_envi[0][ast.name.name] = MType(True, intype, rtn_type)

    # Visit variable declaration
    def visitVarDecl(self, ast, o):
        # Check redeclared
        if ast.variable.name in o[0]:
            raise Redeclared(Variable(), ast.variable.name)
        # composite variable
        if len(ast.varDimen) != 0:
            var_type = ArrayType()
            var_name = ast.variable.name
            o[0][var_name] = MType(False, None, var_type)
        # scalar variable
        else:
            if ast.varInit is not None:
                var_type = self.visit(ast.varInit)
                var_name = ast.variable.name
                o[0][var_name] = MType(False, None, var_type)
            else:
                var_type = Unknown()
                var_name = ast.variable.name
                o[0][var_name] = MType(False, None, var_type)

    # Visit Assignment statement
    def visitAssign(self, ast, o):
        lhs = self.visit(ast.lhs, o)
        rhs = self.visit(ast.rhs, o)
        # Both sides can not be resolve -> raise exception
        if isinstance(lhs.restype, Unknown) and isinstance(rhs.restype, Unknown):
            raise TypeCannotBeInferred(ast)
        # Type infer
        elif isinstance(lhs.restype, Unknown) and not isinstance(rhs.restype, Unknown):
            for env in o:
                if ast.lhs.name.name in env:
                    env[ast.lhs.name.name] = rhs
                    break
        elif not isinstance(lhs.restype, Unknown) and isinstance(rhs.restype, Unknown):
            for env in o:
                if ast.rhs.name.name in env:
                    env[ast.rhs.name.name] = lhs
                    break
        # Both sides must be the same in type
        elif lhs.restype != rhs.restype:
            raise TypeMismatchInStatement(ast)

    # Visit Function call statement
    def visitCallStmt(self, ast, o):
        is_function = False
        param_type = []
        args_type = []
        for env in o:
            if ast.method.name in env and env[ast.method.name].is_func:
                is_function = True
                param_type = env[ast.method.name].intype
                break
        for arg in ast.param:
            args_type.append(self.visit(arg, o))
        # Check undeclared function
        if not is_function:
            raise Undeclared(Function(),ast.method.name)
        # number of passed arguments and number of params must be the same
        if len(args_type) != len(param_type):
            raise TypeMismatchInStatement(ast)
        # Check param types and argument type
        infer_param_type = False
        for i in range(len(param_type)):
            # If there is exists at least one type-unresolved parameter, raise TypeCannotBeInferred() for call statement
            if isinstance(args_type[i].restype, Unknown):
                raise TypeCannotBeInferred(ast)
            # Param type infer
            elif not isinstance(args_type[i].restype, Unknown) and isinstance(param_type[i].restype, Unknown):
                param_type[i] = args_type[i]
                infer_param_type = True
            # Type of argument and associative param must be the same
            elif param_type[i].restype != args_type[i].restype:
                raise TypeMismatchInStatement(ast)
        # Update param type list of function in environment
        if infer_param_type:
            for env in o:
                if ast.method.name in env and env[ast.method.name].is_func:
                    env[ast.method.name].intype = param_type
                    break



    # Visit binary expression
    def visitBinaryOp(self, ast, o):
        if ast.op in ["+", "-", "*", "\\", "%"]:
            pass

        if ast.op in ["+", "-", "*","\\","%"]:
            if isinstance(self.visit(ast.left, o), Unknown): o[0][ast.left.name] = IntType()
            if isinstance(self.visit(ast.right, o), Unknown): o[0][ast.right.name] = IntType()
            if not isinstance(self.visit(ast.left, o), IntType): raise TypeMismatchInExpression(ast)
            elif not isinstance(self.visit(ast.right, o), IntType): raise TypeMismatchInExpression(ast)
            return IntType()
        elif ast.op in ["+.", "-.", "*.","\."]:
            if isinstance(self.visit(ast.left, o), Unknown): o[0][ast.left.name] = FloatType()
            if isinstance(self.visit(ast.right, o), Unknown): o[0][ast.right.name] = FloatType()
            if not isinstance(self.visit(ast.left, o), FloatType): raise TypeMismatchInExpression(ast)
            elif not isinstance(self.visit(ast.right, o), FloatType): raise TypeMismatchInExpression(ast)
            return FloatType()
        elif ast.op in ["==", "!=", "<",">","<=", ">="]:
            if isinstance(self.visit(ast.left, o), Unknown): o[0][ast.left.name] = IntType()
            if isinstance(self.visit(ast.right, o), Unknown): o[0][ast.right.name] = IntType()
            if not isinstance(self.visit(ast.left, o), IntType): raise TypeMismatchInExpression(ast)
            elif not isinstance(self.visit(ast.right, o), IntType): raise TypeMismatchInExpression(ast)
            return BoolType()
        elif ast.op in ["=/=", "<.", ">.","<=.", ">=."]:
            if isinstance(self.visit(ast.left, o), Unknown): o[0][ast.left.name] = FloatType()
            if isinstance(self.visit(ast.right, o), Unknown): o[0][ast.right.name] = FloatType()
            if not isinstance(self.visit(ast.left, o), FloatType): raise TypeMismatchInExpression(ast)
            elif not isinstance(self.visit(ast.right, o), FloatType): raise TypeMismatchInExpression(ast)
            return BoolType()
        elif ast.op in ["&&", "||"]:
            if isinstance(self.visit(ast.left, o), Unknown): o[0][ast.left.name] = BoolType()
            if isinstance(self.visit(ast.right, o), Unknown): o[0][ast.right.name] = BoolType()
            if not isinstance(self.visit(ast.left, o), BoolType): raise TypeMismatchInExpression(ast)
            elif not isinstance(self.visit(ast.right, o), BoolType): raise TypeMismatchInExpression(ast)
            return BoolType()

    # Visit Unary expression
    def visitUnaryOp(self, ast, o):
        if ast.op in ["-"]:
            if isinstance(self.visit(ast.body, o), Unknown): o[0][ast.body.name] = IntType()
            if not isinstance(self.visit(ast.body, o), IntType): raise TypeMismatchInExpression(ast)
            return IntType()
        elif ast.op in ["-."]:
            if isinstance(self.visit(ast.body, o), Unknown): o[0][ast.body.name] = FloatType()
            if not isinstance(self.visit(ast.body, o), FloatType): raise TypeMismatchInExpression(ast)
            return FloatType()
        elif ast.op in ["!"]:
            if isinstance(self.visit(ast.body, o), Unknown): o[0][ast.body.name] = BoolType()
            if not isinstance(self.visit(ast.body, o), BoolType): raise TypeMismatchInExpression(ast)
            return BoolType()

    # Visit array cell
    def visitArrayCell(self, ast, o):
        arr = self.visit(ast.arr)
        if not isinstance(arr, ArrayType):
            raise TypeMismatchInExpression(ast)
        for arr_index in ast.idx:
            index_type = self.visit(arr_index)
            if not isinstance(index_type, IntType):
                raise TypeMismatchInExpression(ast)

    # Visit literals -> return type of literal
    def visitIntLiteral(self, ast, o):
        typ = MType(None, None, IntType())
        return typ

    def visitFloatLiteral(self, ast, o):
        typ = MType(None, None, FloatType())
        return typ

    def visitStringLiteral(self, ast, o):
        typ = MType(None, None, StringType())
        return typ

    def visitBooleanLiteral(self, ast, o):
        typ = MType(None, None, BoolType())
        return typ

    def visitArrayLiteral(self, ast, o):
        typ = MType(None, None, ArrayType())
        return typ
    # visit Id, if declared -> return inferred Id type, if not -> raise exception
    def visitId(self, ast, o):
        for env in o:
            if ast.name.name in env and not env[ast.name.name].is_func:
                return env[ast.name.name]
        raise Undeclared(Identifier(), ast.name.name)