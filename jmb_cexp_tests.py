# Some additional tests, coming mainly from regressions and related examples


def reg_tests(t_parse):
    t_parse('a()', '(call a)')
    t_parse('a(+1)', '(call a (+ 1))')
    t_parse('a()+1', '(+ (call a) 1)')
    t_parse('a, b, c', '(, a b c)')
    t_parse('(a, b, c)', '(, a b c)')
    t_parse('f(a, b, c)', '(call f a b c)')
    t_parse('f(a, b, c), d', '(, (call f a b c) d)')
    t_parse('(a, b, c), d', '(, (, a b c) d)')
    t_parse('- - a', '(- (- a))')
    t_parse('+ - a', '(+ (- a))')
    t_parse('++ -- a', '(++ (-- a))')
    t_parse('a ++ --', '(post-- (post++ a))')
    t_parse('a.b', '(. a b)')
    t_parse('a.b.c', '(. (. a b) c)')
    t_parse('a->b', '(-> a b)')
    t_parse('++a->b', '(++ (-> a b))')
    t_parse('a++ ->b', '(-> (post++ a) b)')


def oddities(t_parse):
    t_parse('a.(x)', '(. a x)')
    t_parse('a.(x+3)', '(. a (+ x 3))')


def errors(t_parse):
    t_parse('x + a b', '')
    t_parse('x[a b]', '')
    t_parse('x[a)]', '')
    t_parse('x(a])', '')
    t_parse('[a + b]', '')
    t_parse('[a b]', '')
    t_parse('+', '')
    t_parse('a +', '')
    t_parse('<=', '')
    t_parse('<= - a + b', '')
    t_parse('a b', '')
    t_parse('a + b @', '')
    t_parse('a + b )', '')
    t_parse('( a + b', '')
    t_parse('( a + b) c', '')
    t_parse('f ( a + b ) c', '')
    t_parse('@ a + b', '')
    t_parse('a @ b', '')
    t_parse('(a @ b)', '')
    t_parse(')', '')


def all_tests(t_parse):
    reg_tests(t_parse)
    oddities(t_parse)
    errors(t_parse)


def check_parsing(parser, s, expected):
    try:
        tree = parser.parse(s)
        sexpr = repr(tree)
        if sexpr != expected:
            if expected == '':
                print('Failing to parse: {} => {}'.format(s, sexpr))
            else:
                print('UNEXPECTED Failure to parse: {} => {} != {}'.format(s, sexpr, expected))
    except RuntimeError as error:
        if expected == '':
            print('Exception while parsing {} => {}'.format(s, error))
        else:
            print('UNEXPECTED exception while parsing: {} => {}, expected {}'.format(s, error, expected))
