from scipy.misc import derivative
import argparse
import re
import warnings

# czyszczę warning ze względu na to, że funkcja derivative z scipy jest przestarzała (a jeśli dobrze zrozumiałam,
# to tylko ona została zezwolona do obliczenia pochodnej - stąd decyzja o nieużywaniu niczego "nowszego")
warnings.filterwarnings("ignore", category=DeprecationWarning) 

def f(x):
    # regex w razie, gdyby wpisana funkcja zależała od innej zmiennej niż x
    # zakładam tak jak w przykładzie, że funkcja zostaje wpisana po "pythonowemu" (tzn. np potęga to '**')
    func = re.sub("[a-zA-z]+", str(x), args.func)       
    return eval(func)

parser = argparse.ArgumentParser()
parser.add_argument("func", type=str, help="Funkcja, dla której będzie wyznaczane przybliżenie miejsca zerowego metodą Newtona")
parser.add_argument("start", type=float, help="Punkt startowy")
parser.add_argument("n_steps", type=int, help="Ilość kroków metody; domyślnie=10", default=10, nargs='?')
parser.add_argument("precision", type=float, help="Dokładność; domyślnie=0.0001", default=0.0001, nargs='?')
args = parser.parse_args()        

result = args.start

for _ in range(args.n_steps):
    prev = result
    result = prev - f(prev)/derivative(f, prev)

    if abs(result - prev) < args.precision or abs(f(result)) < args.precision:
        break

print(result)