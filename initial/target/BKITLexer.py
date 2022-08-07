# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u0221\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\3\2\3\2\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\6\3\6\3\7\3\7\3\7\3\7\5\7\u00b0\n\7\3\b\3\b\3\b")
        buf.write("\3\b\5\b\u00b6\n\b\3\t\3\t\3\t\7\t\u00bb\n\t\f\t\16\t")
        buf.write("\u00be\13\t\5\t\u00c0\n\t\3\n\3\n\7\n\u00c4\n\n\f\n\16")
        buf.write("\n\u00c7\13\n\3\13\3\13\5\13\u00cb\n\13\3\13\3\13\3\13")
        buf.write("\7\13\u00d0\n\13\f\13\16\13\u00d3\13\13\5\13\u00d5\n\13")
        buf.write("\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\7\16\u00e0\n\16")
        buf.write("\f\16\16\16\u00e3\13\16\5\16\u00e5\n\16\3\17\3\17\3\17")
        buf.write("\5\17\u00ea\n\17\3\17\3\17\7\17\u00ee\n\17\f\17\16\17")
        buf.write("\u00f1\13\17\3\20\3\20\3\20\7\20\u00f6\n\20\f\20\16\20")
        buf.write("\u00f9\13\20\3\21\3\21\3\21\5\21\u00fe\n\21\3\21\5\21")
        buf.write("\u0101\n\21\3\22\3\22\5\22\u0105\n\22\3\23\3\23\3\23\3")
        buf.write("\23\7\23\u010b\n\23\f\23\16\23\u010e\13\23\3\23\3\23\3")
        buf.write("\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3$\3$\3$\3$\3")
        buf.write("%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3(\3(\3(\3(\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.")
        buf.write("\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3\62\3\62")
        buf.write("\3\62\3\63\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\67\3\67\3\67\38\38\38\38\39\39\39\3:\3:\3:\3;\3;\3")
        buf.write(";\3;\3<\3<\3<\3<\3=\3=\3>\3>\3>\3?\3?\3?\3@\3@\3A\3A\3")
        buf.write("B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3J\3J\3")
        buf.write("K\3K\7K\u01ed\nK\fK\16K\u01f0\13K\3L\3L\3L\3L\7L\u01f6")
        buf.write("\nL\fL\16L\u01f9\13L\3L\3L\3L\3L\3L\3M\6M\u0201\nM\rM")
        buf.write("\16M\u0202\3M\3M\3N\3N\3N\3N\7N\u020b\nN\fN\16N\u020e")
        buf.write("\13N\3N\3N\3N\3N\3O\3O\3O\3O\7O\u0218\nO\fO\16O\u021b")
        buf.write("\13O\3O\3O\3P\3P\3P\3\u01f7\2Q\3\2\5\2\7\2\t\2\13\2\r")
        buf.write("\2\17\2\21\2\23\2\25\2\27\2\31\2\33\3\35\4\37\5!\6#\7")
        buf.write("%\b\'\t)\n+\13-\f/\r\61\16\63\17\65\20\67\219\22;\23=")
        buf.write("\24?\25A\26C\27E\30G\31I\32K\2M\2O\33Q\34S\35U\36W\37")
        buf.write("Y [!]\"_#a$c%e&g\'i(k)m*o+q,s-u.w/y\60{\61}\62\177\63")
        buf.write("\u0081\64\u0083\65\u0085\66\u0087\67\u00898\u008b9\u008d")
        buf.write(":\u008f;\u0091<\u0093=\u0095>\u0097?\u0099@\u009bA\u009d")
        buf.write("B\u009fC\3\2\16\3\2\62;\3\2\63;\3\2\629\3\2\639\3\2CH")
        buf.write("\4\2GGgg\4\2--//\t\2))^^ddhhppttvv\6\2\f\f\17\17$$^^\3")
        buf.write("\2c|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\2\u022f\2\33\3")
        buf.write("\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2")
        buf.write("\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2")
        buf.write("\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2")
        buf.write("\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2")
        buf.write("\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2")
        buf.write("\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3")
        buf.write("\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a")
        buf.write("\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2")
        buf.write("k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2")
        buf.write("\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2")
        buf.write("\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2")
        buf.write("\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093")
        buf.write("\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2")
        buf.write("\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\3\u00a1")
        buf.write("\3\2\2\2\5\u00a3\3\2\2\2\7\u00a5\3\2\2\2\t\u00a7\3\2\2")
        buf.write("\2\13\u00a9\3\2\2\2\r\u00af\3\2\2\2\17\u00b5\3\2\2\2\21")
        buf.write("\u00bf\3\2\2\2\23\u00c1\3\2\2\2\25\u00c8\3\2\2\2\27\u00d6")
        buf.write("\3\2\2\2\31\u00d9\3\2\2\2\33\u00e4\3\2\2\2\35\u00e6\3")
        buf.write("\2\2\2\37\u00f2\3\2\2\2!\u00fa\3\2\2\2#\u0104\3\2\2\2")
        buf.write("%\u0106\3\2\2\2\'\u0112\3\2\2\2)\u0117\3\2\2\2+\u011d")
        buf.write("\3\2\2\2-\u0126\3\2\2\2/\u0129\3\2\2\2\61\u012e\3\2\2")
        buf.write("\2\63\u0135\3\2\2\2\65\u013d\3\2\2\2\67\u0143\3\2\2\2")
        buf.write("9\u014a\3\2\2\2;\u0153\3\2\2\2=\u0157\3\2\2\2?\u0160\3")
        buf.write("\2\2\2A\u0163\3\2\2\2C\u016d\3\2\2\2E\u0174\3\2\2\2G\u0179")
        buf.write("\3\2\2\2I\u017d\3\2\2\2K\u0183\3\2\2\2M\u0188\3\2\2\2")
        buf.write("O\u018e\3\2\2\2Q\u0194\3\2\2\2S\u0196\3\2\2\2U\u0198\3")
        buf.write("\2\2\2W\u019a\3\2\2\2Y\u019c\3\2\2\2[\u019e\3\2\2\2]\u01a1")
        buf.write("\3\2\2\2_\u01a4\3\2\2\2a\u01a7\3\2\2\2c\u01aa\3\2\2\2")
        buf.write("e\u01ad\3\2\2\2g\u01b0\3\2\2\2i\u01b2\3\2\2\2k\u01b4\3")
        buf.write("\2\2\2m\u01b7\3\2\2\2o\u01ba\3\2\2\2q\u01be\3\2\2\2s\u01c1")
        buf.write("\3\2\2\2u\u01c4\3\2\2\2w\u01c8\3\2\2\2y\u01cc\3\2\2\2")
        buf.write("{\u01ce\3\2\2\2}\u01d1\3\2\2\2\177\u01d4\3\2\2\2\u0081")
        buf.write("\u01d6\3\2\2\2\u0083\u01d8\3\2\2\2\u0085\u01da\3\2\2\2")
        buf.write("\u0087\u01dc\3\2\2\2\u0089\u01de\3\2\2\2\u008b\u01e0\3")
        buf.write("\2\2\2\u008d\u01e2\3\2\2\2\u008f\u01e4\3\2\2\2\u0091\u01e6")
        buf.write("\3\2\2\2\u0093\u01e8\3\2\2\2\u0095\u01ea\3\2\2\2\u0097")
        buf.write("\u01f1\3\2\2\2\u0099\u0200\3\2\2\2\u009b\u0206\3\2\2\2")
        buf.write("\u009d\u0213\3\2\2\2\u009f\u021e\3\2\2\2\u00a1\u00a2\t")
        buf.write("\2\2\2\u00a2\4\3\2\2\2\u00a3\u00a4\t\3\2\2\u00a4\6\3\2")
        buf.write("\2\2\u00a5\u00a6\t\4\2\2\u00a6\b\3\2\2\2\u00a7\u00a8\t")
        buf.write("\5\2\2\u00a8\n\3\2\2\2\u00a9\u00aa\t\6\2\2\u00aa\f\3\2")
        buf.write("\2\2\u00ab\u00ac\7\62\2\2\u00ac\u00b0\7Z\2\2\u00ad\u00ae")
        buf.write("\7\62\2\2\u00ae\u00b0\7z\2\2\u00af\u00ab\3\2\2\2\u00af")
        buf.write("\u00ad\3\2\2\2\u00b0\16\3\2\2\2\u00b1\u00b2\7\62\2\2\u00b2")
        buf.write("\u00b6\7Q\2\2\u00b3\u00b4\7\62\2\2\u00b4\u00b6\7q\2\2")
        buf.write("\u00b5\u00b1\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b6\20\3\2")
        buf.write("\2\2\u00b7\u00c0\7\62\2\2\u00b8\u00bc\t\3\2\2\u00b9\u00bb")
        buf.write("\t\2\2\2\u00ba\u00b9\3\2\2\2\u00bb\u00be\3\2\2\2\u00bc")
        buf.write("\u00ba\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\u00c0\3\2\2\2")
        buf.write("\u00be\u00bc\3\2\2\2\u00bf\u00b7\3\2\2\2\u00bf\u00b8\3")
        buf.write("\2\2\2\u00c0\22\3\2\2\2\u00c1\u00c5\7\60\2\2\u00c2\u00c4")
        buf.write("\t\2\2\2\u00c3\u00c2\3\2\2\2\u00c4\u00c7\3\2\2\2\u00c5")
        buf.write("\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\24\3\2\2\2\u00c7")
        buf.write("\u00c5\3\2\2\2\u00c8\u00ca\t\7\2\2\u00c9\u00cb\t\b\2\2")
        buf.write("\u00ca\u00c9\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00d4\3")
        buf.write("\2\2\2\u00cc\u00d5\7\62\2\2\u00cd\u00d1\t\3\2\2\u00ce")
        buf.write("\u00d0\t\2\2\2\u00cf\u00ce\3\2\2\2\u00d0\u00d3\3\2\2\2")
        buf.write("\u00d1\u00cf\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d5\3")
        buf.write("\2\2\2\u00d3\u00d1\3\2\2\2\u00d4\u00cc\3\2\2\2\u00d4\u00cd")
        buf.write("\3\2\2\2\u00d5\26\3\2\2\2\u00d6\u00d7\7^\2\2\u00d7\u00d8")
        buf.write("\t\t\2\2\u00d8\30\3\2\2\2\u00d9\u00da\7)\2\2\u00da\u00db")
        buf.write("\7$\2\2\u00db\32\3\2\2\2\u00dc\u00e5\7\62\2\2\u00dd\u00e1")
        buf.write("\5\5\3\2\u00de\u00e0\5\3\2\2\u00df\u00de\3\2\2\2\u00e0")
        buf.write("\u00e3\3\2\2\2\u00e1\u00df\3\2\2\2\u00e1\u00e2\3\2\2\2")
        buf.write("\u00e2\u00e5\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e4\u00dc\3")
        buf.write("\2\2\2\u00e4\u00dd\3\2\2\2\u00e5\34\3\2\2\2\u00e6\u00e9")
        buf.write("\5\r\7\2\u00e7\u00ea\5\5\3\2\u00e8\u00ea\5\13\6\2\u00e9")
        buf.write("\u00e7\3\2\2\2\u00e9\u00e8\3\2\2\2\u00ea\u00ef\3\2\2\2")
        buf.write("\u00eb\u00ee\5\3\2\2\u00ec\u00ee\5\13\6\2\u00ed\u00eb")
        buf.write("\3\2\2\2\u00ed\u00ec\3\2\2\2\u00ee\u00f1\3\2\2\2\u00ef")
        buf.write("\u00ed\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0\36\3\2\2\2\u00f1")
        buf.write("\u00ef\3\2\2\2\u00f2\u00f3\5\17\b\2\u00f3\u00f7\5\7\4")
        buf.write("\2\u00f4\u00f6\5\t\5\2\u00f5\u00f4\3\2\2\2\u00f6\u00f9")
        buf.write("\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8")
        buf.write(" \3\2\2\2\u00f9\u00f7\3\2\2\2\u00fa\u0100\5\21\t\2\u00fb")
        buf.write("\u00fd\5\23\n\2\u00fc\u00fe\5\25\13\2\u00fd\u00fc\3\2")
        buf.write("\2\2\u00fd\u00fe\3\2\2\2\u00fe\u0101\3\2\2\2\u00ff\u0101")
        buf.write("\5\25\13\2\u0100\u00fb\3\2\2\2\u0100\u00ff\3\2\2\2\u0101")
        buf.write("\"\3\2\2\2\u0102\u0105\5K&\2\u0103\u0105\5M\'\2\u0104")
        buf.write("\u0102\3\2\2\2\u0104\u0103\3\2\2\2\u0105$\3\2\2\2\u0106")
        buf.write("\u010c\7$\2\2\u0107\u010b\5\31\r\2\u0108\u010b\5\27\f")
        buf.write("\2\u0109\u010b\n\n\2\2\u010a\u0107\3\2\2\2\u010a\u0108")
        buf.write("\3\2\2\2\u010a\u0109\3\2\2\2\u010b\u010e\3\2\2\2\u010c")
        buf.write("\u010a\3\2\2\2\u010c\u010d\3\2\2\2\u010d\u010f\3\2\2\2")
        buf.write("\u010e\u010c\3\2\2\2\u010f\u0110\7$\2\2\u0110\u0111\b")
        buf.write("\23\2\2\u0111&\3\2\2\2\u0112\u0113\7D\2\2\u0113\u0114")
        buf.write("\7q\2\2\u0114\u0115\7f\2\2\u0115\u0116\7{\2\2\u0116(\3")
        buf.write("\2\2\2\u0117\u0118\7D\2\2\u0118\u0119\7t\2\2\u0119\u011a")
        buf.write("\7g\2\2\u011a\u011b\7c\2\2\u011b\u011c\7m\2\2\u011c*\3")
        buf.write("\2\2\2\u011d\u011e\7E\2\2\u011e\u011f\7q\2\2\u011f\u0120")
        buf.write("\7p\2\2\u0120\u0121\7v\2\2\u0121\u0122\7k\2\2\u0122\u0123")
        buf.write("\7p\2\2\u0123\u0124\7w\2\2\u0124\u0125\7g\2\2\u0125,\3")
        buf.write("\2\2\2\u0126\u0127\7F\2\2\u0127\u0128\7q\2\2\u0128.\3")
        buf.write("\2\2\2\u0129\u012a\7G\2\2\u012a\u012b\7n\2\2\u012b\u012c")
        buf.write("\7u\2\2\u012c\u012d\7g\2\2\u012d\60\3\2\2\2\u012e\u012f")
        buf.write("\7G\2\2\u012f\u0130\7n\2\2\u0130\u0131\7u\2\2\u0131\u0132")
        buf.write("\7g\2\2\u0132\u0133\7K\2\2\u0133\u0134\7h\2\2\u0134\62")
        buf.write("\3\2\2\2\u0135\u0136\7G\2\2\u0136\u0137\7p\2\2\u0137\u0138")
        buf.write("\7f\2\2\u0138\u0139\7D\2\2\u0139\u013a\7q\2\2\u013a\u013b")
        buf.write("\7f\2\2\u013b\u013c\7{\2\2\u013c\64\3\2\2\2\u013d\u013e")
        buf.write("\7G\2\2\u013e\u013f\7p\2\2\u013f\u0140\7f\2\2\u0140\u0141")
        buf.write("\7K\2\2\u0141\u0142\7h\2\2\u0142\66\3\2\2\2\u0143\u0144")
        buf.write("\7G\2\2\u0144\u0145\7p\2\2\u0145\u0146\7f\2\2\u0146\u0147")
        buf.write("\7H\2\2\u0147\u0148\7q\2\2\u0148\u0149\7t\2\2\u01498\3")
        buf.write("\2\2\2\u014a\u014b\7G\2\2\u014b\u014c\7p\2\2\u014c\u014d")
        buf.write("\7f\2\2\u014d\u014e\7Y\2\2\u014e\u014f\7j\2\2\u014f\u0150")
        buf.write("\7k\2\2\u0150\u0151\7n\2\2\u0151\u0152\7g\2\2\u0152:\3")
        buf.write("\2\2\2\u0153\u0154\7H\2\2\u0154\u0155\7q\2\2\u0155\u0156")
        buf.write("\7t\2\2\u0156<\3\2\2\2\u0157\u0158\7H\2\2\u0158\u0159")
        buf.write("\7w\2\2\u0159\u015a\7p\2\2\u015a\u015b\7e\2\2\u015b\u015c")
        buf.write("\7v\2\2\u015c\u015d\7k\2\2\u015d\u015e\7q\2\2\u015e\u015f")
        buf.write("\7p\2\2\u015f>\3\2\2\2\u0160\u0161\7K\2\2\u0161\u0162")
        buf.write("\7h\2\2\u0162@\3\2\2\2\u0163\u0164\7R\2\2\u0164\u0165")
        buf.write("\7c\2\2\u0165\u0166\7t\2\2\u0166\u0167\7c\2\2\u0167\u0168")
        buf.write("\7o\2\2\u0168\u0169\7g\2\2\u0169\u016a\7v\2\2\u016a\u016b")
        buf.write("\7g\2\2\u016b\u016c\7t\2\2\u016cB\3\2\2\2\u016d\u016e")
        buf.write("\7T\2\2\u016e\u016f\7g\2\2\u016f\u0170\7v\2\2\u0170\u0171")
        buf.write("\7w\2\2\u0171\u0172\7t\2\2\u0172\u0173\7p\2\2\u0173D\3")
        buf.write("\2\2\2\u0174\u0175\7V\2\2\u0175\u0176\7j\2\2\u0176\u0177")
        buf.write("\7g\2\2\u0177\u0178\7p\2\2\u0178F\3\2\2\2\u0179\u017a")
        buf.write("\7X\2\2\u017a\u017b\7c\2\2\u017b\u017c\7t\2\2\u017cH\3")
        buf.write("\2\2\2\u017d\u017e\7Y\2\2\u017e\u017f\7j\2\2\u017f\u0180")
        buf.write("\7k\2\2\u0180\u0181\7n\2\2\u0181\u0182\7g\2\2\u0182J\3")
        buf.write("\2\2\2\u0183\u0184\7V\2\2\u0184\u0185\7t\2\2\u0185\u0186")
        buf.write("\7w\2\2\u0186\u0187\7g\2\2\u0187L\3\2\2\2\u0188\u0189")
        buf.write("\7H\2\2\u0189\u018a\7c\2\2\u018a\u018b\7n\2\2\u018b\u018c")
        buf.write("\7u\2\2\u018c\u018d\7g\2\2\u018dN\3\2\2\2\u018e\u018f")
        buf.write("\7G\2\2\u018f\u0190\7p\2\2\u0190\u0191\7f\2\2\u0191\u0192")
        buf.write("\7F\2\2\u0192\u0193\7q\2\2\u0193P\3\2\2\2\u0194\u0195")
        buf.write("\7-\2\2\u0195R\3\2\2\2\u0196\u0197\7/\2\2\u0197T\3\2\2")
        buf.write("\2\u0198\u0199\7,\2\2\u0199V\3\2\2\2\u019a\u019b\7^\2")
        buf.write("\2\u019bX\3\2\2\2\u019c\u019d\7\'\2\2\u019dZ\3\2\2\2\u019e")
        buf.write("\u019f\7-\2\2\u019f\u01a0\7\60\2\2\u01a0\\\3\2\2\2\u01a1")
        buf.write("\u01a2\7/\2\2\u01a2\u01a3\7\60\2\2\u01a3^\3\2\2\2\u01a4")
        buf.write("\u01a5\7,\2\2\u01a5\u01a6\7\60\2\2\u01a6`\3\2\2\2\u01a7")
        buf.write("\u01a8\7^\2\2\u01a8\u01a9\7\60\2\2\u01a9b\3\2\2\2\u01aa")
        buf.write("\u01ab\7?\2\2\u01ab\u01ac\7?\2\2\u01acd\3\2\2\2\u01ad")
        buf.write("\u01ae\7#\2\2\u01ae\u01af\7?\2\2\u01aff\3\2\2\2\u01b0")
        buf.write("\u01b1\7>\2\2\u01b1h\3\2\2\2\u01b2\u01b3\7@\2\2\u01b3")
        buf.write("j\3\2\2\2\u01b4\u01b5\7>\2\2\u01b5\u01b6\7?\2\2\u01b6")
        buf.write("l\3\2\2\2\u01b7\u01b8\7@\2\2\u01b8\u01b9\7?\2\2\u01b9")
        buf.write("n\3\2\2\2\u01ba\u01bb\7?\2\2\u01bb\u01bc\7\61\2\2\u01bc")
        buf.write("\u01bd\7?\2\2\u01bdp\3\2\2\2\u01be\u01bf\7>\2\2\u01bf")
        buf.write("\u01c0\7\60\2\2\u01c0r\3\2\2\2\u01c1\u01c2\7@\2\2\u01c2")
        buf.write("\u01c3\7\60\2\2\u01c3t\3\2\2\2\u01c4\u01c5\7>\2\2\u01c5")
        buf.write("\u01c6\7?\2\2\u01c6\u01c7\7\60\2\2\u01c7v\3\2\2\2\u01c8")
        buf.write("\u01c9\7@\2\2\u01c9\u01ca\7?\2\2\u01ca\u01cb\7\60\2\2")
        buf.write("\u01cbx\3\2\2\2\u01cc\u01cd\7#\2\2\u01cdz\3\2\2\2\u01ce")
        buf.write("\u01cf\7(\2\2\u01cf\u01d0\7(\2\2\u01d0|\3\2\2\2\u01d1")
        buf.write("\u01d2\7~\2\2\u01d2\u01d3\7~\2\2\u01d3~\3\2\2\2\u01d4")
        buf.write("\u01d5\7?\2\2\u01d5\u0080\3\2\2\2\u01d6\u01d7\7]\2\2\u01d7")
        buf.write("\u0082\3\2\2\2\u01d8\u01d9\7_\2\2\u01d9\u0084\3\2\2\2")
        buf.write("\u01da\u01db\7*\2\2\u01db\u0086\3\2\2\2\u01dc\u01dd\7")
        buf.write("+\2\2\u01dd\u0088\3\2\2\2\u01de\u01df\7}\2\2\u01df\u008a")
        buf.write("\3\2\2\2\u01e0\u01e1\7\177\2\2\u01e1\u008c\3\2\2\2\u01e2")
        buf.write("\u01e3\7=\2\2\u01e3\u008e\3\2\2\2\u01e4\u01e5\7<\2\2\u01e5")
        buf.write("\u0090\3\2\2\2\u01e6\u01e7\7.\2\2\u01e7\u0092\3\2\2\2")
        buf.write("\u01e8\u01e9\7\60\2\2\u01e9\u0094\3\2\2\2\u01ea\u01ee")
        buf.write("\t\13\2\2\u01eb\u01ed\t\f\2\2\u01ec\u01eb\3\2\2\2\u01ed")
        buf.write("\u01f0\3\2\2\2\u01ee\u01ec\3\2\2\2\u01ee\u01ef\3\2\2\2")
        buf.write("\u01ef\u0096\3\2\2\2\u01f0\u01ee\3\2\2\2\u01f1\u01f2\7")
        buf.write(",\2\2\u01f2\u01f3\7,\2\2\u01f3\u01f7\3\2\2\2\u01f4\u01f6")
        buf.write("\13\2\2\2\u01f5\u01f4\3\2\2\2\u01f6\u01f9\3\2\2\2\u01f7")
        buf.write("\u01f8\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f8\u01fa\3\2\2\2")
        buf.write("\u01f9\u01f7\3\2\2\2\u01fa\u01fb\7,\2\2\u01fb\u01fc\7")
        buf.write(",\2\2\u01fc\u01fd\3\2\2\2\u01fd\u01fe\bL\3\2\u01fe\u0098")
        buf.write("\3\2\2\2\u01ff\u0201\t\r\2\2\u0200\u01ff\3\2\2\2\u0201")
        buf.write("\u0202\3\2\2\2\u0202\u0200\3\2\2\2\u0202\u0203\3\2\2\2")
        buf.write("\u0203\u0204\3\2\2\2\u0204\u0205\bM\3\2\u0205\u009a\3")
        buf.write("\2\2\2\u0206\u020c\7$\2\2\u0207\u020b\5\31\r\2\u0208\u020b")
        buf.write("\5\27\f\2\u0209\u020b\n\n\2\2\u020a\u0207\3\2\2\2\u020a")
        buf.write("\u0208\3\2\2\2\u020a\u0209\3\2\2\2\u020b\u020e\3\2\2\2")
        buf.write("\u020c\u020a\3\2\2\2\u020c\u020d\3\2\2\2\u020d\u020f\3")
        buf.write("\2\2\2\u020e\u020c\3\2\2\2\u020f\u0210\7^\2\2\u0210\u0211")
        buf.write("\n\t\2\2\u0211\u0212\bN\4\2\u0212\u009c\3\2\2\2\u0213")
        buf.write("\u0219\7$\2\2\u0214\u0218\5\31\r\2\u0215\u0218\5\27\f")
        buf.write("\2\u0216\u0218\n\n\2\2\u0217\u0214\3\2\2\2\u0217\u0215")
        buf.write("\3\2\2\2\u0217\u0216\3\2\2\2\u0218\u021b\3\2\2\2\u0219")
        buf.write("\u0217\3\2\2\2\u0219\u021a\3\2\2\2\u021a\u021c\3\2\2\2")
        buf.write("\u021b\u0219\3\2\2\2\u021c\u021d\bO\5\2\u021d\u009e\3")
        buf.write("\2\2\2\u021e\u021f\13\2\2\2\u021f\u0220\bP\6\2\u0220\u00a0")
        buf.write("\3\2\2\2\35\2\u00af\u00b5\u00bc\u00bf\u00c5\u00ca\u00d1")
        buf.write("\u00d4\u00e1\u00e4\u00e9\u00ed\u00ef\u00f7\u00fd\u0100")
        buf.write("\u0104\u010a\u010c\u01ee\u01f7\u0202\u020a\u020c\u0217")
        buf.write("\u0219\7\3\23\2\b\2\2\3N\3\3O\4\3P\5")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    DEC_INT_LIT = 1
    HEX_INT_LIT = 2
    OCT_INT_LIT = 3
    FLT_LIT = 4
    BOOL_LIT = 5
    STR_LIT = 6
    BODY = 7
    BREAK = 8
    CONTINUE = 9
    DO = 10
    ELSE = 11
    ELSEIF = 12
    ENDBODY = 13
    ENDIF = 14
    ENDFOR = 15
    ENDWHILE = 16
    FOR = 17
    FUNCTION = 18
    IF = 19
    PARAMETER = 20
    RETURN = 21
    THEN = 22
    VAR = 23
    WHILE = 24
    ENDDO = 25
    ADD_I = 26
    SUB_I = 27
    MUL_I = 28
    DIV_I = 29
    MOD_I = 30
    ADD_F = 31
    SUB_F = 32
    MUL_F = 33
    DIV_F = 34
    EQ_I = 35
    NEQ_I = 36
    LT_I = 37
    GT_I = 38
    LTE_I = 39
    GTE_I = 40
    NEQ_F = 41
    LT_F = 42
    GT_F = 43
    LTE_F = 44
    GTE_F = 45
    NOT = 46
    AND = 47
    OR = 48
    ASSIGN = 49
    LS = 50
    RS = 51
    LB = 52
    RB = 53
    LC = 54
    RC = 55
    SEMI = 56
    COLON = 57
    COMMA = 58
    DOT = 59
    ID = 60
    COMMENT = 61
    WS = 62
    ILLEGAL_ESCAPE = 63
    UNCLOSE_STRING = 64
    ERROR_CHAR = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", "'ElseIf'", 
            "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", "'For'", "'Function'", 
            "'If'", "'Parameter'", "'Return'", "'Then'", "'Var'", "'While'", 
            "'EndDo'", "'+'", "'-'", "'*'", "'\\'", "'%'", "'+.'", "'-.'", 
            "'*.'", "'\\.'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
            "'=/='", "'<.'", "'>.'", "'<=.'", "'>=.'", "'!'", "'&&'", "'||'", 
            "'='", "'['", "']'", "'('", "')'", "'{'", "'}'", "';'", "':'", 
            "','", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "DEC_INT_LIT", "HEX_INT_LIT", "OCT_INT_LIT", "FLT_LIT", "BOOL_LIT", 
            "STR_LIT", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", 
            "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", 
            "IF", "PARAMETER", "RETURN", "THEN", "VAR", "WHILE", "ENDDO", 
            "ADD_I", "SUB_I", "MUL_I", "DIV_I", "MOD_I", "ADD_F", "SUB_F", 
            "MUL_F", "DIV_F", "EQ_I", "NEQ_I", "LT_I", "GT_I", "LTE_I", 
            "GTE_I", "NEQ_F", "LT_F", "GT_F", "LTE_F", "GTE_F", "NOT", "AND", 
            "OR", "ASSIGN", "LS", "RS", "LB", "RB", "LC", "RC", "SEMI", 
            "COLON", "COMMA", "DOT", "ID", "COMMENT", "WS", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "DEGIT", "DEGIT_NO_ZERO", "OCT_DEGIT", "OCT_DEGIT_NO_ZERO", 
                  "HEX_CHAR", "HEX_PREFIX", "OCT_PREFIX", "FLT_INT_PART", 
                  "FLT_DEC_PART", "FLT_EXP_PART", "ESCAPE_CHAR", "DOUBLE_QUOTE_CHAR", 
                  "DEC_INT_LIT", "HEX_INT_LIT", "OCT_INT_LIT", "FLT_LIT", 
                  "BOOL_LIT", "STR_LIT", "BODY", "BREAK", "CONTINUE", "DO", 
                  "ELSE", "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", 
                  "FOR", "FUNCTION", "IF", "PARAMETER", "RETURN", "THEN", 
                  "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", "ADD_I", "SUB_I", 
                  "MUL_I", "DIV_I", "MOD_I", "ADD_F", "SUB_F", "MUL_F", 
                  "DIV_F", "EQ_I", "NEQ_I", "LT_I", "GT_I", "LTE_I", "GTE_I", 
                  "NEQ_F", "LT_F", "GT_F", "LTE_F", "GTE_F", "NOT", "AND", 
                  "OR", "ASSIGN", "LS", "RS", "LB", "RB", "LC", "RC", "SEMI", 
                  "COLON", "COMMA", "DOT", "ID", "COMMENT", "WS", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING", "ERROR_CHAR" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[17] = self.STR_LIT_action 
            actions[76] = self.ILLEGAL_ESCAPE_action 
            actions[77] = self.UNCLOSE_STRING_action 
            actions[78] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STR_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                raise IllegalEscape(self.text[1:])

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	raise UncloseString(self.text[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	raise ErrorToken(self.text);

     


