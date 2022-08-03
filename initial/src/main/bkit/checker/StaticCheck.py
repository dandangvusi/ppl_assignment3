
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
    intype:List[Type]
    restype:Type

@dataclass
class Symbol:
    name: str
    mtype:Type

class StaticChecker(BaseVisitor):
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = [
            Symbol("int_of_float",MType([FloatType()],IntType())),
            Symbol("float_of_int",MType([IntType()],FloatType())),
            Symbol("int_of_string",MType([StringType()],IntType())),
            Symbol("string_of_int",MType([IntType()],StringType())),
            Symbol("float_of_string",MType([StringType()],FloatType())),
            Symbol("string_of_float",MType([FloatType()],StringType())),
            Symbol("bool_of_string",MType([StringType()],BoolType())),
            Symbol("string_of_bool",MType([BoolType()],StringType())),
            Symbol("read",MType([],StringType())),
            Symbol("printLn",MType([],VoidType())),
            Symbol("printStr",MType([StringType()],VoidType())),
            Symbol("printStrLn",MType([StringType()],VoidType()))]
   
    def check(self):
        return self.visit(self.ast,self.global_envi)

    def visitProgram(self,ast, o):
        # Check main function
        is_main_func_defined = False
        for decl in ast.decl:
            if isinstance(decl, FuncDecl) and decl.name.name == "main":
                is_main_func_defined = True
                break
        if not is_main_func_defined:
            raise NoEntryPoint()
        # Check redeclared


    # Visit Function declaration
    def visitFuncDecl(self, ast, o):
        if ast.name.name in o[0]:
            raise Redeclared(Function(),ast.name.name)
        param_type = [dict()]
        local_decl = [dict()]
        for param in ast.param:
            self.visit(param, param_type)
        for decl in ast.body[0]:
            self.visit(decl, local_decl)
        local_env = param_type + local_decl
        for stmt in ast.body[1]:
            self.visit(stmt, local_env)
        o[0][ast.name.name] = local_env[0]

    # Visit variable declaration
    def visitVarDecl(self, ast, o):
        if ast.variable.name in o[0]:
            raise Redeclared(Variable(),ast.variable.name)
        # composite variable
        if len(ast.varDimen) != 0:
            if ast.varInit is not None:
                o[0][ast.variable.name] = self.visit(ast.varInit)
            else:
                o[0][ast.variable.name] = Unknown()
        # scalar variable
        else:
            if ast.varInit is not None:
                o[0][ast.variable.name] = self.visit(ast.varInit)
            else:
                o[0][ast.variable.name] = Unknown()

    # Visit Assignment statement
    def visitAssign(self, ast, o):
        lhs = self.visit(ast.lhs, o)
        rhs = self.visit(ast.rhs, o)
        # Both sides can not be resolve -> raise exception
        if isinstance(lhs, Unknown) and isinstance(rhs, Unknown):
            raise TypeCannotBeInferred(ast)
        # Type infer
        elif isinstance(lhs, Unknown) and not isinstance(rhs, Unknown):
            for env in o:
                if ast.lhs.name.name in env:
                    env[ast.lhs.name.name] = rhs
                    break
        elif not isinstance(lhs, Unknown) and isinstance(rhs, Unknown):
            for env in o:
                if ast.rhs.name.name in env:
                    env[ast.rhs.name.name] = lhs
                    break
        # Both sides must be the same in type
        elif lhs != rhs:
            raise TypeMismatchInStatement(ast)

    # Visit Function call statement
    def visitCallStmt(self, ast, o):
        isFunction = False
        param_type = dict()
        args_type = []
        for env in o:
            if ast.method.name in env and isinstance(env[ast.method.name], dict):
                isFunction = True
                param_type = env[ast.method.name]
                break
        for arg in ast.param:
            args_type.append(self.visit(arg, o))
        if isFunction == False:
            raise Undeclared(Function(),ast.method.name)
        # number of passed arguments and number of params must be the same
        if len(args_type) != len(param_type):
            raise TypeMismatchInStatement(ast)
        param_type_vals = param_type.values()
        param_type_names = param_type.keys()
        for i in range(len(param_type_vals)):
            # If there is exists at least one type-unresolved parameter, raise TypeCannotBeInferred() for call statement
            if isinstance(args_type[i], Unknown):
                raise TypeCannotBeInferred(ast)
            elif not isinstance(args_type[i], Unknown):
                param_type[param_type_names[i]] = args_type[i]
            # Type of argument and associative param must be the same
            elif param_type_vals[i] != args_type[i]:
                raise TypeMismatchInStatement(ast)



    # Visit binary expression
    def visitBinaryOp(self, ast, o):
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

    # Visit literals -> return type of literal
    def visitIntLiteral(self, ast, o):
        return IntType()
    def visitFloatLiteral(self, ast, o):
        return FloatType()

    def visitStringLiteral(self, ast, o):
        return StringType()

    def visitBooleanLiteral(self, ast, o):
        return BoolType()

    def visitArrayLiteral(self, ast, o):
        return ArrayType()
    # visit Id, if declared -> return inferred Id type, if not -> raise exception
    def visitId(self, ast, o):
        for env in o:
            if ast.name.name in env and not isinstance(env[ast.name.name], dict):
                return env[ast.name.name]
        raise Undeclared(Identifier(), ast.name.name)