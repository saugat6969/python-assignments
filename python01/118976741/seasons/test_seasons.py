from seasons import check_date
def main():
    test_invalid()
    test_valid()

def test_valid():
    assert check_date("1999-01-01")==("1999","01","01")
    assert check_date("1999-12-31")==("1999","12","31")
    
def test_invalid():
    assert check_date("January 1,1999")==None
    assert check_date("july 2 ,1999")==None
    assert check_date("01-09-1999")==None



