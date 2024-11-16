from bank import value

def main():
    test_greeting_0()
    test_greeting_20()
    test_greeting_except()

def test_greeting_0():
    assert value('hello')==0
    assert value('Hello sk')==0
    assert value('hello sir')==0
    assert value('hello mam')==0
     
    assert value('Hello mam')==0
def test_greeting_20():
    assert value('hi')==20
    assert value('hy')==20
    assert value('hie')==20

def test_greeting_except():
    assert value('good morning')==100
    assert value('good evening')==100
    assert value('good afternoon')==100

if __name__=="__main__":
    main()
