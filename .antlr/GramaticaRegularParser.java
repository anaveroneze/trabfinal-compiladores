// Generated from /home/ana/Área de Trabalho/2019-1/compiladores/final/trabalhofinal-ana/GramaticaRegular.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class GramaticaRegularParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, VAR=14, VAR_T=15, VAZIO=16, WS=17;
	public static final int
		RULE_gram = 0, RULE_naoterminais = 1, RULE_terminais = 2, RULE_simbolos = 3, 
		RULE_simboloster = 4, RULE_inicial = 5, RULE_producoes = 6, RULE_producao = 7, 
		RULE_transicao = 8;
	public static final String[] ruleNames = {
		"gram", "naoterminais", "terminais", "simbolos", "simboloster", "inicial", 
		"producoes", "producao", "transicao"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'V '", "'T '", "'P '", "'S '", "'= ['", "']'", "', '", "'= '", 
		"'('", "'>'", "')'", "'), '", "' | '", null, null, "'#'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, "VAR", "VAR_T", "VAZIO", "WS"
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
	public String getGrammarFileName() { return "GramaticaRegular.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public GramaticaRegularParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
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
		public TerminalNode EOF() { return getToken(GramaticaRegularParser.EOF, 0); }
		public GramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_gram; }
	}

	public final GramContext gram() throws RecognitionException {
		GramContext _localctx = new GramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_gram);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(18);
			match(T__0);
			setState(19);
			naoterminais();
			setState(20);
			match(T__1);
			setState(21);
			terminais();
			setState(22);
			match(T__2);
			setState(23);
			producoes();
			setState(24);
			match(T__3);
			setState(25);
			inicial();
			setState(26);
			match(EOF);
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
		enterRule(_localctx, 2, RULE_naoterminais);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(28);
			match(T__4);
			setState(29);
			simbolos();
			setState(30);
			match(T__5);
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
		public SimbolosterContext simboloster() {
			return getRuleContext(SimbolosterContext.class,0);
		}
		public TerminaisContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_terminais; }
	}

	public final TerminaisContext terminais() throws RecognitionException {
		TerminaisContext _localctx = new TerminaisContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_terminais);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(32);
			match(T__4);
			setState(33);
			simboloster();
			setState(34);
			match(T__5);
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

	public static class SimbolosContext extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(GramaticaRegularParser.VAR, 0); }
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
		enterRule(_localctx, 6, RULE_simbolos);
		try {
			setState(40);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(36);
				match(VAR);
				setState(37);
				match(T__6);
				setState(38);
				simbolos();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(39);
				match(VAR);
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

	public static class SimbolosterContext extends ParserRuleContext {
		public TerminalNode VAR_T() { return getToken(GramaticaRegularParser.VAR_T, 0); }
		public SimbolosterContext simboloster() {
			return getRuleContext(SimbolosterContext.class,0);
		}
		public SimbolosterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_simboloster; }
	}

	public final SimbolosterContext simboloster() throws RecognitionException {
		SimbolosterContext _localctx = new SimbolosterContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_simboloster);
		try {
			setState(46);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(42);
				match(VAR_T);
				setState(43);
				match(T__6);
				setState(44);
				simboloster();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(45);
				match(VAR_T);
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

	public static class InicialContext extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(GramaticaRegularParser.VAR, 0); }
		public InicialContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_inicial; }
	}

	public final InicialContext inicial() throws RecognitionException {
		InicialContext _localctx = new InicialContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_inicial);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(48);
			match(T__7);
			setState(49);
			match(VAR);
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
		enterRule(_localctx, 12, RULE_producoes);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(51);
			match(T__4);
			setState(52);
			producao();
			setState(53);
			match(T__5);
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
		public TerminalNode VAR() { return getToken(GramaticaRegularParser.VAR, 0); }
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
		enterRule(_localctx, 14, RULE_producao);
		try {
			setState(68);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(55);
				match(T__8);
				setState(56);
				match(VAR);
				setState(57);
				match(T__9);
				setState(58);
				transicao();
				setState(59);
				match(T__10);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(61);
				match(T__8);
				setState(62);
				match(VAR);
				setState(63);
				match(T__9);
				setState(64);
				transicao();
				setState(65);
				match(T__11);
				setState(66);
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
		public TerminalNode VAR_T() { return getToken(GramaticaRegularParser.VAR_T, 0); }
		public TerminalNode VAR() { return getToken(GramaticaRegularParser.VAR, 0); }
		public TransicaoContext transicao() {
			return getRuleContext(TransicaoContext.class,0);
		}
		public TerminalNode VAZIO() { return getToken(GramaticaRegularParser.VAZIO, 0); }
		public TransicaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_transicao; }
	}

	public final TransicaoContext transicao() throws RecognitionException {
		TransicaoContext _localctx = new TransicaoContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_transicao);
		try {
			setState(77);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(70);
				match(VAR_T);
				setState(71);
				match(VAR);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(72);
				match(VAR_T);
				setState(73);
				match(VAR);
				setState(74);
				match(T__12);
				setState(75);
				transicao();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(76);
				match(VAZIO);
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

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\23R\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3"+
		"\5\3\5\5\5+\n\5\3\6\3\6\3\6\3\6\5\6\61\n\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b"+
		"\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\tG\n\t\3\n\3\n"+
		"\3\n\3\n\3\n\3\n\3\n\5\nP\n\n\3\n\2\2\13\2\4\6\b\n\f\16\20\22\2\2\2M\2"+
		"\24\3\2\2\2\4\36\3\2\2\2\6\"\3\2\2\2\b*\3\2\2\2\n\60\3\2\2\2\f\62\3\2"+
		"\2\2\16\65\3\2\2\2\20F\3\2\2\2\22O\3\2\2\2\24\25\7\3\2\2\25\26\5\4\3\2"+
		"\26\27\7\4\2\2\27\30\5\6\4\2\30\31\7\5\2\2\31\32\5\16\b\2\32\33\7\6\2"+
		"\2\33\34\5\f\7\2\34\35\7\2\2\3\35\3\3\2\2\2\36\37\7\7\2\2\37 \5\b\5\2"+
		" !\7\b\2\2!\5\3\2\2\2\"#\7\7\2\2#$\5\n\6\2$%\7\b\2\2%\7\3\2\2\2&\'\7\20"+
		"\2\2\'(\7\t\2\2(+\5\b\5\2)+\7\20\2\2*&\3\2\2\2*)\3\2\2\2+\t\3\2\2\2,-"+
		"\7\21\2\2-.\7\t\2\2.\61\5\n\6\2/\61\7\21\2\2\60,\3\2\2\2\60/\3\2\2\2\61"+
		"\13\3\2\2\2\62\63\7\n\2\2\63\64\7\20\2\2\64\r\3\2\2\2\65\66\7\7\2\2\66"+
		"\67\5\20\t\2\678\7\b\2\28\17\3\2\2\29:\7\13\2\2:;\7\20\2\2;<\7\f\2\2<"+
		"=\5\22\n\2=>\7\r\2\2>G\3\2\2\2?@\7\13\2\2@A\7\20\2\2AB\7\f\2\2BC\5\22"+
		"\n\2CD\7\16\2\2DE\5\20\t\2EG\3\2\2\2F9\3\2\2\2F?\3\2\2\2G\21\3\2\2\2H"+
		"I\7\21\2\2IP\7\20\2\2JK\7\21\2\2KL\7\20\2\2LM\7\17\2\2MP\5\22\n\2NP\7"+
		"\22\2\2OH\3\2\2\2OJ\3\2\2\2ON\3\2\2\2P\23\3\2\2\2\6*\60FO";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}