// Generated from /home/ana/Área de Trabalho/2019-1/compiladores/final/trabalhofinal-ana/gramaticaRegular.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class gramaticaRegularParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, VAR_T=14, VAR=15, VAZIO=16;
	public static final int
		RULE_simbolos = 0, RULE_simbolos_t = 1, RULE_gram = 2, RULE_naoterminais = 3, 
		RULE_terminais = 4, RULE_producoes = 5, RULE_producao = 6, RULE_transicao = 7, 
		RULE_inicial = 8;
	public static final String[] ruleNames = {
		"simbolos", "simbolos_t", "gram", "naoterminais", "terminais", "producoes", 
		"producao", "transicao", "inicial"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "', '", "'V'", "'T'", "'P'", "'S'", "'= ['", "']'", "'('", "' > '", 
		"')'", "'), '", "' | '", "'= '", null, null, "'#'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, "VAR_T", "VAR", "VAZIO"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "gramaticaRegular.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public gramaticaRegularParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class SimbolosContext extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(gramaticaRegularParser.VAR, 0); }
		public SimbolosContext simbolos() {
			return getRuleContext(SimbolosContext.class,0);
		}
		public SimbolosContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_simbolos; }
	}

	public final SimbolosContext simbolos() throws RecognitionException {
		SimbolosContext _localctx = new SimbolosContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_simbolos);
		try {
			setState(22);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(18);
				match(VAR);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(19);
				match(VAR);
				setState(20);
				match(T__0);
				setState(21);
				simbolos();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Simbolos_tContext extends ParserRuleContext {
		public TerminalNode VAR_T() { return getToken(gramaticaRegularParser.VAR_T, 0); }
		public Simbolos_tContext simbolos_t() {
			return getRuleContext(Simbolos_tContext.class,0);
		}
		public Simbolos_tContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_simbolos_t; }
	}

	public final Simbolos_tContext simbolos_t() throws RecognitionException {
		Simbolos_tContext _localctx = new Simbolos_tContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_simbolos_t);
		try {
			setState(28);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(24);
				match(VAR_T);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(25);
				match(VAR_T);
				setState(26);
				match(T__0);
				setState(27);
				simbolos_t();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class GramContext extends ParserRuleContext {
		public NaoterminaisContext naoterminais() {
			return getRuleContext(NaoterminaisContext.class,0);
		}
		public TerminaisContext terminais() {
			return getRuleContext(TerminaisContext.class,0);
		}
		public ProducoesContext producoes() {
			return getRuleContext(ProducoesContext.class,0);
		}
		public InicialContext inicial() {
			return getRuleContext(InicialContext.class,0);
		}
		public GramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_gram; }
	}

	public final GramContext gram() throws RecognitionException {
		GramContext _localctx = new GramContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_gram);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(30);
			match(T__1);
			setState(31);
			naoterminais();
			setState(32);
			match(T__2);
			setState(33);
			terminais();
			setState(34);
			match(T__3);
			setState(35);
			producoes();
			setState(36);
			match(T__4);
			setState(37);
			inicial();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class NaoterminaisContext extends ParserRuleContext {
		public SimbolosContext simbolos() {
			return getRuleContext(SimbolosContext.class,0);
		}
		public NaoterminaisContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_naoterminais; }
	}

	public final NaoterminaisContext naoterminais() throws RecognitionException {
		NaoterminaisContext _localctx = new NaoterminaisContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_naoterminais);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(39);
			match(T__5);
			setState(40);
			simbolos();
			setState(41);
			match(T__6);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TerminaisContext extends ParserRuleContext {
		public Simbolos_tContext simbolos_t() {
			return getRuleContext(Simbolos_tContext.class,0);
		}
		public TerminaisContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_terminais; }
	}

	public final TerminaisContext terminais() throws RecognitionException {
		TerminaisContext _localctx = new TerminaisContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_terminais);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(43);
			match(T__5);
			setState(44);
			simbolos_t();
			setState(45);
			match(T__6);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ProducoesContext extends ParserRuleContext {
		public ProducaoContext producao() {
			return getRuleContext(ProducaoContext.class,0);
		}
		public ProducoesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_producoes; }
	}

	public final ProducoesContext producoes() throws RecognitionException {
		ProducoesContext _localctx = new ProducoesContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_producoes);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(47);
			match(T__5);
			setState(48);
			producao();
			setState(49);
			match(T__6);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ProducaoContext extends ParserRuleContext {
		public TerminalNode VAR_T() { return getToken(gramaticaRegularParser.VAR_T, 0); }
		public TransicaoContext transicao() {
			return getRuleContext(TransicaoContext.class,0);
		}
		public ProducaoContext producao() {
			return getRuleContext(ProducaoContext.class,0);
		}
		public ProducaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_producao; }
	}

	public final ProducaoContext producao() throws RecognitionException {
		ProducaoContext _localctx = new ProducaoContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_producao);
		try {
			setState(64);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(51);
				match(T__7);
				setState(52);
				match(VAR_T);
				setState(53);
				match(T__8);
				setState(54);
				transicao();
				setState(55);
				match(T__9);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(57);
				match(T__7);
				setState(58);
				match(VAR_T);
				setState(59);
				match(T__8);
				setState(60);
				transicao();
				setState(61);
				match(T__10);
				setState(62);
				producao();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TransicaoContext extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(gramaticaRegularParser.VAR, 0); }
		public TerminalNode VAR_T() { return getToken(gramaticaRegularParser.VAR_T, 0); }
		public TransicaoContext transicao() {
			return getRuleContext(TransicaoContext.class,0);
		}
		public TerminalNode VAZIO() { return getToken(gramaticaRegularParser.VAZIO, 0); }
		public TransicaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_transicao; }
	}

	public final TransicaoContext transicao() throws RecognitionException {
		TransicaoContext _localctx = new TransicaoContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_transicao);
		try {
			setState(71);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VAR:
				enterOuterAlt(_localctx, 1);
				{
				setState(66);
				match(VAR);
				setState(67);
				match(VAR_T);
				setState(68);
				match(T__11);
				setState(69);
				transicao();
				}
				break;
			case VAZIO:
				enterOuterAlt(_localctx, 2);
				{
				setState(70);
				match(VAZIO);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class InicialContext extends ParserRuleContext {
		public TerminalNode VAR_T() { return getToken(gramaticaRegularParser.VAR_T, 0); }
		public InicialContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_inicial; }
	}

	public final InicialContext inicial() throws RecognitionException {
		InicialContext _localctx = new InicialContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_inicial);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(73);
			match(T__12);
			setState(74);
			match(VAR_T);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22O\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2"+
		"\3\2\5\2\31\n\2\3\3\3\3\3\3\3\3\5\3\37\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4"+
		"\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3"+
		"\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\bC\n\b\3\t\3\t\3\t\3\t\3\t\5"+
		"\tJ\n\t\3\n\3\n\3\n\3\n\2\2\13\2\4\6\b\n\f\16\20\22\2\2\2I\2\30\3\2\2"+
		"\2\4\36\3\2\2\2\6 \3\2\2\2\b)\3\2\2\2\n-\3\2\2\2\f\61\3\2\2\2\16B\3\2"+
		"\2\2\20I\3\2\2\2\22K\3\2\2\2\24\31\7\21\2\2\25\26\7\21\2\2\26\27\7\3\2"+
		"\2\27\31\5\2\2\2\30\24\3\2\2\2\30\25\3\2\2\2\31\3\3\2\2\2\32\37\7\20\2"+
		"\2\33\34\7\20\2\2\34\35\7\3\2\2\35\37\5\4\3\2\36\32\3\2\2\2\36\33\3\2"+
		"\2\2\37\5\3\2\2\2 !\7\4\2\2!\"\5\b\5\2\"#\7\5\2\2#$\5\n\6\2$%\7\6\2\2"+
		"%&\5\f\7\2&\'\7\7\2\2\'(\5\22\n\2(\7\3\2\2\2)*\7\b\2\2*+\5\2\2\2+,\7\t"+
		"\2\2,\t\3\2\2\2-.\7\b\2\2./\5\4\3\2/\60\7\t\2\2\60\13\3\2\2\2\61\62\7"+
		"\b\2\2\62\63\5\16\b\2\63\64\7\t\2\2\64\r\3\2\2\2\65\66\7\n\2\2\66\67\7"+
		"\20\2\2\678\7\13\2\289\5\20\t\29:\7\f\2\2:C\3\2\2\2;<\7\n\2\2<=\7\20\2"+
		"\2=>\7\13\2\2>?\5\20\t\2?@\7\r\2\2@A\5\16\b\2AC\3\2\2\2B\65\3\2\2\2B;"+
		"\3\2\2\2C\17\3\2\2\2DE\7\21\2\2EF\7\20\2\2FG\7\16\2\2GJ\5\20\t\2HJ\7\22"+
		"\2\2ID\3\2\2\2IH\3\2\2\2J\21\3\2\2\2KL\7\17\2\2LM\7\20\2\2M\23\3\2\2\2"+
		"\6\30\36BI";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}