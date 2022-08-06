import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test1(self):
        """Test variable declaration"""
        input = """Var: x;"""
        expect = str(Program([VarDecl(Id("x"),[],None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test2(self):
        """Test variable declaration"""
        input = """Var: x = 1;"""
        expect = str(Program([VarDecl(Id("x"),[],IntLiteral(1))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test3(self):
        """Test variable declaration"""
        input = """Var: arr[10];"""
        expect = str(Program([VarDecl(Id("arr"),[10],None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test4(self):
        """Test variable declaration"""
        input = """Var: arr[3] = {1, 2, 3};"""
        expect = str(Program([VarDecl(Id("arr"),[3],ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test5(self):
        """Test variable declaration"""
        input = """Var: arr[2][3] = {{1, 2, 3}, {4, 5, 6}};"""
        expect = str(Program([VarDecl(Id("arr"),[2, 3],ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2),
                    IntLiteral(3)]), ArrayLiteral([IntLiteral(4), IntLiteral(5), IntLiteral(6)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test6(self):
        """Test variable declaration"""
        input = """Var: x, arr[10];"""
        expect = str(Program([VarDecl(Id("x"),[],None),VarDecl(Id("arr"),[10],None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test7(self):
        """Test variable declaration"""
        input = """Var: x, y = 1;"""
        expect = str(Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],IntLiteral(1))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test8(self):
        """Test variable declaration"""
        input = """Var: x = 1.0, y = 1, z = 1e-10;"""
        expect = str(Program([VarDecl(Id("x"),[],FloatLiteral(1.0)),VarDecl(Id("y"),[],IntLiteral(1)),VarDecl(Id("z"),[],FloatLiteral(1e-10))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test9(self):
        """Test variable declaration"""
        input = """Var: x = "hello", y = True, z = False;"""
        expect = str(Program([VarDecl(Id("x"),[],StringLiteral("hello")),VarDecl(Id("y"),[],BooleanLiteral(True)),VarDecl(Id("z"),[],BooleanLiteral(False))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test10(self):
        """Test variable declaration"""
        input = """Var: arr1[2] = {1, 2}, arr2[2][3] = {{1, 2, 3}, {4, 5, 6}};"""
        expect = str(Program([VarDecl(Id("arr1"),[2],ArrayLiteral([IntLiteral(1), IntLiteral(2)])),VarDecl(Id("arr2"),[2, 3],
                ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)]), ArrayLiteral([IntLiteral(4), IntLiteral(5), IntLiteral(6)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test11(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: x = 4, y;
                y = x + 6;
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(4)),VarDecl(Id("y"),[],None)],
                [Assign(Id("y"),BinaryOp("+",Id("x"),IntLiteral(6)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test12(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: x = 4, y = 5, z = 6, t;
                t = x + y + z;
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(4)),VarDecl(Id("y"),[],IntLiteral(5)),
                VarDecl(Id("z"),[],IntLiteral(6)), VarDecl(Id("t"),[],None)],
                [Assign(Id("t"),BinaryOp("+",BinaryOp("+",Id("x"),Id("y")),Id("z")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test13(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: x = 4, y = 5, z = 6, t;
                t = x + y + z + 5;
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(4)),VarDecl(Id("y"),[],IntLiteral(5)),
                VarDecl(Id("z"),[],IntLiteral(6)), VarDecl(Id("t"),[],None)],
                [Assign(Id("t"),BinaryOp("+",BinaryOp("+",BinaryOp("+",Id("x"),Id("y")),Id("z")),IntLiteral(5)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test14(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: x = 4, y = 5, z = 6, t;
                t = x + y - z;
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(4)),VarDecl(Id("y"),[],IntLiteral(5)),
                VarDecl(Id("z"),[],IntLiteral(6)), VarDecl(Id("t"),[],None)],
                [Assign(Id("t"),BinaryOp("-",BinaryOp("+",Id("x"),Id("y")),Id("z")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test15(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: x = 4, y = 5, z = 6, t;
                t = x - y + z - 5;
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(4)),VarDecl(Id("y"),[],IntLiteral(5)),
                VarDecl(Id("z"),[],IntLiteral(6)), VarDecl(Id("t"),[],None)],
                [Assign(Id("t"),BinaryOp("-",BinaryOp("+",BinaryOp("-",Id("x"),Id("y")),Id("z")),IntLiteral(5)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test16(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: x = 4.5, y = 5.2e-1, z = 6.9, t;
                t = x -. y +. z -. 5e-10;
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],FloatLiteral(4.5)),VarDecl(Id("y"),[],FloatLiteral(5.2e-1)),
                VarDecl(Id("z"),[],FloatLiteral(6.9)), VarDecl(Id("t"),[],None)],
                [Assign(Id("t"),BinaryOp("-.",BinaryOp("+.",BinaryOp("-.",Id("x"),Id("y")),Id("z")),FloatLiteral(5e-10)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test17(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: x = 4.5, y = 5.2e-1, z = 6.9, t;
                t = x *. y +. z *. 5e-10;
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],FloatLiteral(4.5)),VarDecl(Id("y"),[],FloatLiteral(5.2e-1)),
                VarDecl(Id("z"),[],FloatLiteral(6.9)), VarDecl(Id("t"),[],None)],
                [Assign(Id("t"),BinaryOp("+.",BinaryOp("*.",Id("x"),Id("y")),BinaryOp("*.",Id("z"),FloatLiteral(5e-10))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test18(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: x = 4, y = 5, z = 6, t;
                t = x * y - z \ 5;
            EndBody.
        """
        expect = str(Program(
            [FuncDecl(Id("main"), [], ([VarDecl(Id("x"), [], IntLiteral(4)), VarDecl(Id("y"), [], IntLiteral(5)),
                                        VarDecl(Id("z"), [], IntLiteral(6)), VarDecl(Id("t"), [], None)],
                                       [Assign(Id("t"),BinaryOp("-",BinaryOp("*",Id("x"),Id("y")),BinaryOp("\\",Id("z"),IntLiteral(5))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))

    def test19(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: x = 4, y = 5, z = 6, t;
                t = x \ y \ z * 5;
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(4)),VarDecl(Id("y"),[],IntLiteral(5)),
                VarDecl(Id("z"),[],IntLiteral(6)), VarDecl(Id("t"),[],None)],
                [Assign(Id("t"),BinaryOp("*",BinaryOp("\\",BinaryOp("\\",Id("x"),Id("y")),Id("z")),IntLiteral(5)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test20(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: x = 4.5, y = 5.2e-1, z = 6.9, t;
                t = x \. y *. z \. 5e-10;
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"), [], (
        [VarDecl(Id("x"), [], FloatLiteral(4.5)), VarDecl(Id("y"), [], FloatLiteral(5.2e-1)),
         VarDecl(Id("z"), [], FloatLiteral(6.9)), VarDecl(Id("t"), [], None)],
        [Assign(Id("t"),BinaryOp("\.", BinaryOp("*.", BinaryOp("\.", Id("x"), Id("y")), Id("z")), FloatLiteral(5e-10)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    def test21(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: x = 4, y = 5, z = 6, t;
                t = -x * y - z \ -5;
            EndBody.
        """
        expect = str(Program(
            [FuncDecl(Id("main"), [], ([VarDecl(Id("x"), [], IntLiteral(4)), VarDecl(Id("y"), [], IntLiteral(5)),
                                        VarDecl(Id("z"), [], IntLiteral(6)), VarDecl(Id("t"), [], None)],
                                       [Assign(Id("t"),BinaryOp("-",BinaryOp("*",UnaryOp("-",Id("x")),Id("y")),BinaryOp("\\",Id("z"),UnaryOp("-",IntLiteral(5)))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))

    def test22(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: x = 4.5, y = 5.2e-1, z = 6.9, t;
                t = x *. y +. -.z *. 5e-10;
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],FloatLiteral(4.5)),VarDecl(Id("y"),[],FloatLiteral(5.2e-1)),
                VarDecl(Id("z"),[],FloatLiteral(6.9)), VarDecl(Id("t"),[],None)],
                [Assign(Id("t"),BinaryOp("+.",BinaryOp("*.",Id("x"),Id("y")),BinaryOp("*.",UnaryOp("-.",Id("z")),FloatLiteral(5e-10))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test23(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c;
                c = a && b;
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("a"),[],BooleanLiteral(True)),VarDecl(Id("b"),[],BooleanLiteral(False)),
                VarDecl(Id("c"),[],None)],
                [Assign(Id("c"),BinaryOp("&&",Id("a"),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test24(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c;
                c = a && b || False;
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("a"),[],BooleanLiteral(True)),VarDecl(Id("b"),[],BooleanLiteral(False)),
                VarDecl(Id("c"),[],None)],
                [Assign(Id("c"),BinaryOp("||",BinaryOp("&&",Id("a"),Id("b")),BooleanLiteral(False)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test25(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c;
                c = !a && b;
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"), [], (
        [VarDecl(Id("a"), [], BooleanLiteral(True)), VarDecl(Id("b"), [], BooleanLiteral(False)),
         VarDecl(Id("c"), [], None)],
        [Assign(Id("c"), BinaryOp("&&", UnaryOp("!",Id("a")), Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    def test26(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c;
                c = !a || !b && True;
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"), [], (
        [VarDecl(Id("a"), [], BooleanLiteral(True)), VarDecl(Id("b"), [], BooleanLiteral(False)),
         VarDecl(Id("c"), [], None)],
        [Assign(Id("c"),BinaryOp("&&",BinaryOp("||",UnaryOp("!",Id("a")),UnaryOp("!",Id("b"))),BooleanLiteral(True)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    def test27(self):
        """Test variable declaration"""
        input = """
        Function: main
            Body:
                Var: arr[3] = {1, 2, 3}, a = 1, b = 2, c;
                c = arr[3] + b;
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("arr"),[3],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]))
                                                       ,VarDecl(Id("a"),[],IntLiteral(1)),VarDecl(Id("b"),[],IntLiteral(2)),VarDecl(Id("c"),[],None)],
                                                      [Assign(Id("c"),BinaryOp("+",ArrayCell(Id("arr"),[IntLiteral(3)]),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test28(self):
        """Test variable declaration"""
        input = """
        Function: main
            Body:
                Var: arr[3] = {1, 2, 3}, a = 1, b = 2, c;
                c = arr[2] + b * arr[0];
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("arr"),[3],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]))
                                                       ,VarDecl(Id("a"),[],IntLiteral(1)),VarDecl(Id("b"),[],IntLiteral(2)),VarDecl(Id("c"),[],None)],
                                                      [Assign(Id("c"),BinaryOp("+",ArrayCell(Id("arr"),[IntLiteral(2)]),BinaryOp("*",Id("b"),
                                                    ArrayCell(Id("arr"),[IntLiteral(0)]))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test29(self):
        """Test for statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                For (i = 0, i < 10, 1) Do
                    x = x + i;
                EndFor.
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                                                      [For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(1),([],[Assign(Id("x"),BinaryOp("+",Id("x"),Id("i")))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test30(self):
        """Test for statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                For (i = 0, i < 10, 1) Do
                    Var: y = 2;
                    x = y + i;
                EndFor.
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(1),
                ([VarDecl(Id("y"),[],IntLiteral(2))],
                [Assign(Id("x"),BinaryOp("+",Id("y"),Id("i")))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    def test31(self):
        """Test for statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                For (i = 0, i =/= 10, 1*2) Do
                    Var: y = 2;
                    x = y + i;
                EndFor.
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [For(Id("i"),IntLiteral(0),BinaryOp("=/=",Id("i"),IntLiteral(10)),BinaryOp("*",IntLiteral(1),IntLiteral(2)),
                ([VarDecl(Id("y"),[],IntLiteral(2))],
                [Assign(Id("x"),BinaryOp("+",Id("y"),Id("i")))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,331))

    def test32(self):
        """Test for statement"""
        input = """
        Function: main
            Body:
                For (i = 0, i =/= 10, 1*2) Do
                
                EndFor.
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([],
                [For(Id("i"),IntLiteral(0),BinaryOp("=/=",Id("i"),IntLiteral(10)),BinaryOp("*",IntLiteral(1),IntLiteral(2)),
                ([],
                []))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,332))

    def test33(self):
        """Test var declaration statement"""
        input = """
        Function: main
            Body:
                Var: a = 1, b = 1.3, c = 4e-1, d = "Hello", e = True;
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"), [], ([VarDecl(Id("a"),[],IntLiteral(1)),
                VarDecl(Id("b"),[],FloatLiteral(1.3)),VarDecl(Id("c"),[],FloatLiteral(4e-1)),VarDecl(Id("d"),[],StringLiteral("Hello")),
                VarDecl(Id("e"),[],BooleanLiteral(True))],[]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))

    def test34(self):
        """Test var assign statement"""
        input = """
        Function: main
            Body:
                Var: a = 1, b = 1.3, c = 4e-1, d = "Hello", e;
                e = 3.14 *. b *. b *. b *. (4. \. 3.);
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"), [], ([VarDecl(Id("a"),[],IntLiteral(1)),
                VarDecl(Id("b"),[],FloatLiteral(1.3)),VarDecl(Id("c"),[],FloatLiteral(4e-1)),VarDecl(Id("d"),[],StringLiteral("Hello")),
                VarDecl(Id("e"),[],None)],[Assign(Id("e"),BinaryOp("*.",BinaryOp("*.",BinaryOp("*.",BinaryOp("*.",FloatLiteral(3.14),Id("b")),Id("b")),Id("b")),BinaryOp("\.",FloatLiteral(4.),FloatLiteral(3.))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))

    def test35(self):
        """Test var assign statement"""
        input = """
        Function: main
            Body:
                Var: arr[3] = {1,2,3}, b = 69;
                arr[1] = b;
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"), [],
                ([VarDecl(Id("arr"),[3],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])),VarDecl(Id("b"),[],IntLiteral(69))],
                [Assign(ArrayCell(Id("arr"),[IntLiteral(1)]),Id("b"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))

    def test36(self):
        """Test If statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                If x % 2 == 0 Then
                    x = x + 1;
                ElseIf x > 0 Then
                    x = x + 2;
                ElseIf x > 100 Then
                    x = x + 3;
                Else
                    x = x + 4;
                EndIf.
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [If([(BinaryOp("==",BinaryOp("%",Id("x"),IntLiteral(2)),IntLiteral(0)),[],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))]),
                     (BinaryOp(">",Id("x"),IntLiteral(0)),[],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(2)))]),
                     (BinaryOp(">",Id("x"),IntLiteral(100)),[],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(3)))])],
                    ([],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(4)))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test37(self):
        """Test If statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                If x % 2 == 0 Then
                    x = x + 1;
                ElseIf x > 0 Then
                    x = x + 2;
                Else
                    x = x + 4;
                EndIf.
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [If([(BinaryOp("==",BinaryOp("%",Id("x"),IntLiteral(2)),IntLiteral(0)),[],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))]),
                     (BinaryOp(">",Id("x"),IntLiteral(0)),[],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(2)))])],
                    ([],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(4)))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test38(self):
        """Test If statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                If x % 2 == 0 Then
                    x = x + 1;
                Else
                    x = x + 4;
                EndIf.
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [If([(BinaryOp("==",BinaryOp("%",Id("x"),IntLiteral(2)),IntLiteral(0)),[],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))])],
                    ([],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(4)))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test39(self):
        """Test If statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                If x % 2 == 0 Then
                    x = x + 1;
                EndIf.
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [If([(BinaryOp("==",BinaryOp("%",Id("x"),IntLiteral(2)),IntLiteral(0)),[],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))])],
                    ([],[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test40(self):
        """Test While statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                While x < 10 Do
                    x = x + 1;
                EndWhile.
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [While(BinaryOp("<",Id("x"),IntLiteral(10)),([],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,340))

    def test41(self):
        """Test While statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                While x < 100 Do
                    Var: y = 5;
                    x = x + y;
                EndWhile.
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [While(BinaryOp("<",Id("x"),IntLiteral(100)),(
                [VarDecl(Id("y"),[],IntLiteral(5))],
                [Assign(Id("x"),BinaryOp("+",Id("x"),Id("y")))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test42(self):
        """Test While statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                While x < 100 - 5 * 2 Do
                    Var: y = 5;
                    x = x + y;
                EndWhile.
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [While(BinaryOp("<",Id("x"),BinaryOp("-",IntLiteral(100),BinaryOp("*",IntLiteral(5),IntLiteral(2)))),(
                [VarDecl(Id("y"),[],IntLiteral(5))],
                [Assign(Id("x"),BinaryOp("+",Id("x"),Id("y")))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def test43(self):
        """Test Do-While statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                Do
                    x = x + 1;
                While x < 10
                EndDo.
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [Dowhile(([],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))]),BinaryOp("<",Id("x"),IntLiteral(10)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test44(self):
        """Test Do-While statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                Do
                    Var: y = 5;
                    x = x + y;
                While x < 10
                EndDo.
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [Dowhile(([VarDecl(Id("y"),[],IntLiteral(5))],
                [Assign(Id("x"),BinaryOp("+",Id("x"),Id("y")))]),BinaryOp("<",Id("x"),IntLiteral(10)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def test45(self):
        """Test Do-While statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                Do
                    Var: y = 5;
                    x = x + y;
                While x < 100 - 5 * 2
                EndDo.
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [Dowhile(([VarDecl(Id("y"),[],IntLiteral(5))],
                [Assign(Id("x"),BinaryOp("+",Id("x"),Id("y")))]),
                BinaryOp("<",Id("x"),BinaryOp("-",IntLiteral(100),BinaryOp("*",IntLiteral(5),IntLiteral(2)))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    def test46(self):
        """Test If statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                If x % 2 == 0 Then
                    Break;
                EndIf.
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [If([(BinaryOp("==",BinaryOp("%",Id("x"),IntLiteral(2)),IntLiteral(0)),[],[Break()])],
                    ([],[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test47(self):
        """Test Continue statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                If x % 2 == 0 Then
                    Continue;
                EndIf.
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [If([(BinaryOp("==",BinaryOp("%",Id("x"),IntLiteral(2)),IntLiteral(0)),[],[Continue()])],
                    ([],[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,347))

    def test48(self):
        """Test Func call statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                add_one(5);
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [CallStmt(Id("add_one"),[IntLiteral(5)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test49(self):
        """Test Func call statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                foo();
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [CallStmt(Id("foo"),[])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    def test50(self):
        """Test Func call statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                foo(x);
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [CallStmt(Id("foo"),[Id("x")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,350))

    def test51(self):
        """Test Func call statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                foo(x, 2);
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [CallStmt(Id("foo"),[Id("x"),IntLiteral(2)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,351))

    def test52(self):
        """Test Func call statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                x = x + 1;
                foo(x, 2);
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1))),CallStmt(Id("foo"),[Id("x"),IntLiteral(2)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,352))

    def test53(self):
        """Test Func call statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                x = x + 1;
                foo(x, 2 * 5, 1);
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1))),CallStmt(Id("foo"),[Id("x"),BinaryOp("*",IntLiteral(2),IntLiteral(5)),IntLiteral(1)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test54(self):
        """Test Func call statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                x = x + 1;
                foo(x, 2 * 5, arr[2]);
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1))),CallStmt(Id("foo"),[Id("x"),BinaryOp("*",IntLiteral(2),IntLiteral(5)),ArrayCell(Id("arr"),[IntLiteral(2)])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def test55(self):
        """Test Return statement"""
        input = """
        Function: add_one
            Parameter: n
            Body:
                Return n + 1;
            EndBody.
        Function: main
            Body:
                Var: x = 5;
                add_one(x);
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("add_one"),[VarDecl(Id("n"),[],None)],([],[Return(BinaryOp("+",Id("n"),IntLiteral(1)))])),
                              FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],[CallStmt(Id("add_one"),[Id("x")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,355))

    def test56(self):
        """Test Func call statement"""
        input = """
        Function: foo
            Parameter: n
            Body:
                Return;
            EndBody.
        Function: main
            Body:
                Var: x = 5;
                foo(x);
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[Return(None)])),
                              FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],[CallStmt(Id("foo"),[Id("x")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test57(self):
        """Test Func call statement (built in function)"""
        input = """
        Function: main
            Body:
                Var: x = "Hello", y = "PPL";
                printLn();
                print(x);
                printLn();
                print(y);
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],StringLiteral("Hello")),VarDecl(Id("y"),[],StringLiteral("PPL"))],
                                                      [CallStmt(Id("printLn"),[]),
                                                       CallStmt(Id("print"),[Id("x")]),
                                                       CallStmt(Id("printLn"),[]),
                                                       CallStmt(Id("print"),[Id("y")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,357))

    def test58(self):
        """Test Func call statement (built in function)"""
        input = """
        Function: main
            Body:
                Var: x = "Hello", y = "PPL";
                printLn();
                print(x);
                print(" ");
                print(y);
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],StringLiteral("Hello")),VarDecl(Id("y"),[],StringLiteral("PPL"))],
                                                      [CallStmt(Id("printLn"),[]),
                                                       CallStmt(Id("print"),[Id("x")]),
                                                       CallStmt(Id("print"),[StringLiteral(" ")]),
                                                       CallStmt(Id("print"),[Id("y")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    def test59(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: x = 4, y = 5, z = 6, t;
                t = x + y + add_one(z);
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(4)),VarDecl(Id("y"),[],IntLiteral(5)),
                VarDecl(Id("z"),[],IntLiteral(6)), VarDecl(Id("t"),[],None)],
                [Assign(Id("t"),BinaryOp("+",BinaryOp("+",Id("x"),Id("y")),CallExpr(Id("add_one"),[Id("z")])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,359))

    def test60(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: arr[3] = {1,2,3}, b = 1, c;
                arr[0] = 3 + arr[0 + abs(-b)];
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],
                ([VarDecl(Id("arr"),[3],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])),
                VarDecl(Id("b"),[],IntLiteral(1)),VarDecl(Id("c"),[],None)],
                [Assign(ArrayCell(Id("arr"),[IntLiteral(0)]),BinaryOp("+",IntLiteral(3),ArrayCell(Id("arr"),[BinaryOp("+",IntLiteral(0),CallExpr(Id("abs"),[UnaryOp("-",Id("b"))]))])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,360))

    def test61(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: arr[3] = {1,2,3}, b = 1, c;
                return_arr()[b] = 3 + arr[0 + abs(-b)];
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],
                ([VarDecl(Id("arr"),[3],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])),
                VarDecl(Id("b"),[],IntLiteral(1)),VarDecl(Id("c"),[],None)],
                [Assign(ArrayCell(CallExpr(Id("return_arr"),[]),[Id("b")]),BinaryOp("+",IntLiteral(3),ArrayCell(Id("arr"),
                [BinaryOp("+",IntLiteral(0),CallExpr(Id("abs"),[UnaryOp("-",Id("b"))]))])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,361))

    def test62(self):
        """Test function declaration and expression"""
        input = """
        Var: x = 10, y = 20;
        Function: main
            Body:
                Var: a, b;
                a = x + y;
                b = 2 * y;
            EndBody.
        """
        expect = str(Program([VarDecl(Id("x"),[],IntLiteral(10)),VarDecl(Id("y"),[],IntLiteral(20)),
                              FuncDecl(Id("main"),[],
                                ([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],
                                 [Assign(Id("a"),BinaryOp("+",Id("x"),Id("y"))),
                                  Assign(Id("b"),BinaryOp("*",IntLiteral(2),Id("y")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,362))

    def test63(self):
        """Test function declaration and expression"""
        input = """
        Var: x = 10;
        Var: y = 20;
        Function: main
            Body:
                Var: a;
                Var: b;
                a = x + y;
                b = 2 * y;
            EndBody.
        """
        expect = str(Program([VarDecl(Id("x"),[],IntLiteral(10)),VarDecl(Id("y"),[],IntLiteral(20)),
                              FuncDecl(Id("main"),[],
                                ([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],
                                 [Assign(Id("a"),BinaryOp("+",Id("x"),Id("y"))),
                                  Assign(Id("b"),BinaryOp("*",IntLiteral(2),Id("y")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,363))

    def test64(self):
        """Test for statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                For (i = 0, i < 10, 1) Do
                    If i % 2 == 0 Then
                        Continue;
                    EndIf.
                    print(i);
                EndFor.
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(1),
                ([],
                [If([(BinaryOp("==",BinaryOp("%",Id("i"),IntLiteral(2)),IntLiteral(0)),[],[Continue()])],([],[])),CallStmt(Id("print"),[Id("i")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,364))

    def test65(self):
        """Test for statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                For (i = 0, i < 10, 1) Do
                    If i > 5 Then
                        Break;
                    EndIf.
                    print(i);
                EndFor.
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(1),
                ([],
                [If([(BinaryOp(">",Id("i"),IntLiteral(5)),[],[Break()])],([],[])),CallStmt(Id("print"),[Id("i")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,365))

    def test66(self):
        """Test While statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                While x < 100 Do
                    Var: y = 5;
                    x = x + y;
                    If x >= 50 Then
                        Break;
                    EndIf.
                EndWhile.
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [While(BinaryOp("<",Id("x"),IntLiteral(100)),(
                [VarDecl(Id("y"),[],IntLiteral(5))],
                [Assign(Id("x"),BinaryOp("+",Id("x"),Id("y"))),
                 If([(BinaryOp(">=",Id("x"),IntLiteral(50)),[],[Break()])],([],[]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,366))

    def test67(self):
        """Test While statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                While x < 100 * 2 Do
                    Var: y = 5;
                    x = x + y;
                    If x >= 50 Then
                        Continue;
                    EndIf.
                EndWhile.
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [While(BinaryOp("<",Id("x"),BinaryOp("*",IntLiteral(100),IntLiteral(2))),(
                [VarDecl(Id("y"),[],IntLiteral(5))],
                [Assign(Id("x"),BinaryOp("+",Id("x"),Id("y"))),
                 If([(BinaryOp(">=",Id("x"),IntLiteral(50)),[],[Continue()])],([],[]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,367))

    def test68(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                a = (2 + 3)*(4 - 2);
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([],
                [Assign(Id("a"),BinaryOp("*",BinaryOp("+",IntLiteral(2),IntLiteral(3)),BinaryOp("-",IntLiteral(4),IntLiteral(2))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,368))

    def test69(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                a = (2 + 3)*(4 - 2) - 5 % 2;
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([],
                [Assign(Id("a"),BinaryOp("-",BinaryOp("*",BinaryOp("+",IntLiteral(2),IntLiteral(3)),
                BinaryOp("-",IntLiteral(4),IntLiteral(2))),BinaryOp("%",IntLiteral(5),IntLiteral(2))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,369))

    def test70(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                a = (2 + 3)*(4 - 2) - 5 % 2 * arr[0];
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([],
                [Assign(Id("a"),BinaryOp("-",BinaryOp("*",BinaryOp("+",IntLiteral(2),IntLiteral(3)),
                BinaryOp("-",IntLiteral(4),IntLiteral(2))),BinaryOp("*",BinaryOp("%",IntLiteral(5),IntLiteral(2)),ArrayCell(Id("arr"),[IntLiteral(0)]))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,370))

    def test71(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                a = (2 + 3)*(4 - 2) - 5 % 2 * arr[0 + x];
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([],
                [Assign(Id("a"),BinaryOp("-",BinaryOp("*",BinaryOp("+",IntLiteral(2),IntLiteral(3)),
                BinaryOp("-",IntLiteral(4),IntLiteral(2))),BinaryOp("*",BinaryOp("%",IntLiteral(5),IntLiteral(2)),ArrayCell(Id("arr"),[BinaryOp("+",IntLiteral(0),Id("x"))]))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,371))

    def test72(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                a = (2 + -3)*(4 - -2) - 5 % 2 * arr[0 + x];
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([],
                [Assign(Id("a"),BinaryOp("-",BinaryOp("*",BinaryOp("+",IntLiteral(2),UnaryOp("-",IntLiteral(3))),
                BinaryOp("-",IntLiteral(4),UnaryOp("-",IntLiteral(2)))),BinaryOp("*",BinaryOp("%",IntLiteral(5),IntLiteral(2)),ArrayCell(Id("arr"),[BinaryOp("+",IntLiteral(0),Id("x"))]))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,372))

    def test73(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                a = ---2;
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([],
                [Assign(Id("a"),UnaryOp("-",UnaryOp("-",UnaryOp("-",IntLiteral(2)))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,373))

    def test74(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                a = !!!True;
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([],
                [Assign(Id("a"),UnaryOp("!",UnaryOp("!",UnaryOp("!",BooleanLiteral(True)))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,374))

    def test75(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                If bool_of_string("True") Then
                    a = int_of_string(read());
                    b = float_of_int(a) +. 2.0;
                EndIf.
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([],
                [If([(CallExpr(Id("bool_of_string"),[StringLiteral("True")]),[],
                    [Assign(Id("a"),CallExpr(Id("int_of_string"),[CallExpr(Id("read"),[])])),
                     Assign(Id("b"),BinaryOp("+.",CallExpr(Id("float_of_int"),[Id("a")]),FloatLiteral(2.0)))])],
                    ([],[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,375))

    def test76(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                a[1][2] = 4 * 5 - 2;
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([],
                [Assign(ArrayCell(Id("a"),[IntLiteral(1),IntLiteral(2)]),BinaryOp("-",BinaryOp("*",IntLiteral(4),IntLiteral(5)),IntLiteral(2)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,376))

    def test77(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                a[1][foo(2)] = 4 * 5 - 2;
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([],
                [Assign(ArrayCell(Id("a"),[IntLiteral(1),CallExpr(Id("foo"),[IntLiteral(2)])]),BinaryOp("-",BinaryOp("*",IntLiteral(4),IntLiteral(5)),IntLiteral(2)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,377))

    def test78(self):
        """Test function declaration and expression"""
        input = """
        Var: x;
        Function: fact
            Parameter: n
            Body:
                If n==0 Then
                    Return 1;
                Else
                    Return n*fact(n-1);
                EndIf.
            EndBody.
        Function: main
            Body:
                x = 10;
                fact(x);
            EndBody.
        """
        expect = str(Program([VarDecl(Id("x"),[],None),
            FuncDecl(Id("fact"),[VarDecl(Id("n"),[],None)],([],[If([(BinaryOp("==",Id("n"),IntLiteral(0)),[],
            [Return(IntLiteral(1))])],([],[Return(BinaryOp("*",Id("n"),CallExpr(Id("fact"),[BinaryOp("-",Id("n"),IntLiteral(1))])))]))])),
            FuncDecl(Id("main"),[],([],[Assign(Id("x"),IntLiteral(10)),CallStmt(Id("fact"),[Id("x")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,378))

    def test79(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                a[3 + foo(2)] = a[b[2][3]];
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([],
                [Assign(ArrayCell(Id("a"),[BinaryOp("+",IntLiteral(3),CallExpr(Id("foo"),[IntLiteral(2)]))]),
                ArrayCell(Id("a"),[ArrayCell(Id("b"),[IntLiteral(2),IntLiteral(3)])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,379))

    def test80(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:

            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([],[]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,380))

    def test81(self):
        """Test function declaration and expression"""
        input = """
        Function: double
            Parameter: n
            Body:
                Return n * 2;
            EndBody.
        Function: main
            Body:
                Var: x = 5;
                print(double(x + 4));
            EndBody.
        """
        expect = str(Program([
            FuncDecl(Id("double"),[VarDecl(Id("n"),[],None)],([],[Return(BinaryOp("*",Id("n"),IntLiteral(2)))]))
            ,FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],[CallStmt(Id("print"),[CallExpr(Id("double"),[BinaryOp("+",Id("x"),IntLiteral(4))])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,381))

    def test82(self):
        """Test function declaration and expression"""
        input = """
        Function: double
            Parameter: n
            Body:
                Return n * 2;
            EndBody.
        Function: main
            Body:
                Var: x = 5;
                print(double(x + 4 - 3));
            EndBody.
        """
        expect = str(Program([
            FuncDecl(Id("double"),[VarDecl(Id("n"),[],None)],([],[Return(BinaryOp("*",Id("n"),IntLiteral(2)))]))
            ,FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],[CallStmt(Id("print"),[CallExpr(Id("double"),
            [BinaryOp("-",BinaryOp("+",Id("x"),IntLiteral(4)),IntLiteral(3))])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,382))

    def test83(self):
        """Test function declaration and expression"""
        input = """
        Function: add
            Parameter: a, b
            Body:
                Return a + b;
            EndBody.
        Function: main
            Body:
                Var: x = 5, y = 10;
                print(add(x, y));
            EndBody.
        """
        expect = str(Program([
            FuncDecl(Id("add"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([],[Return(BinaryOp("+",Id("a"),Id("b")))]))
            ,FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5)),VarDecl(Id("y"),[],IntLiteral(10))],
            [CallStmt(Id("print"),[CallExpr(Id("add"),[Id("x"),Id("y")])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,383))

    def test84(self):
        """Test function declaration and expression"""
        input = """
        Function: add
            Parameter: a, b
            Body:
                Return a + b;
            EndBody.
        Function: main
            Body:
                Var: x = 5, y = 10;
                print(add(2*x, y\\2));
            EndBody.
        """
        expect = str(Program([
            FuncDecl(Id("add"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([],[Return(BinaryOp("+",Id("a"),Id("b")))]))
            ,FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5)),VarDecl(Id("y"),[],IntLiteral(10))],
            [CallStmt(Id("print"),[CallExpr(Id("add"),[BinaryOp("*",IntLiteral(2),Id("x")),BinaryOp("\\",Id("y"),IntLiteral(2))])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,384))

    def test85(self):
        """Test function declaration and expression"""
        input = """
        Function: isGreaterZero
            Parameter: n
            Body:
                Return n > 0;
            EndBody.
        Function: main
            Body:
                Var: x = 5;
                print(isGreaterZero(4 * 4 - 3));
            EndBody.
        """
        expect = str(Program([
            FuncDecl(Id("isGreaterZero"),[VarDecl(Id("n"),[],None)],([],[Return(BinaryOp(">",Id("n"),IntLiteral(0)))]))
            ,FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],[CallStmt(Id("print"),[CallExpr(Id("isGreaterZero"),[BinaryOp("-",BinaryOp("*",IntLiteral(4),IntLiteral(4)),IntLiteral(3))])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,385))

    def test86(self):
        """Test function declaration and expression"""
        input = """
        Function: abs
            Parameter: n
            Body:
                If n >= 0 Then
                    Return n;
                Else
                    Return -n;
                EndIf.
            EndBody.
        Function: main
            Body:
                Var: x = 5;
                print(abs(x));
            EndBody.
        """
        expect = str(Program([
            FuncDecl(Id("abs"),[VarDecl(Id("n"),[],None)],([],[If([(BinaryOp(">=",Id("n"),IntLiteral(0)),[],[Return(Id("n"))])],([],[Return(UnaryOp("-",Id("n")))]))]))
            ,FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],[CallStmt(Id("print"),[CallExpr(Id("abs"),[Id("x")])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,386))

    def test87(self):
        """Test If statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                If x % 2 == 0 Then
                    Var: y = 2;
                    Var: y = 2;
                    x = x + 1;
                    x = x + 1;
                ElseIf x > 0 Then
                    Var: y = 2;
                    Var: y = 2;
                    x = x + 2;
                    x = x + 2;
                ElseIf x > 100 Then
                    Var: y = 2;
                    Var: y = 2;
                    x = x + 3;
                    x = x + 3;
                Else
                    Var: y = 2;
                    Var: y = 2;
                    x = x + 4;
                    x = x + 4;
                EndIf.
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [If([(BinaryOp("==",BinaryOp("%",Id("x"),IntLiteral(2)),IntLiteral(0)),[VarDecl(Id("y"),[],IntLiteral(2)),VarDecl(Id("y"),[],IntLiteral(2))],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1))),Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))]),
                     (BinaryOp(">",Id("x"),IntLiteral(0)),[VarDecl(Id("y"),[],IntLiteral(2)),VarDecl(Id("y"),[],IntLiteral(2))],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(2))),Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(2)))]),
                     (BinaryOp(">",Id("x"),IntLiteral(100)),[VarDecl(Id("y"),[],IntLiteral(2)),VarDecl(Id("y"),[],IntLiteral(2))],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(3))),Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(3)))])],
                    ([VarDecl(Id("y"),[],IntLiteral(2)),VarDecl(Id("y"),[],IntLiteral(2))],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(4))),Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(4)))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,387))

    def test88(self):
        """Test If statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                If x % 2 == 0 Then
                    Var: y = 2;
                    x = x + 1;
                ElseIf x > 0 Then
                    Var: y = 2;
                    x = x + 2;
                ElseIf x > 100 Then
                    Var: y = 2;
                    x = x + 3;
                Else
                    Var: y = 2;
                    x = x + 4;
                EndIf.
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [If([(BinaryOp("==",BinaryOp("%",Id("x"),IntLiteral(2)),IntLiteral(0)),[VarDecl(Id("y"),[],IntLiteral(2))],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))]),
                     (BinaryOp(">",Id("x"),IntLiteral(0)),[VarDecl(Id("y"),[],IntLiteral(2))],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(2)))]),
                     (BinaryOp(">",Id("x"),IntLiteral(100)),[VarDecl(Id("y"),[],IntLiteral(2))],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(3)))])],
                    ([VarDecl(Id("y"),[],IntLiteral(2))],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(4)))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,388))

    def test89(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                If x > 0 Then
                    print("x is greater than 0");
                EndIf.
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [If([(BinaryOp(">",Id("x"),IntLiteral(0)),[],[CallStmt(Id("print"),[StringLiteral("x is greater than 0")])])],([],[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,389))

    def test90(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                If x > 0 Then
                    print("x is greater than 0");
                ElseIf x == 0 Then
                    print("x is equal to 0");
                EndIf.
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [If([(BinaryOp(">",Id("x"),IntLiteral(0)),[],[CallStmt(Id("print"),[StringLiteral("x is greater than 0")])]),
                (BinaryOp("==",Id("x"),IntLiteral(0)),[],[CallStmt(Id("print"),[StringLiteral("x is equal to 0")])])],
                ([],[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,390))

    def test91(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                If x > 0 Then
                    print("x is greater than 0");
                ElseIf x == 0 Then
                    print("x is equal to 0");
                Else
                    print("nothing");
                EndIf.
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [If([(BinaryOp(">",Id("x"),IntLiteral(0)),[],[CallStmt(Id("print"),[StringLiteral("x is greater than 0")])]),
                (BinaryOp("==",Id("x"),IntLiteral(0)),[],[CallStmt(Id("print"),[StringLiteral("x is equal to 0")])])],
                ([],[CallStmt(Id("print"),[StringLiteral("nothing")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,391))

    def test92(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                If x > 0 Then
                    print("x is greater than 0");
                ElseIf x == 0 Then
                    print("x is equal to 0");
                ElseIf x == 0 Then
                    print("x is equal to 0");
                Else
                    print("nothing");
                EndIf.
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [If([(BinaryOp(">",Id("x"),IntLiteral(0)),[],[CallStmt(Id("print"),[StringLiteral("x is greater than 0")])]),
                (BinaryOp("==",Id("x"),IntLiteral(0)),[],[CallStmt(Id("print"),[StringLiteral("x is equal to 0")])]),
                (BinaryOp("==",Id("x"),IntLiteral(0)),[],[CallStmt(Id("print"),[StringLiteral("x is equal to 0")])])],
                ([],[CallStmt(Id("print"),[StringLiteral("nothing")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,392))

    def test93(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: x = 4.5, y = 5.2e-1, z = 6.9, t;
                Var: x = 4.5, y = 5.2e-1, z = 6.9, t;
                t = x *. y +. z *. 5e-10;
                t = x *. y +. z *. 5e-10;
                t = x *. y +. z *. 5e-10;
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],FloatLiteral(4.5)),VarDecl(Id("y"),[],FloatLiteral(5.2e-1)),
                VarDecl(Id("z"),[],FloatLiteral(6.9)), VarDecl(Id("t"),[],None),VarDecl(Id("x"),[],FloatLiteral(4.5)),VarDecl(Id("y"),[],FloatLiteral(5.2e-1)),
                VarDecl(Id("z"),[],FloatLiteral(6.9)), VarDecl(Id("t"),[],None)],
                [Assign(Id("t"),BinaryOp("+.",BinaryOp("*.",Id("x"),Id("y")),BinaryOp("*.",Id("z"),FloatLiteral(5e-10)))),
                 Assign(Id("t"),BinaryOp("+.",BinaryOp("*.",Id("x"),Id("y")),BinaryOp("*.",Id("z"),FloatLiteral(5e-10)))),
                 Assign(Id("t"),BinaryOp("+.",BinaryOp("*.",Id("x"),Id("y")),BinaryOp("*.",Id("z"),FloatLiteral(5e-10))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,393))

    def test94(self):
        """Test function declaration and expression"""
        input = """
        Var: x = 5;
        Var: x = 5;
        Var: x = 5;
        Function: main
            Body:
                Var: x = 4, y = 5, z = 6, t;
                t = x - y + z - 5;
            EndBody.
        """
        expect = str(Program([VarDecl(Id("x"),[],IntLiteral(5)),VarDecl(Id("x"),[],IntLiteral(5)),VarDecl(Id("x"),[],IntLiteral(5)),FuncDecl(Id("main"),[],
                ([VarDecl(Id("x"),[],IntLiteral(4)),VarDecl(Id("y"),[],IntLiteral(5)),
                VarDecl(Id("z"),[],IntLiteral(6)), VarDecl(Id("t"),[],None)],
                [Assign(Id("t"),BinaryOp("-",BinaryOp("+",BinaryOp("-",Id("x"),Id("y")),Id("z")),IntLiteral(5)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,394))

    def test95(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: x = 0xFF, y = 0XA, z = 0o567, t = 0O77;
                t = x - y + z - 5;
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(255)),VarDecl(Id("y"),[],IntLiteral(10)),
                VarDecl(Id("z"),[],IntLiteral(375)), VarDecl(Id("t"),[],IntLiteral(63))],
                [Assign(Id("t"),BinaryOp("-",BinaryOp("+",BinaryOp("-",Id("x"),Id("y")),Id("z")),IntLiteral(5)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,395))

    def test96(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: x = "This is a string containing tab \\t", y = "He asked me: '\"Where is John?'\"", z = "ab'"c\\n def", t = "a'bc\\'";
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],StringLiteral("This is a string containing tab \\t")),
                                                       VarDecl(Id("y"),[],StringLiteral("He asked me: '\"Where is John?'\"")),
                                                        VarDecl(Id("z"),[],StringLiteral("""ab'"c\\n def""")),
                                                       VarDecl(Id("t"),[],StringLiteral("a'bc\\'"))],
                []))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,396))

    def test97(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                If x > 0 Then
                    print("x is greater than 0");
                ElseIf x == 0 Then
                    print("x is equal to 0");
                ElseIf x == 0 Then
                    print("x is equal to 0");
                Else
                    print("nothing");
                EndIf.
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [If([(BinaryOp(">",Id("x"),IntLiteral(0)),[],[CallStmt(Id("print"),[StringLiteral("x is greater than 0")])]),
                (BinaryOp("==",Id("x"),IntLiteral(0)),[],[CallStmt(Id("print"),[StringLiteral("x is equal to 0")])]),
                (BinaryOp("==",Id("x"),IntLiteral(0)),[],[CallStmt(Id("print"),[StringLiteral("x is equal to 0")])])],
                ([],[CallStmt(Id("print"),[StringLiteral("nothing")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,397))

    def test98(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                If x > 0 Then
                    print("x is greater than 0");
                ElseIf x == 0 Then
                    print("x is equal to 0");
                ElseIf x == 0 Then
                    print("x is equal to 0");
                Else
                    print("nothing");
                EndIf.
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [If([(BinaryOp(">",Id("x"),IntLiteral(0)),[],[CallStmt(Id("print"),[StringLiteral("x is greater than 0")])]),
                (BinaryOp("==",Id("x"),IntLiteral(0)),[],[CallStmt(Id("print"),[StringLiteral("x is equal to 0")])]),
                (BinaryOp("==",Id("x"),IntLiteral(0)),[],[CallStmt(Id("print"),[StringLiteral("x is equal to 0")])])],
                ([],[CallStmt(Id("print"),[StringLiteral("nothing")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,398))

    def test99(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                If x > 0 Then
                    print("x is greater than 0");
                ElseIf x == 0 Then
                    print("x is equal to 0");
                ElseIf x == 0 Then
                    print("x is equal to 0");
                Else
                    print("nothing");
                EndIf.
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [If([(BinaryOp(">",Id("x"),IntLiteral(0)),[],[CallStmt(Id("print"),[StringLiteral("x is greater than 0")])]),
                (BinaryOp("==",Id("x"),IntLiteral(0)),[],[CallStmt(Id("print"),[StringLiteral("x is equal to 0")])]),
                (BinaryOp("==",Id("x"),IntLiteral(0)),[],[CallStmt(Id("print"),[StringLiteral("x is equal to 0")])])],
                ([],[CallStmt(Id("print"),[StringLiteral("nothing")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,399))

    def test100(self):
        """Test function declaration and expression"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                If x > 0 Then
                    print("x is greater than 0");
                ElseIf x == 0 Then
                    print("x is equal to 0");
                ElseIf x == 0 Then
                    print("x is equal to 0");
                Else
                    print("nothing");
                EndIf.
            EndBody.
        """
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],
                [If([(BinaryOp(">",Id("x"),IntLiteral(0)),[],[CallStmt(Id("print"),[StringLiteral("x is greater than 0")])]),
                (BinaryOp("==",Id("x"),IntLiteral(0)),[],[CallStmt(Id("print"),[StringLiteral("x is equal to 0")])]),
                (BinaryOp("==",Id("x"),IntLiteral(0)),[],[CallStmt(Id("print"),[StringLiteral("x is equal to 0")])])],
                ([],[CallStmt(Id("print"),[StringLiteral("nothing")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,400))