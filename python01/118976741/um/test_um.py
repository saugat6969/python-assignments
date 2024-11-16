from um import count

def main():
    test_um()
    test_space()
    test_not_um()


def test_um():
    assert count('um')==1
    assert count('um?')==1
    assert count('um...')==1
    assert count('hello,um,world,um')==2
def test_not_um():
    assert count('yummmy')==0
    assert count('hi')==0

def test_space():
    assert count('UM')==1
    assert count('   um')==1
    assert count('um   ')==1
    assert count('um,yummy')==1
if __name__=="__main__":
    main()
