import urllib.request
from progressbar import ProgressBar, Percentage, Bar

def download_python():
    url = 'http://www.python.org/ftp/python/2.7/Python-2.7.tar.bz2'
    fname = url.split('/')[-1]

    try:
        u = urllib.request.urlopen(url)
        with open(fname, 'wb') as file:  # Usar 'with' para manejar el archivo
            meta = u.info()
            file_size = int(meta.get("Content-Length"))
            print("Descargando: %s Bytes: %s" % (fname, file_size))

            pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=file_size).start()
            bytes_downloaded = 0
            chunk_size = 10240

            while True:
                buffer = u.read(chunk_size)
                if buffer:
                    file.write(buffer)
                    bytes_downloaded += len(buffer)  # Actualizar con el tamaño real del buffer
                    pbar.update(bytes_downloaded)
                else:
                    break

            pbar.finish()
    except Exception as e:
        print(f"Error: {e}")

# Llamar a la función para descargar Python
download_python()