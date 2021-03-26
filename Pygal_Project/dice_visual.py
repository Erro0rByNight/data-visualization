from die import die
import pygal

# Create two d6 dice.

die_1 = die()
die_2 = die()

# Make some rolls , and store the results in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides

for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling two d6 1000 times."
hist.x_labels = ['1','2','3','4','5','6','7','8','9','10','11','12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('d6 + d6',frequencies)
hist.render_to_file('dice_visual.svg')
