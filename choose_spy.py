from numpy.random import choice

spies = [
    'Alice',
    'Papa Danger',
    'Irish',
    'Bling Twin',
    'General',
    'Smallman',
    'Orange Sari',
    'Red Dress',
    'Plain Twin',
    'Rocker',
    'Mom',
    'Boots',
    'Taft',
    'Queen',
    'Sikh',
    'Duke',
    'Disney',
    'Salmon',
    'Pearls',
    'Cowboy',
    'Wheels'
]

weights = [0.1, 0.08, 0.07, 0.07, 0.07, 0.06, 0.06,
            0.06, 0.05, 0.05, 0.05, 0.04, 0.04, 0.04,
            0.04, 0.03, 0.03, 0.03, 0.02, 0.01, 0.0]

chosen_spies = []

for i in range(100):
    spy = choice(spies, p=weights)
    chosen_spies.append(spy)

print(chosen_spies)