#!/usr/bin/env python
# coding: utf-8

# from datasets import load_dataset, load_from_disk
# otsl_subset = load_dataset('ds4sd/FinTabNet_OTSL', split="test")
# loaded_dataset = otsl_subset
# otsl_subset.save_to_disk("cached_otsl_subset")
# loaded_dataset = load_from_disk("cached_otsl_subset")


def convert_otsl_list(otsl_list):
    final_seq = []
    for e in otsl_list:
        if e == 'fcel' or e == 'ecel':
            final_seq.append('C')
        elif e == 'lcel':
            final_seq.append('L')
        elif e == 'ucel':
            final_seq.append('U')
        elif e == 'xcel':
            final_seq.append('X')
        elif e == 'nl':
            final_seq.append('N')
        else:
            final_seq.append('C')
    return final_seq


def count_contiguous_occurrences(s, target_char):
    count = 0
    for char in s:
        if char == target_char:
            count += 1
        else:
            break
    return count

def get_cell_spans(otsl_matrix, i, j):
    entry = otsl_matrix[i][j]
    if entry != 'C':
        return 0, 0
    else:
        row_seq = ''.join(otsl_matrix[i])[j + 1:]
        col_seq = ''.join(row[j] for row in otsl_matrix)[i + 1:]
        rs = count_contiguous_occurrences(row_seq, 'L')
        cs = count_contiguous_occurrences(col_seq, 'U')
        return rs, cs

def get_conv_html_from_otsl(otsl_matrix, R, C):                
    html_string = '<html><table><tbody>'
    # Generate string
    for i in range(R):
        html_string += '<tr>'
        for j in range(C + 1):
            e = otsl_matrix[i][j]
            if e == 'C':
                rs, cs = get_cell_spans(otsl_matrix, i, j)
                if rs and cs:
                    #There is rowspan and colspan
                    html_string += f'<td rowpsan="{rs + 1}" colspan="{cs + 1}"></td>'
                elif rs and not cs:
                    # There is only row span
                    html_string += f'<td colspan="{rs + 1}"></td>'
                elif not rs and cs:
                    # There is only col span
                    html_string += f'<td rowspan="{cs + 1}"></td>'
                else:
                    # Normal cell
                    html_string += '<td></td>'
            elif e == 'N':
                # New row will start
                html_string += '</tr>'
            else:
                continue
    html_string += '</tbody></table></html>'
    return html_string


def align_otsl_from_rows_cols(otsl_string, rows, cols):
    N = len(otsl_string)
    C = cols
    R = rows
    if N != (C + 1) * R:
        # Needs correction
        actual_N = (C + 1) * R
        if N > actual_N:
            otsl_string = otsl_string[:actual_N]
            otsl_string = otsl_string[:-1] + 'N'
        else:
            diff = actual_N - N
            suffix = 'C' * (diff - 1) + 'N'
            otsl_string = otsl_string + suffix

    # Make sure Ns are at correct position !!
    # Remove if N is misplaced
    otsl_string_list =[]
    for i in range(len(list(otsl_string))):
        char = otsl_string[i]
        if i > 0 and (i + 1) % (C + 1) == 0:
            char = 'N'
        else:
            if otsl_string[i] == 'N':
                char = 'C'
        otsl_string_list.append(char)
    final_otsl_string = ''.join(otsl_string_list)
    return final_otsl_string

def convert_to_html(otsl_string, R, C):
    # Get N(sequence length), R(rows), C(cols)
    # C = int(otsl_string.find('N'))
    N = len(otsl_string)
    
    if N != (C + 1) * R:
        # Needs correction
        actual_N = (C + 1) * R
        if N > actual_N:
            otsl_string = otsl_string[:actual_N]
            otsl_string = otsl_string[:-1] + 'N'
        else:
            diff = actual_N - N
            suffix = 'C' * (diff - 1) + 'N'
            otsl_string = otsl_string + suffix
    
    # Init OTSL matrix
    otsl_matrix = [[otsl_string[i * (C + 1) + j] for j in range(C + 1)] for i in range(R)]

    # Handle for 'U' in first row, replace by 'C'
    for i in range(len(otsl_matrix[0])):
        if otsl_matrix[0][i] == 'U':
            otsl_matrix[0][i] = 'C'
    
    # Handle for L in first column, replace by 'C'
    for i in range(R):
        if otsl_matrix[i][0] == 'L':
            otsl_matrix[i][0] = 'C'

    # Return converted string
    return get_conv_html_from_otsl(otsl_matrix, R, C)



# for e in loaded_dataset:
#     # Read data
#     html_string = ''.join(e['html'])
#     otsl_string = ''.join(convert_otsl_list(e['otsl']))
#     converted_string = convert_to_html(otsl_string)
#     if converted_string != html_string:
#         print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in otsl_matrix]))
#         print(converted_string)
#         print(html_string)




