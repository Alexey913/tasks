def row_gt_col(max_row, max_col):
    for i in range(min(len(max_col), len(max_row))):
        if max_row[i] > max_col[i]:
            return True
        if max_row[i] < max_col[i]:
            return False
        
print(row_gt_col([2,2,1],[1,1,2]))