
all: cpp py

cpp: tt.cpp
	@g++ tt.cpp
	@./a.out
py: pytt.py
	@python3 pytt.py