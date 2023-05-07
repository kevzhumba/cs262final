if __name__ == '__main__':
    to_write = []
    with open('packets_small.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line and line.startswith('14'):
                to_write.append(line)
    with open('packets_small_clean.txt', 'w') as f:
        f.writelines(to_write)
