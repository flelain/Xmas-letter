import random
import yaml
import sys

FILE: str = './participants.yaml'

def read_yaml() -> list:
    with open(FILE, 'r') as f:
        participants = yaml.safe_load(f)
        return participants

def has_family(participant) -> bool:
    if 'family' in participant.keys():
        return True
    return False

def random_reorder(participants: list) -> list:
    # participants expected like:
    # [{name: Bilbo, email: bilbo@contree.org, family(optional): sacquet},
    #  {name: Gandalf, email: gandalf@thegrey.net, family(optional): wizards}]
    nb_p = len(participants)
    p = list(participants)
    rand_p = []
    iter = 0
    super_iter = 0
    while len(p) > 0:
        if rand_p:
            prev = rand_p[-1]
        else:
            prev = {'name': '', 'email': ''}
        rand_index = random.randrange(len(p))
        next = p[rand_index]
        if has_family(next) and has_family(prev):
            if next['family'] == prev['family']:
                if iter > 5:
                    if super_iter > 5:
                        raise Exception(f"No solution found after {super_iter*iter} iterations. Can the problem really be solved?")
                    p = list(participants)
                    rand_p = []
                    iter = 0
                    super_iter += 1
                else:
                    iter += 1
                continue
        rand_p.append(next)
        p.pop(rand_index)
        if len(rand_p) == nb_p:
            if has_family(rand_p[-1]) and has_family(rand_p[0]):
                if rand_p[-1]['family'] == rand_p[0]['family']:
                    p = list(participants)
                    rand_p = []
    return rand_p
	    	
def main():
    """tbd"""
    participants = read_yaml()
    try:
        ordered_p = random_reorder(participants)
    except Exception as _err:
        print(_err)
    if len(ordered_p) > 1:
        for i in range(len(ordered_p) - 1):
            print(f'{ordered_p[i]["name"]} offers a gift to {ordered_p[i+1]["name"]}')
    print(f'{ordered_p[-1]["name"]} offers a gift to {ordered_p[0]["name"]}')
    
if __name__ == '__main__':
    sys.exit(main())
