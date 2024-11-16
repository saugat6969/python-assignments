from plates import is_valid
def main():
    test_min_max()
    test_two_letters()
    test_middle_no()
    test_number_zero()
    test_other()





def test_min_max():

    assert is_valid('AA')==True

    assert is_valid('ABCDEF')==True

    assert is_valid('A')==False

    assert is_valid('ASDFGHJKK')==False


def test_two_letters():
    assert is_valid('AA')==True

    assert is_valid('A2')==False

    assert is_valid('2A')==False

    assert is_valid('22')==False


def test_middle_no():

    assert is_valid('AAA222')==True
  




def test_number_zero():

    assert is_valid('CS50')==True

    assert is_valid('CS05')==False
def test_other():

    assert is_valid('SK,99')==False

    assert is_valid('AA.90')==False

    assert is_valid('PI!3N')==False




if __name__ == "__main__":
    main()
