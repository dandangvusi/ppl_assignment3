
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
    type_infer_error: bool = False

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

    """
    PROGRAM
    """
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

    """
    DECLARATION
    """
    # Visit Function declaration
    def visitFuncDecl(self, ast, global_envi):
        # Check redeclared function name
        if ast.name.name in global_envi[0]:
            raise Redeclared(Function(), ast.name.name)
        local_decl = [dict()]
        param_list = [dict()]
        # Check redeclared param
        for param in ast.param:
            if param.variable.name in param_list[0]:
                raise Redeclared(Parameter(), param.variable.name)
            else:
                param_type = Unknown()
                param_name = param.variable.name
                param_list[0][param_name] = MType(False, None, param_type)
                local_decl[0][param_name] = MType(False, None, param_type)
        # Check redeclared local variable
        for decl in ast.body[0]:
            self.visit(decl, local_decl)
        rtn_type = VoidType()
        new_envi = local_decl + global_envi
        # Visit statements
        for stmt in ast.body[1]:
            rt_type = self.visit(stmt, new_envi)
            if rt_type is not None:
                rtn_type = rt_type
            # if isinstance(stmt, Return):
            #     rtn_type = self.visit(stmt, new_envi)
            # else:
            #     self.visit(stmt, new_envi)
        # Add function to environment
        intype = []
        for param in ast.param:
            if param.variable.name in new_envi[0]:
                intype.append(new_envi[0][param.variable.name].restype)
            else:
                intype.append(Unknown())
        if isinstance(rtn_type, MType):
            global_envi[0][ast.name.name] = MType(True, intype, rtn_type.restype)
        else:
            global_envi[0][ast.name.name] = MType(True, intype, rtn_type)

    # Visit variable declaration
    def visitVarDecl(self, ast, o):
        # Check redeclared
        if ast.variable.name in o[0]:
            raise Redeclared(Variable(), ast.variable.name)
        # composite variable
        if len(ast.varDimen) != 0:
            if ast.varInit is not None:
                var_name = ast.variable.name
                var_dim = ast.varDimen
                value_type = self.visit(ast.varInit, o).restype.eletype
                var_type = ArrayType(var_dim, value_type)
                o[0][var_name] = MType(False, None, var_type)
            else:
                var_name = ast.variable.name
                var_dim = ast.varDimen
                value_type = Unknown()
                var_type = ArrayType(var_dim, value_type)
                o[0][var_name] = MType(False, None, var_type)
        # scalar variable
        else:
            if ast.varInit is not None:
                var_type = self.visit(ast.varInit, o)
                var_name = ast.variable.name
                o[0][var_name] = MType(False, None, var_type.restype)
            else:
                var_type = Unknown()
                var_name = ast.variable.name
                o[0][var_name] = MType(False, None, var_type)

    """
    EXPRESSIONS
    """
    # Visit binary expression
    def visitBinaryOp(self, ast, o):
        left = self.visit(ast.left, o)
        right = self.visit(ast.right, o)
        if ast.op in ["+", "-", "*", "\\", "%"]:
            # Id
            if not left.is_func and isinstance(left.restype, Unknown):
                self.type_infer_id(ast.left.name, o, MType(False, None, IntType()))
            if not right.is_func and isinstance(right.restype, Unknown):
                self.type_infer_id(ast.right.name, o, MType(False, None, IntType()))
            # Funcall
            if left.is_func and isinstance(left.restype, Unknown):
                left.restype = IntType()
                self.type_infer_func(ast.left.name, o, left)
            if right.is_func and isinstance(right.restype, Unknown):
                right.restype = IntType()
                self.type_infer_func(ast.right.name, o, right)
            if isinstance(self.visit(ast.left, o).restype, ArrayType):
                if not isinstance(self.visit(ast.left, o).restype.eletype, IntType): raise TypeMismatchInExpression(ast)
            else:
                if not isinstance(self.visit(ast.left, o).restype, IntType): raise TypeMismatchInExpression(ast)
            if isinstance(self.visit(ast.right, o).restype, ArrayType):
                if not isinstance(self.visit(ast.right, o).restype.eletype, IntType): raise TypeMismatchInExpression(ast)
            else:
                if not isinstance(self.visit(ast.right, o).restype, IntType): raise TypeMismatchInExpression(ast)
            if self.visit(ast.left, o).type_infer_error or self.visit(ast.right, o).type_infer_error:
                return MType(None, None, IntType(), True)
            return MType(None, None, IntType())
        elif ast.op in ["+.", "-.", "*.","\."]:
            # Id
            if not left.is_func and isinstance(left.restype, Unknown): self.type_infer_id(ast.left.name, o, MType(False, None, FloatType()))
            if not right.is_func and isinstance(right.restype, Unknown): self.type_infer_id(ast.right.name, o, MType(False, None, FloatType()))
            # Funcall
            if left.is_func and isinstance(left.restype, Unknown):
                left.restype = FloatType()
                self.type_infer_func(ast.left.name, o, left)
            if right.is_func and isinstance(right.restype, Unknown):
                right.restype = FloatType()
                self.type_infer_func(ast.right.name, o, right)
            if isinstance(self.visit(ast.left, o).restype, ArrayType):
                if not isinstance(self.visit(ast.left, o).restype.eletype, FloatType): raise TypeMismatchInExpression(ast)
            else:
                if not isinstance(self.visit(ast.left, o).restype, FloatType): raise TypeMismatchInExpression(ast)
            if isinstance(self.visit(ast.right, o).restype, ArrayType):
                if not isinstance(self.visit(ast.right, o).restype.eletype, FloatType): raise TypeMismatchInExpression(ast)
            else:
                if not isinstance(self.visit(ast.right, o).restype, FloatType): raise TypeMismatchInExpression(ast)
            if self.visit(ast.left, o).type_infer_error or self.visit(ast.right, o).type_infer_error:
                return MType(None, None, FloatType(), True)
            return MType(None, None, FloatType())
        elif ast.op in ["==", "!=", "<",">","<=", ">="]:
            # Id
            if not left.is_func and isinstance(left.restype, Unknown): self.type_infer_id(ast.left.name, o, MType(False, None, IntType()))
            if not right.is_func and isinstance(right.restype, Unknown): self.type_infer_id(ast.right.name, o, MType(False, None, IntType()))
            # Funcall
            if left.is_func and isinstance(left.restype, Unknown):
                left.restype = IntType()
                self.type_infer_func(ast.left.name, o, left)
            if right.is_func and isinstance(right.restype, Unknown):
                right.restype = IntType()
                self.type_infer_func(ast.right.name, o, right)
            if isinstance(self.visit(ast.left, o).restype, ArrayType):
                if not isinstance(self.visit(ast.left, o).restype.eletype, IntType): raise TypeMismatchInExpression(ast)
            else:
                if not isinstance(self.visit(ast.left, o).restype, IntType): raise TypeMismatchInExpression(ast)
            if isinstance(self.visit(ast.right, o).restype, ArrayType):
                if not isinstance(self.visit(ast.right, o).restype.eletype, IntType): raise TypeMismatchInExpression(ast)
            else:
                if not isinstance(self.visit(ast.right, o).restype, IntType): raise TypeMismatchInExpression(ast)
            if self.visit(ast.left, o).type_infer_error or self.visit(ast.right, o).type_infer_error:
                return MType(None, None, BoolType(), True)
            return MType(None, None, BoolType())
        elif ast.op in ["=/=", "<.", ">.","<=.", ">=."]:
            # Id
            if not left.is_func and isinstance(left.restype, Unknown): self.type_infer_id(ast.left.name, o, MType(False, None, FloatType()))
            if not right.is_func and isinstance(right.restype, Unknown): self.type_infer_id(ast.right.name, o, MType(False, None, FloatType()))
            # Funcall
            if left.is_func and isinstance(left.restype, Unknown):
                left.restype = FloatType()
                self.type_infer_func(ast.left.name, o, left)
            if right.is_func and isinstance(right.restype, Unknown):
                right.restype = FloatType()
                self.type_infer_func(ast.right.name, o, right)
            if isinstance(self.visit(ast.left, o).restype, ArrayType):
                if not isinstance(self.visit(ast.left, o).restype.eletype, FloatType): raise TypeMismatchInExpression(ast)
            else:
                if not isinstance(self.visit(ast.left, o).restype, FloatType): raise TypeMismatchInExpression(ast)
            if isinstance(self.visit(ast.right, o).restype, ArrayType):
                if not isinstance(self.visit(ast.right, o).restype.eletype, FloatType): raise TypeMismatchInExpression(ast)
            else:
                if not isinstance(self.visit(ast.right, o).restype, FloatType): raise TypeMismatchInExpression(ast)
            if self.visit(ast.left, o).type_infer_error or self.visit(ast.right, o).type_infer_error:
                return MType(None, None, BoolType(), True)
            return MType(None, None, BoolType())
        elif ast.op in ["&&", "||"]:
            # Id
            if not left.is_func and isinstance(left.restype, Unknown): self.type_infer_id(ast.left.name, o, MType(False, None, BoolType()))
            if not right.is_func and isinstance(right.restype, Unknown): self.type_infer_id(ast.right.name, o, MType(False, None, BoolType()))
            # Funcall
            if left.is_func and isinstance(left.restype, Unknown):
                left.restype = BoolType()
                self.type_infer_func(ast.left.name, o, left)
            if right.is_func and isinstance(right.restype, Unknown):
                right.restype = BoolType()
                self.type_infer_func(ast.right.name, o, right)
            if isinstance(self.visit(ast.left, o).restype, ArrayType):
                if not isinstance(self.visit(ast.left, o).restype.eletype, BoolType): raise TypeMismatchInExpression(ast)
            else:
                if not isinstance(self.visit(ast.left, o).restype, BoolType): raise TypeMismatchInExpression(ast)
            if isinstance(self.visit(ast.right, o).restype, ArrayType):
                if not isinstance(self.visit(ast.right, o).restype.eletype, BoolType): raise TypeMismatchInExpression(ast)
            else:
                if not isinstance(self.visit(ast.right, o).restype, BoolType): raise TypeMismatchInExpression(ast)
            if self.visit(ast.left, o).type_infer_error or self.visit(ast.right, o).type_infer_error:
                return MType(None, None, BoolType(), True)
            return MType(None, None, BoolType())

    # Visit Unary expression
    def visitUnaryOp(self, ast, o):
        body = self.visit(ast.body, o)
        op = ast.op
        if op in ["-"]:
            # Id
            if not body.is_func and isinstance(body.restype, Unknown): self.type_infer_id(ast.body.name, o, MType(False, None, IntType()))
            # Funcall
            if body.is_func and isinstance(body.restype, Unknown):
                body.restype = IntType()
                self.type_infer_func(ast.body.name, o, body)
            if not isinstance(self.visit(ast.body, o).restype, IntType): raise TypeMismatchInExpression(ast)
            if self.visit(ast.body, o).type_infer_error:
                return MType(None, None, IntType(), True)
            return MType(None, None, IntType())
        elif op in ["-."]:
            # Id
            if not body.is_func and isinstance(body.restype, Unknown): self.type_infer_id(ast.body.name, o, MType(False, None, FloatType()))
            # Funcall
            if body.is_func and isinstance(body.restype, Unknown):
                body.restype = FloatType()
                self.type_infer_func(ast.body.name, o, body)
            if not isinstance(self.visit(ast.body, o).restype, FloatType): raise TypeMismatchInExpression(ast)
            if self.visit(ast.body, o).type_infer_error:
                return MType(None, None, FloatType(), True)
            return MType(None, None, FloatType())
        elif op in ["!"]:
            # Id
            if not body.is_func and isinstance(body.restype, Unknown): self.type_infer_id(ast.body.name, o, MType(False, None, BoolType()))
            # Funcall
            if body.is_func and isinstance(body.restype, Unknown):
                body.restype = BoolType()
                self.type_infer_func(ast.body.name, o, body)
            if not isinstance(self.visit(ast.body, o).restype, BoolType): raise TypeMismatchInExpression(ast)
            if self.visit(ast.body, o).type_infer_error:
                return MType(None, None, BoolType(), True)
            return MType(None, None, BoolType())

    # Visit Call expression
    def visitCallExpr(self, ast, o):
        is_function = False
        param_type = []
        args_type = []
        rtn_type = None
        type_infer_error = False
        for env in o:
            if ast.method.name in env and env[ast.method.name].is_func:
                is_function = True
                param_type = env[ast.method.name].intype
                rtn_type = env[ast.method.name]
                break
        for arg in ast.param:
            args_type.append(self.visit(arg, o))
        # Check undeclared function
        if not is_function:
            raise Undeclared(Function(), ast.method.name)
        # number of passed arguments and number of params must be the same
        if len(args_type) != len(param_type):
            raise TypeMismatchInExpression(ast)
        # Check param types and argument type
        infer_param_type = False
        for i in range(len(param_type)):
            # If there is exists at least one type-unresolved parameter, raise TypeCannotBeInferred() for call statement
            if isinstance(args_type[i].restype, Unknown) and isinstance(param_type[i], Unknown):
                # raise TypeCannotBeInferred(ast)
                type_infer_error = True
            # Param type infer
            elif not isinstance(args_type[i].restype, Unknown) and isinstance(param_type[i], Unknown):
                param_type[i] = args_type[i]
                infer_param_type = True
            # Argument type infer
            elif isinstance(args_type[i].restype, Unknown) and not isinstance(param_type[i], Unknown):
                args_type[i] = param_type[i]
            # Type of argument and associative param must be the same
            elif type(param_type[i]) is not type(args_type[i].restype):
                raise TypeMismatchInExpression(ast)
        # Update param type list of function in environment
        if infer_param_type:
            for env in o:
                if ast.method.name in env and env[ast.method.name].is_func:
                    env[ast.method.name].intype = param_type
                    break
        if type_infer_error:
            rtn_type.type_infer_error = True
            return rtn_type
        else:
            return rtn_type

    """
    LITERALS
    """
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
        eletype = self.visit(ast.value[0], o).restype
        dimen = self.get_array_dim(ast.value)
        typ = MType(None, None, ArrayType(dimen, eletype))
        return typ

    """
    LHS
    """
    # Visit array cell
    def visitArrayCell(self, ast, o):
        arr = self.visit(ast.arr, o)
        if not isinstance(arr.restype, ArrayType):
            raise TypeMismatchInExpression(ast)
        for arr_index in ast.idx:
            index_type = self.visit(arr_index, o)
            if not isinstance(index_type.restype, IntType):
                raise TypeMismatchInExpression(ast)
        for env in o:
            if ast.arr.name in env and isinstance(env[ast.arr.name].restype, ArrayType):
                return env[ast.arr.name]

    # visit Id, if declared -> return inferred Id type, if not -> raise exception
    def visitId(self, ast, o):
        for env in o:
            if ast.name in env and not env[ast.name].is_func:
                return env[ast.name]
        raise Undeclared(Identifier(), ast.name)

    """
    STATEMENTS
    """
    # Visit Assignment statement
    def visitAssign(self, ast, o):
        # lhs is Id
        if isinstance(ast.lhs, Id):
            lhs = self.visit(ast.lhs, o)
            rhs = self.visit(ast.rhs, o)
            # Both sides can not be resolve -> raise exception
            if isinstance(lhs.restype, Unknown) and isinstance(rhs.restype, Unknown):
                raise TypeCannotBeInferred(ast)
            elif rhs.type_infer_error:
                raise TypeCannotBeInferred(ast)
            # Type infer
            elif isinstance(lhs.restype, Unknown) and not isinstance(rhs.restype, Unknown):
                for env in o:
                    if ast.lhs.name in env and not env[ast.lhs.name].is_func:
                        env[ast.lhs.name].restype = rhs.restype
                        break
            elif not isinstance(lhs.restype, Unknown) and isinstance(rhs.restype, Unknown):
                for env in o:
                    if ast.rhs.name in env and not env[ast.rhs.name].is_func:
                        env[ast.rhs.name].restype = lhs.restype
                        break
            # Both sides must be the same in type
            elif type(lhs.restype) is not type(rhs.restype):
                raise TypeMismatchInStatement(ast)
        # lhs is array cell
        else:
            lhs = self.visit(ast.lhs, o)
            rhs = self.visit(ast.rhs, o)
            # Both sides can not be resolve -> raise exception
            if isinstance(lhs.restype.eletype, Unknown) and isinstance(rhs.restype, Unknown):
                raise TypeCannotBeInferred(ast)
            elif rhs.type_infer_error:
                raise TypeCannotBeInferred(ast)
            # Type infer
            elif isinstance(lhs.restype.eletype, Unknown) and not isinstance(rhs.restype, Unknown):
                for env in o:
                    if ast.lhs.arr.name in env and not env[ast.lhs.arr.name].is_func:
                        env[ast.lhs.arr.name].restype.eletype = rhs.restype
                        break
            elif not isinstance(lhs.restype.eletype, Unknown) and isinstance(rhs.restype, Unknown):
                for env in o:
                    if ast.rhs.name in env and not env[ast.rhs.name].is_func:
                        env[ast.rhs.name].restype = lhs.restype.eletype
                        break
            # Both sides must be the same in type
            elif type(lhs.restype.eletype) is not type(rhs.restype):
                raise TypeMismatchInStatement(ast)

    # Visit If statement
    def visitIf(self, ast, o):
        rtn_type = None
        for if_stmt in ast.ifthenStmt:
            local_decl = [dict()]
            cond_type = self.visit(if_stmt[0], o)
            if isinstance(cond_type.restype, Unknown):
                raise TypeCannotBeInferred(ast)
            elif cond_type.type_infer_error:
                raise TypeCannotBeInferred(ast)
            if not isinstance(cond_type.restype, BoolType):
                raise TypeMismatchInStatement(ast)
            for var_decl in if_stmt[1]:
                self.visit(var_decl, local_decl)
            new_env = local_decl + o
            for stmt in if_stmt[2]:
                tmp = self.visit(stmt, new_env)
                if tmp is not None:
                    rtn_type = tmp
        return rtn_type

    # Visit For statement
    def visitFor(self, ast, o):
        local_decl = [dict()]
        rtn_type = None
        exp1_type = self.visit(ast.expr1, o)
        if isinstance(exp1_type.restype, Unknown):
            raise TypeCannotBeInferred(ast)
        elif exp1_type.type_infer_error:
            raise TypeCannotBeInferred(ast)
        if not isinstance(exp1_type.restype, IntType):
            raise TypeMismatchInStatement(ast)
        local_decl[0][ast.idx1.name] = MType(False, None, exp1_type.restype)
        new_env = local_decl + o
        exp3_type = self.visit(ast.expr3, new_env)
        if isinstance(exp3_type.restype, Unknown):
            raise TypeCannotBeInferred(ast)
        elif exp3_type.type_infer_error:
            raise TypeCannotBeInferred(ast)
        if not isinstance(exp3_type.restype, IntType):
            raise TypeMismatchInStatement(ast)
        exp2_type = self.visit(ast.expr2, new_env)
        if isinstance(exp2_type.restype, Unknown):
            raise TypeCannotBeInferred(ast)
        elif exp2_type.type_infer_error:
            raise TypeCannotBeInferred(ast)
        if not isinstance(exp2_type.restype, BoolType):
            raise TypeMismatchInStatement(ast)
        for var_decl in ast.loop[0]:
            self.visit(var_decl, new_env)
        for stmt in ast.loop[1]:
            tmp = self.visit(stmt, new_env)
            if tmp is not None:
                rtn_type = tmp
        return rtn_type


    # Visit Break statement
    def visitBreak(self, ast, o):
        pass

    # Visit Continue statement
    def visitContinue(self, ast, o):
        pass

    # Visit Return statement
    def visitReturn(self, ast, o):
        if ast.expr is not None:
            rtn_type = self.visit(ast.expr, o)
            if isinstance(rtn_type.restype, Unknown):
                raise TypeCannotBeInferred(ast)
            elif rtn_type.type_infer_error:
                raise TypeCannotBeInferred(ast)
            return rtn_type.restype
        return VoidType()

    # Visit DoWhile statement
    def visitDowhile(self, ast, o):
        rtn_type = None
        cond_type = self.visit(ast.exp, o)
        if isinstance(cond_type.restype, Unknown):
            raise TypeCannotBeInferred(ast)
        elif cond_type.type_infer_error:
            raise TypeCannotBeInferred(ast)
        if not isinstance(cond_type.restype, BoolType):
            raise TypeMismatchInStatement(ast)
        local_decl = [dict()]
        for var_decl in ast.sl[0]:
            self.visit(var_decl, local_decl)
        new_env = local_decl + o
        for stmt in ast.sl[1]:
            tmp = self.visit(stmt, new_env)
            if tmp is not None:
                rtn_type = tmp
        return rtn_type

    # Visit While statement
    def visitWhile(self, ast, o):
        rtn_type = None
        cond_type = self.visit(ast.exp, o)
        if isinstance(cond_type.restype, Unknown):
            raise TypeCannotBeInferred(ast)
        elif cond_type.type_infer_error:
            raise TypeCannotBeInferred(ast)
        if not isinstance(cond_type.restype, BoolType):
            raise TypeMismatchInStatement(ast)
        local_decl = [dict()]
        for var_decl in ast.sl[0]:
            self.visit(var_decl, local_decl)
        new_env = local_decl + o
        for stmt in ast.sl[1]:
            tmp = self.visit(stmt, new_env)
            if tmp is not None:
                rtn_type = tmp
        return rtn_type

    # Visit Function call statement
    def visitCallStmt(self, ast, o):
        is_function = False
        param_type = []
        args_type = []
        rtn_type = None
        for env in o:
            if ast.method.name in env and env[ast.method.name].is_func:
                is_function = True
                param_type = env[ast.method.name].intype
                rtn_type = env[ast.method.name]
                break
        for arg in ast.param:
            args_type.append(self.visit(arg, o))
        # Check undeclared function
        if not is_function:
            raise Undeclared(Function(), ast.method.name)
        # number of passed arguments and number of params must be the same
        if len(args_type) != len(param_type):
            raise TypeMismatchInStatement(ast)
        # Check param types and argument type
        infer_param_type = False
        for i in range(len(param_type)):
            # If there is exists at least one type-unresolved parameter, raise TypeCannotBeInferred() for call statement
            if isinstance(args_type[i].restype, Unknown) and isinstance(param_type[i], Unknown):
                raise TypeCannotBeInferred(ast)
            # Param type infer
            elif not isinstance(args_type[i].restype, Unknown) and isinstance(param_type[i], Unknown):
                param_type[i] = args_type[i]
                infer_param_type = True
            # Argument type infer
            elif isinstance(args_type[i].restype, Unknown) and not isinstance(param_type[i], Unknown):
                args_type[i] = param_type[i]
            # Type of argument and associative param must be the same
            elif type(param_type[i]) is not type(args_type[i].restype):
                raise TypeMismatchInStatement(ast)
        # Check return type of function is not VoidType
        if not isinstance(rtn_type.restype, VoidType):
            raise TypeMismatchInStatement(ast)
        # Update param type list of function in environment
        if infer_param_type:
            for env in o:
                if ast.method.name in env and env[ast.method.name].is_func:
                    env[ast.method.name].intype = param_type
                    break
        return rtn_type

    """
    HELPER METHODS
    """
    # Infer type for identifier
    def type_infer_id(self, id_name, env, id_type):
        for e in env:
            if id_name in e:
                e[id_name] = id_type
                break

    # Infer type for identifier
    def type_infer_func(self, func_name, env, func_type):
        for e in env:
            if func_name in e:
                e[func_name] = func_type
                break

    # Get dimension of an array literal
    def get_array_dim(self, value_list):
        if not isinstance(value_list[0], ArrayLiteral):
            return [len(value_list)]
        return [len(value_list)] + self.get_array_dim(value_list[0])
