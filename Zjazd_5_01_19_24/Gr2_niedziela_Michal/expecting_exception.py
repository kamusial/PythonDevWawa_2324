def to_powinno_failowac():
    raise ValueError("")


try:
    to_powinno_failowac()
except ValueError:
    print("Złapałem oczekiwany przez nas wyjątek")
else:
    print("KOD W SEKCJI 'try' NIE WYRZUCIŁ ŻADNEGO WYJĄTKU :<")
    raise AssertionError("MIAŁO SIE WYWALIĆ, a tak sie nie stało :(((((((")
finally:
    print("WYKONUJĘ SIĘ ZAWSZE")
