print("Discover Your Chinese Zodiac Sign")
InputCZS = int(input("Enter your Birth Year: "))

if InputCZS in [1924, 1936, 1948, 1960, 1972, 1984, 1996, 2008, 2020, 2032]:
    UserChineseZS = "Rat"
    print("The Chinese Zodiac Sign of your Birth Year is", UserChineseZS)
elif InputCZS in [1925, 1937, 1949, 1961, 1973, 1985, 1997, 2009, 2021, 2033]:
    UserChineseZS = "Ox"
    print("The Chinese Zodiac Sign of your Birth Year is", UserChineseZS)
elif InputCZS in [1926, 1938, 1950, 1962, 1974, 1986, 1998, 2010, 2022, 2034]:
    UserChineseZS = "Tiger"
    print("The Chinese Zodiac Sign of your Birth Year is", UserChineseZS)
elif InputCZS in [1927, 1939, 1951, 1963, 1975, 1987, 1999, 2011, 2023, 2035]:
    UserChineseZS = "Rabbit"
    print("The Chinese Zodiac Sign of your Birth Year is", UserChineseZS)
elif InputCZS in [1928, 1940, 1952, 1964, 1976, 1988, 2000, 2012, 2024, 2036]:
    UserChineseZS = "Dragon"
    print("The Chinese Zodiac Sign of your Birth Year is", UserChineseZS)
elif InputCZS in [1929, 1941, 1953, 1965, 1977, 1989, 2001, 2013, 2025, 2037]:
    UserChineseZS = "Snake"
    print("The Chinese Zodiac Sign of your Birth Year is", UserChineseZS)
elif InputCZS in [1930, 1942, 1954, 1966, 1978, 1990, 2002, 2014, 2026, 2038]:
    UserChineseZS = "Horse"
    print("The Chinese Zodiac Sign of your Birth Year is", UserChineseZS)
elif InputCZS in [1931, 1943, 1955, 1967, 1979, 1991, 2003, 2015, 2027, 2039]:
    UserChineseZS = "Goat"
    print("The Chinese Zodiac Sign of your Birth Year is", UserChineseZS)
elif InputCZS in [1932, 1944, 1956, 1968, 1980, 1992, 2004, 2016, 2028, 2040]:
    UserChineseZS = "Monkey"
    print("The Chinese Zodiac Sign of your Birth Year is", UserChineseZS)
elif InputCZS in [1933, 1945, 1957, 1969, 1981, 1993, 2005, 2017, 2029, 2041]:
    UserChineseZS = "Rooster"
    print("The Chinese Zodiac Sign of your Birth Year is", UserChineseZS)
elif InputCZS in [1934, 1946, 1958, 1970, 1982, 1994, 2006, 2018, 2030, 2042]:
    UserChineseZS = "Dog"
    print("The Chinese Zodiac Sign of your Birth Year is", UserChineseZS)
elif InputCZS in [1935, 1947, 1959, 1971, 1983, 1995, 2007, 2019, 2031, 2043]:
    UserChineseZS = "Pig"
    print("The Chinese Zodiac Sign of your Birth Year is", UserChineseZS)
elif InputCZS < 1924:
    print("You can't be that old")
else:
    print("It's impossible that you were born in the future.")


