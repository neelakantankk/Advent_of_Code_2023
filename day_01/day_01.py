from parts import *

def main():

    filename="input"
    with open(filename,'r') as infile:
        answer_a = part_a(infile)

    with open(filename, 'r') as infile:
        answer_b = part_b(infile)
    
    print(answer_a)
    print(answer_b)
    

if __name__ == '__main__':
    main()

