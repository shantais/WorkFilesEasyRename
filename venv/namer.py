def rename(base, file_list):

    n_list = []
    for idx, file in enumerate(file_list):
        if idx == 0:
            n_list.append(base + 'toc.pdf')
        # elif idx == len(file_list) - 2:
        #     n_list.append(base + 'auth.pdf')
        # elif idx == len(file_list) - 1:
        #     n_list.append(base + 'sc.pdf')
        # elif idx == len(file_list) - 2:
        #     n_list.append(base + 'sc.pdf')
        elif idx == len(file_list) - 1:
            n_list.append(base + 'auth.pdf')
        # elif idx == len(file_list) - 1:
        #     n_list.append(base + 'rw.pdf')
        # elif idx <= 10:
        #     n_list.append(base + '0' + str(idx-1) + '.pdf')
        # else:
        #     n_list.append(base + str(idx-1) + '.pdf')
        elif idx < 10:
            n_list.append(base + '0' + str(idx) + '.pdf')
        else:
            n_list.append(base + str(idx) + '.pdf')

    return n_list
