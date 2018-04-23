# smoke test
from jeopardy import jeopardyfinal
def test_smoke():
	assert True == True

p100_ans = programming_100()

def test_prog_100():
	assert p100_ans.correct("c" or "C") == "Correct!"
	assert p100_ans("a" or"A") == "Wrong"

