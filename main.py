def round_robin(competitors):
    """
    Takes a list of N names and generates a schedule consisting of N-1 days of N/2 matches.
    Every competitor plays a match every day and, by the end of all N-1 days, everyone will
    have played against everyone else.

    :param competitors: list containing all competitors' names
    :return: matches for each day
    """

    # if there is an odd number of competitors, add '###' to the list
    # '###' counts as an instant win and will be matched against every competitor
    if len(competitors) % 2:
        competitors.append('###')

    # number of competitors
    count = len(competitors)
    # number of days
    n_days = count - 1
    # number of daily matches
    #
    # typecasting to 'int' is required, otherwise 'daily_matches' would be treated
    # as a float and would not be usable inside of the 'range()' function
    daily_matches = int(count / 2)

    # list containing every match of each day
    days = []

    for day in range(n_days):
        # reset list containing pairings for the current day
        pairings = []
        for match in range(daily_matches):
            # take first and last, second and penultimate and so on
            #
            # this line would always do the same thing each day
            # if it weren't for the following instruction
            pairings.append((competitors[match], competitors[count-match-1]))

        # remove last competitor and put it after the first one
        #
        # you can understand why this is done by looking at
        # 1-factorization of a complete graph
        #
        # place each vertex in a circle with the first vertex in the center.
        # it really doesn't matter which vertex you pick to be in the center,
        # as long as you adjust everything else accordingly. picking the first
        # (or last) vertex is just easier.
        # each daily match will be one of the central edges plus every other edge
        # perpendicular to that edge
        #
        # in this script, vertex 0 is treated as the central vertex and, as such, never changes position
        # while the others rotate around it clockwise to generate each possible pairing
        #
        # reference links:
        # https://en.wikipedia.org/wiki/Graph_factorization#Complete_graphs
        competitors.insert(1, competitors.pop())

        # save current day
        days.append(pairings)

    return days


# put your competitors here
for turn in round_robin(['Alice', 'Bob', 'Claire', 'David', 'Emily', 'Frank', 'Gwen', 'Harry']):
    for pairing in turn:
        print(' - '.join(pairing))
    print()
