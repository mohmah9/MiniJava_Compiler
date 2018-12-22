# Generated from MiniJava.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniJavaParser import MiniJavaParser
else:
    from MiniJavaParser import MiniJavaParser

# This class defines a complete listener for a parse tree produced by MiniJavaParser.
class MiniJavaListener(ParseTreeListener):

    # Enter a parse tree produced by MiniJavaParser#goal.
    def enterGoal(self, ctx:MiniJavaParser.GoalContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#goal.
    def exitGoal(self, ctx:MiniJavaParser.GoalContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#mainclass.
    def enterMainclass(self, ctx:MiniJavaParser.MainclassContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#mainclass.
    def exitMainclass(self, ctx:MiniJavaParser.MainclassContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#dec_class.
    def enterDec_class(self, ctx:MiniJavaParser.Dec_classContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#dec_class.
    def exitDec_class(self, ctx:MiniJavaParser.Dec_classContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#dec_var.
    def enterDec_var(self, ctx:MiniJavaParser.Dec_varContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#dec_var.
    def exitDec_var(self, ctx:MiniJavaParser.Dec_varContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#dec_method.
    def enterDec_method(self, ctx:MiniJavaParser.Dec_methodContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#dec_method.
    def exitDec_method(self, ctx:MiniJavaParser.Dec_methodContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#parameters.
    def enterParameters(self, ctx:MiniJavaParser.ParametersContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#parameters.
    def exitParameters(self, ctx:MiniJavaParser.ParametersContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#parameterDeclaration.
    def enterParameterDeclaration(self, ctx:MiniJavaParser.ParameterDeclarationContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#parameterDeclaration.
    def exitParameterDeclaration(self, ctx:MiniJavaParser.ParameterDeclarationContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#mtype.
    def enterMtype(self, ctx:MiniJavaParser.MtypeContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#mtype.
    def exitMtype(self, ctx:MiniJavaParser.MtypeContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#state_lrparents.
    def enterState_lrparents(self, ctx:MiniJavaParser.State_lrparentsContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#state_lrparents.
    def exitState_lrparents(self, ctx:MiniJavaParser.State_lrparentsContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#state_if.
    def enterState_if(self, ctx:MiniJavaParser.State_ifContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#state_if.
    def exitState_if(self, ctx:MiniJavaParser.State_ifContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#state_while.
    def enterState_while(self, ctx:MiniJavaParser.State_whileContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#state_while.
    def exitState_while(self, ctx:MiniJavaParser.State_whileContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#state_print.
    def enterState_print(self, ctx:MiniJavaParser.State_printContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#state_print.
    def exitState_print(self, ctx:MiniJavaParser.State_printContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#state_def.
    def enterState_def(self, ctx:MiniJavaParser.State_defContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#state_def.
    def exitState_def(self, ctx:MiniJavaParser.State_defContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#state_array_def.
    def enterState_array_def(self, ctx:MiniJavaParser.State_array_defContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#state_array_def.
    def exitState_array_def(self, ctx:MiniJavaParser.State_array_defContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#expr_int.
    def enterExpr_int(self, ctx:MiniJavaParser.Expr_intContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#expr_int.
    def exitExpr_int(self, ctx:MiniJavaParser.Expr_intContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#expr_op.
    def enterExpr_op(self, ctx:MiniJavaParser.Expr_opContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#expr_op.
    def exitExpr_op(self, ctx:MiniJavaParser.Expr_opContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#expr_int_array.
    def enterExpr_int_array(self, ctx:MiniJavaParser.Expr_int_arrayContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#expr_int_array.
    def exitExpr_int_array(self, ctx:MiniJavaParser.Expr_int_arrayContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#expr_this.
    def enterExpr_this(self, ctx:MiniJavaParser.Expr_thisContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#expr_this.
    def exitExpr_this(self, ctx:MiniJavaParser.Expr_thisContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#expr_new_array.
    def enterExpr_new_array(self, ctx:MiniJavaParser.Expr_new_arrayContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#expr_new_array.
    def exitExpr_new_array(self, ctx:MiniJavaParser.Expr_new_arrayContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#expr_method_calling.
    def enterExpr_method_calling(self, ctx:MiniJavaParser.Expr_method_callingContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#expr_method_calling.
    def exitExpr_method_calling(self, ctx:MiniJavaParser.Expr_method_callingContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#expr_bool.
    def enterExpr_bool(self, ctx:MiniJavaParser.Expr_boolContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#expr_bool.
    def exitExpr_bool(self, ctx:MiniJavaParser.Expr_boolContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#expr_length.
    def enterExpr_length(self, ctx:MiniJavaParser.Expr_lengthContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#expr_length.
    def exitExpr_length(self, ctx:MiniJavaParser.Expr_lengthContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#expr_not.
    def enterExpr_not(self, ctx:MiniJavaParser.Expr_notContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#expr_not.
    def exitExpr_not(self, ctx:MiniJavaParser.Expr_notContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#expr_lrparents.
    def enterExpr_lrparents(self, ctx:MiniJavaParser.Expr_lrparentsContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#expr_lrparents.
    def exitExpr_lrparents(self, ctx:MiniJavaParser.Expr_lrparentsContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#expr_id.
    def enterExpr_id(self, ctx:MiniJavaParser.Expr_idContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#expr_id.
    def exitExpr_id(self, ctx:MiniJavaParser.Expr_idContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#expr_array.
    def enterExpr_array(self, ctx:MiniJavaParser.Expr_arrayContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#expr_array.
    def exitExpr_array(self, ctx:MiniJavaParser.Expr_arrayContext):
        pass


