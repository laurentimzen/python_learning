# give me some states!
states = {
    'Oregon': 'OR',
    'New Mexico': 'NM',
    'South Carolina': 'SC',
    'Utah': 'UT',
    'Colorado': 'CO'
}

# give me some cities btch
cities = {
    'OR': 'Portland',
    'NM': 'Los Alamos',
    'SC': 'Myrtle Beach',
}
cities['UT'] = 'Salt Lake city'
cities['CO'] = 'Denver'


print '-' * 15
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)


print '-' * 15
print "Oregon is: ", states['Oregon']
print "New Mexico is: ", states['New Mexico']

print '-' * 15
for abbrev, city in cities.items():
    print "%s is a city in %s" % (city, abbrev)

states.pop('Utah')
print states

states.push('Idaho')
print states
