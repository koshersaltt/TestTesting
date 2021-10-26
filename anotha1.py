from main import AdditionTest, MultiplicationTest

def TestAdd():
        assert AdditionTest(2,3) == 5
        assert AdditionTest(5,3) == 8
        print("Add Function works correctly")

if __name__ == '__main__':
        TestAdd()