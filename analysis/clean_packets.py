if __name__ == '__main__':
    to_write = []
    with open('packets.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line and line.startswith('17'):
                to_write.append(line)
    with open('packets_clean.txt', 'w') as f:
        f.writelines(to_write)
