import os

# Chemin du répertoire parent
parent_directory_path = '_exercices'

# Parcourir tous les dossiers et sous-répertoires dans le répertoire parent
for root, dirs, files in os.walk(parent_directory_path):
    for dir_name in dirs:
        # Vérifier si le nom du dossier contient des points
        if '.' in dir_name:
            # Renommer le dossier en supprimant les points
            new_dir_name = dir_name.replace('.','_')

            # Utiliser os.rename() pour renommer le dossier
            os.rename(os.path.join(root, dir_name), os.path.join(root, new_dir_name))
        directory_path=parent_directory_path+'/'+new_dir_name
        for file_name in os.listdir(directory_path):
            # Vérifier si le nom du fichier contient des points
            if '.' in file_name:
                # Renommer le fichier en supprimant les points
                new_file_name = file_name.replace('.','_',1)
                os.rename(os.path.join(directory_path, file_name), os.path.join(directory_path, new_file_name))