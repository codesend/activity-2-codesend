import matplotlib.pyplot as plot

def graphSnowfall(t):
    counts = [0] * 10

    with open(t, 'r') as file:
        for line in file:
            if line.strip() == '':
                continue

            snowfall = int(line.strip())
            if snowfall <= 100:
                index = (snowfall - 1) // 10
            else:
                index = 9
            counts[index] += 1

    ranges = []
    for i in range(10):
        range_str = '{}-{}'.format(i*10+1, (i+1)*10)
        ranges.append(range_str)

    plot.bar(ranges, counts)
    plot.xlabel('Snowfall')
    plot.ylabel('Occurrences')
    plot.title('Snowfall Accumulation')
    plot.show()
