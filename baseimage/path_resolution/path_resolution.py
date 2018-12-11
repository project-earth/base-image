import os


def generate_file_path(root_data_dir, sceneid='', kind='', file=''):
	""" Generates absolute filepaths to different file resources related to the earth project. Takes
		a root data directory to prefix to relative paths. Other arguments

		If no valid `kind` argument is given, the function returns the root data directory.

		The `kind` argument can take three values:
		- 'database'
		- 'raw'
		- 'preproc'
	"""
	if kind == 'database':
		if sceneid == '': return(os.path.join(root_data_dir, 'preproc/database.hdf5f'))
		else: return(os.path.join(sceneid, file))

	if kind == 'raw':
		if file == 'metadata': file = sceneid + '_MTL.txt'
		elif file == 'tar': file = sceneid
		elif file == 'B1': file = sceneid + '_B1.TIF'
		elif file == 'B2': file = sceneid + '_B2.TIF'
		elif file == 'B3': file = sceneid + '_B3.TIF'
		elif file == 'B4': file = sceneid + '_B4.TIF'
		elif file == 'B5': file = sceneid + '_B5.TIF'
		elif file == 'B6': file = sceneid + '_B6.TIF'
		elif file == 'B7': file = sceneid + '_B7.TIF'
		elif file == 'B8': file = sceneid + '_B8.TIF'
		elif file == 'B9': file = sceneid + '_B9.TIF'
		elif file == 'B10': file = sceneid + '_B10.TIF'
		elif file == 'B11': file = sceneid + '_B11.TIF'
		elif file == 'BQA': file = sceneid + '_BQA.TIF'
		return os.path.join(root_data_dir, 'raw/{0}/'.format(sceneid), file)

	if kind == 'preproc':
		if file == 'visible' and sceneid != '': sceneid += '_V.TIF'
		if file == 'cloud_detection_clustering': sceneid += '.jpg'
		return os.path.join(root_data_dir, kind, file, sceneid)

	return(root_data_dir)


def check_create_folder(folder_path):
	""" Given a file path, checks if path exists and if it does not, creates a directory with that path.
	"""
	if not os.path.exists(folder_path):
		os.makedirs(folder_path)
	return folder_path
