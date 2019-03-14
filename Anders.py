def main():
    fromEdgelistToPandasToCSV(outputName)
    dataframe = readPandasIntoMemory(path(filename))
    backboning(dataframe,outputName)
    dataframe = readPandasIntoMemory(path(filename))
    mapping(dataframe)
    dataframe = readPandasIntoMemory(path(filename))
    profit("?")

if __name__ == '__main__':
    main()
