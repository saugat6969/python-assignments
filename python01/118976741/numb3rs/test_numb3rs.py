from numb3rs import validate
def main():
    test_ip()
    test_range()
    test_string()



def test_ip():
    assert validate(r"127.0.0.1")==True
    assert validate(r"255.255.255.255")==True
    assert validate(r"1")==False
    assert validate(r"1.2")==False
    assert validate(r"10.10.10.10.10")==False



def test_range():
    assert validate(r"512.512.512.512")==False
    assert validate(r"1.2.3.1000")==False
    assert validate(r"1.1.1.512")==False

def test_string():
    assert validate("cat")==False



if __name__=="__main__":
    main()
