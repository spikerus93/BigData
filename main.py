from imdb_counter import mapper, reducer, print_results


def print_imdb(file_paths=None):

    if __name__ == "__main__":
        mapper_results = [mapper(file_path) for file_path in file_paths]
        mean, M2 = reducer(mapper_results)
        print_results(len(file_paths), mean, M2)

