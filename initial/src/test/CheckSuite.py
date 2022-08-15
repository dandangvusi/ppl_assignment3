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

    def test_32(self):
        """Test type mismatch in For statement"""
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [For(Id("i"),IntLiteral(0),BinaryOp("=/=",Id("i"),IntLiteral(10)),BinaryOp("*.",FloatLiteral(1.0),FloatLiteral(2.0)),
                ([VarDecl(Id("y"),[],IntLiteral(2))],
                [Assign(Id("x"),BinaryOp("+",Id("y"),Id("i")))]))]))])
        expect = str(TypeMismatchInStatement(For(Id("i"),IntLiteral(0),BinaryOp("=/=",Id("i"),IntLiteral(10)),BinaryOp("*.",FloatLiteral(1.0),FloatLiteral(2.0)),
                ([VarDecl(Id("y"),[],IntLiteral(2))],
                [Assign(Id("x"),BinaryOp("+",Id("y"),Id("i")))]))))
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_33(self):
        """Test type mismatch in For statement"""
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [For(Id("i"),IntLiteral(0),BinaryOp("=/=",Id("i"),IntLiteral(10)),BinaryOp("\.",FloatLiteral(1.0),FloatLiteral(2.0)),
                ([VarDecl(Id("y"),[],IntLiteral(2))],
                [Assign(Id("x"),BinaryOp("+",Id("y"),Id("i")))]))]))])
        expect = str(TypeMismatchInStatement(For(Id("i"),IntLiteral(0),BinaryOp("=/=",Id("i"),IntLiteral(10)),BinaryOp("\.",FloatLiteral(1.0),FloatLiteral(2.0)),
                ([VarDecl(Id("y"),[],IntLiteral(2))],
                [Assign(Id("x"),BinaryOp("+",Id("y"),Id("i")))]))))
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_34(self):
        """Test type mismatch in For statement"""
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [For(Id("i"),IntLiteral(0),BinaryOp("=/=",Id("i"),IntLiteral(10)),FloatLiteral(2.0),
                ([VarDecl(Id("y"),[],IntLiteral(2))],
                [Assign(Id("x"),BinaryOp("+",Id("y"),Id("i")))]))]))])
        expect = str(TypeMismatchInStatement(For(Id("i"),IntLiteral(0),BinaryOp("=/=",Id("i"),IntLiteral(10)),FloatLiteral(2.0),
                ([VarDecl(Id("y"),[],IntLiteral(2))],
                [Assign(Id("x"),BinaryOp("+",Id("y"),Id("i")))]))))
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_35(self):
        """Test type mismatch in For statement"""
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [For(Id("i"),IntLiteral(0),BinaryOp("+",Id("i"),IntLiteral(10)),BinaryOp("*",IntLiteral(1),IntLiteral(2)),
                ([VarDecl(Id("y"),[],IntLiteral(2))],
                [Assign(Id("x"),BinaryOp("+",Id("y"),Id("i")))]))]))])
        expect = str(TypeMismatchInStatement(For(Id("i"),IntLiteral(0),BinaryOp("+",Id("i"),IntLiteral(10)),BinaryOp("*",IntLiteral(1),IntLiteral(2)),
                ([VarDecl(Id("y"),[],IntLiteral(2))],
                [Assign(Id("x"),BinaryOp("+",Id("y"),Id("i")))]))))
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_36(self):
        """Test type mismatch in For statement"""
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [For(Id("i"),IntLiteral(0),BinaryOp("%",Id("i"),IntLiteral(10)),BinaryOp("*",IntLiteral(1),IntLiteral(2)),
                ([VarDecl(Id("y"),[],IntLiteral(2))],
                [Assign(Id("x"),BinaryOp("+",Id("y"),Id("i")))]))]))])
        expect = str(TypeMismatchInStatement(For(Id("i"),IntLiteral(0),BinaryOp("%",Id("i"),IntLiteral(10)),BinaryOp("*",IntLiteral(1),IntLiteral(2)),
                ([VarDecl(Id("y"),[],IntLiteral(2))],
                [Assign(Id("x"),BinaryOp("+",Id("y"),Id("i")))]))))
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_37(self):
        """Test type mismatch in Array cell"""
        input = Program([FuncDecl(Id("main"), [],
                ([VarDecl(Id("arr"),[3],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])),VarDecl(Id("b"),[],IntLiteral(69))],
                [Assign(ArrayCell(Id("arr"),[FloatLiteral(1.0)]),Id("b"))]))])
        expect = str(TypeMismatchInExpression(ArrayCell(Id("arr"),[FloatLiteral(1.0)])))
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_38(self):
        """Test type mismatch in Array cell"""
        input = Program([FuncDecl(Id("main"), [],
                ([VarDecl(Id("arr"),[3],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])),VarDecl(Id("b"),[],FloatLiteral(2.0))],
                [Assign(ArrayCell(Id("arr"),[Id("b")]),IntLiteral(1))]))])
        expect = str(TypeMismatchInExpression(ArrayCell(Id("arr"),[Id("b")])))
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_39(self):
        """Test type mismatch in While statement"""
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [While(BinaryOp("+",Id("x"),IntLiteral(100)),(
                [VarDecl(Id("y"),[],IntLiteral(5))],
                [Assign(Id("x"),BinaryOp("+",Id("x"),Id("y")))]))]))])
        expect = str(TypeMismatchInStatement(While(BinaryOp("+",Id("x"),IntLiteral(100)),(
                [VarDecl(Id("y"),[],IntLiteral(5))],
                [Assign(Id("x"),BinaryOp("+",Id("x"),Id("y")))]))))
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_40(self):
        """Test type mismatch in While statement"""
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [While(Id("x"),(
                [VarDecl(Id("y"),[],IntLiteral(5))],
                [Assign(Id("x"),BinaryOp("+",Id("x"),Id("y")))]))]))])
        expect = str(TypeMismatchInStatement(While(Id("x"),(
                [VarDecl(Id("y"),[],IntLiteral(5))],
                [Assign(Id("x"),BinaryOp("+",Id("x"),Id("y")))]))))
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_41(self):
        """Test type mismatch in Binary expression"""
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],BooleanLiteral(True))],
                [While(Id("x"),(
                [VarDecl(Id("y"),[],IntLiteral(5))],
                [Assign(Id("x"),BinaryOp("+",Id("x"),Id("y")))]))]))])
        expect = str(TypeMismatchInExpression(BinaryOp("+",Id("x"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_42(self):
        """Test type mismatch assign statement"""
        input = Program([FuncDecl(Id("main"), [],
                ([VarDecl(Id("arr"),[3],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])),VarDecl(Id("b"),[],FloatLiteral(6.9))],
                [Assign(ArrayCell(Id("arr"),[IntLiteral(1)]),Id("b"))]))])
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id("arr"),[IntLiteral(1)]),Id("b"))))
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_43(self):
        """Test type mismatch assign statement"""
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [While(BinaryOp("<",Id("x"),BinaryOp("-",IntLiteral(100),BinaryOp("*",IntLiteral(5),IntLiteral(2)))),(
                [VarDecl(Id("y"),[],FloatLiteral(5.0))],
                [Assign(Id("x"),Id("y"))]))]))])
        expect = str(TypeMismatchInStatement(Assign(Id("x"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_44(self):
        """Test type mismatch assign statement"""
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("a"),[],StringLiteral("Dan"))],
                [Assign(Id("a"),BinaryOp("-",BinaryOp("*",BinaryOp("+",IntLiteral(2),IntLiteral(3)),
                BinaryOp("-",IntLiteral(4),IntLiteral(2))),BinaryOp("%",IntLiteral(5),IntLiteral(2))))]))])
        expect = str(TypeMismatchInStatement(Assign(Id("a"),BinaryOp("-",BinaryOp("*",BinaryOp("+",IntLiteral(2),IntLiteral(3)),
                BinaryOp("-",IntLiteral(4),IntLiteral(2))),BinaryOp("%",IntLiteral(5),IntLiteral(2))))))
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_45(self):
        """Test type mismatch in Do-While statement"""
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [Dowhile(([VarDecl(Id("y"),[],IntLiteral(5))],
                [Assign(Id("x"),BinaryOp("+",Id("x"),Id("y")))]),Id("x"))]))])
        expect = str(TypeMismatchInStatement(Dowhile(([VarDecl(Id("y"),[],IntLiteral(5))],
                [Assign(Id("x"),BinaryOp("+",Id("x"),Id("y")))]),Id("x"))))
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_46(self):
        """Test type mismatch in Do-While statement"""
        input = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [Dowhile(([VarDecl(Id("y"),[],IntLiteral(5))],
                [Assign(Id("x"),BinaryOp("+",Id("x"),Id("y")))]),StringLiteral("Dan"))]))])
        expect = str(TypeMismatchInStatement(Dowhile(([VarDecl(Id("y"),[],IntLiteral(5))],
                [Assign(Id("x"),BinaryOp("+",Id("x"),Id("y")))]),StringLiteral("Dan"))))
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_47(self):
        """Test type mismatch in func call statement"""
        input = Program([FuncDecl(Id("add_one"),[VarDecl(Id("n"),[],None)],([],[Return(BinaryOp("+",Id("n"),IntLiteral(1)))])),
                              FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],[CallStmt(Id("add_one"),[Id("x")])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("add_one"),[Id("x")])))
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_48(self):
        """Test type mismatch in func call statement"""
        input = Program([VarDecl(Id("x"),[],None),
            FuncDecl(Id("fact"),[VarDecl(Id("n"),[],None)],([],[If([(BinaryOp("==",Id("n"),IntLiteral(0)),[],
            [Return(IntLiteral(1))])],([],[Return(BinaryOp("*",Id("n"),CallExpr(Id("fact"),[BinaryOp("-",Id("n"),IntLiteral(1))])))]))])),
            FuncDecl(Id("main"),[],([],[Assign(Id("x"),IntLiteral(10)),CallStmt(Id("fact"),[Id("x")])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("fact"),[Id("x")])))
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_49(self):
        """Test type mismatch in func call statement (invalid number of args)"""
        input = Program([FuncDecl(Id("main"),[],([],
                [CallStmt(Id("printStr"), [StringLiteral("Hi"), StringLiteral("Dan")])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStr"), [StringLiteral("Hi"), StringLiteral("Dan")])))
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_50(self):
        """Test type mismatch in func call statement (invalid type of args)"""
        input = Program([FuncDecl(Id("main"),[],([],
                [CallStmt(Id("printStr"), [IntLiteral(6)])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStr"), [IntLiteral(6)])))
        self.assertTrue(TestChecker.test(input,expect,450))