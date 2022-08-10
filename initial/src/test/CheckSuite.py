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

    def test_15(self):
        """Test undeclared variable"""
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(4)),VarDecl(Id("y"),[],None)],
                [Assign(Id("z"),BinaryOp("+",Id("x"),Id("y")))]))])
        expect = str(Undeclared(Identifier(), "z"))
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_16(self):
        """Test undeclared parameter"""
        input = Program([
            FuncDecl(Id("add"),[VarDecl(Id("b"),[],None)],([],[Return(BinaryOp("+",Id("a"),Id("b")))]))
            ,FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5)),VarDecl(Id("y"),[],IntLiteral(10))],
            [CallStmt(Id("print"),[CallExpr(Id("add"),[Id("x"),Id("y")])])]))])
        expect = str(Undeclared(Identifier(), "a"))
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_17(self):
        """Test undeclared function"""
        input = Program([
            FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5)),VarDecl(Id("y"),[],IntLiteral(10))],
            [CallStmt(Id("print"),[CallExpr(Id("add"),[Id("x"),Id("y")])])]))])
        expect = str(Undeclared(Function(), "add"))
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_18(self):
        """Test undeclared variable"""
        input = Program([VarDecl(Id("x"),[],None),
            FuncDecl(Id("fact"),[],([],[If([(BinaryOp("==",Id("n"),IntLiteral(0)),[],
            [Return(IntLiteral(1))])],([],[Return(BinaryOp("*",Id("n"),CallExpr(Id("fact"),[BinaryOp("-",Id("n"),IntLiteral(1))])))]))])),
            FuncDecl(Id("main"),[],([],[Assign(Id("x"),IntLiteral(10)),CallStmt(Id("fact"),[Id("x")])]))])
        expect = str(Undeclared(Identifier(), "n"))
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_19(self):
        """Test undeclared variable"""
        input = Program([FuncDecl(Id("main"),[],([],
                [Assign(ArrayCell(Id("a"),[IntLiteral(1),IntLiteral(2)]),BinaryOp("-",BinaryOp("*",IntLiteral(4),IntLiteral(5)),IntLiteral(2)))]))])
        expect = str(Undeclared(Identifier(), "a"))
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_20(self):
        """Test undeclared variable"""
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("a"),[],None)],
                [If([(CallExpr(Id("bool_of_string"),[StringLiteral("True")]),[],
                [Assign(Id("a"),CallExpr(Id("int_of_string"),[CallExpr(Id("read"),[])])),
                Assign(Id("b"),BinaryOp("+.",CallExpr(Id("float_of_int"),[Id("a")]),FloatLiteral(2.0)))])],
                ([],[]))]))])
        expect = str(Undeclared(Identifier(), "b"))
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_21(self):
        """Test undeclared variable"""
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [While(BinaryOp("<",Id("x"),BinaryOp("*",IntLiteral(100),IntLiteral(2))),(
                [],
                [Assign(Id("x"),BinaryOp("+",Id("x"),Id("y"))),
                 If([(BinaryOp(">=",Id("x"),IntLiteral(50)),[],[Continue()])],([],[]))]))]))])
        expect = str(Undeclared(Identifier(), "y"))
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_22(self):
        """Test undeclared variable"""
        input = Program([FuncDecl(Id("main"),[],([],
                [Dowhile(([VarDecl(Id("y"),[],IntLiteral(5))],
                [Assign(Id("x"),BinaryOp("+",Id("x"),Id("y")))]),
                BinaryOp("<",Id("x"),BinaryOp("-",IntLiteral(100),BinaryOp("*",IntLiteral(5),IntLiteral(2)))))]))])
        expect = str(Undeclared(Identifier(), "x"))
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_23(self):
        """Test undeclared variable"""
        input = Program([FuncDecl(Id("main"),[],([],
                [Dowhile(([VarDecl(Id("y"),[],IntLiteral(5))],
                []),
                BinaryOp("<",Id("x"),BinaryOp("-",IntLiteral(100),BinaryOp("*",IntLiteral(5),IntLiteral(2)))))]))])
        expect = str(Undeclared(Identifier(), "x"))
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_24(self):
        """Test undeclared variable"""
        input = Program([FuncDecl(Id("add_one"),[],([],[Return(BinaryOp("+",Id("n"),IntLiteral(1)))])),
                              FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],[CallStmt(Id("add_one"),[Id("x")])]))])
        expect = str(Undeclared(Identifier(), "n"))
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_25(self):
        """Test undeclared variable"""
        input = Program([FuncDecl(Id("main"),[],([],
                [If([(BinaryOp("==",BinaryOp("%",Id("x"),IntLiteral(2)),IntLiteral(0)),[VarDecl(Id("y"),[],IntLiteral(2)),VarDecl(Id("y"),[],IntLiteral(2))],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1))),Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))]),
                     (BinaryOp(">",Id("x"),IntLiteral(0)),[VarDecl(Id("y"),[],IntLiteral(2)),VarDecl(Id("y"),[],IntLiteral(2))],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(2))),Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(2)))]),
                     (BinaryOp(">",Id("x"),IntLiteral(100)),[VarDecl(Id("y"),[],IntLiteral(2)),VarDecl(Id("y"),[],IntLiteral(2))],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(3))),Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(3)))])],
                    ([VarDecl(Id("y"),[],IntLiteral(2)),VarDecl(Id("y"),[],IntLiteral(2))],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(4))),Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(4)))]))]))])
        expect = str(Undeclared(Identifier(), "x"))
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_26(self):
        """Test undeclared function"""
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(4)),VarDecl(Id("y"),[],IntLiteral(5)),
                VarDecl(Id("z"),[],IntLiteral(6)), VarDecl(Id("t"),[],None)],
                [Assign(Id("t"),BinaryOp("+",BinaryOp("+",Id("x"),Id("y")),CallExpr(Id("add_one"),[Id("z")])))]))])
        expect = str(Undeclared(Function(), "add_one"))
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_27(self):
        """Test type mismatch in If statement"""
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [If([(BinaryOp("%",Id("x"),IntLiteral(2)),[],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))]),
                     (BinaryOp(">",Id("x"),IntLiteral(0)),[],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(2)))]),
                     (BinaryOp(">",Id("x"),IntLiteral(100)),[],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(3)))])],
                    ([],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(4)))]))]))])
        expect = str(TypeMismatchInStatement(If([(BinaryOp("%",Id("x"),IntLiteral(2)),[],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))]),
                     (BinaryOp(">",Id("x"),IntLiteral(0)),[],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(2)))]),
                     (BinaryOp(">",Id("x"),IntLiteral(100)),[],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(3)))])],
                    ([],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(4)))]))))
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_28(self):
        """Test type mismatch in If statement"""
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [If([(BinaryOp("==",BinaryOp("%",Id("x"),IntLiteral(2)),IntLiteral(0)),[],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))]),
                     (IntLiteral(0),[],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(2)))]),
                     (BinaryOp(">",Id("x"),IntLiteral(100)),[],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(3)))])],
                    ([],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(4)))]))]))])
        expect = str(TypeMismatchInStatement(If([(BinaryOp("==",BinaryOp("%",Id("x"),IntLiteral(2)),IntLiteral(0)),[],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))]),
                     (IntLiteral(0),[],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(2)))]),
                     (BinaryOp(">",Id("x"),IntLiteral(100)),[],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(3)))])],
                    ([],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(4)))]))))
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_29(self):
        """Test type mismatch in If statement"""
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [If([(BinaryOp("==",BinaryOp("%",Id("x"),IntLiteral(2)),IntLiteral(0)),[],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))]),
                     (BinaryOp(">",Id("x"),IntLiteral(0)),[],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(2)))]),
                     (Id("x"),[],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(3)))])],
                    ([],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(4)))]))]))])
        expect = str(TypeMismatchInStatement(If([(BinaryOp("==",BinaryOp("%",Id("x"),IntLiteral(2)),IntLiteral(0)),[],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))]),
                     (BinaryOp(">",Id("x"),IntLiteral(0)),[],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(2)))]),
                     (Id("x"),[],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(3)))])],
                    ([],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(4)))]))))
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_30(self):
        """Test type mismatch in For statement"""
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],FloatLiteral(5.0))],
                [For(Id("i"),Id("x"),BinaryOp("=/=",Id("i"),IntLiteral(10)),BinaryOp("*",IntLiteral(1),IntLiteral(2)),
                ([VarDecl(Id("y"),[],IntLiteral(2))],
                [Assign(Id("x"),BinaryOp("+",Id("y"),Id("i")))]))]))])
        expect = str(TypeMismatchInStatement(For(Id("i"),Id("x"),BinaryOp("=/=",Id("i"),IntLiteral(10)),BinaryOp("*",IntLiteral(1),IntLiteral(2)),
                ([VarDecl(Id("y"),[],IntLiteral(2))],
                [Assign(Id("x"),BinaryOp("+",Id("y"),Id("i")))]))))
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_31(self):
        """Test type mismatch in For statement"""
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],FloatLiteral(5.0))],
                [For(Id("i"),FloatLiteral(5.0),BinaryOp("=/=",Id("i"),IntLiteral(10)),BinaryOp("*",IntLiteral(1),IntLiteral(2)),
                ([VarDecl(Id("y"),[],IntLiteral(2))],
                [Assign(Id("x"),BinaryOp("+",Id("y"),Id("i")))]))]))])
        expect = str(TypeMismatchInStatement(For(Id("i"),FloatLiteral(5.0),BinaryOp("=/=",Id("i"),IntLiteral(10)),BinaryOp("*",IntLiteral(1),IntLiteral(2)),
                ([VarDecl(Id("y"),[],IntLiteral(2))],
                [Assign(Id("x"),BinaryOp("+",Id("y"),Id("i")))]))))
        self.assertTrue(TestChecker.test(input,expect,431))