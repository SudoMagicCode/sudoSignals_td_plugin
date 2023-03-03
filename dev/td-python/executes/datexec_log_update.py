# me - this DAT.
# 
# dat - the changed DAT
# rows - a list of row indices
# cols - a list of column indices
# cells - the list of cells that have changed content
# prev - the list of previous string contents of the changed cells
# 
# Make sure the corresponding toggle is enabled in the DAT Execute DAT.
# 
# If rows or columns are deleted, sizeChange will be called instead of row/col/cellChange.


def onTableChange(dat):
	return

def onRowChange(dat, rows):
	return

def onColChange(dat, cols):
	return

def onCellChange(dat, cells, prev):
	for each_cell in cells:
		if each_cell.row == 1 and each_cell.col == 1:
			if each_cell.val == '':
				pass
			else:
				op('base_private_ext').ext.Signals.SetLogFromTable(op(dat.par.dat.eval()))
	return

def onSizeChange(dat):
	return
	