import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):
    def test_1(self):
        """Test undeclared function"""
        input = Program([FuncDecl(Id("main"),[],([],[
            CallExpr(Id("foo"),[])]))])
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_2(self):
        """Test different number of param in call expression"""
        input = Program([
                FuncDecl(Id("main"),[],([],[
                    CallStmt(Id("printStrLn"),[
                        CallExpr(Id("read"),[IntLiteral(4)])
                        ])]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_3(self):
        """Test different number of param in call statement"""
        input = Program([
                FuncDecl(Id("main"),[],([],[
                    CallStmt(Id("printStrLn"),[])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_4(self):
        """Test no entry point"""
        input = Program([FuncDecl(Id("add_one"),[VarDecl(Id("n"),[],None)],([],[Return(BinaryOp("+",Id("n"),IntLiteral(1)))]))])
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_5(self):
        """Test redeclared global variable"""
        input = Program([VarDecl(Id("x"),[],IntLiteral(10)),VarDecl(Id("x"),[],IntLiteral(20)),
                              FuncDecl(Id("main"),[],
                                ([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],
                                 [Assign(Id("a"),BinaryOp("+",Id("x"),Id("y"))),
                                  Assign(Id("b"),BinaryOp("*",IntLiteral(2),Id("y")))]))])
        expect = str(Redeclared(Variable(), "x"))
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_6(self):
        """Test redeclared local variable"""
        input = Program([VarDecl(Id("x"),[],IntLiteral(10)),VarDecl(Id("y"),[],IntLiteral(20)),
                              FuncDecl(Id("main"),[],
                                ([VarDecl(Id("a"),[],None),VarDecl(Id("a"),[],None)],
                                 [Assign(Id("a"),BinaryOp("+",Id("x"),Id("y"))),
                                  Assign(Id("b"),BinaryOp("*",IntLiteral(2),Id("y")))]))])
        expect = str(Redeclared(Variable(), "a"))
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_7(self):
        """Test redeclared global variable"""
        input = Program([VarDecl(Id("x"),[],None),VarDecl(Id("x"),[],IntLiteral(20)),
                              FuncDecl(Id("main"),[],
                                ([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],
                                 [Assign(Id("a"),BinaryOp("+",Id("x"),Id("y"))),
                                  Assign(Id("b"),BinaryOp("*",IntLiteral(2),Id("y")))]))])
        expect = str(Redeclared(Variable(), "x"))
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_8(self):
        """Test redeclared global variable"""
        input = Program([VarDecl(Id("x"),[],None),VarDecl(Id("x"),[],None),
                              FuncDecl(Id("main"),[],
                                ([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],
                                 [Assign(Id("a"),BinaryOp("+",Id("x"),Id("y"))),
                                  Assign(Id("b"),BinaryOp("*",IntLiteral(2),Id("y")))]))])
        expect = str(Redeclared(Variable(), "x"))
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_9(self):
        """Test redeclared global variable"""
        input = Program([VarDecl(Id("x"),[],IntLiteral(10)),VarDecl(Id("x"),[],None),
                              FuncDecl(Id("main"),[],
                                ([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],
                                 [Assign(Id("a"),BinaryOp("+",Id("x"),Id("y"))),
                                  Assign(Id("b"),BinaryOp("*",IntLiteral(2),Id("y")))]))])
        expect = str(Redeclared(Variable(), "x"))
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_10(self):
        """Test redeclared local variable"""
        input = Program([VarDecl(Id("x"),[],IntLiteral(10)),VarDecl(Id("y"),[],IntLiteral(20)),
                              FuncDecl(Id("main"),[],
                                ([VarDecl(Id("a"),[],None),VarDecl(Id("a"),[],IntLiteral(2))],
                                 [Assign(Id("a"),BinaryOp("+",Id("x"),Id("y"))),
                                  Assign(Id("b"),BinaryOp("*",IntLiteral(2),Id("y")))]))])
        expect = str(Redeclared(Variable(), "a"))
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_11(self):
        """Test redeclared param"""
        input = Program([
            FuncDecl(Id("add"),[VarDecl(Id("a"),[],None),VarDecl(Id("a"),[],None)],([],[Return(BinaryOp("+",Id("a"),Id("b")))]))
            ,FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5)),VarDecl(Id("y"),[],IntLiteral(10))],
            [CallStmt(Id("print"),[CallExpr(Id("add"),[Id("x"),Id("y")])])]))])
        expect = str(Redeclared(Parameter(), "a"))
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_12(self):
        """Test redeclared function"""
        input = Program([
            FuncDecl(Id("add"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([],[Return(BinaryOp("+",Id("a"),Id("b")))])),
            FuncDecl(Id("add"), [VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None)],
                     ([], [Return(BinaryOp("*", Id("a"), Id("b")))]))
            ,FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5)),VarDecl(Id("y"),[],IntLiteral(10))],
            [CallStmt(Id("print"),[CallExpr(Id("add"),[Id("x"),Id("y")])])]))])
        expect = str(Redeclared(Function(), "add"))
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_13(self):
        """Test redeclared function"""
        input = Program([
            VarDecl(Id("add"),[],IntLiteral(10)),
            FuncDecl(Id("add"), [VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None)],
                     ([], [Return(BinaryOp("*", Id("a"), Id("b")))]))
            ,FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5)),VarDecl(Id("y"),[],IntLiteral(10))],
            [CallStmt(Id("print"),[CallExpr(Id("add"),[Id("x"),Id("y")])])]))])
        expect = str(Redeclared(Function(), "add"))
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_14(self):
        """Test redeclared param"""
        input = Program([
            FuncDecl(Id("add"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("a"),[],None)],([],[Return(BinaryOp("+",Id("a"),Id("b")))]))
            ,FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5)),VarDecl(Id("y"),[],IntLiteral(10))],
            [CallStmt(Id("print"),[CallExpr(Id("add"),[Id("x"),Id("y")])])]))])
        expect = str(Redeclared(Parameter(), "a"))
        self.assertTrue(TestChecker.test(input,expect,414))