
"""
 * @author nhphung
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
        [self.visit(x,o) for x in ast.decl]

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
        # number of passed arguments is not equal to number of param
        if len(args_type) != len(param_type):
            raise TypeMismatchInStatement(ast)
        param_type_vals = param_type.values()
        param_type_names = param_type.keys()



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

    def visitId(self, ast, o):
        pass