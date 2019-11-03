user = "-57.95293,-31.403828,-57.952818,-31.403224,-57.952593,-31.40231,-57.952428,-31.401407,-57.952245,-31.400474,-57.952076,-31.399558,-57.951967,-31.399488,-57.95182,-31.399444,-57.952375,-31.398235,-57.95253,-31.397995,-57.952733,-31.397839,-57.952831,-31.397784,-57.953002,-31.397714,-57.953978,-31.397229,-57.954157,-31.397152,-57.954339,-31.397056,-57.954162,-31.395905,-57.953981,-31.394821,-57.953818,-31.393777,-57.953644,-31.392658,-57.953398,-31.39122,-57.952013,-31.391303,-57.950884,-31.391394,-57.950744,-31.390264,-57.951885,-31.390162,-57.952235,-31.390131"
chofer = "-57.951575,-31.404198,-57.951714,-31.404178,-57.95156,-31.403403,-57.951376,-31.402471,-57.951222,-31.401694,-57.951156,-31.401602,-57.95108,-31.40157,-57.951051,-31.401558,-57.951027,-31.401539,-57.95101,-31.401515,-57.951018,-31.401434,-57.951039,-31.401413,-57.951073,-31.401345,-57.951217,-31.401054,-57.951779,-31.399521,-57.95182,-31.399444,-57.952375,-31.398235,-57.95253,-31.397995,-57.952733,-31.397839,-57.952831,-31.397784,-57.953002,-31.397714,-57.953978,-31.397229,-57.954157,-31.397152,-57.954339,-31.397056,-57.954162,-31.395905,-57.953981,-31.394821,-57.953818,-31.393777,-57.953644,-31.392658,-57.953398,-31.39122,-57.953237,-31.390043,-57.953015,-31.38879,-57.952862,-31.387717,-57.952858,-31.387686"


def unformat_coordinates(a):
    a = a.split(",")
    b = []
    for i in range(len(a)):
        if i != len(a)-1:
            b.append([float(a[i]), float(a[i+1])])
    return b

def match_routes(user_array, driver_array, max_difference=0.006, first_only=False):
    """Determine if two routes are available for a match"""
    matching_points = []
    if len(user_array) >= len(driver_array):
        main_array, second_array = user_array, driver_array
    else:
        main_array, second_array = driver_array, user_array
    for i in range(len(second_array)):
        a = abs(abs(main_array[i][0]) - abs(second_array[i][0]))
        b = abs(abs(main_array[i][1]) - abs(second_array[i][1]))
        if (a + b) <= max_difference:
            matching_points.append([main_array[i][0], main_array[i][1]])
    if len(matching_points) > 0 and first_only:
        return [matching_points[0]]
    return matching_points

user_array = unformat_coordinates(user)
chofer_array = unformat_coordinates(chofer)
#print(match_routes(user_array, chofer_array, 0.1))
"""A difference of 0.006 is half a cuadra"""