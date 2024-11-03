import os
import datetime
import shutil


def FilesInFolders(folder_name):
	files = os.listdir(folder_name)

	if not os.path.exists(f"{folder_name}/RAWs"):
		os.mkdir(f"{folder_name}/RAWs")
	dng_path = f"{folder_name}/RAWs"

	for file in files:
		file_full = os.path.join(folder_name, file)
		timestamp = os.path.getctime(file_full)
		creation_date = datetime.datetime.fromtimestamp(timestamp)
		date_folder = creation_date.strftime("%Y_%m_%d")

		if file.lower().endswith('.dng'):
			if not os.path.exists(f"{folder_name}/RAWs/{date_folder}"):
				os.mkdir(f"{folder_name}/RAWs/{date_folder}")
			shutil.move(os.path.join(folder_name, file),
			            os.path.join(f"{dng_path}/{date_folder}", file))

		if file.lower().endswith('.jpg') or file.lower().endswith('.mp4'):
			if not os.path.exists(f"{folder_name}/{date_folder}"):
				os.mkdir(f"{folder_name}/{date_folder}")
			shutil.move(os.path.join(folder_name, file),
			            os.path.join(f"{folder_name}/{date_folder}", file))



if __name__ == '__main__':
	FilesInFolders("D:/Drona")
