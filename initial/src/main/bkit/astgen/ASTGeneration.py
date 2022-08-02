from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

class ASTGeneration(BKITVisitor):
    # program: glob_var_decl_part func_decl_part EOF;
    def visitProgram(self,ctx:BKITParser.ProgramContext):
        var_decls = self.visit(ctx.glob_var_decl_part())
        func_decls = self.visit(ctx.func_decl_part())
        decl = var_decls + func_decls
        return Program(decl)

    # glob_var_decl_part: var_decl_list?;
    def visitGlob_var_decl_part(self, ctx:BKITParser.Glob_var_decl_partContext):
        if ctx.var_decl_list():
            return self.visit(ctx.var_decl_list())
        else:
            return []

    # var_decl_list: var_decl var_decl_list | var_decl;
    def visitVar_decl_list(self, ctx:BKITParser.Var_decl_listContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.var_decl())
        else:
            return self.visit(ctx.var_decl()) + self.visit(ctx.var_decl_list())

    # var_decl: VAR COLON var_list SEMI;
    def visitVar_decl(self, ctx:BKITParser.Var_declContext):
        return self.visit(ctx.var_list())

    # var_list: var COMMA var_list | var;
    def visitVar_list(self, ctx:BKITParser.Var_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.var())]
        else:
            return [self.visit(ctx.var())] + self.visit(ctx.var_list())

    # var: scalar_var | compo_var;
    def visitVar(self, ctx:BKITParser.VarContext):
        if ctx.scalar_var():
            return self.visit(ctx.scalar_var())
        else:
            return self.visit(ctx.compo_var())

    # scalar_var: ID (ASSIGN literal)?;
    def visitScalar_var(self, ctx:BKITParser.Scalar_varContext):
        variable = Id(ctx.ID().getText())
        varDimen = []
        if ctx.ASSIGN():
            varInit = self.visit(ctx.literal())
            return VarDecl(variable, varDimen, varInit)
        else:
            return VarDecl(variable, varDimen, None)

    # compo_var: ID dimensions (ASSIGN array_lit)?;
    def visitCompo_var(self, ctx:BKITParser.Compo_varContext):
        variable = Id(ctx.ID().getText())
        varDimen = self.visit(ctx.dimensions())
        if ctx.ASSIGN():
            varInit = self.visit(ctx.array_lit())
            return VarDecl(variable, varDimen, varInit)
        else:
            return VarDecl(variable, varDimen, None)


    # func_decl_part: func_decl_list?;
    def visitFunc_decl_part(self, ctx:BKITParser.Func_decl_partContext):
        if ctx.func_decl_list():
            return self.visit(ctx.func_decl_list())
        else:
            return []

    # func_decl_list: func_decl func_decl_list | func_decl;
    def visitFunc_decl_list(self, ctx:BKITParser.Func_decl_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.func_decl())]
        else:
            return [self.visit(ctx.func_decl())] + self.visit(ctx.func_decl_list())

    # func_decl: FUNCTION COLON ID func_param? func_body;
    def visitFunc_decl(self, ctx:BKITParser.Func_declContext):
        name = Id(ctx.ID().getText())
        func_var_decls, func_stmts = self.visit(ctx.func_body())
        body = (func_var_decls, func_stmts)
        if ctx.func_param():
            param = self.visit(ctx.func_param())
            return FuncDecl(name, param, body)
        else:
            param = []
            return FuncDecl(name, param, body)

    # func_param: PARAMETER COLON param_list;
    def visitFunc_param(self, ctx:BKITParser.Func_paramContext):
        return self.visit(ctx.param_list())

    # param_list: param COMMA param_list | param;
    def visitParam_list(self, ctx:BKITParser.Param_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.param())]
        else:
            return [self.visit(ctx.param())] + self.visit(ctx.param_list())

    # param: ID | ID dimensions;
    def visitParam(self, ctx:BKITParser.ParamContext):
        if ctx.getChildCount() == 1:
            variable = Id(ctx.ID().getText())
            varDimen = []
            varInit = None
            return VarDecl(variable, varDimen, varInit)
        else:
            variable = Id(ctx.ID().getText())
            varDimen = self.visit(ctx.dimensions())
            varInit = None
            return VarDecl(variable, varDimen, varInit)

    # func_body: BODY COLON stmt_list ENDBODY DOT;
    def visitFunc_body(self, ctx:BKITParser.Func_bodyContext):
        return self.visit(ctx.stmt_list())

    # stmt_list: var_decl_stmt_list? other_stmt_list?;
    def visitStmt_list(self, ctx:BKITParser.Stmt_listContext):
        if ctx.getChildCount() == 2:
            var_decls = self.visit(ctx.var_decl_stmt_list())
            stmts = self.visit(ctx.other_stmt_list())
            return var_decls, stmts
        elif ctx.getChildCount() == 1 and ctx.var_decl_stmt_list():
            var_decls = self.visit(ctx.var_decl_stmt_list())
            stmts = []
            return var_decls, stmts
        elif ctx.getChildCount() == 1 and ctx.other_stmt_list():
            var_decls = []
            stmts = self.visit(ctx.other_stmt_list())
            return var_decls, stmts
        else:
            var_decls = []
            stmts = []
            return var_decls, stmts

    # var_decl_stmt_list: var_decl_stmt var_decl_stmt_list | var_decl_stmt;
    def visitVar_decl_stmt_list(self, ctx:BKITParser.Var_decl_stmt_listContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.var_decl_stmt())
        else:
            return self.visit(ctx.var_decl_stmt()) + self.visit(ctx.var_decl_stmt_list())

    # other_stmt_list: other_stmt other_stmt_list | other_stmt;
    def visitOther_stmt_list(self, ctx:BKITParser.Other_stmt_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.other_stmt())]
        else:
            return [self.visit(ctx.other_stmt())] + self.visit(ctx.other_stmt_list())

    # other_stmt: assign_stmt | if_stmt | for_stmt | while_stmt | do_while_stmt | break_stmt | continue_stmt | call_stmt | return_stmt;
    def visitOther_stmt(self, ctx:BKITParser.Other_stmtContext):
        if ctx.assign_stmt():
            return self.visit(ctx.assign_stmt())
        elif ctx.if_stmt():
            return self.visit(ctx.if_stmt())
        elif ctx.for_stmt():
            return self.visit(ctx.for_stmt())
        elif ctx.while_stmt():
            return self.visit(ctx.while_stmt())
        elif ctx.do_while_stmt():
            return self.visit(ctx.do_while_stmt())
        elif ctx.break_stmt():
            return self.visit(ctx.break_stmt())
        elif ctx.continue_stmt():
            return self.visit(ctx.continue_stmt())
        elif ctx.call_stmt():
            return self.visit(ctx.call_stmt())
        else:
            return self.visit(ctx.return_stmt())

    # var_decl_stmt: VAR COLON var_list SEMI;
    def visitVar_decl_stmt(self, ctx: BKITParser.Var_decl_stmtContext):
        return self.visit(ctx.var_list())

    # assign_stmt: (ID | index_exp) ASSIGN exp SEMI;
    def visitAssign_stmt(self, ctx: BKITParser.Assign_stmtContext):
        rhs = self.visit(ctx.exp())
        if ctx.ID():
            lhs = Id(ctx.ID().getText())
            return Assign(lhs, rhs)
        else:
            lhs = self.visit(ctx.index_exp())
            return Assign(lhs, rhs)

    # if_stmt: IF exp THEN stmt_list else_if_list? (ELSE stmt_list)? ENDIF DOT;
    def visitIf_stmt(self, ctx:BKITParser.If_stmtContext):
        # if part
        ifthenStmt = []
        if_exp  = self.visit(ctx.exp())
        if_var_decls, if_stmts = self.visit(ctx.stmt_list(0))
        if_tuple = (if_exp, if_var_decls, if_stmts)
        ifthenStmt.append(if_tuple)
        # if part only
        if ctx.getChildCount() == 6:
            elseStmt = ([], [])
            return If(ifthenStmt, elseStmt)
        # if part & else if part
        elif ctx.getChildCount() == 7:
            else_if_tuples = self.visit(ctx.else_if_list())
            ifthenStmt = ifthenStmt + else_if_tuples
            elseStmt = ([], [])
            return If(ifthenStmt, elseStmt)
        # if part & else part
        elif ctx.getChildCount() == 8:
            else_var_decls, else_stmts = self.visit(ctx.stmt_list(1))
            elseStmt = (else_var_decls, else_stmts)
            return If(ifthenStmt, elseStmt)
        # if part & else if part & else part
        else:
            else_if_tuples = self.visit(ctx.else_if_list())
            ifthenStmt = ifthenStmt + else_if_tuples
            else_var_decls, else_stmts = self.visit(ctx.stmt_list(1))
            elseStmt = (else_var_decls, else_stmts)
            return If(ifthenStmt, elseStmt)

    # else_if_list: else_if else_if_list | else_if;
    def visitElse_if_list(self, ctx:BKITParser.Else_if_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.else_if())]
        else:
            return [self.visit(ctx.else_if())] + self.visit(ctx.else_if_list())

    # else_if: ELSEIF exp THEN stmt_list;
    def visitElse_if(self, ctx:BKITParser.Else_ifContext):
        else_if_exp = self.visit(ctx.exp())
        else_if_var_decls, else_if_stmts = self.visit(ctx.stmt_list())
        return (else_if_exp, else_if_var_decls, else_if_stmts)

    # for_stmt: FOR LB ID ASSIGN exp COMMA exp COMMA exp RB DO stmt_list ENDFOR DOT;
    def visitFor_stmt(self, ctx:BKITParser.For_stmtContext):
        idx1 = Id(ctx.ID().getText())
        expr1 = self.visit(ctx.exp(0))
        expr2 = self.visit(ctx.exp(1))
        expr3 = self.visit(ctx.exp(2))
        var_decls, stmts = self.visit(ctx.stmt_list())
        loop = (var_decls, stmts)
        return For(idx1, expr1, expr2, expr3, loop)

    # while_stmt: WHILE exp DO stmt_list ENDWHILE DOT;
    def visitWhile_stmt(self, ctx:BKITParser.While_stmtContext):
        exp = self.visit(ctx.exp())
        var_decls, stmts = self.visit(ctx.stmt_list())
        sl = (var_decls, stmts)
        return While(exp, sl)

    # do_while_stmt: DO stmt_list WHILE exp ENDDO DOT;
    def visitDo_while_stmt(self, ctx:BKITParser.Do_while_stmtContext):
        exp = self.visit(ctx.exp())
        var_decls, stmts = self.visit(ctx.stmt_list())
        sl = (var_decls, stmts)
        return Dowhile(sl, exp)

    # break_stmt: BREAK SEMI;
    def visitBreak_stmt(self, ctx:BKITParser.Break_stmtContext):
        return Break()

    # continue_stmt: CONTINUE SEMI;
    def visitContinue_stmt(self, ctx:BKITParser.Continue_stmtContext):
        return Continue()

    # call_stmt: ID LB exp_list? RB SEMI;
    def visitCall_stmt(self, ctx:BKITParser.Call_stmtContext):
        method = Id(ctx.ID().getText())
        if ctx.exp_list():
            param = self.visit(ctx.exp_list())
            return CallStmt(method, param)
        else:
            param = []
            return CallStmt(method, param)


    # return_stmt: RETURN exp? SEMI;
    def visitReturn_stmt(self, ctx:BKITParser.Return_stmtContext):
        if ctx.exp():
            expr = self.visit(ctx.exp())
            return Return(expr)
        return Return(None)

    # exp: exp1 (EQ_I | NEQ_I | LT_I | GT_I | LTE_I | GTE_I | NEQ_F | LT_F | GT_F | LTE_F | GTE_F) exp1 | exp1;
    def visitExp(self, ctx:BKITParser.ExpContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp1(0))
        else:
            op = ""
            if ctx.EQ_I():
                op = ctx.EQ_I().getText()
            elif ctx.NEQ_I():
                op = ctx.NEQ_I().getText()
            elif ctx.LT_I():
                op = ctx.LT_I().getText()
            elif ctx.GT_I():
                op = ctx.GT_I().getText()
            elif ctx.LTE_I():
                op = ctx.LTE_I().getText()
            elif ctx.GTE_I():
                op = ctx.GTE_I().getText()
            elif ctx.NEQ_F():
                op = ctx.NEQ_F().getText()
            elif ctx.LT_F():
                op = ctx.LT_F().getText()
            elif ctx.GT_F():
                op = ctx.GT_F().getText()
            elif ctx.LTE_F():
                op = ctx.LTE_F().getText()
            else:
                op = ctx.GTE_F().getText()
            left = self.visit(ctx.exp1(0))
            right = self.visit(ctx.exp1(1))
            return BinaryOp(op, left, right)

    # exp1: exp1 (AND | OR) exp2 | exp2;
    def visitExp1(self, ctx:BKITParser.Exp1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp2())
        else:
            op = ""
            if ctx.AND():
                op = ctx.AND().getText()
            else:
                op = ctx.OR().getText()
            left = self.visit(ctx.exp1())
            right = self.visit(ctx.exp2())
            return BinaryOp(op, left, right)

    # exp2: exp2 (ADD_I | ADD_F | SUB_I | SUB_F) exp3 | exp3;
    def visitExp2(self, ctx:BKITParser.Exp2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp3())
        else:
            op = ""
            if ctx.ADD_I():
                op = ctx.ADD_I().getText()
            elif ctx.ADD_F():
                op = ctx.ADD_F().getText()
            elif ctx.SUB_I():
                op = ctx.SUB_I().getText()
            else:
                op = ctx.SUB_F().getText()
            left = self.visit(ctx.exp2())
            right = self.visit(ctx.exp3())
            return BinaryOp(op, left, right)

    # exp3: exp3 (MUL_I | MUL_F | DIV_I | DIV_F | MOD_I) exp4 | exp4;
    def visitExp3(self, ctx:BKITParser.Exp3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp4())
        else:
            op = ""
            if ctx.MUL_I():
                op = ctx.MUL_I().getText()
            elif ctx.MUL_F():
                op = ctx.MUL_F().getText()
            elif ctx.DIV_I():
                op = ctx.DIV_I().getText()
            elif ctx.DIV_F():
                op = ctx.DIV_F().getText()
            else:
                op = ctx.MOD_I().getText()
            left = self.visit(ctx.exp3())
            right = self.visit(ctx.exp4())
            return BinaryOp(op, left, right)

    # exp4: NOT exp4 | exp5;
    def visitExp4(self, ctx:BKITParser.Exp4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp5())
        else:
            op = ctx.NOT().getText()
            body = self.visit(ctx.exp4())
            return UnaryOp(op, body)

    # exp5: (SUB_I | SUB_F) exp5 | index_exp | func_call_exp;
    def visitExp5(self, ctx:BKITParser.Exp5Context):
        if ctx.getChildCount() == 2:
            op = ""
            if ctx.SUB_I():
                op = ctx.SUB_I().getText()
            else:
                op = ctx.SUB_F().getText()
            body = self.visit(ctx.exp5())
            return UnaryOp(op, body)
        elif ctx.index_exp():
            return self.visit(ctx.index_exp())
        else:
            return self.visit(ctx.func_call_exp())

    # index_exp: (ID|func_call) index_operator;
    def visitIndex_exp(self, ctx:BKITParser.Index_expContext):
        if ctx.ID():
            arr = Id(ctx.ID().getText())
            idx = self.visit(ctx.index_operator())
            return ArrayCell(arr, idx)
        else:
            arr = self.visit(ctx.func_call())
            idx = self.visit(ctx.index_operator())
            return ArrayCell(arr, idx)

    # index_operator: LS exp RS | LS exp RS index_operator;
    def visitIndex_operator(self, ctx:BKITParser.Index_operatorContext):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.exp())]
        else:
            return [self.visit(ctx.exp())] + self.visit(ctx.index_operator())

    # func_call_exp: func_call | operand;
    def visitFunc_call_exp(self, ctx:BKITParser.Func_call_expContext):
        if ctx.func_call():
            return self.visit(ctx.func_call())
        else:
            return self.visit(ctx.operand())

    # operand: literal | ID | LB exp RB;
    def visitOperand(self, ctx:BKITParser.OperandContext):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        else:
            return self.visit(ctx.exp())

    # func_call: ID LB exp_list? RB;
    def visitFunc_call(self, ctx:BKITParser.Func_callContext):
        method = Id(ctx.ID().getText())
        if ctx.exp_list():
            param = self.visit(ctx.exp_list())
            return CallExpr(method, param)
        else:
            param = []
            return CallExpr(method, param)

    # exp_list: exp COMMA exp_list | exp;
    def visitExp_list(self, ctx:BKITParser.Exp_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.exp())]
        else:
            return [self.visit(ctx.exp())] + self.visit(ctx.exp_list())

    # literal: DEC_INT_LIT | HEX_INT_LIT | OCT_INT_LIT | FLT_LIT | BOOL_LIT | STR_LIT | array_lit;
    def visitLiteral(self, ctx:BKITParser.LiteralContext):
        if ctx.DEC_INT_LIT():
            return IntLiteral(int(ctx.DEC_INT_LIT().getText(), base = 10))
        elif ctx.HEX_INT_LIT():
            return IntLiteral(int(ctx.HEX_INT_LIT().getText(), base = 16))
        elif ctx.OCT_INT_LIT():
            return IntLiteral(int(ctx.OCT_INT_LIT().getText(), base = 8))
        elif ctx.FLT_LIT():
            return FloatLiteral(float(ctx.FLT_LIT().getText()))
        elif ctx.BOOL_LIT():
            return BooleanLiteral(ctx.BOOL_LIT().getText() == "True")
        elif ctx.STR_LIT():
            return StringLiteral(ctx.STR_LIT().getText())
        else:
            return self.visit(ctx.array_lit())

    # dimensions: dimension dimensions | dimension;
    def visitDimensions(self, ctx:BKITParser.DimensionsContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.dimension())]
        else:
            return [self.visit(ctx.dimension())] + self.visit(ctx.dimensions())

    # dimension: LS (DEC_INT_LIT | HEX_INT_LIT | OCT_INT_LIT) RS;
    def visitDimension(self, ctx:BKITParser.DimensionContext):
        if ctx.DEC_INT_LIT():
            return int(ctx.DEC_INT_LIT().getText(), base = 10)
        elif ctx.HEX_INT_LIT():
            return int(ctx.HEX_INT_LIT().getText(), base = 16)
        elif ctx.OCT_INT_LIT():
            return int(ctx.OCT_INT_LIT().getText(), base = 8)

    # array_lit: LC array_element_list RC;
    def visitArray_lit(self, ctx:BKITParser.Array_litContext):
        value = self.visit(ctx.array_element_list())
        return ArrayLiteral(value)

    # array_element_list: array_element COMMA array_element_list | array_element;
    def visitArray_element_list(self, ctx:BKITParser.Array_element_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.array_element())]
        else:
            return [self.visit(ctx.array_element())] + self.visit(ctx.array_element_list())

    # array_element: literal;
    def visitArray_element(self, ctx:BKITParser.Array_elementContext):
        return self.visit(ctx.literal())