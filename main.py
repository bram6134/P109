import csv
import plotly.figure_factory as figure_factory
import plotly.graph_objects as graph_objects
import pandas
import statistics
import random

df = pandas.read_csv("StudentsPerformance.csv")
data = df["reading score"].tolist()

mean = sum(data)/len(data)
median = statistics.median(data)
mode = statistics.mode(data)
standard_deviation = statistics.stdev(data)

first_stdev_start, first_stdev_end = mean - standard_deviation, mean + standard_deviation
second_stdev_start, second_stdev_end = mean - (2*standard_deviation), mean + (2*standard_deviation)
third_stdev_start, third_stdev_end = mean - (3*standard_deviation), mean + (3*standard_deviation)

fig = figure_factory.create_distplot([data], ["READING SCORES"], show_hist = False)
fig.add_trace(graph_objects.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "MEAN"))
fig.add_trace(graph_objects.Scatter(x = [first_stdev_start, first_stdev_start], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 1"))
fig.add_trace(graph_objects.Scatter(x = [first_stdev_end, first_stdev_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 1"))
fig.add_trace(graph_objects.Scatter(x = [second_stdev_start, second_stdev_start], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 2"))
fig.add_trace(graph_objects.Scatter(x = [second_stdev_end, second_stdev_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 2"))
fig.show()

within1stdev = [result for result in data if result > first_stdev_start and result < first_stdev_end]
within2stdev = [result for result in data if result > second_stdev_start and result < second_stdev_end]
within3stdev = [result for result in data if result > third_stdev_start and result < third_stdev_end]

print("Mean: {}".format(mean))
print("Median: {}".format(median))
print("Mode: {}".format(mode))
print("{}% of data for height lies within 1 standard deviation".format(len(within1stdev)*100/len(data)))
print("{}% of data for height lies within 2 standard deviation".format(len(within2stdev)*100/len(data)))
print("{}% of data for height lies within 3 standard deviation".format(len(within3stdev)*100/len(data)))